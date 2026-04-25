/*
Copyright (c) 2006-2016 Lawrence Livermore National Security, LLC.
Produced at the Lawrence Livermore National Laboratory
UCRL-CODE-224807.

All rights reserved. Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

o Redistributions of source code must retain the above copyright notice, this list of conditions and the disclaimer below.

o Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the disclaimer (as noted below) in the documentation and/or other materials provided with the distribution.

o Neither the name of the LLNS/LLNL nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL LAWRENCE LIVERMORE NATIONAL SECURITY, LLC, THE U.S. DEPARTMENT OF ENERGY OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.
Additional BSD Notice

1. This notice is required to be provided under our contract with the U.S. Department of Energy (DOE). This work was produced at Lawrence Livermore National Laboratory under Contract No. DE-AC52-07NA27344 with the DOE.

2. Neither the United States Government nor Lawrence Livermore National Security, LLC nor any of their employees, makes any warranty, express or implied, or assumes any liability or responsibility for the accuracy, completeness, or usefulness of any information, apparatus, product, or process disclosed, or represents that its use would not infringe privately-owned rights.

3. Also, reference herein to any specific commercial products, process, or services by trade name, trademark, manufacturer or otherwise does not necessarily constitute or imply its endorsement, recommendation, or favoring by the United States Government or Lawrence Livermore National Security, LLC. The views and opinions of authors expressed herein do not necessarily state or reflect those of the United States Government or Lawrence Livermore National Security, LLC, and shall not be used for advertising or product endorsement purposes.
*/

/*
 * SmpDelayed.cc
 *
 * Six-group Keepin delayed neutron sampling for the LLNL Fission Library.
 *
 * When delayoption >= 2, delayed neutrons are appended to the fission
 * event's unified neutron array with exponentially-distributed emission
 * times.  Prompt neutrons retain neutronAges[i] = fission_time (delay=0);
 * delayed neutrons have neutronAges[i] = fission_time + sampled_delay.
 * Consumers distinguish prompt from delayed by comparing getnage_() to
 * the fission time passed to gen*fissevt_().
 *
 * Keepin six-group parameters from:
 *   G.R. Keepin, "Physics of Nuclear Kinetics", Addison-Wesley, 1965.
 *   M.C. Brady and T.R. England, ORNL/TM-11968, 1989.
 *
 * Energy spectra: Maxwellian with T = 0.30 MeV (<E> = 0.45 MeV), a
 * reasonable first approximation for all six groups.  Group-resolved
 * spectra can be substituted here without changing the API.
 */

#include "fissionEvent.h"
#include <math.h>
#include <string.h>

#define NGROUPS 6

struct KeepinParams {
   int    isotope;         /* ZA number of fissioning nucleus  */
   int    fissiontype;     /* 0 = spontaneous, 1 = induced     */
   double nu_d;            /* total delayed neutrons per fission event */
   double a[NGROUPS];      /* relative group abundances (sum = 1)     */
   double lambda[NGROUPS]; /* group decay constants (1/s)             */
};

/*
 * DATA PROVENANCE AND VERIFICATION NOTES
 * =======================================
 * The lambda_i (decay constants, s^-1) and a_i (group fractions) below are
 * from Keepin 1965 (G.R. Keepin, "Physics of Nuclear Kinetics", Table 5.2)
 * and Brady & England 1989 (ORNL/TM-11968).  These are the classic six-group
 * fast-spectrum parameterizations used in most Monte Carlo codes.
 *
 * KNOWN DISCREPANCY vs ENDF/B-VIII.0:
 *   ENDF/B-VIII.0 uses re-evaluated delayed neutron constants from the
 *   IAEA CRP "Nuclear Data for the Calculation of Thermal Reactor Neutron
 *   Cross Sections" (2002) and subsequent evaluations.  For Pu-239, the
 *   OpenMC regression test (test_data_neutron.py) asserts:
 *       sum(lambda_i) = 4.037  (ENDF/B-VIII.0)
 *   compared to:
 *       sum(lambda_i) = 4.979  (Keepin 1965, used below)
 *   The ~20% difference is concentrated in groups 5-6 (fastest precursors).
 *
 *   For applications dominated by U-235 (e.g. Godiva: 93.5% U-235),
 *   Keepin 1965 U-235 values are very well-established and the Pu-239
 *   discrepancy is irrelevant.  For other isotope mixes, run
 *   tools/extract_endf_delayed.py against an OpenMC nuclear data library
 *   to obtain ENDF/B-VIII.0 consistent values and replace entries below.
 *
 * nu_d values:
 *   Induced fission: nu_d = beta_eff * nubar at fast-spectrum conditions.
 *   Spontaneous fission: nu_d approximated from known SF yields; marked
 *   "approximate" -- replace with measured values when available.
 *
 * T (Maxwellian temperature for energy sampling) is a single value for all
 * entries; see smpMaxwellian() below.
 */
