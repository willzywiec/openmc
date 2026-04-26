"""(alpha,n) source-term integration via ALPHANSO.

Wraps the ALPHANSO neutron-source calculator
(https://github.com/alphanso-org/alphanso) as an :class:`openmc.IndependentSource`.

ALPHANSO is a modern Python replacement for SOURCES-4C: it computes the
(alpha,n) neutron production rate and energy spectrum for a given material
composition using GNDS evaluated nuclear data.

In an actinide system the total neutron source is the sum of three
independent contributions:

  * Spontaneous fission                   -> handled by OpenMC's SF source
  * Induced fission (chain reaction)      -> handled by transport
  * (alpha,n) reactions on light nuclei   -> ALPHANSO

For oxide fuels (UO2, PuO2), MOX, and americium-bearing material, (alpha,n)
is often the dominant non-multiplied neutron source.

Example
-------
>>> import openmc
>>> # PuO2 with isotopic vector
>>> matdef = {'Pu-239': 0.94, 'Pu-240': 0.06, 'O-16': 0.00756, 'O-18': 1.7e-5}
>>> src = openmc.alphanso_source(
...     matdef=matdef,
...     calc_type='homogeneous',
...     position=(0.0, 0.0, 0.0),
... )
>>> model.settings.source = src

Requires the ``alphanso`` package (``pip install alphanso``).
"""

from __future__ import annotations

from typing import Iterable, Mapping, Sequence

import openmc
import openmc.stats


def alphanso_source(
    matdef: Mapping,
    calc_type: str = 'homogeneous',
    *,
    position: Sequence[float] = (0.0, 0.0, 0.0),
    neutron_energy_bins: Iterable[float] | None = None,
    extra_config: Mapping | None = None,
) -> openmc.IndependentSource:
    """Build an :class:`openmc.IndependentSource` from an ALPHANSO calculation.

    Parameters
    ----------
    matdef : dict
        Material composition. Keys are isotope identifiers ('Pu-239',
        natural elements like 'C', or ZAID integers like 4009); values
        are mass (or atom) fractions per ALPHANSO's convention.
    calc_type : {'beam', 'homogeneous', 'interface', 'sandwich'}
        ALPHANSO geometry mode. ``'homogeneous'`` is the typical case for
        a uniform actinide-bearing material.
    position : sequence of float
        Spatial source location ``(x, y, z)`` in cm.
    neutron_energy_bins : iterable of float, optional
        Energy bin edges in MeV passed through to ALPHANSO. If ``None``,
        ALPHANSO's default grid is used.
    extra_config : dict, optional
        Additional keys forwarded into the ALPHANSO config dict (for
        ``calc_type='beam'`` you must include ``beam_energy``, etc.).

    Returns
    -------
    openmc.IndependentSource
        Isotropic point source with energy distribution sampled from
        ALPHANSO's tabulated (alpha,n) neutron spectrum. Strength is set
        to the ALPHANSO yield (n/s/g for ``homogeneous``, n/alpha for
        ``beam``); rescale via ``source.strength`` if a different
        normalisation is desired.
    """
    try:
        from alphanso.transport import Transport
    except ImportError as exc:
        raise ImportError(
            "ALPHANSO is not installed. Install with `pip install alphanso` "
            "to use openmc.alphanso_source()."
        ) from exc

    config: dict = {'calc_type': calc_type, 'matdef': dict(matdef)}
    if neutron_energy_bins is not None:
        config['neutron_energy_bins'] = list(neutron_energy_bins)
    if extra_config:
        config.update(extra_config)

    results = Transport.calculate(config)

    # Pull spectrum and bin edges (MeV in ALPHANSO).
    spectrum = results.get('an_spectrum_absolute')
    if spectrum is None:
        spectrum = results['an_spectrum']
    bins_MeV = results.get('neutron_energy_bins')
    if bins_MeV is None:
        raise RuntimeError(
            "ALPHANSO did not return 'neutron_energy_bins'; cannot build "
            "an OpenMC energy distribution."
        )

    # ALPHANSO returns histogram-style (N edges, N-1 bin densities).
    # OpenMC's Tabular with histogram interpolation expects matching
    # lengths; use linear-linear over bin centres for smoothness.
    n_edges = len(bins_MeV)
    n_vals = len(spectrum)
    if n_vals == n_edges - 1:
        centres_MeV = [
            0.5 * (bins_MeV[i] + bins_MeV[i + 1]) for i in range(n_vals)
        ]
        x_eV = [e * 1e6 for e in centres_MeV]
        p = list(spectrum)
    elif n_vals == n_edges:
        x_eV = [e * 1e6 for e in bins_MeV]
        p = list(spectrum)
    else:
        raise RuntimeError(
            f"ALPHANSO spectrum length ({n_vals}) inconsistent with bin "
            f"edges ({n_edges}); expected N-1 or N."
        )

    energy = openmc.stats.Tabular(x_eV, p, interpolation='linear-linear')

    # Yield: 'an_yield' for beam, 'combined_yield' (alpha-n + SF) for
    # homogeneous, etc. Use whichever ALPHANSO provided; fall back to 1.
    strength = (
        results.get('an_yield')
        or results.get('combined_yield')
        or 1.0
    )

    return openmc.IndependentSource(
        space=openmc.stats.Point(tuple(position)),
        angle=openmc.stats.Isotropic(),
        energy=energy,
        particle='neutron',
        strength=float(strength),
    )


__all__ = ['alphanso_source']
