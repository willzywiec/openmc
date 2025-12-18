"""
PMF004-6: LLNL Pu Array Phase II - bare - 4x4x4 - 6kg - case 212
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.601000e-02)
mat1.add_nuclide("Pu240", 2.923600e-03)
mat1.add_nuclide("Pu241", 2.243300e-04)
mat1.add_nuclide("Pu242", 4.856600e-06)
mat1.add_element("Al", 2.179500e-06)
mat1.add_element("Ag", 1.090300e-07)
mat1.add_element("B", 1.087900e-06)
mat1.add_element("C", 1.762600e-04)
mat1.add_element("Ca", 2.934600e-05)
mat1.add_element("Cu", 9.254100e-07)
mat1.add_element("Cr", 4.523900e-06)
mat1.add_element("Fe", 7.370900e-06)
mat1.add_element("Mg", 9.678000e-06)
mat1.add_element("Mn", 1.070400e-06)
mat1.add_element("Na", 5.115800e-07)
mat1.add_element("Ni", 1.002000e-05)
mat1.add_element("Pb", 5.676200e-08)
mat1.add_element("Si", 6.281400e-06)
mat1.add_element("Sn", 1.981800e-07)
mat1.add_element("Ti", 1.228200e-06)

# Aluminum
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.179500e-02)
mat2.add_element("Cu", 1.493800e-03)
mat2.add_element("Fe", 8.094000e-05)
mat2.add_element("Mg", 1.239900e-05)
mat2.add_element("Mn", 8.227900e-05)
mat2.add_element("Si", 1.073000e-04)
mat2.add_element("Ti", 1.888200e-05)
mat2.add_element("Zn", 2.304600e-05)

# Aluminum
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.596300e-02)
mat3.add_element("Cr", 3.149700e-05)
mat3.add_element("Cu", 1.121100e-03)
mat3.add_element("Fe", 1.462200e-04)
mat3.add_element("Mg", 1.010700e-03)
mat3.add_element("Mn", 1.788600e-04)
mat3.add_element("Si", 2.915600e-04)
mat3.add_element("Zn", 6.262300e-05)

# Aluminum
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 5.840200e-02)
mat4.add_element("Cu", 6.444200e-05)
mat4.add_element("Fe", 2.053100e-04)
mat4.add_element("Mg", 7.076400e-04)
mat4.add_element("Mn", 3.727000e-04)
mat4.add_element("Si", 1.749700e-04)
mat4.add_element("Zn", 6.263400e-05)

# Aluminum
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 5.827400e-02)
mat5.add_element("Cr", 6.254200e-05)
mat5.add_element("Cu", 6.396800e-05)
mat5.add_element("Fe", 2.038000e-04)
mat5.add_element("Mg", 6.689800e-04)
mat5.add_element("Mn", 4.439500e-05)
mat5.add_element("Si", 3.473600e-04)
mat5.add_element("Ti", 5.093900e-05)
mat5.add_element("Zn", 6.217400e-05)

# Aluminum
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Al", 3.599700e-02)
mat6.add_element("Cr", 3.863300e-05)
mat6.add_element("Cu", 3.951400e-05)
mat6.add_element("Fe", 1.258900e-04)
mat6.add_element("Mg", 4.132500e-04)
mat6.add_element("Mn", 2.742300e-05)
mat6.add_element("Si", 2.145700e-04)
mat6.add_element("Ti", 3.146600e-05)
mat6.add_element("Zn", 3.840600e-05)

# Aluminum
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Al", 4.476600e-02)
mat7.add_element("Cr", 4.804500e-05)
mat7.add_element("Cu", 4.914000e-05)
mat7.add_element("Fe", 1.565600e-04)
mat7.add_element("Mg", 5.139100e-04)
mat7.add_element("Mn", 3.410400e-05)
mat7.add_element("Si", 2.668400e-04)
mat7.add_element("Ti", 3.913100e-05)
mat7.add_element("Zn", 4.776200e-05)

# Aluminum
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Al", 5.700200e-02)
mat8.add_element("Cr", 3.208200e-05)
mat8.add_element("Cu", 1.141900e-03)
mat8.add_element("Fe", 1.493500e-04)
mat8.add_element("Mg", 1.029500e-03)
mat8.add_element("Mn", 1.821800e-04)
mat8.add_element("Si", 2.969700e-04)
mat8.add_element("Zn", 6.378600e-05)

# Aluminum
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Al", 1.724900e-02)
mat9.add_element("Cr", 1.851200e-05)
mat9.add_element("Cu", 1.893500e-05)
mat9.add_element("Fe", 6.032600e-05)
mat9.add_element("Mg", 1.980200e-04)
mat9.add_element("Mn", 1.314100e-05)
mat9.add_element("Si", 1.028200e-04)
mat9.add_element("Ti", 1.507800e-05)
mat9.add_element("Zn", 1.840300e-05)

# Iron (steel)
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_element("Fe", 8.450600e-02)
mat10.add_element("C", 3.168700e-04)
mat10.add_element("Mn", 3.204100e-04)
mat10.add_element("P", 2.303900e-05)
mat10.add_element("S", 3.709800e-05)
mat10.add_element("Si", 1.693900e-05)
mat10.add_element("Sn", 1.202500e-04)

# Homogenized
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_element("Al", 3.201600e-03)
mat11.add_element("C", 2.092900e-04)
mat11.add_element("Cu", 2.550100e-02)
mat11.add_element("Cr", 5.959600e-04)
mat11.add_element("Fe", 1.090600e-02)
mat11.add_element("Mg", 5.782300e-05)
mat11.add_element("Mn", 5.237800e-05)
mat11.add_element("Mo", 8.343300e-05)
mat11.add_element("Pb", 6.385500e-07)
mat11.add_element("S", 8.253700e-06)
mat11.add_element("Si", 2.168900e-04)
mat11.add_element("Sn", 1.706700e-04)
mat11.add_element("V", 6.103500e-05)
mat11.add_element("Zn", 1.617700e-02)

# Concrete
mat12 = openmc.Material(material_id=12)
mat12.set_density("sum")
mat12.add_element("Al", 7.350000e-04)
mat12.add_element("C", 3.814400e-03)
mat12.add_element("Ca", 1.158800e-02)
mat12.add_element("Fe", 1.968000e-04)
mat12.add_nuclide("H1", 1.486800e-02)
mat12.add_element("Mg", 5.870000e-04)
mat12.add_element("Na", 3.040000e-04)
mat12.add_nuclide("O16", 4.151900e-02)
mat12.add_element("Si", 6.037000e-03)
mat12.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11, mat12])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat5)
u1_cell0.region = 
u1_cell1 = openmc.Cell(fill=mat10)
u1_cell1.region = 
u1_cell2 = openmc.Cell(fill=mat1)
u1_cell2.region = 
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = 
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = 
u1_cell5 = openmc.Cell(fill=mat6)
u1_cell5.region = 
u1_cell6 = openmc.Cell(fill=mat10)
u1_cell6.region = 
u1_cell7 = openmc.Cell(fill=mat1)
u1_cell7.region = 
u1_cell8 = openmc.Cell(fill=mat4)
u1_cell8.region = 
u1_cell9 = openmc.Cell(fill=mat4)
u1_cell9.region = 
u1_cell10 = openmc.Cell(fill=mat7)
u1_cell10.region = 
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10])

u2_cell0 = openmc.Cell(fill=mat11)
u2_cell0.region = 
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = 
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = 
u2_cell3 = openmc.Cell(fill=mat5)
u2_cell3.region = 
u2_cell4 = openmc.Cell(fill=mat5)
u2_cell4.region = 
u2_cell5 = openmc.Cell(fill=mat5)
u2_cell5.region = 
u2_cell6 = openmc.Cell(fill=mat5)
u2_cell6.region = 
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Tube
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.translation = (-30.285, -30.285, 0.0)
cell1.region = 

# Tube
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.translation = (-30.285, -10.095, 0.0)
cell2.region = 

# Tube
cell3 = openmc.Cell(cell_id=3, fill=universe2)
cell3.translation = (-30.285, 10.095, 0.0)
cell3.region = 

# Tube
cell4 = openmc.Cell(cell_id=4, fill=universe2)
cell4.translation = (-30.285, 30.285, 0.0)
cell4.region = 

# Tube
cell5 = openmc.Cell(cell_id=5, fill=universe2)
cell5.translation = (-10.095, -30.285, 0.0)
cell5.region = 

# Tube
cell6 = openmc.Cell(cell_id=6, fill=universe2)
cell6.translation = (-10.095, -10.095, 0.0)
cell6.region = 

# Tube
cell7 = openmc.Cell(cell_id=7, fill=universe2)
cell7.translation = (-10.095, 10.095, 0.0)
cell7.region = 

# Tube
cell8 = openmc.Cell(cell_id=8, fill=universe2)
cell8.translation = (-10.095, 30.285, 0.0)
cell8.region = 

# Tube
cell9 = openmc.Cell(cell_id=9, fill=universe2)
cell9.translation = (10.095, -30.285, 0.0)
cell9.region = 

# Tube
cell10 = openmc.Cell(cell_id=10, fill=universe2)
cell10.translation = (10.095, -10.095, 0.0)
cell10.region = 

# Tube
cell11 = openmc.Cell(cell_id=11, fill=universe2)
cell11.translation = (10.095, 10.095, 0.0)
cell11.region = 

# Tube
cell12 = openmc.Cell(cell_id=12, fill=universe2)
cell12.translation = (10.095, 30.285, 0.0)
cell12.region = 

# Tube
cell13 = openmc.Cell(cell_id=13, fill=universe2)
cell13.translation = (30.285, -30.285, 0.0)
cell13.region = 

# Tube
cell14 = openmc.Cell(cell_id=14, fill=universe2)
cell14.translation = (30.285, -10.095, 0.0)
cell14.region = 

# Tube
cell15 = openmc.Cell(cell_id=15, fill=universe2)
cell15.translation = (30.285, 10.095, 0.0)
cell15.region = 

# Tube
cell16 = openmc.Cell(cell_id=16, fill=universe2)
cell16.translation = (30.285, 30.285, 0.0)
cell16.region = 

# I-beam
cell17 = openmc.Cell(cell_id=17, fill=mat8)
cell17.region = 

# I-beam
cell18 = openmc.Cell(cell_id=18, fill=mat8)
cell18.region = 

# I-beam
cell19 = openmc.Cell(cell_id=19, fill=mat8)
cell19.region = 

# I-beam
cell20 = openmc.Cell(cell_id=20, fill=mat8)
cell20.region = 

# O-beam
cell21 = openmc.Cell(cell_id=21, fill=mat8)
cell21.region = 

# O-beam
cell22 = openmc.Cell(cell_id=22, fill=mat8)
cell22.region = 

# O-beam
cell23 = openmc.Cell(cell_id=23, fill=mat8)
cell23.region = 

# O-beam
cell24 = openmc.Cell(cell_id=24, fill=mat8)
cell24.region = 

# Table
cell25 = openmc.Cell(cell_id=25, fill=mat2)
cell25.region = 

# Frame
cell26 = openmc.Cell(cell_id=26, fill=mat9)
cell26.region = 

# Cncrt
cell27 = openmc.Cell(cell_id=27, fill=mat12)
cell27.region = 

# THS
cell39 = openmc.Cell(cell_id=39, fill=mat7)
cell39.region = 

# Part
cell47 = openmc.Cell(cell_id=47, fill=universe1)
cell47.translation = (0.0, 0.0, 132.2042)
cell47.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell39, cell47])
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
source.space = openmc.stats.Box((-31.285, -31.285, 94.8167), (31.285, 31.285, 141.2733))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