static const KeepinParams keepin_table[] = {
   /* ---- induced fission ------------------------------------------------
    * Sources: Keepin 1965 Table 5.2 (U-233, U-235, Pu-239),
    *          Brady & England ORNL/TM-11968 1989 (U-238, Pu-241).
    * lambda_i are fundamental nuclear decay constants measured repeatedly;
    * a_i and nu_d are fast-spectrum (FREYA energy range) values.
    * Run tools/extract_endf_delayed.py to cross-check against ENDF/B-VIII.0.
    * -------------------------------------------------------------------- */

   /* U-233 (92233) fast, Keepin 1965 Table 5.2
    * sum(lambda)=4.140  nu_d=beta*nubar=0.00270*2.71=0.00733 */
   { 92233, 1, 0.00733,
     {0.0860, 0.2740, 0.2270, 0.3170, 0.0730, 0.0230},
     {0.01260, 0.03370, 0.13900, 0.32500, 1.13000, 2.50000} },

   /* U-235 (92235) fast, Keepin 1965 Table 5.2
    * sum(lambda)=4.605  nu_d=beta*nubar=0.0065*2.43=0.01585
    * Critical isotope for Godiva (93.5% U-235): well-constrained. */
   { 92235, 1, 0.01585,
     {0.0330, 0.2190, 0.1960, 0.3950, 0.1150, 0.0420},
     {0.01240, 0.03050, 0.11100, 0.30100, 1.14000, 3.01000} },

   /* U-238 (92238) fast, Brady-England ORNL/TM-11968 1989
    * sum(lambda)=5.988  nu_d=beta*nubar=0.0148*2.91=0.04300 */
   { 92238, 1, 0.04300,
     {0.0130, 0.1370, 0.1620, 0.3880, 0.2250, 0.0750},
     {0.01320, 0.03210, 0.13900, 0.35800, 1.41600, 4.02000} },

   /* U-239 (92239) induced -- U-238 parameters used as approximation */
   { 92239, 1, 0.04300,
     {0.0130, 0.1370, 0.1620, 0.3880, 0.2250, 0.0750},
     {0.01320, 0.03210, 0.13900, 0.35800, 1.41600, 4.02000} },

   /* Pu-239 (94239) fast, Keepin 1965 Table 5.2
    * sum(lambda)=4.979  nu_d=0.00622
    * CAUTION: ENDF/B-VIII.0 has sum(lambda)=4.037 (see provenance note). */
   { 94239, 1, 0.00622,
     {0.0350, 0.2980, 0.2110, 0.3260, 0.0930, 0.0370},
     {0.01290, 0.03110, 0.13400, 0.33100, 1.26000, 3.21000} },

   /* Pu-241 (94241) fast, Brady-England ORNL/TM-11968 1989
    * sum(lambda)=5.599  nu_d=0.01600 */
   { 94241, 1, 0.01600,
     {0.0100, 0.2290, 0.1730, 0.3900, 0.1480, 0.0500},
     {0.01282, 0.02990, 0.12400, 0.35200, 1.61000, 3.47000} },

   /* ---- spontaneous fission --------------------------------------------
    * ENDF does not carry SF delayed neutron data.  Group structure is
    * borrowed from the nearest fissile isotope (same lambda_i); nu_d is
    * from known SF beta values and nubar.  All SF entries are approximate.
    * -------------------------------------------------------------------- */

   /* U-238 SF -- same lambda/a as U-238 induced (approximate) */
   { 92238, 0, 0.04300,
     {0.0130, 0.1370, 0.1620, 0.3880, 0.2250, 0.0750},
     {0.01320, 0.03210, 0.13900, 0.35800, 1.41600, 4.02000} },

   /* Pu-238 SF (94238) -- approximate; Pu-239 group structure, nu_d~0.00484 */
   { 94238, 0, 0.00484,
     {0.0350, 0.2980, 0.2110, 0.3260, 0.0930, 0.0370},
     {0.01290, 0.03110, 0.13400, 0.33100, 1.26000, 3.21000} },

   /* Pu-240 SF (94240) -- approximate; Pu-239 group structure, nu_d~0.00453 */
   { 94240, 0, 0.00453,
     {0.0350, 0.2980, 0.2110, 0.3260, 0.0930, 0.0370},
     {0.01290, 0.03110, 0.13400, 0.33100, 1.26000, 3.21000} },

   /* Pu-242 SF (94242) -- approximate; Pu-241 group structure, nu_d~0.00490 */
   { 94242, 0, 0.00490,
     {0.0100, 0.2290, 0.1730, 0.3900, 0.1480, 0.0500},
     {0.01282, 0.02990, 0.12400, 0.35200, 1.61000, 3.47000} },

   /* Cm-244 SF (96244) -- approximate; Pu-239 group structure, nu_d~0.00240 */
   { 96244, 0, 0.00240,
     {0.0350, 0.2980, 0.2110, 0.3260, 0.0930, 0.0370},
     {0.01290, 0.03110, 0.13400, 0.33100, 1.26000, 3.21000} },

   /* Cf-252 SF (98252) -- measured six-group data, literature consensus
    * Brady-England 1989 / Keepin 1965; nu_d=0.00978 (beta~0.0032, nubar~3.06) */
   { 98252, 0, 0.00978,
     {0.0200, 0.1920, 0.2330, 0.3410, 0.1580, 0.0560},
     {0.01330, 0.03250, 0.12400, 0.34800, 1.38000, 3.97000} },
};

