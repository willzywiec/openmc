"""
PMF030-1S: 8.0372 kg alpha-239Pu(88%); 4.49cm Graphite reflected; detailed model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# a-Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu241", 8.236300e-04)
mat1.add_element("Fe", 3.307100e-04)
mat1.add_element("C", 1.408700e-03)
mat1.add_element("H", 3.566000e-04)
mat1.add_element("N", 3.849100e-05)
mat1.add_nuclide("O16", 5.706000e-05)

# a-Pu
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu241", 9.147400e-04)
mat2.add_element("Fe", 3.068700e-04)
mat2.add_element("C", 2.003500e-03)
mat2.add_element("H", 8.382400e-04)
mat2.add_element("N", 9.047800e-05)
mat2.add_nuclide("O16", 1.341300e-04)

# a-Pu
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Pu241", 6.714700e-04)
mat3.add_element("Fe", 2.653400e-04)
mat3.add_element("C", 1.105300e-03)
mat3.add_element("H", 2.001100e-04)
mat3.add_element("N", 2.160000e-05)
mat3.add_nuclide("O16", 3.202000e-05)

# a-Pu
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("Pu241", 7.478600e-04)
mat4.add_element("Fe", 3.064600e-04)
mat4.add_element("C", 1.203500e-03)
mat4.add_element("H", 2.776700e-04)
mat4.add_element("N", 2.997100e-05)
mat4.add_nuclide("O16", 4.443100e-05)

# a-Pu
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("Pu241", 5.969200e-04)
mat5.add_element("Fe", 2.862800e-04)
mat5.add_element("C", 1.401800e-03)
mat5.add_element("H", 4.350300e-04)
mat5.add_element("N", 4.695600e-05)
mat5.add_nuclide("O16", 6.960900e-05)

# Graphite
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("C", 7.721300e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# aPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = 

# aPu
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = 

# aPu
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = 

# aPu
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = 

# aPu
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = 

# C
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
