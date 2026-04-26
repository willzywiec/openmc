"""Tests for the full-analog FREYA fission sampling setting (Phase 4).

Analog mode calls FREYA once per fission event and banks all nn correlated
prompt neutrons, with each per-neutron weight rescaled so the total banked
weight equals the non-analog path. These tests cover the Python setting
plumbing — they don't require OpenMC to have been built with the FREYA
fission library, because XML serialization is independent of the C++ build.
"""

import openmc
import pytest


def test_freya_analog_default():
    settings = openmc.Settings()
    assert settings.freya_analog is None


def test_freya_analog_setter_typecheck():
    settings = openmc.Settings()
    with pytest.raises(TypeError):
        settings.freya_analog = "true"
    with pytest.raises(TypeError):
        settings.freya_analog = 1


@pytest.mark.parametrize("value", [True, False])
def test_freya_analog_xml_roundtrip(run_in_tmpdir, value):
    settings = openmc.Settings()
    settings.freya_analog = value
    settings.export_to_xml()

    # Verify the element was written
    import xml.etree.ElementTree as ET
    tree = ET.parse("settings.xml")
    root = tree.getroot()
    elem = root.find("freya_analog")
    assert elem is not None
    assert elem.text == str(value).lower()


def test_freya_analog_omitted_when_unset(run_in_tmpdir):
    settings = openmc.Settings()
    settings.export_to_xml()

    import xml.etree.ElementTree as ET
    tree = ET.parse("settings.xml")
    root = tree.getroot()
    assert root.find("freya_analog") is None
