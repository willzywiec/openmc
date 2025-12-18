"""
PMF003-1: LLNL Pu Array - bare - 2x2x2 - case 101
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

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat8)
u1_cell0.region = -surf4 & -surf6
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf4 & +surf5 & -surf6
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = -surf6 & +surf10 & -surf11
u1_cell3 = openmc.Cell(fill=mat5)
u1_cell3.region = +surf11 & -surf12
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell4.region = +surf12 & -surf13
u1_cell5 = openmc.Cell(fill=mat1)
u1_cell5.region = +surf13 & -surf14 & -surf15
u1_cell6 = openmc.Cell(fill=mat2)
u1_cell6.region = +surf13 & +surf14 & -surf15
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = +surf15 & -surf16
u1_cell8 = openmc.Cell(fill=mat4)
u1_cell8.region = +surf16 & -surf17
u1_cell9 = openmc.Cell(fill=mat2)
u1_cell9.region = +surf10 & +surf17 & -surf21
u1_cell10 = openmc.Cell(fill=mat6)
u1_cell10.region = +surf21 & -surf22
u1_cell11 = openmc.Cell(fill=mat1)
u1_cell11.region = -surf14 & +surf22 & -surf23
u1_cell12 = openmc.Cell(fill=mat2)
u1_cell12.region = +surf14 & +surf22 & -surf23
u1_cell13 = openmc.Cell(fill=mat2)
u1_cell13.region = +surf23 & -surf24
u1_cell14 = openmc.Cell(fill=mat4)
u1_cell14.region = +surf24 & -surf25
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11, u1_cell12, u1_cell13, u1_cell14])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Spprt
cell1 = openmc.Cell(cell_id=1, fill=mat7)
cell1.region = -surf1 & -surf2

# Table
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = -surf1 & +surf2 & -surf3

# Stack1
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (3.65, 3.65, 0.0)
cell3.region = -surf1 & +surf3 & -surf41

# Stack2
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.translation = (-3.65, 3.65, 0.0)
cell4.region = -surf1 & +surf3 & -surf42

# Stack3
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.translation = (-3.65, -3.65, 0.0)
cell5.region = -surf1 & +surf3 & -surf43

# Stack4
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.translation = (3.65, -3.65, 0.0)
cell6.region = -surf1 & +surf3 & -surf44

# THS
cell22 = openmc.Cell(cell_id=22, fill=mat4)
cell22.region = +surf24 & -surf25

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell22])
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
source.space = openmc.stats.Box((-4.65, -4.65, 16.5), (4.65, 4.65, 23.9))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
