"""
SMF011-1: Np-237 sphere surrounded by HEU shells and polyethylene (detailed model)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Np sphere
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Np237", 5.092600e-02)
mat1.add_nuclide("U233", 1.857700e-06)
mat1.add_nuclide("U234", 2.963300e-07)
mat1.add_nuclide("U235", 1.407400e-05)
mat1.add_nuclide("U236", 7.834900e-08)
mat1.add_nuclide("U238", 1.562600e-06)
mat1.add_nuclide("Pu238", 8.234000e-07)
mat1.add_nuclide("Pu239", 1.627100e-05)
mat1.add_nuclide("Pu240", 1.161900e-06)
mat1.add_nuclide("Pu241", 3.116600e-08)
mat1.add_nuclide("Pu242", 1.603200e-07)
mat1.add_nuclide("Am241", 3.337500e-07)
mat1.add_nuclide("Am243", 9.157500e-05)

# Tungsten sheild
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("W", 5.669700e-02)
mat2.add_element("Ni", 3.507900e-03)
mat2.add_element("Fe", 3.686400e-03)

# Inner nickel cladding
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Ni", 9.023400e-02)

# Outer nickel cladding
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Ni", 8.503000e-02)

# SS304
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 6.048300e-02)
mat5.add_element("Cr", 1.646900e-02)
mat5.add_element("Ni", 6.484900e-03)

# Polyethylene reflector shells
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("C", 4.024700e-02)
mat6.add_nuclide("H1", 8.049500e-02)
mat6.add_s_alpha_beta("c_H_in_CH2")

# Polyethylene spacer
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("C", 4.157800e-02)
mat7.add_nuclide("H1", 8.315600e-02)
mat7.add_s_alpha_beta("c_H_in_CH2")

# Aluminum parts
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Al", 6.037600e-02)

# Bottom polyethylene reflector
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("C", 4.105600e-02)
mat9.add_nuclide("H1", 8.211300e-02)
mat9.add_s_alpha_beta("c_H_in_CH2")

# Top polyethylene reflector
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_element("C", 4.101700e-02)
mat10.add_nuclide("H1", 8.203400e-02)
mat10.add_s_alpha_beta("c_H_in_CH2")

# HEU shells
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_nuclide("U234", 4.868700e-04)
mat11.add_nuclide("U235", 4.427800e-02)
mat11.add_nuclide("U236", 2.224400e-04)
mat11.add_nuclide("U238", 2.510700e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Al
cell1 = openmc.Cell(cell_id=1, fill=mat8)
cell1.region = 

# SS304
cell2 = openmc.Cell(cell_id=2, fill=mat5)
cell2.region = 

# SS304
cell3 = openmc.Cell(cell_id=3, fill=mat5)
cell3.region = 

# SS304
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = 

# Al
cell5 = openmc.Cell(cell_id=5, fill=mat8)
cell5.region = 

# Al
cell6 = openmc.Cell(cell_id=6, fill=mat8)
cell6.region = 

# Al
cell7 = openmc.Cell(cell_id=7, fill=mat8)
cell7.region = 

# Al
cell8 = openmc.Cell(cell_id=8, fill=mat8)
cell8.region = 

# Al
cell9 = openmc.Cell(cell_id=9, fill=mat7)
cell9.region = 

# Np
cell10 = openmc.Cell(cell_id=10, fill=mat1)
cell10.region = 

# W
cell11 = openmc.Cell(cell_id=11, fill=mat2)
cell11.region = 

# Ni
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = 

# Ni
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = 

# Al
cell14 = openmc.Cell(cell_id=14, fill=mat8)
cell14.region = 

# Al
cell15 = openmc.Cell(cell_id=15, fill=mat8)
cell15.region = 

# Al
cell16 = openmc.Cell(cell_id=16, fill=mat8)
cell16.region = 

# Al
cell17 = openmc.Cell(cell_id=17, fill=mat8)
cell17.region = 

# HEU
cell18 = openmc.Cell(cell_id=18, fill=mat11)
cell18.region = 

# HEU
cell19 = openmc.Cell(cell_id=19, fill=mat11)
cell19.region = 

# HEU
cell20 = openmc.Cell(cell_id=20, fill=mat11)
cell20.region = 

# HEU
cell21 = openmc.Cell(cell_id=21, fill=mat11)
cell21.region = 

# HEU
cell22 = openmc.Cell(cell_id=22, fill=mat11)
cell22.region = 

# HEU
cell23 = openmc.Cell(cell_id=23, fill=mat11)
cell23.region = 

# HEU
cell24 = openmc.Cell(cell_id=24, fill=mat11)
cell24.region = 

# HEU
cell25 = openmc.Cell(cell_id=25, fill=mat11)
cell25.region = 

# CH2
cell26 = openmc.Cell(cell_id=26, fill=mat6)
cell26.region = 

# CH2
cell27 = openmc.Cell(cell_id=27, fill=mat6)
cell27.region = 

# CH2
cell28 = openmc.Cell(cell_id=28, fill=mat9)
cell28.region = 

# HEU
cell29 = openmc.Cell(cell_id=29, fill=mat11)
cell29.region = 

# HEU
cell30 = openmc.Cell(cell_id=30, fill=mat11)
cell30.region = 

# HEU
cell31 = openmc.Cell(cell_id=31, fill=mat11)
cell31.region = 

# HEU
cell32 = openmc.Cell(cell_id=32, fill=mat11)
cell32.region = 

# HEU
cell33 = openmc.Cell(cell_id=33, fill=mat11)
cell33.region = 

# HEU
cell34 = openmc.Cell(cell_id=34, fill=mat11)
cell34.region = 

# HEU
cell35 = openmc.Cell(cell_id=35, fill=mat11)
cell35.region = 

# HEU
cell36 = openmc.Cell(cell_id=36, fill=mat11)
cell36.region = 

# HEU
cell37 = openmc.Cell(cell_id=37, fill=mat11)
cell37.region = 

# CH2
cell38 = openmc.Cell(cell_id=38, fill=mat6)
cell38.region = 

# CH2
cell39 = openmc.Cell(cell_id=39, fill=mat10)
cell39.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39])
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
