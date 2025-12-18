"""
PU-SOL-THERM-022 (Case 13) Hc = 54.24 @ H/X=355; 18.88 wt-% Pu-240; Paraffin + Cd
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 86.0 gPu/L
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 1.608100e-04)
mat1.add_nuclide("Pu240", 4.074600e-05)
mat1.add_nuclide("Pu241", 1.234800e-05)
mat1.add_nuclide("Pu242", 2.400000e-06)
mat1.add_nuclide("Am241", 1.031300e-06)
mat1.add_element("N", 2.288500e-03)
mat1.add_nuclide("O16", 3.691200e-02)
mat1.add_nuclide("H1", 6.142400e-02)
mat1.add_element("Fe", 2.061500e-05)
mat1.add_element("Cr", 6.488400e-06)
mat1.add_element("Ni", 4.595900e-06)
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
cell1.region = +surf1 & -surf2 & +surf6 & -surf7

# WATER
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = -surf2 & +surf8 & -surf9

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf1 & +surf5 & -surf6 & -surf8

# SST
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = -surf1 & -surf8

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf3 & +surf6 & -surf7 & -surf8 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & +surf17 & +surf18

# SST
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf1 & +surf7 & -surf8

# CAD
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf1 & +surf4 & -surf5 & -surf8

# PRFFN
cell8 = openmc.Cell(cell_id=8, fill=mat5)
cell8.region = +surf1 & -surf4 & -surf8

# AIR
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = +surf3 & +surf6 & -surf7 & -surf8 & -surf11

# AIR
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = +surf3 & +surf6 & -surf7 & -surf8 & -surf12

# AIR
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = +surf3 & +surf6 & -surf7 & -surf8 & -surf13

# AIR
cell12 = openmc.Cell(cell_id=12, fill=mat6)
cell12.region = +surf3 & +surf6 & -surf7 & -surf8 & -surf14

# AIR
cell13 = openmc.Cell(cell_id=13, fill=mat6)
cell13.region = +surf3 & +surf6 & -surf7 & -surf8 & -surf15

# AIR
cell14 = openmc.Cell(cell_id=14, fill=mat6)
cell14.region = +surf3 & +surf6 & -surf7 & -surf8 & -surf16

# AIR
cell15 = openmc.Cell(cell_id=15, fill=mat6)
cell15.region = +surf3 & +surf6 & -surf7 & -surf8 & -surf17

# AIR
cell16 = openmc.Cell(cell_id=16, fill=mat6)
cell16.region = +surf3 & +surf6 & -surf7 & -surf8 & -surf18

# AIR
cell17 = openmc.Cell(cell_id=17, fill=mat6)
cell17.region = +surf2 & -surf3 & +surf6 & -surf7

# AIR
cell18 = openmc.Cell(cell_id=18, fill=mat6)
cell18.region = +surf2 & +surf8 & -surf9

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18])
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
source.space = openmc.stats.Box((-18.0, -18.0, 25.0), (18.0, 18.0, 27.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
