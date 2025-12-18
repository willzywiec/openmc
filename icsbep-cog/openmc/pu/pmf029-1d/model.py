"""
PMF029-1D: 0.800cm void; 12.0346kg alpha-239Pu(88%); unreflected; detailed model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# a-Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu241", 8.938400e-04)
mat1.add_element("Fe", 2.998600e-04)
mat1.add_element("C", 1.957700e-03)
mat1.add_element("H", 8.190900e-04)
mat1.add_element("N", 8.841100e-05)
mat1.add_nuclide("O16", 1.310600e-04)

# a-Pu
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu241", 6.714700e-04)
mat2.add_element("Fe", 2.653400e-04)
mat2.add_element("C", 1.105300e-03)
mat2.add_element("H", 2.001100e-04)
mat2.add_element("N", 2.160000e-05)
mat2.add_nuclide("O16", 3.202000e-05)

# a-Pu
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Pu241", 7.407900e-04)
mat3.add_element("Fe", 3.035600e-04)
mat3.add_element("C", 1.192200e-03)
mat3.add_element("H", 2.750500e-04)
mat3.add_element("N", 2.968800e-05)
mat3.add_nuclide("O16", 4.401100e-05)

# a-Pu
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("Pu241", 5.942500e-04)
mat4.add_element("Fe", 2.850000e-04)
mat4.add_element("C", 1.395600e-03)
mat4.add_element("H", 4.330800e-04)
mat4.add_element("N", 4.674600e-05)
mat4.add_nuclide("O16", 6.929700e-05)

# a-Pu
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("Pu241", 8.478700e-04)
mat5.add_element("Fe", 3.639500e-04)
mat5.add_element("C", 1.361700e-03)
mat5.add_element("H", 2.609200e-04)
mat5.add_element("N", 2.816300e-05)
mat5.add_nuclide("O16", 4.174900e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# aPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# aPu
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

# aPu
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf3 & -surf4

# aPu
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf4 & -surf5

# aPu
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf5 & -surf6

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5])
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
