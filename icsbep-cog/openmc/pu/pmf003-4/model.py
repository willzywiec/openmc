"""
PMF003-4: LLNL Pu Array - 3x3x3 with polyethylene reflection on one side - case 104
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

# Polyethylene (CH2) reflector
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_nuclide("H1", 7.899600e-02)
mat9.add_element("C", 3.949800e-02)
mat9.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat8)
u1_cell0.region = 
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = 
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = 
u1_cell3 = openmc.Cell(fill=mat5)
u1_cell3.region = 
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell4.region = 
u1_cell5 = openmc.Cell(fill=mat1)
u1_cell5.region = 
u1_cell6 = openmc.Cell(fill=mat2)
u1_cell6.region = 
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = 
u1_cell8 = openmc.Cell(fill=mat4)
u1_cell8.region = 
u1_cell9 = openmc.Cell(fill=mat2)
u1_cell9.region = 
u1_cell10 = openmc.Cell(fill=mat5)
u1_cell10.region = 
u1_cell11 = openmc.Cell(fill=mat6)
u1_cell11.region = 
u1_cell12 = openmc.Cell(fill=mat1)
u1_cell12.region = 
u1_cell13 = openmc.Cell(fill=mat2)
u1_cell13.region = 
u1_cell14 = openmc.Cell(fill=mat2)
u1_cell14.region = 
u1_cell15 = openmc.Cell(fill=mat4)
u1_cell15.region = 
u1_cell16 = openmc.Cell(fill=mat2)
u1_cell16.region = 
u1_cell17 = openmc.Cell(fill=mat5)
u1_cell17.region = 
u1_cell18 = openmc.Cell(fill=mat6)
u1_cell18.region = 
u1_cell19 = openmc.Cell(fill=mat1)
u1_cell19.region = 
u1_cell20 = openmc.Cell(fill=mat2)
u1_cell20.region = 
u1_cell21 = openmc.Cell(fill=mat2)
u1_cell21.region = 
u1_cell22 = openmc.Cell(fill=mat4)
u1_cell22.region = 
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11, u1_cell12, u1_cell13, u1_cell14, u1_cell15, u1_cell16, u1_cell17, u1_cell18, u1_cell19, u1_cell20, u1_cell21, u1_cell22])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Spprt
cell1 = openmc.Cell(cell_id=1, fill=mat7)
cell1.region = 

# Table
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = 

# Stack1
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (-10.15, 10.15, 0.0)
cell3.region = 

# Stack2
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.translation = (-10.15, 0.0, 0.0)
cell4.region = 

# Stack3
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.translation = (-10.15, -10.15, 0.0)
cell5.region = 

# Stack4
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.translation = (0.0, 10.15, 0.0)
cell6.region = 

# Stack5
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.translation = (0.0, 0.0, 0.0)
cell7.region = 

# Stack6
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.translation = (0.0, -10.15, 0.0)
cell8.region = 

# Stack7
cell9 = openmc.Cell(cell_id=9, fill=universe1)
cell9.translation = (10.15, 10.15, 0.0)
cell9.region = 

# Stack8
cell10 = openmc.Cell(cell_id=10, fill=universe1)
cell10.translation = (10.15, 0.0, 0.0)
cell10.region = 

# Stack9
cell11 = openmc.Cell(cell_id=11, fill=universe1)
cell11.translation = (10.15, -10.15, 0.0)
cell11.region = 

# Poly
cell12 = openmc.Cell(cell_id=12, fill=mat9)
cell12.region = 

# THS
cell36 = openmc.Cell(cell_id=36, fill=mat4)
cell36.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell36])
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
source.space = openmc.stats.Box((-11.15, -11.15, 16.5), (11.15, 11.15, 33.8))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
