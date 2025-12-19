"""
IEU-MET-FAST-003-1S: Bare spherical assembly of 277.312 kg U(36) [Simplified Model] Rev. 2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(36)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.527200e-04)
mat1.add_nuclide("U235", 1.711800e-02)
mat1.add_nuclide("U238", 2.921100e-02)
mat1.add_element("C", 7.738900e-04)
mat1.add_element("Fe", 1.205800e-04)
mat1.add_element("W", 1.008700e-05)
mat1.add_element("Cu", 3.813300e-04)
mat1.add_element("Ni", 4.128800e-04)

materials = openmc.Materials([mat1])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=15.324, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U36
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

root_universe = openmc.Universe(cells=[cell1])
geometry = openmc.Geometry(root_universe)

# ==============================================================================
# Settings
# ==============================================================================

settings = openmc.Settings()
settings.particles = 10000
settings.batches = 150
settings.inactive = 10
settings.run_mode = "eigenvalue"

source = openmc.IndependentSource()
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
