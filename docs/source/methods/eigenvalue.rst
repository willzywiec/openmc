.. _methods_eigenvalue:

=======================
Eigenvalue Calculations
=======================

An eigenvalue calculation, also referred to as a criticality calculation, is a
transport simulation wherein the source of neutrons includes a fissionable
material. Some common eigenvalue calculations include the simulation of nuclear
reactors, spent fuel pools, nuclear weapons, and other fissile systems. The
reason they are called *eigenvalue* calculations is that the transport equation
becomes an eigenvalue equation if a fissionable source is present since then the
source of neutrons will depend on the flux of neutrons itself. Eigenvalue
simulations using Monte Carlo methods are becoming increasingly common with the
advent of high-performance computing.

This section will explore the theory behind and implementation of eigenvalue
calculations in a Monte Carlo code.

.. _method-successive-generations:

--------------------------------
Method of Successive Generations
--------------------------------

The method used to converge on the fission source distribution in an eigenvalue
calculation, known as the method of successive generations, was first introduced
by [Lieberoth]_. In this method, a finite number of neutron histories,
:math:`N`, are tracked through their lifetime iteratively. If fission occurs,
rather than tracking the resulting fission neutrons, the spatial coordinates of
the fission site, the sampled outgoing energy and direction of the fission
neutron, and the weight of the neutron are stored for use in the subsequent
generation. In OpenMC, the array used for storing the fission site information
is called the *fission bank*. At the end of each fission generation, :math:`N`
source sites for the next generation must be randomly sampled from the :math:`M`
fission sites that were stored to ensure that the neutron population does not
grow exponentially. The sampled source sites are stored in an array called the
*source bank* and can be retrieved during the subsequent generation.

It's important to recognize that in the method of successive generations, we
must start with some assumption on how the fission source sites are distributed
since the distribution is not known *a priori*. Typically, a user will make a
guess as to what the distribution is -- this guess could be a uniform
distribution over some region of the geometry or simply a point
source. Fortunately, regardless of the choice of initial source distribution,
the method is guaranteed to converge to the true source distribution. Until the
source distribution converges, tallies should not be scored to since they will
otherwise include contributions from an unconverged source distribution.

The method by which the fission source iterations are parallelized can have a
large impact on the achievable parallel scaling. This topic is discussed at length
in :ref:`fission-bank-algorithms`.

-------------------------
Source Convergence Issues
-------------------------

.. _methods-shannon-entropy:

Diagnosing Convergence with Shannon Entropy
-------------------------------------------

As discussed earlier, it is necessary to converge both :math:`k_{eff}` and the
source distribution before any tallies can begin. Moreover, the convergence rate
of the source distribution is in general slower than that of :math:`k_{eff}`.
One should thus examine not only the convergence of :math:`k_{eff}` but also the
convergence of the source distribution in order to make decisions on when to
start active batches.

However, the representation of the source distribution makes it a bit more
difficult to analyze its convergence. Since :math:`k_{eff}` is a scalar
quantity, it is easy to simply look at a line plot of :math:`k_{eff}` versus the
number of batches and this should give the user some idea about whether it has
converged. On the other hand, the source distribution at any given batch is a
finite set of coordinates in Euclidean space. In order to analyze the
convergence, we would either need to use a method for assessing convergence of
an N-dimensional quantity or transform our set of coordinates into a scalar
metric. The latter approach has been developed considerably over the last decade
and a method now commonly used in Monte Carlo eigenvalue calculations is to use
a metric called the `Shannon entropy`_, a concept borrowed from information
theory.

To compute the Shannon entropy of the source distribution, we first need to
discretize the source distribution rather than having a set of coordinates in
Euclidean space. This can be done by superimposing a structured mesh over the
geometry (containing at least all fissionable materials). Then, the fraction of
source sites that are present in each mesh element is counted:

.. math::
    :label: fraction-source

    S_i = \frac{\text{Source sites in $i$-th mesh element}}{\text{Total number of
    source sites}}

The Shannon entropy is then computed as

.. math::
    :label: shannon-entropy

    H = - \sum_{i=1}^N S_i \log_2 S_i

where :math:`N` is the number of mesh elements. With equation
:eq:`shannon-entropy`, we now have a scalar metric that we can use to assess the
convergence of the source distribution by observing line plots of the Shannon
entropy versus the number of batches.