static const int NKEEPINENTRIES =
   (int)(sizeof(keepin_table) / sizeof(keepin_table[0]));

/*
 * Maxwellian temperature for delayed neutron energy sampling.
 * T = 0.30 MeV gives <E> = (3/2)*T = 0.45 MeV, consistent with the
 * typical average delayed neutron energy of 0.4-0.5 MeV.
 */
static const double DELAYED_MAXWELLIAN_T = 0.30;

/* -------------------------------------------------------------------------
 * smpPoisson -- Knuth algorithm; efficient for small mu (<< 20).
 * For nu_d values in this library (0.002 -- 0.043), this never exceeds
 * a handful of iterations in the rare event that nu > 0.
 * ------------------------------------------------------------------------- */
static int smpPoisson(double mu) {
   if (mu <= 0.0) return 0;
   double L = exp(-mu);
   int    k = 0;
   double p = 1.0;
   do {
      k++;
      p *= fissionEvent::fisslibrng();
   } while (p > L && k < 200); /* safety cap against degenerate RNG */
   return k - 1;
}

/* -------------------------------------------------------------------------
 * smpMaxwellian -- Kellerer's method for f(E) ∝ sqrt(E) exp(-E/T).
 *   E = -T * [ln(r1) + ln(r2) * cos²(π/2 * r3)]
 *   <E> = (3/2) T  (verified by expected-value calculation)
 * Uses 3 random numbers per sample.
 * ------------------------------------------------------------------------- */
static double smpMaxwellian(double T) {
   double r1 = fissionEvent::fisslibrng();
   double r2 = fissionEvent::fisslibrng();
   double r3 = fissionEvent::fisslibrng();
   double c  = cos(1.5707963267948966 * r3); /* cos(pi/2 * r3) */
   return -T * (log(r1) + log(r2) * c * c);
}

/* =========================================================================
 * fissionEvent::extendNeutronArrays
 *
 * Resize all six neutron kinematic arrays to hold n_additional more
 * entries beyond the current neutronNu.  Existing data is preserved;
 * new slots are uninitialised (caller fills them).  neutronNu is NOT
 * incremented here -- that is the caller's responsibility.
 * ========================================================================= */
