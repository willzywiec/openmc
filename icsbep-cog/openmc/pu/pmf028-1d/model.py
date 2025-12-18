"""
PMF028-1D: 1.176cm void; 9.821 kg delta-239Pu(89%); 19.65cm Steel reflector; detailed model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# d-Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu241", 3.656900e-04)
mat1.add_element("Ga", 2.212600e-03)
mat1.add_element("Fe", 3.946200e-04)
mat1.add_element("C", 7.645100e-04)
mat1.add_element("Ni", 2.096200e-03)

# d-Pu
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu241", 3.904000e-04)
mat2.add_element("Ga", 2.124900e-03)
mat2.add_element("Fe", 4.171100e-04)
mat2.add_element("C", 8.533500e-04)
mat2.add_element("Ni", 8.677400e-04)

# d-Pu
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Pu241", 3.222100e-04)
mat3.add_element("Ga", 2.228000e-03)
mat3.add_element("Fe", 4.801400e-04)
mat3.add_element("C", 9.238000e-04)
mat3.add_element("Ni", 1.344400e-03)

# d-Pu
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("Pu241", 4.350600e-04)
mat4.add_element("Ga", 2.295800e-03)
mat4.add_element("Fe", 4.282900e-04)
mat4.add_element("C", 8.425100e-04)
mat4.add_element("Ni", 1.778200e-03)

# d-Pu
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("Pu241", 4.050300e-04)
mat5.add_element("Ga", 2.259000e-03)
mat5.add_element("Fe", 4.783000e-04)
mat5.add_element("C", 9.969300e-04)
mat5.add_element("Ni", 1.518700e-03)

# Steel
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 7.949900e-02)
mat6.add_element("C", 1.128100e-03)
mat6.add_element("Si", 1.608100e-04)
mat6.add_element("Cr", 2.605900e-04)
mat6.add_element("Mn", 3.288500e-04)
mat6.add_element("Ni", 2.308700e-04)
mat6.add_element("Cu", 2.132300e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# dPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = 

# dPu
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = 

# dPu
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = 

# dPu
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = 

# dPu
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = 

# Steel
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6])
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
source.space = openmc.stats.Box((-3.0, -3.0, -3.0), (3.0, 3.0, 3.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