In recent years, researchers have started looking at ways of automatically
assessing source convergence to relieve the burden on the user of having to look
at plots of :math:`k_{eff}` and the Shannon entropy. A number of methods have
been proposed (see e.g. [Romano]_, [Ueki]_), but each of these is not without
problems.

Shannon entropy is calculated differently for the random ray solver, as
described :ref:`in the random ray theory section
<methods-shannon-entropy-random-ray>`. Additionally, as the Shannon entropy only
serves as a diagnostic tool for convergence of the fission source distribution,
there is currently no diagnostic to determine if the scattering source
distribution in random ray is converged.

---------------------------
Uniform Fission Site Method
---------------------------

Generally speaking, the variance of a Monte Carlo tally will be inversely
proportional to the number of events that score to the tally. In a reactor
problem, this implies that regions with low relative power density will have
higher variance that regions with high relative power density. One method to
circumvent the uneven distribution of relative errors is the uniform fission
site (UFS) method introduced by [Sutton]_. In this method, the portion of the
problem containing fissionable material is subdivided into a number of cells
(typically using a structured mesh). Rather than producing

.. math::

    m = \frac{w}{k} \frac{\nu\Sigma_f}{\Sigma_t}

fission sites at each collision where :math:`w` is the weight of the neutron,
:math:`k` is the previous-generation estimate of the neutron multiplication
factor, :math:`\nu\Sigma_f` is the neutron production cross section, and
:math:`\Sigma_t` is the total cross section, in the UFS method we produce

.. math::

    m_{UFS} = \frac{w}{k} \frac{\nu\Sigma_f}{\Sigma_t} \frac{v_i}{s_i}

fission sites at each collision where :math:`v_i` is the fraction of the total
volume occupied by cell :math:`i` and :math:`s_i` is the fraction of the fission
source contained in cell :math:`i`. To ensure that no bias is introduced, the
weight of each fission site stored in the fission bank is :math:`s_i/v_i` rather
than unity. By ensuring that the expected number of fission sites in each mesh
cell is constant, the collision density across all cells, and hence the variance
of tallies, is more uniform than it would be otherwise.

.. _methods_alpha_eigenvalue:

-----------------------
Alpha Eigenvalue Solver
-----------------------

In addition to the standard :math:`k`-eigenvalue, OpenMC can calculate the alpha
eigenvalue (:math:`\alpha`), which represents the time constant governing the
exponential growth or decay of the prompt neutron population. The alpha
eigenvalue depends on the effective delayed neutron fraction
:math:`\beta_\text{eff}` and the IFP-weighted prompt generation time
:math:`\Lambda_p`.

Two forms of the alpha eigenvalue are reported, where :math:`k_p = k_\text{eff}
\cdot (1 - \beta_\text{eff})` is the prompt multiplication factor:

1. The **delayed critical alpha** assumes the system is exactly delayed critical
   (:math:`\rho = 0`):

   .. math::

       \alpha_\text{dc} = \frac{-\beta_\text{eff}}{\Lambda_p \cdot k_p}

2. The **static alpha** uses the system's actual reactivity state:

   .. math::

       \alpha = \frac{k_p - 1}{\Lambda_p \cdot k_p}

A negative :math:`\alpha` indicates that prompt neutrons are decaying (the
system is below prompt critical), :math:`\alpha = 0` corresponds to prompt
criticality, and a positive :math:`\alpha` means the prompt neutron population
is growing exponentially.

Iterated Fission Probability (IFP) Method
-----------------------------------------

The generation times and delayed neutron fraction used in the alpha calculation
are computed using the Iterated Fission Probability (IFP) method
[Hurwitz_1964]_. IFP provides adjoint-weighted kinetics parameters without
requiring an explicit adjoint transport calculation. The key insight is that the
importance of a neutron can be estimated by tracking its descendants over
several generations: a neutron whose progeny survive and continue to cause
fissions has high importance, while one whose line dies out has low importance.

OpenMC implements IFP by maintaining a *genealogy* for each fission neutron.
Each genealogy is a rolling window of size :math:`N_\text{gen}` (set via
``settings.ifp_n_generation``, default 10) that records the properties of the
neutron's direct ancestors. Two genealogy chains are tracked in parallel:

- **Lifetime genealogy**: records the neutron lifetime (time from birth to next
  fission) at each ancestor generation.
- **Delayed group genealogy**: records the delayed neutron group number (1--6
  for delayed, 0 for prompt) at each ancestor generation.

