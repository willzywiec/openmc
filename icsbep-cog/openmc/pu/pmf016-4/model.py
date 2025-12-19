"""
PMF016-4: Flooded 3x3x3 arrays of 3kg Pu metal cylinders; Hw=62.78; dx=dy=13.00; dz=12.75
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.605400e-02)
mat1.add_nuclide("Pu240", 2.926400e-03)
mat1.add_nuclide("Pu241", 9.988200e-05)
mat1.add_nuclide("Pu242", 4.861300e-06)
mat1.add_nuclide("Am241", 1.246700e-04)

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

# Al-3003
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 3.535800e-02)
mat5.add_element("Cu", 3.089100e-05)
mat5.add_element("Fe", 1.230200e-04)
mat5.add_element("Mn", 2.143800e-04)
mat5.add_element("Si", 2.096800e-04)
mat5.add_element("Zn", 1.504800e-05)
mat5.add_nuclide("H1", 2.689400e-02)
mat5.add_nuclide("O16", 1.344700e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

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

u2_cell0 = openmc.Cell(fill=mat6)
u2_cell1 = openmc.Cell(fill=mat5)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Sleeve
cell1 = openmc.Cell(cell_id=1, fill=universe2)
# Sleeve
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.translation = (-13.0, -13.0, 0.0)
# Sleeve
cell3 = openmc.Cell(cell_id=3, fill=universe2)
cell3.translation = (0.0, -13.0, 0.0)
# Sleeve
cell4 = openmc.Cell(cell_id=4, fill=universe2)
cell4.translation = (13.0, -13.0, 0.0)
# Sleeve
cell5 = openmc.Cell(cell_id=5, fill=universe2)
cell5.translation = (-13.0, 0.0, 0.0)
# Sleeve
cell6 = openmc.Cell(cell_id=6, fill=universe2)
cell6.translation = (13.0, 0.0, 0.0)
# Sleeve
cell7 = openmc.Cell(cell_id=7, fill=universe2)
cell7.translation = (-13.0, 13.0, 0.0)
# Sleeve
cell8 = openmc.Cell(cell_id=8, fill=universe2)
cell8.translation = (0.0, 13.0, 0.0)
# Sleeve
cell9 = openmc.Cell(cell_id=9, fill=universe2)
cell9.translation = (13.0, 13.0, 0.0)
# Water
cell10 = openmc.Cell(cell_id=10, fill=mat6)
# SS304L
cell16 = openmc.Cell(cell_id=16, fill=mat4)
# Al3003
cell19 = openmc.Cell(cell_id=19, fill=mat5)
root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell16, cell19])
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
source.space = openmc.stats.Box((-14.0, -14.0, 40.2), (14.0, 14.0, 42.2))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
