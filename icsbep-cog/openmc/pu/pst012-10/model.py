"""
PU-SOL-THERM-012 (Case 10) Hc = 23.11 @ H/X=1164; 18.91 wt-% Pu-240; 5 sides water reflection
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 26.9 gPu/L
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 5.036240e-05)
mat1.add_nuclide("Pu240", 1.276110e-05)
mat1.add_nuclide("Pu241", 3.782790e-06)
mat1.add_nuclide("Pu242", 7.641340e-07)
mat1.add_nuclide("Am241", 4.099310e-07)
mat1.add_element("N", 1.528540e-03)
mat1.add_nuclide("O16", 3.549270e-02)
mat1.add_nuclide("H1", 6.304260e-02)
mat1.add_element("Fe", 6.362090e-06)
mat1.add_element("Cr", 2.045900e-06)
mat1.add_element("Ni", 1.450040e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Water
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.668800e-02)
mat2.add_nuclide("O16", 3.334400e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

# SST
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 6.134400e-02)
mat3.add_element("Cr", 1.647200e-02)
mat3.add_element("Ni", 8.105000e-03)

# Lucoflex
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 4.104700e-02)
mat4.add_element("C", 2.736500e-02)
mat4.add_element("Cl", 1.368200e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Steel
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 8.508600e-02)
mat5.add_element("C", 5.554500e-04)

# Concrete
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 1.035000e-02)
mat6.add_nuclide("B10", 1.602000e-06)
mat6.add_nuclide("O16", 4.347000e-02)
mat6.add_element("Al", 1.563000e-03)
mat6.add_element("Si", 1.417000e-02)
mat6.add_element("Ca", 6.424000e-03)
mat6.add_element("Fe", 7.621000e-04)
mat6.add_s_alpha_beta("c_H_in_H2O")

# Air
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("O16", 1.078400e-05)
mat7.add_element("N", 4.309000e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# AIR
cell1 = openmc.Cell(cell_id=1, fill=mat7)
cell1.region = -surf2

# LCFLX
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = +surf2 & -surf3

# SOLN
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = -surf1 & -surf4

# AIR
cell4 = openmc.Cell(cell_id=4, fill=mat7)
cell4.region = +surf1 & +surf3 & -surf4

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf3 & +surf4 & -surf5

# AIR
cell6 = openmc.Cell(cell_id=6, fill=mat7)
cell6.region = +surf1 & +surf3 & +surf4 & +surf5 & -surf6 & -surf7

# WATER
cell7 = openmc.Cell(cell_id=7, fill=mat2)
cell7.region = -surf1 & +surf3 & +surf4 & +surf5 & -surf6 & -surf7

# STEEL
cell8 = openmc.Cell(cell_id=8, fill=mat5)
cell8.region = +surf6 & -surf7

# AIR
cell9 = openmc.Cell(cell_id=9, fill=mat7)
cell9.region = +surf3 & +surf4 & +surf5 & +surf6 & +surf7 & -surf8

# CNCRT
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = +surf8 & -surf9

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10])
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
source.space = openmc.stats.Point((0.0, 0.0, 11.6))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
