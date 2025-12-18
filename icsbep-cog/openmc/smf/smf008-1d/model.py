"""
SMF008-1: Np-237 sphere surrounded by HEU shells (detailed model)
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
mat7.add_element("Al", 5.923800e-02)

# Other aluminum parts
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Al", 6.037600e-02)

# HEU shell #21
mat21 = openmc.Material(material_id=21)
mat21.set_density("sum")
mat21.add_nuclide("U234", 4.896100e-04)
mat21.add_nuclide("U235", 4.452700e-02)
mat21.add_nuclide("U236", 2.236900e-04)
mat21.add_nuclide("U238", 2.524800e-03)

# HEU shell #22
mat22 = openmc.Material(material_id=22)
mat22.set_density("sum")
mat22.add_nuclide("U234", 4.894600e-04)
mat22.add_nuclide("U235", 4.451300e-02)
mat22.add_nuclide("U236", 2.236200e-04)
mat22.add_nuclide("U238", 2.524000e-03)

# HEU shell #23
mat23 = openmc.Material(material_id=23)
mat23.set_density("sum")
mat23.add_nuclide("U234", 4.892300e-04)
mat23.add_nuclide("U235", 4.449300e-02)
mat23.add_nuclide("U236", 2.235200e-04)
mat23.add_nuclide("U238", 2.522800e-03)

# HEU shell #24
mat24 = openmc.Material(material_id=24)
mat24.set_density("sum")
mat24.add_nuclide("U234", 4.905200e-04)
mat24.add_nuclide("U235", 4.460900e-02)
mat24.add_nuclide("U236", 2.241000e-04)
mat24.add_nuclide("U238", 2.529500e-03)

# HEU shell #25
mat25 = openmc.Material(material_id=25)
mat25.set_density("sum")
mat25.add_nuclide("U234", 4.853400e-04)
mat25.add_nuclide("U235", 4.413900e-02)
mat25.add_nuclide("U236", 2.217400e-04)
mat25.add_nuclide("U238", 2.502800e-03)

# HEU shell #26
mat26 = openmc.Material(material_id=26)
mat26.set_density("sum")
mat26.add_nuclide("U234", 4.880300e-04)
mat26.add_nuclide("U235", 4.438300e-02)
mat26.add_nuclide("U236", 2.229700e-04)
mat26.add_nuclide("U238", 2.516600e-03)

# HEU shell #27
mat27 = openmc.Material(material_id=27)
mat27.set_density("sum")
mat27.add_nuclide("U234", 4.875300e-04)
mat27.add_nuclide("U235", 4.433800e-02)
mat27.add_nuclide("U236", 2.227400e-04)
mat27.add_nuclide("U238", 2.514100e-03)

# HEU shell #28
mat28 = openmc.Material(material_id=28)
mat28.set_density("sum")
mat28.add_nuclide("U234", 4.891900e-04)
mat28.add_nuclide("U235", 4.448900e-02)
mat28.add_nuclide("U236", 2.235000e-04)
mat28.add_nuclide("U238", 2.522600e-03)

# HEU shell #29
mat29 = openmc.Material(material_id=29)
mat29.set_density("sum")
mat29.add_nuclide("U234", 4.862500e-04)
mat29.add_nuclide("U235", 4.422100e-02)
mat29.add_nuclide("U236", 2.221500e-04)
mat29.add_nuclide("U238", 2.507500e-03)

# HEU shell #30
mat30 = openmc.Material(material_id=30)
mat30.set_density("sum")
mat30.add_nuclide("U234", 4.860700e-04)
mat30.add_nuclide("U235", 4.420500e-02)
mat30.add_nuclide("U236", 2.220700e-04)
mat30.add_nuclide("U238", 2.506500e-03)

# HEU shell #31
mat31 = openmc.Material(material_id=31)
mat31.set_density("sum")
mat31.add_nuclide("U234", 4.884600e-04)
mat31.add_nuclide("U235", 4.442200e-02)
mat31.add_nuclide("U236", 2.231600e-04)
mat31.add_nuclide("U238", 2.518900e-03)

# HEU shell #32
mat32 = openmc.Material(material_id=32)
mat32.set_density("sum")
mat32.add_nuclide("U234", 4.876600e-04)
mat32.add_nuclide("U235", 4.434900e-02)
mat32.add_nuclide("U236", 2.228000e-04)
mat32.add_nuclide("U238", 2.514700e-03)

# HEU shell #33
mat33 = openmc.Material(material_id=33)
mat33.set_density("sum")
mat33.add_nuclide("U234", 4.876100e-04)
mat33.add_nuclide("U235", 4.434500e-02)
mat33.add_nuclide("U236", 2.227800e-04)
mat33.add_nuclide("U238", 2.514500e-03)

# HEU shell #34
mat34 = openmc.Material(material_id=34)
mat34.set_density("sum")
mat34.add_nuclide("U234", 4.873900e-04)
mat34.add_nuclide("U235", 4.432500e-02)
mat34.add_nuclide("U236", 2.226800e-04)
mat34.add_nuclide("U238", 2.513400e-03)

# HEU shell #35
mat35 = openmc.Material(material_id=35)
mat35.set_density("sum")
mat35.add_nuclide("U234", 4.886300e-04)
mat35.add_nuclide("U235", 4.443800e-02)
mat35.add_nuclide("U236", 2.232400e-04)
mat35.add_nuclide("U238", 2.519700e-03)

# HEU shell #36
mat36 = openmc.Material(material_id=36)
mat36.set_density("sum")
mat36.add_nuclide("U234", 4.895300e-04)
mat36.add_nuclide("U235", 4.451900e-02)
mat36.add_nuclide("U236", 2.236500e-04)
mat36.add_nuclide("U238", 2.524400e-03)

# HEU shell #37
mat37 = openmc.Material(material_id=37)
mat37.set_density("sum")
mat37.add_nuclide("U234", 4.974600e-04)
mat37.add_nuclide("U235", 4.524100e-02)
mat37.add_nuclide("U236", 2.272800e-04)
mat37.add_nuclide("U238", 2.565300e-03)

# HEU shell #38
mat38 = openmc.Material(material_id=38)
mat38.set_density("sum")
mat38.add_nuclide("U234", 4.797800e-04)
mat38.add_nuclide("U235", 4.363300e-02)
mat38.add_nuclide("U236", 2.192000e-04)
mat38.add_nuclide("U238", 2.474100e-03)

# HEU shell #39
mat39 = openmc.Material(material_id=39)
mat39.set_density("sum")
mat39.add_nuclide("U234", 4.892900e-04)
mat39.add_nuclide("U235", 4.449700e-02)
mat39.add_nuclide("U236", 2.235400e-04)
mat39.add_nuclide("U238", 2.523100e-03)

# HEU shell #40
mat40 = openmc.Material(material_id=40)
mat40.set_density("sum")
mat40.add_nuclide("U234", 4.879300e-04)
mat40.add_nuclide("U235", 4.437400e-02)
mat40.add_nuclide("U236", 2.229200e-04)
mat40.add_nuclide("U238", 2.516100e-03)

# HEU shell #41
mat41 = openmc.Material(material_id=41)
mat41.set_density("sum")
mat41.add_nuclide("U234", 4.882300e-04)
mat41.add_nuclide("U235", 4.440100e-02)
mat41.add_nuclide("U236", 2.230600e-04)
mat41.add_nuclide("U238", 2.517700e-03)

# HEU shell #42
mat42 = openmc.Material(material_id=42)
mat42.set_density("sum")
mat42.add_nuclide("U234", 4.881800e-04)
mat42.add_nuclide("U235", 4.439700e-02)
mat42.add_nuclide("U236", 2.230400e-04)
mat42.add_nuclide("U238", 2.517400e-03)

# HEU shell #43
mat43 = openmc.Material(material_id=43)
mat43.set_density("sum")
mat43.add_nuclide("U234", 4.888900e-04)
mat43.add_nuclide("U235", 4.446100e-02)
mat43.add_nuclide("U236", 2.233600e-04)
mat43.add_nuclide("U238", 2.521100e-03)

# HEU shell #44
mat44 = openmc.Material(material_id=44)
mat44.set_density("sum")
mat44.add_nuclide("U234", 4.888700e-04)
mat44.add_nuclide("U235", 4.445900e-02)
mat44.add_nuclide("U236", 2.233500e-04)
mat44.add_nuclide("U238", 2.521000e-03)

# HEU shell #45
mat45 = openmc.Material(material_id=45)
mat45.set_density("sum")
mat45.add_nuclide("U234", 4.885000e-04)
mat45.add_nuclide("U235", 4.442600e-02)
mat45.add_nuclide("U236", 2.231800e-04)
mat45.add_nuclide("U238", 2.519100e-03)

# HEU shell #46
mat46 = openmc.Material(material_id=46)
mat46.set_density("sum")
mat46.add_nuclide("U234", 4.885600e-04)
mat46.add_nuclide("U235", 4.443100e-02)
mat46.add_nuclide("U236", 2.232100e-04)
mat46.add_nuclide("U238", 2.519400e-03)

# HEU shell #47
mat47 = openmc.Material(material_id=47)
mat47.set_density("sum")
mat47.add_nuclide("U234", 4.894600e-04)
mat47.add_nuclide("U235", 4.451400e-02)
mat47.add_nuclide("U236", 2.236200e-04)
mat47.add_nuclide("U238", 2.524000e-03)

# HEU shell #48
mat48 = openmc.Material(material_id=48)
mat48.set_density("sum")
mat48.add_nuclide("U234", 4.904300e-04)
mat48.add_nuclide("U235", 4.460100e-02)
mat48.add_nuclide("U236", 2.240600e-04)
mat48.add_nuclide("U238", 2.529000e-03)

# HEU shell #49
mat49 = openmc.Material(material_id=49)
mat49.set_density("sum")
mat49.add_nuclide("U234", 4.883000e-04)
mat49.add_nuclide("U235", 4.440800e-02)
mat49.add_nuclide("U236", 2.230900e-04)
mat49.add_nuclide("U238", 2.518100e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat21, mat22, mat23, mat24, mat25, mat26, mat27, mat28, mat29, mat30, mat31, mat32, mat33, mat34, mat35, mat36, mat37, mat38, mat39, mat40, mat41, mat42, mat43, mat44, mat45, mat46, mat47, mat48, mat49])

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

# SS304
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = 

# SS304
cell10 = openmc.Cell(cell_id=10, fill=mat5)
cell10.region = 

# Al
cell11 = openmc.Cell(cell_id=11, fill=mat7)
cell11.region = 

# Np
cell12 = openmc.Cell(cell_id=12, fill=mat1)
cell12.region = 

# W
cell13 = openmc.Cell(cell_id=13, fill=mat2)
cell13.region = 

# Ni
cell14 = openmc.Cell(cell_id=14, fill=mat3)
cell14.region = 

# Ni
cell15 = openmc.Cell(cell_id=15, fill=mat3)
cell15.region = 

# Al
cell16 = openmc.Cell(cell_id=16, fill=mat8)
cell16.region = 

# Al
cell17 = openmc.Cell(cell_id=17, fill=mat8)
cell17.region = 

# SS301
cell18 = openmc.Cell(cell_id=18, fill=mat6)
cell18.region = 

# Al
cell19 = openmc.Cell(cell_id=19, fill=mat8)
cell19.region = 

# Al
cell20 = openmc.Cell(cell_id=20, fill=mat8)
cell20.region = 

# Al
cell21 = openmc.Cell(cell_id=21, fill=mat8)
cell21.region = 

# Al
cell22 = openmc.Cell(cell_id=22, fill=mat8)
cell22.region = 

# Al
cell23 = openmc.Cell(cell_id=23, fill=mat8)
cell23.region = 

# Al
cell24 = openmc.Cell(cell_id=24, fill=mat8)
cell24.region = 

# Al
cell25 = openmc.Cell(cell_id=25, fill=mat8)
cell25.region = 

# SS304
cell26 = openmc.Cell(cell_id=26, fill=mat5)
cell26.region = 

# SS304
cell27 = openmc.Cell(cell_id=27, fill=mat5)
cell27.region = 

# HEU
cell28 = openmc.Cell(cell_id=28, fill=mat21)
cell28.region = 

# HEU
cell29 = openmc.Cell(cell_id=29, fill=mat23)
cell29.region = 

# HEU
cell30 = openmc.Cell(cell_id=30, fill=mat25)
cell30.region = 

# HEU
cell31 = openmc.Cell(cell_id=31, fill=mat27)
cell31.region = 

# HEU
cell32 = openmc.Cell(cell_id=32, fill=mat29)
cell32.region = 

# HEU
cell33 = openmc.Cell(cell_id=33, fill=mat31)
cell33.region = 

# HEU
cell34 = openmc.Cell(cell_id=34, fill=mat33)
cell34.region = 

# HEU
cell35 = openmc.Cell(cell_id=35, fill=mat35)
cell35.region = 

# HEU
cell36 = openmc.Cell(cell_id=36, fill=mat37)
cell36.region = 

# HEU
cell37 = openmc.Cell(cell_id=37, fill=mat39)
cell37.region = 

# HEU
cell38 = openmc.Cell(cell_id=38, fill=mat41)
cell38.region = 

# HEU
cell39 = openmc.Cell(cell_id=39, fill=mat43)
cell39.region = 

# HEU
cell40 = openmc.Cell(cell_id=40, fill=mat45)
cell40.region = 

# HEU
cell41 = openmc.Cell(cell_id=41, fill=mat47)
cell41.region = 

# HEU
cell42 = openmc.Cell(cell_id=42, fill=mat49)
cell42.region = 

# HEU
cell43 = openmc.Cell(cell_id=43, fill=mat22)
cell43.region = 

# HEU
cell44 = openmc.Cell(cell_id=44, fill=mat24)
cell44.region = 

# HEU
cell45 = openmc.Cell(cell_id=45, fill=mat26)
cell45.region = 

# HEU
cell46 = openmc.Cell(cell_id=46, fill=mat28)
cell46.region = 

# HEU
cell47 = openmc.Cell(cell_id=47, fill=mat30)
cell47.region = 

# HEU
cell48 = openmc.Cell(cell_id=48, fill=mat32)
cell48.region = 

# HEU
cell49 = openmc.Cell(cell_id=49, fill=mat34)
cell49.region = 

# HEU
cell50 = openmc.Cell(cell_id=50, fill=mat36)
cell50.region = 

# HEU
cell51 = openmc.Cell(cell_id=51, fill=mat38)
cell51.region = 

# HEU
cell52 = openmc.Cell(cell_id=52, fill=mat40)
cell52.region = 

# HEU
cell53 = openmc.Cell(cell_id=53, fill=mat42)
cell53.region = 

# HEU
cell54 = openmc.Cell(cell_id=54, fill=mat44)
cell54.region = 

# HEU
cell55 = openmc.Cell(cell_id=55, fill=mat46)
cell55.region = 

# HEU
cell56 = openmc.Cell(cell_id=56, fill=mat48)
cell56.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49, cell50, cell51, cell52, cell53, cell54, cell55, cell56])
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
source.space = openmc.stats.Point((0.0, 0.0, -0.3175))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
