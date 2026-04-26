"""Tests for FreyaSFSource (Phase 5).

Spontaneous-fission source backed by FREYA's correlated event generator.
Covers Python plumbing only — XML round-trip and type checking. Running
with FREYA actually loaded is a build-dependent integration test.
"""

import openmc
import pytest


def test_freya_sf_defaults():
    src = openmc.FreyaSFSource(za=98252)
    assert src.type == 'freya_sf'
    assert src.za == 98252
    assert src.position == (0.0, 0.0, 0.0)
    assert src.n_events == 10000
    assert src.include_photons is False
    assert src.seed == 1
    assert src.strength == 1.0


def test_freya_sf_full_config():
    src = openmc.FreyaSFSource(
        za=94240,
        position=(1.5, 2.5, 3.5),
        n_events=50000,
        include_photons=True,
        seed=42,
        strength=2.7e3,
    )
    assert src.za == 94240
    assert src.position == (1.5, 2.5, 3.5)
    assert src.n_events == 50000
    assert src.include_photons is True
    assert src.seed == 42
    assert src.strength == 2.7e3


@pytest.mark.parametrize("bad_za", [0, -1, 1.5])
def test_freya_sf_za_validation(bad_za):
    with pytest.raises((ValueError, TypeError)):
        openmc.FreyaSFSource(za=bad_za)


def test_freya_sf_position_validation():
    with pytest.raises(ValueError):
        openmc.FreyaSFSource(za=98252, position=(1.0, 2.0))
    with pytest.raises(ValueError):
        openmc.FreyaSFSource(za=98252, position=(1.0, 2.0, 3.0, 4.0))


@pytest.mark.parametrize("bad_n", [0, -100, 1.5])
def test_freya_sf_n_events_validation(bad_n):
    with pytest.raises((ValueError, TypeError)):
        openmc.FreyaSFSource(za=98252, n_events=bad_n)


def test_freya_sf_xml_roundtrip():
    src = openmc.FreyaSFSource(
        za=98252,
        position=(0.5, -1.0, 2.0),
        n_events=5000,
        include_photons=True,
        seed=9,
        strength=4.2,
    )
    elem = src.to_xml_element()

    assert elem.tag == 'source'
    assert elem.get('type') == 'freya_sf'
    assert float(elem.get('strength')) == 4.2

    # Round-trip parse
    parsed = openmc.SourceBase.from_xml_element(elem)
    assert isinstance(parsed, openmc.FreyaSFSource)
    assert parsed.za == 98252
    assert parsed.position == (0.5, -1.0, 2.0)
    assert parsed.n_events == 5000
    assert parsed.include_photons is True
    assert parsed.seed == 9
    assert parsed.strength == pytest.approx(4.2)


def test_freya_sf_settings_integration(run_in_tmpdir):
    """Settings.export_to_xml() should accept a FreyaSFSource."""
    settings = openmc.Settings()
    settings.run_mode = 'fixed source'
    settings.particles = 100
    settings.batches = 5
    settings.source = openmc.FreyaSFSource(za=98252, n_events=100)
    settings.export_to_xml()

    # Verify the XML element is well-formed
    import xml.etree.ElementTree as ET
    tree = ET.parse('settings.xml')
    src_elem = tree.getroot().find('source')
    assert src_elem is not None
    assert src_elem.get('type') == 'freya_sf'
    assert src_elem.find('za').text == '98252'