void fissionEvent::extendNeutronArrays(int n_additional) {
   if (n_additional <= 0) return;

   int nu_new = neutronNu + n_additional;

   double* ne = new double[nu_new];
   double* nv = new double[nu_new];
   double* nu = new double[nu_new];
   double* nV = new double[nu_new];
   double* nw = new double[nu_new];
   double* na = new double[nu_new];

   if (neutronNu > 0) {
      memcpy(ne, neutronEnergies,   neutronNu * sizeof(double));
      memcpy(nv, neutronVelocities, neutronNu * sizeof(double));
      memcpy(nu, neutronDircosu,    neutronNu * sizeof(double));
      memcpy(nV, neutronDircosv,    neutronNu * sizeof(double));
      memcpy(nw, neutronDircosw,    neutronNu * sizeof(double));
      memcpy(na, neutronAges,       neutronNu * sizeof(double));

      delete[] neutronEnergies;
      delete[] neutronVelocities;
      delete[] neutronDircosu;
      delete[] neutronDircosv;
      delete[] neutronDircosw;
      delete[] neutronAges;
   }

   neutronEnergies   = ne;
   neutronVelocities = nv;
   neutronDircosu    = nu;
   neutronDircosv    = nV;
   neutronDircosw    = nw;
   neutronAges       = na;
}

/* =========================================================================
 * fissionEvent::SmpDelayed
 *
 * Sample and append delayed neutrons to the current fission event using
 * the six-group Keepin formalism.  Only active when delayoption >= 2.
 *
 *   isotope     -- ZA of the fissioning nucleus (target, not compound)
 *   time        -- absolute fission time (seconds)
 *   spontaneous -- true for SF, false for neutron-induced fission
 *
 * After this call:
 *   neutronNu    includes both prompt and delayed neutrons
 *   neutronAges  = time             for prompt (delay = 0)
 *   neutronAges  = time + t_delay   for delayed, where t_delay is sampled
 *                                   from exp(lambda_i) for group i
 *
 * Consumers use getnage_(index) - fission_time to obtain the per-neutron
 * emission delay; all neutrons with delay > 0 are delayed neutrons.
 * ========================================================================= */
void fissionEvent::SmpDelayed(int isotope, double time, bool spontaneous) {
   if (delayoption < 2) return;

   /* --- find Keepin parameters for this isotope and fission type --- */
   int fissiontype = spontaneous ? 0 : 1;
   const KeepinParams* params = 0;
   for (int i = 0; i < NKEEPINENTRIES; i++) {
      if (keepin_table[i].isotope    == isotope &&
          keepin_table[i].fissiontype == fissiontype) {
         params = &keepin_table[i];
         break;
      }
   }
   if (!params) return; /* isotope not tabulated -- skip silently */

   /* --- sample total number of delayed neutrons from Poisson(nu_d) --- */
   int nd = smpPoisson(params->nu_d);
   if (nd <= 0) return;

   /* --- extend neutron arrays to accommodate the delayed neutrons --- */
   extendNeutronArrays(nd);

   /* --- build cumulative group probability for group selection --- */
   double cumul[NGROUPS];
   cumul[0] = params->a[0];
   for (int g = 1; g < NGROUPS; g++)
      cumul[g] = cumul[g - 1] + params->a[g];

   /* --- fill in the delayed neutrons --- */
   for (int k = 0; k < nd; k++) {
      int idx = neutronNu + k;

      /* select group by inverse CDF */
      double u_grp = fisslibrng();
      int grp = NGROUPS - 1;
      for (int g = 0; g < NGROUPS - 1; g++) {
         if (u_grp <= cumul[g]) { grp = g; break; }
      }

      /* emission time: exponential with group decay constant */
      double t_delay = -log(fisslibrng()) / params->lambda[grp];

      /* energy: Maxwellian spectrum */
      double energy = smpMaxwellian(DELAYED_MAXWELLIAN_T);
      if (energy < 1.0e-6) energy = 1.0e-6; /* protect against log(0) */
      if (energy > 20.0)   energy = 20.0;

      neutronEnergies[idx]   = energy;
      neutronVelocities[idx] = SmpNVel(energy);
      SmpIsoDir(&neutronDircosu[idx],
                &neutronDircosv[idx],
                &neutronDircosw[idx]);
      neutronAges[idx] = time + t_delay;
   }

   neutronNu += nd;
}
