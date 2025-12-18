"""
PMF037-10: Flooded 2x2x2 array of double-canned 3kg Pu parts in water; Hw=29.6; dx=dy=11.994; dz=8.255
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium (cases 1-10)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.605400e-02)
mat1.add_nuclide("Pu240", 2.926400e-03)
mat1.add_nuclide("Pu241", 1.421400e-04)
mat1.add_nuclide("Pu242", 4.861300e-06)
mat1.add_nuclide("Am241", 8.240900e-05)

# Al-3004
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.831100e-02)
mat2.add_element("Cu", 6.444200e-05)
mat2.add_element("Fe", 2.053100e-04)
mat2.add_element("Mg", 7.076400e-04)
mat2.add_element("Mn", 3.727000e-04)
mat2.add_element("Si", 1.749700e-04)
mat2.add_element("Zn", 6.262500e-05)

# Mild steel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 3.154700e-04)
mat3.add_element("Fe", 8.413100e-02)
mat3.add_element("Mn", 3.189900e-04)
mat3.add_element("P", 2.293700e-05)
mat3.add_element("S", 3.692200e-05)
mat3.add_element("Si", 1.686400e-05)
mat3.add_element("Sn", 1.197000e-04)

# SS-304L
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 1.183300e-04)
mat4.add_element("Cr", 1.738400e-02)
mat4.add_element("Fe", 5.790200e-02)
mat4.add_element("Mn", 1.731900e-03)
mat4.add_element("Ni", 8.106100e-03)
mat4.add_element("Si", 1.693900e-03)

# Al-6061
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 5.818300e-02)
mat5.add_element("Cr", 6.254200e-05)
mat5.add_element("Cu", 6.396800e-05)
mat5.add_element("Fe", 2.038000e-04)
mat5.add_element("Mg", 6.689800e-04)
mat5.add_element("Mn", 4.439500e-05)
mat5.add_element("Si", 3.473600e-04)
mat5.add_element("Ti", 5.093900e-05)
mat5.add_element("Zn", 6.216400e-05)

# Water
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.673500e-02)
mat6.add_nuclide("O16", 3.336800e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = 
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = 
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = 
u1_cell3 = openmc.Cell()
u1_cell3.region = 
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = 
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CanPart
cell1 = openmc.Cell(cell_id=1, fill=universe1)
cell1.translation = (0.0, 0.0, 10.715)
cell1.region = 

# CanPart
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.translation = (11.994, 0.0, 10.715)
cell2.region = 

# CanPart
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (0.0, -11.994, 10.715)
cell3.region = 

# CanPart
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.translation = (11.994, -11.994, 10.715)
cell4.region = 

# CanPart
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.translation = (0.0, 0.0, 18.97)
cell5.region = 

# CanPart
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.translation = (11.994, 0.0, 18.97)
cell6.region = 

# CanPart
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.translation = (0.0, -11.994, 18.97)
cell7.region = 

# CanPart
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.translation = (11.994, -11.994, 18.97)
cell8.region = 

# Tray
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = 

# Tray
cell10 = openmc.Cell(cell_id=10, fill=mat5)
cell10.region = 

# Tray
cell11 = openmc.Cell(cell_id=11, fill=mat5)
cell11.region = 

# Tray
cell12 = openmc.Cell(cell_id=12, fill=mat5)
cell12.region = 

# Tray
cell13 = openmc.Cell(cell_id=13, fill=mat5)
cell13.region = 

# Tray
cell14 = openmc.Cell(cell_id=14, fill=mat5)
cell14.region = 

# Water
cell15 = openmc.Cell(cell_id=15, fill=mat6)
cell15.region = 

# Water
cell16 = openmc.Cell(cell_id=16, fill=mat6)
cell16.region = 

# Water
cell17 = openmc.Cell(cell_id=17, fill=mat6)
cell17.region = 

# Water
cell18 = openmc.Cell(cell_id=18, fill=mat6)
cell18.region = 

# Water
cell19 = openmc.Cell(cell_id=19, fill=mat6)
cell19.region = 

# Water
cell20 = openmc.Cell(cell_id=20, fill=mat6)
cell20.region = 

# Water
cell21 = openmc.Cell(cell_id=21, fill=mat6)
cell21.region = 

# Water
cell22 = openmc.Cell(cell_id=22, fill=mat6)
cell22.region = 

# Water
cell23 = openmc.Cell(cell_id=23, fill=mat6)
cell23.region = 

# Water
cell24 = openmc.Cell(cell_id=24, fill=mat6)
cell24.region = 

# Water
cell25 = openmc.Cell(cell_id=25, fill=mat6)
cell25.region = 

# Tank
cell26 = openmc.Cell(cell_id=26, fill=mat5)
cell26.region = 

# SS304L
cell32 = openmc.Cell(cell_id=32, fill=mat4)
cell32.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell32])
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
source.space = openmc.stats.Box((-1.0, -12.994, 13.0285), (12.994, 1.0, 23.2835))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