When a fission occurs, the new fission site inherits its parent's genealogy,
extended by one generation with the parent's current lifetime and delayed group
number. The oldest entry is discarded once the genealogy reaches size
:math:`N_\text{gen}`. Tallies are scored only from fission sites whose
genealogy has reached full length, ensuring that the importance weighting has
converged over :math:`N_\text{gen}` generations.

IFP Tally Scores
~~~~~~~~~~~~~~~~

When alpha calculations are enabled (``settings.calculate_alpha = True``),
OpenMC creates an internal tally with four IFP scores:

.. table:: **IFP tally scores for alpha eigenvalue calculation**
   :align: center

   =================================== ====================================================
   Score                               What it accumulates
   =================================== ====================================================
   ``ifp-time-numerator``              :math:`\ell_0 \cdot w` (ancestor lifetime × weight)
   ``ifp-denominator``                 :math:`w` (particle weight at fission)
   ``ifp-prompt-time-numerator``       :math:`\ell_0 \cdot w` (prompt ancestors only)
   ``ifp-prompt-denominator``          :math:`w` (prompt ancestors only)
   =================================== ====================================================

Here :math:`\ell_0` is the lifetime of the oldest tracked ancestor (i.e., the
ancestor :math:`N_\text{gen}` generations back) and :math:`w` is the statistical
weight of the fission neutron being scored. The "prompt" variants score only when
the oldest ancestor was a prompt neutron (delayed group = 0), filtering out
fission chains that passed through a delayed neutron emission.

A fission neutron contributes to the tally only when its genealogy has reached
the required length of :math:`N_\text{gen}` entries. This means that the first
:math:`N_\text{gen}` generations of the simulation (typically covered by
inactive batches) are used to build up the genealogies before scoring begins.

From Tally Scores to Kinetics Parameters
~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~

The effective generation time :math:`\Lambda_\text{eff}` is the ratio of the
IFP-weighted lifetime to the IFP normalization, divided by :math:`k_\text{eff}`:

.. math::

    \Lambda_\text{eff} = \frac{S_\text{ifp-time-numerator}}{S_\text{ifp-denominator} \times k_\text{eff}}

The prompt generation time :math:`\Lambda_p` uses the prompt-only scores:

.. math::

    \Lambda_p = \frac{S_\text{ifp-prompt-time-numerator}}{S_\text{ifp-prompt-denominator} \times k_\text{eff}}

The effective delayed neutron fraction is obtained from the prompt
:math:`k`-eigenvalue:

.. math::

    \beta_\text{eff} = \frac{k_\text{eff} - k_\text{prompt}}{k_\text{eff}}

where :math:`k_\text{prompt}` is scored using a tracklength estimator that
excludes delayed neutron contributions.

With these three quantities and the prompt multiplication factor
:math:`k_p = k_\text{eff} \cdot (1 - \beta_\text{eff})`, the two alpha
eigenvalues are computed as:

.. math::

    \alpha_\text{dc} &= \frac{-\beta_\text{eff}}{\Lambda_p \cdot k_p} \\
    \alpha &= \frac{k_p - 1}{\Lambda_p \cdot k_p}

Uncertainties on all derived quantities are computed via standard error
propagation from the tally variances and the variance of
:math:`k_\text{eff}`.

.. _Shannon entropy: https://mcnp.lanl.gov/pdf_files/TechReport_2006_LANL_LA-UR-06-3737_Brown.pdf

.. [Lieberoth] J. Lieberoth, "A Monte Carlo Technique to Solve the Static
   Eigenvalue Problem of the Boltzmann Transport Equation," *Nukleonik*, **11**,
   213-219 (1968).

.. [Romano] Paul K. Romano, "Application of the Stochastic Oscillator to Assess
   Source Convergence in Monte Carlo Criticality Calculations,"
   *Proc. International Conference on Mathematics, Computational Methods, and
   Reactor Physics*, Saratoga Springs, New York (2009).

.. [Sutton] Daniel J. Kelly, Thomas M. Sutton, and Stephen C. Wilson, "MC21
   Analysis of the Nuclear Energy Agency Monte Carlo Performance Benchmark
   Problem," *Proc. PHYSOR 2012*, Knoxville, Tennessee, Apr. 15--20 (2012).

.. [Ueki] Taro Ueki, "On-the-Fly Judgments of Monte Carlo Fission Source
   Convergence," *Trans. Am. Nucl. Soc.*, **98**, 512 (2008).
