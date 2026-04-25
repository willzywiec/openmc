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
 * Eight-group Spriggs delayed neutron sampling for the LLNL Fission Library.
 *
 * When delayoption >= 2, delayed neutrons are appended to the fission
 * event's unified neutron array with exponentially-distributed emission
 * times.  Prompt neutrons retain neutronAges[i] = fission_time (delay=0);
 * delayed neutrons have neutronAges[i] = fission_time + sampled_delay.
 * Consumers distinguish prompt from delayed by comparing getnage_() to
 * the fission time passed to gen*fissevt_().
 *
 * GROUP MODEL
 * -----------
 * Uses the Spriggs 8-group consistent half-life basis:
 *   G.D. Spriggs, J.M. Campbell, V.M. Piksaikin,
 *   "An 8-group delayed neutron model based on a consistent set of half-lives",
 *   Progress in Nuclear Energy 41(1-4), 223-251 (2002).
 *
 * KEY INSIGHT: In the classical 6-group Keepin model, fitting both the decay
 * constants (lambda_i) AND abundances (a_i) simultaneously is numerically
 * non-unique.  Different time windows, statistics, and starting guesses all
 * converge to different lambda values, which is why Keepin (1965), Tuttle (1979),
 * and ENDF/B-VIII.0 disagree by 10-20% on the same isotope.
 *
 * Spriggs' fix: fix the 8 lambda values to physical precursor half-lives
 * (Br-87, I-137, Br-88, and five shorter-lived dominant precursors).
 * With lambda fixed, the abundances are the ONLY free parameters -- the fit
 * becomes linear and well-determined.  Results from different experiments for
 * the same isotope agree much better in this basis.
 *
 * ABUNDANCES
 * ----------
 * The per-isotope abundances (a_i) are taken directly from the recommended
 * fast-fission datasets in Table VII of Spriggs, Campbell & Piksaikin (2002).
 * Each entry cites the specific dataset number from Spriggs & Campbell (1999),
 * LA-UR-98-918.  The lambda[] array is isotope-independent and unchanged.
 *
 * ENERGY SPECTRA
 * --------------
 * Maxwellian with T = 0.30 MeV, giving <E> = 0.45 MeV.  Group-resolved
 * spectra (Spriggs 1999, LA-UR-99-4000) can be substituted without changing
 * the API or group structure.
 */

#include "fissionEvent.h"
#include <math.h>
#include <string.h>

#define NGROUPS 8

/*
 * Spriggs 8-group consistent decay constants (s^-1).
 * Derived from dominant precursor half-lives; identical for all isotopes.
 * Source: Spriggs, Campbell & Piksaikin (2002), Prog. Nucl. Energy 41, 223-251.
 *
 *   Group | T_1/2 (s) | lambda (s^-1) | Dominant precursor
 *   ------|-----------|---------------|--------------------
 *     1   |  55.600   |  0.012462     | Br-87
 *     2   |  24.500   |  0.028292     | I-137
 *     3   |  16.300   |  0.042525     | Br-88
 *     4   |   5.210   |  0.133042     |
 *     5   |   2.370   |  0.292468     |
 *     6   |   1.040   |  0.666490     |
 *     7   |   0.424   |  1.634780     |
 *     8   |   0.195   |  3.554570     |
 */
static const double spriggs_lambda[NGROUPS] = {
   0.012462,   /* Group 1: T1/2 = 55.6 s  (Br-87)  */
   0.028292,   /* Group 2: T1/2 = 24.5 s  (I-137)  */
   0.042525,   /* Group 3: T1/2 = 16.3 s  (Br-88)  */
   0.133042,   /* Group 4: T1/2 =  5.21 s          */
   0.292468,   /* Group 5: T1/2 =  2.37 s          */
   0.666490,   /* Group 6: T1/2 =  1.04 s          */
   1.634780,   /* Group 7: T1/2 =  0.424 s         */
   3.554570    /* Group 8: T1/2 =  0.195 s         */
};

struct SpriggsParams {
   int    isotope;      /* ZA number of fissioning nucleus */
   int    fissiontype;  /* 0 = spontaneous, 1 = induced    */
   double nu_d;         /* total delayed neutrons per fission event */
   double a[NGROUPS];   /* relative group abundances (sum = 1); lambda is global */
};

/*
 * Per-isotope 8-group abundances.
 *
 * nu_d: total delayed neutrons per fission at fast-spectrum conditions
 *   (nu_d = beta_eff * nubar).  SF entries use known SF delayed fractions.
 *
 * Abundances: Table VII recommended fast-fission datasets from
 *   Spriggs, Campbell & Piksaikin (2002), Prog. Nucl. Energy 41, 223-251.
 * Dataset numbers reference the Spriggs & Campbell (1999) compilation,
 *   LA-UR-98-918.
 * SF entries use induced-fission abundances of the nearest related isotope
 *   as an approximation; Spriggs (2002) covers only neutron-induced fission.
 */
