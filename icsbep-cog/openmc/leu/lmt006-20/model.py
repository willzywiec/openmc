"""
LMT006-20: Bugey case 50; 46 type 1 tubes; 9.7cm pitch; Hw=57.07cm
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(1.6) Metal
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 7.017800e-06)
mat1.add_nuclide("U235", 7.554400e-04)
mat1.add_nuclide("U238", 4.586600e-02)
mat1.add_element("Fe", 5.961400e-05)
mat1.add_element("Al", 2.879100e-04)
mat1.add_element("C", 9.239500e-04)

# Water
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.669200e-02)
mat2.add_nuclide("O16", 3.334600e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

# Steel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 8.508600e-02)
mat3.add_element("C", 5.554500e-04)

# 85% SST and
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 1.000400e-02)
mat4.add_nuclide("O16", 5.001900e-03)
mat4.add_element("Fe", 4.989000e-02)
mat4.add_element("Cr", 1.399900e-02)
mat4.add_element("Ni", 6.890200e-03)
mat4.add_element("Mn", 1.472100e-03)
mat4.add_element("Si", 1.439800e-03)
mat4.add_element("P", 5.222300e-05)
mat4.add_element("S", 3.782800e-05)
mat4.add_element("C", 1.010000e-04)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Air
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("O16", 1.126300e-05)
mat5.add_element("N", 4.198500e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# U-shaped plates/inner
surf1 = openmc.model.RectangularParallelepiped(-4.5, 4.5, -50.0, 50.0, -8.2, -0.6000000000000005)
# U-shaped plates/outer
surf2 = openmc.model.RectangularParallelepiped(-4.7, 4.7, -50.0, 50.0, -8.4, -0.40000000000000036)
# Additional plate w/water in (smeared) holes
surf3 = openmc.model.RectangularParallelepiped(-59.7, 59.7, -50.0, 50.0, -49.95, 49.95)
# Fuel tube/inner
surf4 = openmc.ZCylinder(surface_id=4, r=3.75)
# Fuel tube/outer
surf5 = openmc.ZCylinder(surface_id=5, x0=0.0, y0=59.0, r=4.85)
# Steel disk
surf6 = openmc.ZCylinder(surface_id=6, x0=59.0, y0=59.5, r=4.85)
# Beam/inner
surf7 = openmc.model.RectangularParallelepiped(-1.8, 1.8, -499.95, 499.95, 60.7, 64.3)
# Beam/outer
surf8 = openmc.model.RectangularParallelepiped(-2.0, 2.0, -50.0, 50.0, 60.5, 64.5)
# Basic fuel tube and disk
# surf101: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf102: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf103: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf104: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf105: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf106: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf107: Error converting surface type "c": could not convert string to float: 'tr'
# Second row
# surf111: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf112: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf113: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf114: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf115: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf116: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf117: Error converting surface type "c": could not convert string to float: 'tr'
# Third row
# surf121: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf122: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf123: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf124: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf125: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf126: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf127: Error converting surface type "c": could not convert string to float: 'tr'
# Fourth row
# surf131: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf132: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf133: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf134: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf135: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf136: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf137: Error converting surface type "c": could not convert string to float: 'tr'
# Fifth row
# surf141: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf142: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf143: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf144: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf145: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf146: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf147: Error converting surface type "c": could not convert string to float: 'tr'
# Sixth row
# surf151: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf152: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf153: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf154: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf155: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf156: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf157: Error converting surface type "c": could not convert string to float: 'tr'
# Seventh row
# surf161: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf162: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf163: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf164: Error converting surface type "c": could not convert string to float: 'tr'
# Arbitrary
surf900 = openmc.ZPlane(surface_id=900, z0=60.0)
surf901 = openmc.ZPlane(surface_id=901, z0=-4.4)
surf902 = openmc.ZPlane(surface_id=902, z0=-0.4)
surf903 = openmc.ZPlane(surface_id=903, z0=0.0)
# Critical water height, Hw
surf904 = openmc.ZPlane(surface_id=904, z0=57.07)
# Boundary condition
surf999 = openmc.model.RectangularParallelepiped(-65.0, 65.0, -70.0, 70.0, -35.4, 104.6, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = +surf1 & -surf2
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0])

universe2 = openmc.Universe(universe_id=2, cells=[])

u3_cell0 = openmc.Cell(fill=mat5)
u3_cell0.region = -surf4 & -surf5 & +surf904
u3_cell1 = openmc.Cell(fill=mat2)
u3_cell1.region = -surf4 & -surf5 & -surf904
u3_cell2 = openmc.Cell(fill=mat1)
u3_cell2.region = +surf4 & -surf5
u3_cell3 = openmc.Cell(fill=mat3)
u3_cell3.region = +surf5 & -surf6
u3_cell4 = openmc.Cell(fill=mat5)
u3_cell4.region = +surf5 & +surf6 & +surf904 & -surf999
u3_cell5 = openmc.Cell(fill=mat2)
u3_cell5.region = +surf5 & +surf6 & -surf904 & -surf999
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4, u3_cell5])

u4_cell0 = openmc.Cell(fill=mat3)
u4_cell0.region = +surf7 & -surf8 & -surf999
u4_cell1 = openmc.Cell(fill=mat5)
u4_cell1.region = -surf7 & -surf8 & +surf904 & -surf999
u4_cell2 = openmc.Cell(fill=mat2)
u4_cell2.region = -surf7 & -surf8 & -surf904 & -surf999
u4_cell3 = openmc.Cell(fill=mat5)
u4_cell3.region = +surf8 & +surf904 & -surf999
u4_cell4 = openmc.Cell(fill=mat2)
u4_cell4.region = +surf8 & -surf904 & -surf999
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

u5_cell0 = openmc.Cell(fill=mat5)
u5_cell0.region = +surf904 & -surf999
u5_cell1 = openmc.Cell(fill=mat5)
u5_cell1.region = +surf904 & -surf999
u5_cell2 = openmc.Cell(fill=mat2)
u5_cell2.region = -surf904 & -surf999
u5_cell3 = openmc.Cell(fill=mat2)
u5_cell3.region = -surf904 & -surf999
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0, u5_cell1, u5_cell2, u5_cell3])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Beams
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = +surf900 & -surf999

# Ftube
cell2 = openmc.Cell(cell_id=2, fill=universe3)
cell2.translation = (-40.0, -40.0, 0.0)
cell2.region = +surf903

# Ftube
cell3 = openmc.Cell(cell_id=3, fill=universe3)
cell3.translation = (-40.0, -30.3, 0.0)
cell3.region = +surf903

# Ftube
cell4 = openmc.Cell(cell_id=4, fill=universe3)
cell4.translation = (-40.0, -20.6, 0.0)
cell4.region = +surf903

# Ftube
cell5 = openmc.Cell(cell_id=5, fill=universe3)
cell5.translation = (-40.0, -10.9, 0.0)
cell5.region = +surf903

# Ftube
cell6 = openmc.Cell(cell_id=6, fill=universe3)
cell6.translation = (-40.0, -1.2, 0.0)
cell6.region = +surf903

# Ftube
cell7 = openmc.Cell(cell_id=7, fill=universe3)
cell7.translation = (-40.0, 8.5, 0.0)
cell7.region = +surf903

# Ftube
cell8 = openmc.Cell(cell_id=8, fill=universe3)
cell8.translation = (-40.0, 18.2, 0.0)
cell8.region = +surf903

# Ftube
cell9 = openmc.Cell(cell_id=9, fill=universe3)
cell9.translation = (-30.3, -40.0, 0.0)
cell9.region = +surf903

# Ftube
cell10 = openmc.Cell(cell_id=10, fill=universe3)
cell10.translation = (-30.3, -30.3, 0.0)
cell10.region = +surf903

# Ftube
cell11 = openmc.Cell(cell_id=11, fill=universe3)
cell11.translation = (-30.3, -20.6, 0.0)
cell11.region = +surf903

# Ftube
cell12 = openmc.Cell(cell_id=12, fill=universe3)
cell12.translation = (-30.3, -10.9, 0.0)
cell12.region = +surf903

# Ftube
cell13 = openmc.Cell(cell_id=13, fill=universe3)
cell13.translation = (-30.3, -1.2, 0.0)
cell13.region = +surf903

# Ftube
cell14 = openmc.Cell(cell_id=14, fill=universe3)
cell14.translation = (-30.3, 8.5, 0.0)
cell14.region = +surf903

# Ftube
cell15 = openmc.Cell(cell_id=15, fill=universe3)
cell15.translation = (-30.3, 18.2, 0.0)
cell15.region = +surf903

# Ftube
cell16 = openmc.Cell(cell_id=16, fill=universe3)
cell16.translation = (-20.6, -40.0, 0.0)
cell16.region = +surf903

# Ftube
cell17 = openmc.Cell(cell_id=17, fill=universe3)
cell17.translation = (-20.6, -30.3, 0.0)
cell17.region = +surf903

# Ftube
cell18 = openmc.Cell(cell_id=18, fill=universe3)
cell18.translation = (-20.6, -20.6, 0.0)
cell18.region = +surf903

# Ftube
cell19 = openmc.Cell(cell_id=19, fill=universe3)
cell19.translation = (-20.6, -10.9, 0.0)
cell19.region = +surf903

# Ftube
cell20 = openmc.Cell(cell_id=20, fill=universe3)
cell20.translation = (-20.6, -1.2, 0.0)
cell20.region = +surf903

# Ftube
cell21 = openmc.Cell(cell_id=21, fill=universe3)
cell21.translation = (-20.6, 8.5, 0.0)
cell21.region = +surf903

# Ftube
cell22 = openmc.Cell(cell_id=22, fill=universe3)
cell22.translation = (-20.6, 18.2, 0.0)
cell22.region = +surf903

# Ftube
cell23 = openmc.Cell(cell_id=23, fill=universe3)
cell23.translation = (-10.9, -40.0, 0.0)
cell23.region = +surf903

# Ftube
cell24 = openmc.Cell(cell_id=24, fill=universe3)
cell24.translation = (-10.9, -30.3, 0.0)
cell24.region = +surf903

# Ftube
cell25 = openmc.Cell(cell_id=25, fill=universe3)
cell25.translation = (-10.9, -20.6, 0.0)
cell25.region = +surf903

# Ftube
cell26 = openmc.Cell(cell_id=26, fill=universe3)
cell26.translation = (-10.9, -10.9, 0.0)
cell26.region = +surf903

# Ftube
cell27 = openmc.Cell(cell_id=27, fill=universe3)
cell27.translation = (-10.9, -1.2, 0.0)
cell27.region = +surf903

# Ftube
cell28 = openmc.Cell(cell_id=28, fill=universe3)
cell28.translation = (-10.9, 8.5, 0.0)
cell28.region = +surf903

# Ftube
cell29 = openmc.Cell(cell_id=29, fill=universe3)
cell29.translation = (-10.9, 18.2, 0.0)
cell29.region = +surf903

# Ftube
cell30 = openmc.Cell(cell_id=30, fill=universe3)
cell30.translation = (-1.2, -40.0, 0.0)
cell30.region = +surf903

# Ftube
cell31 = openmc.Cell(cell_id=31, fill=universe3)
cell31.translation = (-1.2, -30.3, 0.0)
cell31.region = +surf903

# Ftube
cell32 = openmc.Cell(cell_id=32, fill=universe3)
cell32.translation = (-1.2, -20.6, 0.0)
cell32.region = +surf903

# Ftube
cell33 = openmc.Cell(cell_id=33, fill=universe3)
cell33.translation = (-1.2, -10.9, 0.0)
cell33.region = +surf903

# Ftube
cell34 = openmc.Cell(cell_id=34, fill=universe3)
cell34.translation = (-1.2, -1.2, 0.0)
cell34.region = +surf903

# Ftube
cell35 = openmc.Cell(cell_id=35, fill=universe3)
cell35.translation = (-1.2, 8.5, 0.0)
cell35.region = +surf903

# Ftube
cell36 = openmc.Cell(cell_id=36, fill=universe3)
cell36.translation = (-1.2, 18.2, 0.0)
cell36.region = +surf903

# Ftube
cell37 = openmc.Cell(cell_id=37, fill=universe3)
cell37.translation = (8.5, -40.0, 0.0)
cell37.region = +surf903

# Ftube
cell38 = openmc.Cell(cell_id=38, fill=universe3)
cell38.translation = (8.5, -30.3, 0.0)
cell38.region = +surf903

# Ftube
cell39 = openmc.Cell(cell_id=39, fill=universe3)
cell39.translation = (8.5, -20.6, 0.0)
cell39.region = +surf903

# Ftube
cell40 = openmc.Cell(cell_id=40, fill=universe3)
cell40.translation = (8.5, -10.9, 0.0)
cell40.region = +surf903

# Ftube
cell41 = openmc.Cell(cell_id=41, fill=universe3)
cell41.translation = (8.5, -1.2, 0.0)
cell41.region = +surf903

# Ftube
cell42 = openmc.Cell(cell_id=42, fill=universe3)
cell42.translation = (8.5, 8.5, 0.0)
cell42.region = +surf903

# Ftube
cell43 = openmc.Cell(cell_id=43, fill=universe3)
cell43.translation = (8.5, 18.2, 0.0)
cell43.region = +surf903

# Ftube
cell44 = openmc.Cell(cell_id=44, fill=universe3)
cell44.translation = (18.2, -30.3, 0.0)
cell44.region = +surf903

# Ftube
cell45 = openmc.Cell(cell_id=45, fill=universe3)
cell45.translation = (18.2, -20.6, 0.0)
cell45.region = +surf903

# Ftube
cell46 = openmc.Cell(cell_id=46, fill=universe3)
cell46.translation = (18.2, -10.9, 0.0)
cell46.region = +surf903

# Ftube
cell47 = openmc.Cell(cell_id=47, fill=universe3)
cell47.translation = (18.2, -1.2, 0.0)
cell47.region = +surf903

# Water
cell48 = openmc.Cell(cell_id=48, fill=mat2)
cell48.region = +surf903 & -surf904 & -surf999

# Air
cell49 = openmc.Cell(cell_id=49, fill=mat5)
cell49.region = -surf900 & +surf903 & +surf904 & -surf999

# Plate
cell50 = openmc.Cell(cell_id=50, fill=mat4)
cell50.region = -surf3 & +surf902 & -surf903 & -surf999

# Water
cell51 = openmc.Cell(cell_id=51, fill=mat2)
cell51.region = +surf3 & +surf902 & -surf903 & -surf999

# Water
cell52 = openmc.Cell(cell_id=52, fill=mat2)
cell52.region = +surf901 & -surf902 & -surf999

# Water
cell53 = openmc.Cell(cell_id=53, fill=mat2)
cell53.region = +surf901 & -surf902 & -surf999

# Water
cell54 = openmc.Cell(cell_id=54, fill=mat2)
cell54.region = -surf901 & -surf999

# Water
cell62 = openmc.Cell(cell_id=62, fill=mat2)
cell62.region = +surf5 & +surf6 & -surf904 & -surf999

# Water
cell68 = openmc.Cell(cell_id=68, fill=mat2)
cell68.region = +surf8 & -surf904 & -surf999

# Water
cell73 = openmc.Cell(cell_id=73, fill=mat2)
cell73.region = -surf904 & -surf999

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49, cell50, cell51, cell52, cell53, cell54, cell62, cell68, cell73])
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
source.space = openmc.stats.Box((-15.9, -15.9, 27.535), (-5.9, -5.9, 29.535))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
