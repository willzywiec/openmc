"""
PU-MET-FAST-005: 8.471 kg Pu(4.90)-1.00Ga 0 15.778 g/cc in 4.699 cm W-(5.5)Ni-(2.5)Cu-(0.7)Zr Alloy @ 17.21 G/CC
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.729100e-02)
mat1.add_nuclide("Pu240", 1.927700e-03)
mat1.add_nuclide("Pu241", 1.219600e-04)
mat1.add_element("Ga", 1.362800e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("W", 5.146800e-02)
mat2.add_element("Ni", 9.712400e-03)
mat2.add_element("Cu", 4.077400e-03)
mat2.add_element("Zr", 7.952800e-04)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# per Section 3.2
surf1 = openmc.Sphere(surface_id=1, r=5.0419)
# THK = 4.699 cm
surf2 = openmc.Sphere(surface_id=2, r=9.7409, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# pualloy
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# w-alloy
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

root_universe = openmc.Universe(cells=[cell1, cell2])
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