static const SpriggsParams keepin_table[] = {
   /* ---- induced fission ------------------------------------------------ */

   /* U-233 (92233) fast  nu_d=0.00733  T_mean=12.38 s
    * Spriggs Table VII #42, Maksyutenko (1967), fast fission */
   { 92233, 1, 0.00733,
     {0.0800, 0.1570, 0.1350, 0.2090, 0.3080, 0.0370, 0.0620, 0.0120} },

   /* U-235 (92235) fast  nu_d=0.01585  T_mean=9.10 s
    * Spriggs Table VII #88, Piksaikin (1997), fast fission
    * Critical isotope for Godiva (93.5% U-235). */
   { 92235, 1, 0.01585,
     {0.0340, 0.1500, 0.0990, 0.2000, 0.3120, 0.0930, 0.0870, 0.0250} },

   /* U-238 (92238) fast  nu_d=0.04300  T_mean=5.30 s
    * Spriggs Table VII #118, Keepin (1957), fast fission */
   { 92238, 1, 0.04300,
     {0.0080, 0.1040, 0.0380, 0.1370, 0.2940, 0.1980, 0.1280, 0.0930} },

   /* U-239 (92239) induced -- U-238 abundances used as approximation */
   { 92239, 1, 0.04300,
     {0.0080, 0.1040, 0.0380, 0.1370, 0.2940, 0.1980, 0.1280, 0.0930} },

   /* Pu-239 (94239) fast  nu_d=0.00622  T_mean=10.36 s
    * Spriggs Table VII #207, Besant (1977), fast fission */
   { 94239, 1, 0.00622,
     {0.0290, 0.2250, 0.0950, 0.1490, 0.3510, 0.0370, 0.0970, 0.0170} },

   /* Pu-241 (94241) fast  nu_d=0.01600  T_mean=7.85 s
    * Spriggs Table VII #230, Gudkov (1989), fast fission */
   { 94241, 1, 0.01600,
     {0.0160, 0.1750, 0.0550, 0.1700, 0.2800, 0.1660, 0.1130, 0.0250} },

   /* ---- spontaneous fission -------------------------------------------- */

   /* U-238 SF  nu_d=0.04300 -- U-238 induced abundances (approximate) */
   { 92238, 0, 0.04300,
     {0.0080, 0.1040, 0.0380, 0.1370, 0.2940, 0.1980, 0.1280, 0.0930} },

   /* Pu-238 SF (94238)  nu_d=0.00484 -- Pu-239 abundances (approximate) */
   { 94238, 0, 0.00484,
     {0.0290, 0.2250, 0.0950, 0.1490, 0.3510, 0.0370, 0.0970, 0.0170} },

   /* Pu-240 SF (94240)  nu_d=0.00453 -- Pu-239 abundances (approximate) */
   { 94240, 0, 0.00453,
     {0.0290, 0.2250, 0.0950, 0.1490, 0.3510, 0.0370, 0.0970, 0.0170} },

   /* Pu-242 SF (94242)  nu_d=0.00490 -- Pu-241 abundances (approximate) */
   { 94242, 0, 0.00490,
     {0.0160, 0.1750, 0.0550, 0.1700, 0.2800, 0.1660, 0.1130, 0.0250} },

   /* Cm-244 SF (96244)  nu_d=0.00240 -- Pu-239 abundances (approximate) */
   { 96244, 0, 0.00240,
     {0.0290, 0.2250, 0.0950, 0.1490, 0.3510, 0.0370, 0.0970, 0.0170} },

   /* Cf-252 SF (98252)  nu_d=0.00978
    * Spriggs (2002) Cf-252 dataset #245 (Chulick 1969) has +/-2400% on G3;
    * abundances retained from Brady-England 6g NNLS expansion. */
   { 98252, 0, 0.00978,
     {0.0161, 0.1123, 0.1031, 0.2021, 0.2686, 0.1396, 0.0930, 0.0651} },
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
 * the Spriggs 8-group consistent half-life formalism.
 * Only active when delayoption >= 2.
 *
 *   isotope     -- ZA of the fissioning nucleus (target, not compound)
 *   time        -- absolute fission time (seconds)
 *   spontaneous -- true for SF, false for neutron-induced fission
 *
 * After this call:
 *   neutronNu    includes both prompt and delayed neutrons
 *   neutronAges  = time             for prompt (delay = 0)
 *   neutronAges  = time + t_delay   for delayed, where t_delay is sampled
 *                                   from Exp(lambda_i) for group i
 *
 * Consumers use getnage_(index) - fission_time to obtain the per-neutron
 * emission delay; all neutrons with delay > 0 are delayed neutrons.
 * ========================================================================= */
void fissionEvent::SmpDelayed(int isotope, double time, bool spontaneous) {
   if (delayoption < 2) return;

   /* --- find parameters for this isotope and fission type --- */
   int fissiontype = spontaneous ? 0 : 1;
   const SpriggsParams* params = 0;
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

      /* select group by inverse CDF on fixed Spriggs lambda values */
      double u_grp = fisslibrng();
      int grp = NGROUPS - 1;
      for (int g = 0; g < NGROUPS - 1; g++) {
         if (u_grp <= cumul[g]) { grp = g; break; }
      }

      /* emission time: exponential with Spriggs group decay constant */
      double t_delay = -log(fisslibrng()) / spriggs_lambda[grp];

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
