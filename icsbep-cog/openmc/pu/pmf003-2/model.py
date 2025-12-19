"""
PMF003-2: LLNL Pu Array - 2x2x2 with CH2 reflection on one side - case 102
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium billet
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.601000e-02)
mat1.add_nuclide("Pu240", 2.923600e-03)
mat1.add_nuclide("Pu241", 2.243300e-04)
mat1.add_nuclide("Pu242", 4.856600e-06)

# Aluminum tube, spacer, and can walls and bottoms
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 6.026300e-02)

# Aluminum table top
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.303100e-02)

# Aluminum "top" heat sinks
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 3.674200e-02)

# Aluminum "bottom" heat sinks
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 3.013900e-02)

# Iron (steel) lid
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 8.412200e-02)

# Iron (steel) table support
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Fe", 5.888500e-03)

# Homogenized "shoe"
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Al", 2.926000e-02)
mat8.add_element("Fe", 7.791100e-03)

# Aluminum milled "bottom" heat sinks
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Al", 3.524200e-02)

# Polyethylene (CH2) reflector
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_nuclide("H1", 7.899600e-02)
mat10.add_element("C", 3.949800e-02)
mat10.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat8)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell3 = openmc.Cell(fill=mat5)
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell5 = openmc.Cell(fill=mat1)
u1_cell6 = openmc.Cell(fill=mat2)
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell8 = openmc.Cell(fill=mat4)
u1_cell9 = openmc.Cell(fill=mat9)
u1_cell10 = openmc.Cell(fill=mat6)
u1_cell11 = openmc.Cell(fill=mat1)
u1_cell12 = openmc.Cell(fill=mat2)
u1_cell13 = openmc.Cell(fill=mat2)
u1_cell14 = openmc.Cell(fill=mat4)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11, u1_cell12, u1_cell13, u1_cell14])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Spprt
cell1 = openmc.Cell(cell_id=1, fill=mat7)
# Table
cell2 = openmc.Cell(cell_id=2, fill=mat3)
# Stack1
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (3.82, 3.82, 0.0)
# Stack2
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.translation = (-3.82, 3.82, 0.0)
# Stack3
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.translation = (-3.82, -3.82, 0.0)
# Stack4
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.translation = (3.82, -3.82, 0.0)
# Poly
cell7 = openmc.Cell(cell_id=7, fill=mat10)
# THS
cell23 = openmc.Cell(cell_id=23, fill=mat4)
root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell23])
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
source.space = openmc.stats.Box((-4.82, -4.82, 16.5), (4.82, 4.82, 24.2))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
