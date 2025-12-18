"""
SMF014-1: Np-237 sphere surrounded by HEU shells and low carbon steel (detailed model)
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

# SS301
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 6.275800e-02)
mat6.add_element("Cr", 1.438000e-02)
mat6.add_element("Ni", 4.777500e-03)

# Aluminum spacer
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Al", 5.897300e-02)

# Other aluminum parts
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Al", 6.037600e-02)

# Bottom Fe reflector
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Fe", 8.302000e-02)

# Top Fe reflector
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_element("Fe", 8.293500e-02)

# HEU shells
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_nuclide("U234", 4.876600e-04)
mat11.add_nuclide("U235", 4.434900e-02)
mat11.add_nuclide("U236", 2.228000e-04)
mat11.add_nuclide("U238", 2.514700e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Al
cell1 = openmc.Cell(cell_id=1, fill=mat8)
# SS304
cell2 = openmc.Cell(cell_id=2, fill=mat5)
# SS304
cell3 = openmc.Cell(cell_id=3, fill=mat5)
# SS304
cell4 = openmc.Cell(cell_id=4, fill=mat5)
# Al
cell5 = openmc.Cell(cell_id=5, fill=mat8)
# Al
cell6 = openmc.Cell(cell_id=6, fill=mat8)
# Al
cell7 = openmc.Cell(cell_id=7, fill=mat8)
# Al
cell8 = openmc.Cell(cell_id=8, fill=mat8)
# Al
cell9 = openmc.Cell(cell_id=9, fill=mat7)
# Np
cell10 = openmc.Cell(cell_id=10, fill=mat1)
# W
cell11 = openmc.Cell(cell_id=11, fill=mat2)
# Ni
cell12 = openmc.Cell(cell_id=12, fill=mat3)
# Ni
cell13 = openmc.Cell(cell_id=13, fill=mat3)
# Al
cell14 = openmc.Cell(cell_id=14, fill=mat8)
# Al
cell15 = openmc.Cell(cell_id=15, fill=mat8)
# Al
cell16 = openmc.Cell(cell_id=16, fill=mat8)
# Al
cell17 = openmc.Cell(cell_id=17, fill=mat8)
# HEU
cell18 = openmc.Cell(cell_id=18, fill=mat11)
# HEU
cell19 = openmc.Cell(cell_id=19, fill=mat11)
# HEU
cell20 = openmc.Cell(cell_id=20, fill=mat11)
# HEU
cell21 = openmc.Cell(cell_id=21, fill=mat11)
# HEU
cell22 = openmc.Cell(cell_id=22, fill=mat11)
# HEU
cell23 = openmc.Cell(cell_id=23, fill=mat11)
# HEU
cell24 = openmc.Cell(cell_id=24, fill=mat11)
# HEU
cell25 = openmc.Cell(cell_id=25, fill=mat11)
# HEU
cell26 = openmc.Cell(cell_id=26, fill=mat11)
# HEU
cell27 = openmc.Cell(cell_id=27, fill=mat11)
# Fe
cell28 = openmc.Cell(cell_id=28, fill=mat9)
# HEU
cell29 = openmc.Cell(cell_id=29, fill=mat11)
# HEU
cell30 = openmc.Cell(cell_id=30, fill=mat11)
# HEU
cell31 = openmc.Cell(cell_id=31, fill=mat11)
# HEU
cell32 = openmc.Cell(cell_id=32, fill=mat11)
# HEU
cell33 = openmc.Cell(cell_id=33, fill=mat11)
# HEU
cell34 = openmc.Cell(cell_id=34, fill=mat11)
# HEU
cell35 = openmc.Cell(cell_id=35, fill=mat11)
# HEU
cell36 = openmc.Cell(cell_id=36, fill=mat11)
# HEU
cell37 = openmc.Cell(cell_id=37, fill=mat11)
# HEU
cell38 = openmc.Cell(cell_id=38, fill=mat11)
# Fe
cell39 = openmc.Cell(cell_id=39, fill=mat10)
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
