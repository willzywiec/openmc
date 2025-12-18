"""
PU-SOL-THERM-022 (Case 6) Hc = 57.65 @ H/X=872; 18.88 wt-% Pu-240
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 36.0 gPu/L
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 6.731500e-05)
mat1.add_nuclide("Pu240", 1.705700e-05)
mat1.add_nuclide("Pu241", 5.168900e-06)
mat1.add_nuclide("Pu242", 1.021400e-06)
mat1.add_nuclide("Am241", 4.316900e-07)
mat1.add_element("N", 1.549700e-03)
mat1.add_nuclide("O16", 3.567000e-02)
mat1.add_nuclide("H1", 6.318600e-02)
mat1.add_element("Fe", 9.489200e-06)
mat1.add_element("Cr", 3.051500e-06)
mat1.add_element("Ni", 2.162800e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Water
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.672200e-02)
mat2.add_nuclide("O16", 3.336100e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

# SST
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 6.133500e-02)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Ni", 8.106000e-03)

# Cadmium
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cd", 4.634000e-02)

# Paraffin
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 7.991100e-02)
mat5.add_element("C", 3.841900e-02)
mat5.add_s_alpha_beta("c_H_in_CH2")

# Air
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("O16", 1.078400e-05)
mat6.add_element("N", 4.309000e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
# WATER
cell2 = openmc.Cell(cell_id=2, fill=mat2)
# SST
cell3 = openmc.Cell(cell_id=3, fill=mat3)
# SST
cell4 = openmc.Cell(cell_id=4, fill=mat3)
# SST
cell5 = openmc.Cell(cell_id=5, fill=mat3)
# SST
cell6 = openmc.Cell(cell_id=6, fill=mat3)
# AIR
cell7 = openmc.Cell(cell_id=7, fill=mat6)
# AIR
cell8 = openmc.Cell(cell_id=8, fill=mat6)
# AIR
cell9 = openmc.Cell(cell_id=9, fill=mat6)
# AIR
cell10 = openmc.Cell(cell_id=10, fill=mat6)
# AIR
cell11 = openmc.Cell(cell_id=11, fill=mat6)
# AIR
cell12 = openmc.Cell(cell_id=12, fill=mat6)
# AIR
cell13 = openmc.Cell(cell_id=13, fill=mat6)
# AIR
cell14 = openmc.Cell(cell_id=14, fill=mat6)
# AIR
cell15 = openmc.Cell(cell_id=15, fill=mat6)
# AIR
cell16 = openmc.Cell(cell_id=16, fill=mat6)
# AIR
cell17 = openmc.Cell(cell_id=17, fill=mat6)
root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17])
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
source.space = openmc.stats.Box((-18.0, -18.0, 28.0), (18.0, 18.0, 30.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
