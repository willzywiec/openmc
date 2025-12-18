"""
PU-MET-FAST-035; 13.685 kg d-Pu(98) in 3.15 cm Pb
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.685000e-02)
mat1.add_nuclide("Pu240", 6.736500e-04)
mat1.add_element("Ga", 2.319300e-03)
mat1.add_element("C", 3.042600e-04)
mat1.add_element("Ni", 1.670000e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu239", 3.657900e-02)
mat2.add_nuclide("Pu240", 6.687500e-04)
mat2.add_element("Ga", 2.315500e-03)
mat2.add_element("C", 3.020500e-04)
mat2.add_element("Ni", 1.933000e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Pu239", 3.651200e-02)
mat3.add_nuclide("Pu240", 6.673900e-04)
mat3.add_element("Ga", 2.297800e-03)
mat3.add_element("C", 2.260800e-04)
mat3.add_element("Ni", 2.305600e-03)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("Pu239", 3.657600e-02)
mat4.add_nuclide("Pu240", 6.687800e-04)
mat4.add_element("Ga", 2.328600e-03)
mat4.add_element("C", 3.020600e-04)
mat4.add_element("Ni", 1.863100e-03)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("Pu239", 3.647100e-02)
mat5.add_nuclide("Pu240", 6.666500e-04)
mat5.add_element("Ga", 2.282300e-03)
mat5.add_element("C", 3.011000e-04)
mat5.add_element("Ni", 1.971500e-03)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 1.834700e-05)
mat6.add_nuclide("Pb207", 4.584200e-04)
mat6.add_nuclide("Pb206", 7.891300e-03)
mat6.add_nuclide("Pb207", 7.236400e-03)
mat6.add_nuclide("Pb208", 1.715800e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# VOID
cell1 = openmc.Cell(cell_id=1)
cell1.region = -surf1

# LAYER1
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf1 & -surf2

# LAYER2
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & -surf3

# LAYER3
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf3 & -surf4

# LAYER4
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf4 & -surf5

# LAYER5
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = +surf5 & -surf6

# RFLCTR
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = +surf6 & -surf7

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7])
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0001))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
