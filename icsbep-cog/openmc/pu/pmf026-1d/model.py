"""
PMF026-1D: 11.9cm steel reflected spherical assembly of 9.7602 kg delta-239Pu(98%): detailed model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.527200e-02)
mat1.add_nuclide("Pu240", 6.447900e-04)
mat1.add_element("Ga", 2.094600e-03)
mat1.add_element("Fe", 1.565900e-04)
mat1.add_element("C", 2.912300e-04)
mat1.add_element("Ni", 4.145900e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu239", 3.682600e-02)
mat2.add_nuclide("Pu240", 6.732000e-04)
mat2.add_element("Ga", 2.200000e-03)
mat2.add_element("Fe", 1.471400e-04)
mat2.add_element("C", 3.040600e-04)
mat2.add_element("Ni", 1.572200e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Pu239", 3.657900e-02)
mat3.add_nuclide("Pu240", 6.687500e-04)
mat3.add_element("Ga", 2.211400e-03)
mat3.add_element("Fe", 1.299200e-04)
mat3.add_element("C", 3.020500e-04)
mat3.add_element("Ni", 1.933000e-03)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("Pu239", 3.651200e-02)
mat4.add_nuclide("Pu240", 6.673900e-04)
mat4.add_element("Ga", 2.194000e-03)
mat4.add_element("Fe", 1.296600e-04)
mat4.add_element("C", 2.260800e-04)
mat4.add_element("Ni", 2.305600e-03)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("Pu239", 3.657600e-02)
mat5.add_nuclide("Pu240", 6.687800e-04)
mat5.add_element("Ga", 2.211500e-03)
mat5.add_element("Fe", 1.461700e-04)
mat5.add_element("C", 3.020600e-04)
mat5.add_element("Ni", 1.863100e-03)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 7.941600e-02)
mat6.add_element("C", 1.126900e-03)
mat6.add_element("Si", 1.606500e-04)
mat6.add_element("Cr", 2.603200e-04)
mat6.add_element("Mn", 3.285000e-04)
mat6.add_element("Ni", 2.306300e-04)
mat6.add_element("Cu", 2.130000e-04)

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Fe", 7.891900e-02)
mat7.add_element("C", 1.119900e-03)
mat7.add_element("Si", 1.596400e-04)
mat7.add_element("Cr", 2.586900e-04)
mat7.add_element("Mn", 3.264500e-04)
mat7.add_element("Ni", 2.291800e-04)
mat7.add_element("Cu", 2.116700e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# dPu1
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# dPu2
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

# dPu3
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf3 & -surf4

# dPu4
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf4 & -surf5

# dPu5
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf5 & -surf6

# Steel1
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf6 & -surf7

# Steel2
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = +surf7 & -surf8

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
source.space = openmc.stats.Box((-2.0, -2.0, -2.0), (2.0, 2.0, 2.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
