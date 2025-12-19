"""
PMF037-16: Flooded 2x2x5 array of double-canned 3kg Pu parts in water; Hw=47.05; dx=dy=11.994; dz=8.255
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium (cases 14-16)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.603100e-02)
mat1.add_nuclide("Pu240", 2.924900e-03)
mat1.add_nuclide("Pu241", 1.420700e-04)
mat1.add_nuclide("Pu242", 4.858800e-06)
mat1.add_nuclide("Am241", 8.236700e-05)

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
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell3 = openmc.Cell()
u1_cell4 = openmc.Cell(fill=mat4)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CanPart
cell1 = openmc.Cell(cell_id=1, fill=universe1)
cell1.translation = (0.0, 11.994, 10.715)
# CanPart
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.translation = (-11.994, 0.0, 10.715)
# CanPart
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (11.994, 0.0, 10.715)
# CanPart
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.translation = (0.0, -11.994, 10.715)
# CanPart
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.translation = (0.0, 11.994, 18.97)
# CanPart
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.translation = (-11.994, 0.0, 18.97)
# CanPart
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.translation = (11.994, 0.0, 18.97)
# CanPart
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.translation = (0.0, -11.994, 18.97)
# CanPart
cell9 = openmc.Cell(cell_id=9, fill=universe1)
cell9.translation = (0.0, 11.994, 27.225)
# CanPart
cell10 = openmc.Cell(cell_id=10, fill=universe1)
cell10.translation = (-11.994, 0.0, 27.225)
# CanPart
cell11 = openmc.Cell(cell_id=11, fill=universe1)
cell11.translation = (11.994, 0.0, 27.225)
# CanPart
cell12 = openmc.Cell(cell_id=12, fill=universe1)
cell12.translation = (0.0, -11.994, 27.225)
# CanPart
cell13 = openmc.Cell(cell_id=13, fill=universe1)
cell13.translation = (0.0, 11.994, 35.48)
# CanPart
cell14 = openmc.Cell(cell_id=14, fill=universe1)
cell14.translation = (-11.994, 0.0, 35.48)
# CanPart
cell15 = openmc.Cell(cell_id=15, fill=universe1)
cell15.translation = (11.994, 0.0, 35.48)
# CanPart
cell16 = openmc.Cell(cell_id=16, fill=universe1)
cell16.translation = (0.0, -11.994, 35.48)
# CanPart
cell17 = openmc.Cell(cell_id=17, fill=universe1)
cell17.translation = (0.0, 11.994, 43.735)
# CanPart
cell18 = openmc.Cell(cell_id=18, fill=universe1)
cell18.translation = (-11.994, 0.0, 43.735)
# CanPart
cell19 = openmc.Cell(cell_id=19, fill=universe1)
cell19.translation = (11.994, 0.0, 43.735)
# CanPart
cell20 = openmc.Cell(cell_id=20, fill=universe1)
cell20.translation = (0.0, -11.994, 43.735)
# Tray
cell21 = openmc.Cell(cell_id=21, fill=mat5)
# Tray
cell22 = openmc.Cell(cell_id=22, fill=mat5)
# Tray
cell23 = openmc.Cell(cell_id=23, fill=mat5)
# Tray
cell24 = openmc.Cell(cell_id=24, fill=mat5)
# Tray
cell25 = openmc.Cell(cell_id=25, fill=mat5)
# Tray
cell26 = openmc.Cell(cell_id=26, fill=mat5)
# Tray
cell27 = openmc.Cell(cell_id=27, fill=mat5)
# Tray
cell28 = openmc.Cell(cell_id=28, fill=mat5)
# Tray
cell29 = openmc.Cell(cell_id=29, fill=mat5)
# Tray
cell30 = openmc.Cell(cell_id=30, fill=mat5)
# Tray
cell31 = openmc.Cell(cell_id=31, fill=mat5)
# Tray
cell32 = openmc.Cell(cell_id=32, fill=mat5)
# Tray
cell33 = openmc.Cell(cell_id=33, fill=mat5)
# Tray
cell34 = openmc.Cell(cell_id=34, fill=mat5)
# Tray
cell35 = openmc.Cell(cell_id=35, fill=mat5)
# Water
cell36 = openmc.Cell(cell_id=36, fill=mat6)
# Water
cell37 = openmc.Cell(cell_id=37, fill=mat6)
# Water
cell38 = openmc.Cell(cell_id=38, fill=mat6)
# Water
cell39 = openmc.Cell(cell_id=39, fill=mat6)
# Water
cell40 = openmc.Cell(cell_id=40, fill=mat6)
# Water
cell41 = openmc.Cell(cell_id=41, fill=mat6)
# Water
cell42 = openmc.Cell(cell_id=42, fill=mat6)
# Water
cell43 = openmc.Cell(cell_id=43, fill=mat6)
# Water
cell44 = openmc.Cell(cell_id=44, fill=mat6)
# Water
cell45 = openmc.Cell(cell_id=45, fill=mat6)
# Water
cell46 = openmc.Cell(cell_id=46, fill=mat6)
# Water
cell47 = openmc.Cell(cell_id=47, fill=mat6)
# Water
cell48 = openmc.Cell(cell_id=48, fill=mat6)
# Water
cell49 = openmc.Cell(cell_id=49, fill=mat6)
# Water
cell50 = openmc.Cell(cell_id=50, fill=mat6)
# Water
cell51 = openmc.Cell(cell_id=51, fill=mat6)
# Water
cell52 = openmc.Cell(cell_id=52, fill=mat6)
# Water
cell53 = openmc.Cell(cell_id=53, fill=mat6)
# Water
cell54 = openmc.Cell(cell_id=54, fill=mat6)
# Water
cell55 = openmc.Cell(cell_id=55, fill=mat6)
# Water
cell56 = openmc.Cell(cell_id=56, fill=mat6)
# Water
cell57 = openmc.Cell(cell_id=57, fill=mat6)
# Water
cell58 = openmc.Cell(cell_id=58, fill=mat6)
# Water
cell59 = openmc.Cell(cell_id=59, fill=mat6)
# Water
cell60 = openmc.Cell(cell_id=60, fill=mat6)
# Water
cell61 = openmc.Cell(cell_id=61, fill=mat6)
# Tank
cell62 = openmc.Cell(cell_id=62, fill=mat5)
# SS304L
cell68 = openmc.Cell(cell_id=68, fill=mat4)
root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49, cell50, cell51, cell52, cell53, cell54, cell55, cell56, cell57, cell58, cell59, cell60, cell61, cell62, cell68])
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
source.space = openmc.stats.Box((-12.994, -12.994, 13.0285), (12.994, 12.994, 39.7935))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
