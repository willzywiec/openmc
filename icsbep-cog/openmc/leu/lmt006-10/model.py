"""
LMT006-10: Case 10; Bugey 12; detailed; 36 type 1 tubes; 11.2cm pitch; Hw=55.50cm
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
surf101 = openmc.ZCylinder(surface_id=101, x0=-40.0, y0=-40.0, r=4.85)
# fuel tube and disk
surf102 = openmc.ZCylinder(surface_id=102, x0=-40.0, y0=-28.8, r=4.85)
# fuel tube and disk
surf103 = openmc.ZCylinder(surface_id=103, x0=-40.0, y0=-17.6, r=4.85)
# fuel tube and disk
surf104 = openmc.ZCylinder(surface_id=104, x0=-40.0, y0=-6.4, r=4.85)
# fuel tube and disk
surf105 = openmc.ZCylinder(surface_id=105, x0=-40.0, y0=4.8, r=4.85)
# fuel tube and disk
surf106 = openmc.ZCylinder(surface_id=106, x0=-40.0, y0=16.0, r=4.85)
# Second row
surf111 = openmc.ZCylinder(surface_id=111, x0=-30.30052, y0=-34.4, r=4.85)
# ditto
surf112 = openmc.ZCylinder(surface_id=112, x0=-30.30052, y0=-23.2, r=4.85)
# ditto
surf113 = openmc.ZCylinder(surface_id=113, x0=-30.30052, y0=-12.0, r=4.85)
# ditto
surf114 = openmc.ZCylinder(surface_id=114, x0=-30.30052, y0=-0.8, r=4.85)
# ditto
surf115 = openmc.ZCylinder(surface_id=115, x0=-30.30052, y0=10.4, r=4.85)
# ditto
surf116 = openmc.ZCylinder(surface_id=116, x0=-30.30052, y0=21.6, r=4.85)
# Third row
surf121 = openmc.ZCylinder(surface_id=121, x0=-20.60103, y0=-40.0, r=4.85)
# ditto
surf122 = openmc.ZCylinder(surface_id=122, x0=-20.60103, y0=-28.8, r=4.85)
# ditto
surf123 = openmc.ZCylinder(surface_id=123, x0=-20.60103, y0=-17.6, r=4.85)
# ditto
surf124 = openmc.ZCylinder(surface_id=124, x0=-20.60103, y0=-6.4, r=4.85)
# ditto
surf125 = openmc.ZCylinder(surface_id=125, x0=-20.60103, y0=4.8, r=4.85)
# ditto
surf126 = openmc.ZCylinder(surface_id=126, x0=-20.60103, y0=16.0, r=4.85)
# Fourth row
surf131 = openmc.ZCylinder(surface_id=131, x0=-10.90155, y0=-34.4, r=4.85)
# ditto
surf132 = openmc.ZCylinder(surface_id=132, x0=-10.90155, y0=-23.2, r=4.85)
# ditto
surf133 = openmc.ZCylinder(surface_id=133, x0=-10.90155, y0=-12.0, r=4.85)
# ditto
surf134 = openmc.ZCylinder(surface_id=134, x0=-10.90155, y0=-0.8, r=4.85)
# ditto
surf135 = openmc.ZCylinder(surface_id=135, x0=-10.90155, y0=10.4, r=4.85)
# ditto
surf136 = openmc.ZCylinder(surface_id=136, x0=-10.90155, y0=21.6, r=4.85)
# Fifth row
surf141 = openmc.ZCylinder(surface_id=141, x0=-1.20206, y0=-40.0, r=4.85)
# ditto
surf142 = openmc.ZCylinder(surface_id=142, x0=-1.20206, y0=-28.8, r=4.85)
# ditto
surf143 = openmc.ZCylinder(surface_id=143, x0=-1.20206, y0=-17.6, r=4.85)
# ditto
surf144 = openmc.ZCylinder(surface_id=144, x0=-1.20206, y0=-6.4, r=4.85)
# ditto
surf145 = openmc.ZCylinder(surface_id=145, x0=-1.20206, y0=4.8, r=4.85)
# ditto
surf146 = openmc.ZCylinder(surface_id=146, x0=-1.20206, y0=16.0, r=4.85)
# Sixth row
surf151 = openmc.ZCylinder(surface_id=151, x0=8.49742, y0=-34.4, r=4.85)
# ditto
surf152 = openmc.ZCylinder(surface_id=152, x0=8.49742, y0=-23.2, r=4.85)
# ditto
surf153 = openmc.ZCylinder(surface_id=153, x0=8.49742, y0=-12.0, r=4.85)
# ditto
surf154 = openmc.ZCylinder(surface_id=154, x0=8.49742, y0=-0.8, r=4.85)
# ditto
surf155 = openmc.ZCylinder(surface_id=155, x0=8.49742, y0=10.4, r=4.85)
# ditto
surf156 = openmc.ZCylinder(surface_id=156, x0=8.49742, y0=21.6, r=4.85)
surf901 = openmc.ZPlane(surface_id=901, z0=-4.4)
surf902 = openmc.ZPlane(surface_id=902, z0=-0.4)
surf903 = openmc.ZPlane(surface_id=903, z0=0.0)
# Critical water height, Hw
surf904 = openmc.ZPlane(surface_id=904, z0=55.50)
# Above disk and below beam
surf905 = openmc.ZPlane(surface_id=905, z0=60.0)
# Boundary condition
surf999 = openmc.model.RectangularParallelepiped(-65.0, 65.0, -70.0, 70.0, -35.4, 104.6, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = +surf1 & -surf2
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0])

universe2 = openmc.Universe(universe_id=2, cells=[])

u3_cell0 = openmc.Cell(fill=mat2)
u3_cell0.region = -surf4 & -surf5 & -surf904
u3_cell1 = openmc.Cell(fill=mat1)
u3_cell1.region = +surf4 & -surf5
u3_cell2 = openmc.Cell(fill=mat2)
u3_cell2.region = +surf4 & +surf5 & -surf904
u3_cell3 = openmc.Cell(fill=mat3)
u3_cell3.region = +surf5 & -surf6
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3])

u4_cell0 = openmc.Cell(fill=mat2)
u4_cell0.region = -surf7 & -surf8 & -surf904
u4_cell1 = openmc.Cell(fill=mat3)
u4_cell1.region = +surf7 & -surf8
u4_cell2 = openmc.Cell(fill=mat2)
u4_cell2.region = +surf8 & -surf904
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2])

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
cell1.region = +surf905 & -surf999

# Ftube
cell2 = openmc.Cell(cell_id=2, fill=universe3)
cell2.translation = (-40.0, -40.0, 0.0)
cell2.region = -surf101 & +surf903 & -surf905 & -surf999

# Ftube
cell3 = openmc.Cell(cell_id=3, fill=universe3)
cell3.translation = (-40.0, -28.8, 0.0)
cell3.region = -surf102 & +surf903 & -surf905 & -surf999

# Ftube
cell4 = openmc.Cell(cell_id=4, fill=universe3)
cell4.translation = (-40.0, -17.6, 0.0)
cell4.region = -surf103 & +surf903 & -surf905 & -surf999

# Ftube
cell5 = openmc.Cell(cell_id=5, fill=universe3)
cell5.translation = (-40.0, -6.4, 0.0)
cell5.region = -surf104 & +surf903 & -surf905 & -surf999

# Ftube
cell6 = openmc.Cell(cell_id=6, fill=universe3)
cell6.translation = (-40.0, 4.8, 0.0)
cell6.region = -surf105 & +surf903 & -surf905 & -surf999

# Ftube
cell7 = openmc.Cell(cell_id=7, fill=universe3)
cell7.translation = (-40.0, 16.0, 0.0)
cell7.region = -surf106 & +surf903 & -surf905 & -surf999

# Ftube
cell8 = openmc.Cell(cell_id=8, fill=universe3)
cell8.translation = (-30.30052, -34.4, 0.0)
cell8.region = -surf111 & +surf903 & -surf905 & -surf999

# Ftube
cell9 = openmc.Cell(cell_id=9, fill=universe3)
cell9.translation = (-30.30052, -23.2, 0.0)
cell9.region = -surf112 & +surf903 & -surf905 & -surf999

# Ftube
cell10 = openmc.Cell(cell_id=10, fill=universe3)
cell10.translation = (-30.30052, -12.0, 0.0)
cell10.region = -surf113 & +surf903 & -surf905 & -surf999

# Ftube
cell11 = openmc.Cell(cell_id=11, fill=universe3)
cell11.translation = (-30.30052, -0.8, 0.0)
cell11.region = -surf114 & +surf903 & -surf905 & -surf999

# Ftube
cell12 = openmc.Cell(cell_id=12, fill=universe3)
cell12.translation = (-30.30052, 10.4, 0.0)
cell12.region = -surf115 & +surf903 & -surf905 & -surf999

# Ftube
cell13 = openmc.Cell(cell_id=13, fill=universe3)
cell13.translation = (-30.30052, 21.6, 0.0)
cell13.region = -surf116 & +surf903 & -surf905 & -surf999

# Ftube
cell14 = openmc.Cell(cell_id=14, fill=universe3)
cell14.translation = (-20.60103, -40.0, 0.0)
cell14.region = -surf121 & +surf903 & -surf905 & -surf999

# Ftube
cell15 = openmc.Cell(cell_id=15, fill=universe3)
cell15.translation = (-20.60103, -28.8, 0.0)
cell15.region = -surf122 & +surf903 & -surf905 & -surf999

# Ftube
cell16 = openmc.Cell(cell_id=16, fill=universe3)
cell16.translation = (-20.60103, -17.6, 0.0)
cell16.region = -surf123 & +surf903 & -surf905 & -surf999

# Ftube
cell17 = openmc.Cell(cell_id=17, fill=universe3)
cell17.translation = (-20.60103, -6.4, 0.0)
cell17.region = -surf124 & +surf903 & -surf905 & -surf999

# Ftube
cell18 = openmc.Cell(cell_id=18, fill=universe3)
cell18.translation = (-20.60103, 4.8, 0.0)
cell18.region = -surf125 & +surf903 & -surf905 & -surf999

# Ftube
cell19 = openmc.Cell(cell_id=19, fill=universe3)
cell19.translation = (-20.60103, 16.0, 0.0)
cell19.region = -surf126 & +surf903 & -surf905 & -surf999

# Ftube
cell20 = openmc.Cell(cell_id=20, fill=universe3)
cell20.translation = (-10.90155, -34.4, 0.0)
cell20.region = -surf131 & +surf903 & -surf905 & -surf999

# Ftube
cell21 = openmc.Cell(cell_id=21, fill=universe3)
cell21.translation = (-10.90155, -23.2, 0.0)
cell21.region = -surf132 & +surf903 & -surf905 & -surf999

# Ftube
cell22 = openmc.Cell(cell_id=22, fill=universe3)
cell22.translation = (-10.90155, -12.0, 0.0)
cell22.region = -surf133 & +surf903 & -surf905 & -surf999

# Ftube
cell23 = openmc.Cell(cell_id=23, fill=universe3)
cell23.translation = (-10.90155, -0.8, 0.0)
cell23.region = -surf134 & +surf903 & -surf905 & -surf999

# Ftube
cell24 = openmc.Cell(cell_id=24, fill=universe3)
cell24.translation = (-10.90155, 10.4, 0.0)
cell24.region = -surf135 & +surf903 & -surf905 & -surf999

# Ftube
cell25 = openmc.Cell(cell_id=25, fill=universe3)
cell25.translation = (-10.90155, 21.6, 0.0)
cell25.region = -surf136 & +surf903 & -surf905 & -surf999

# Ftube
cell26 = openmc.Cell(cell_id=26, fill=universe3)
cell26.translation = (-1.20206, -40.0, 0.0)
cell26.region = -surf141 & +surf903 & -surf905 & -surf999

# Ftube
cell27 = openmc.Cell(cell_id=27, fill=universe3)
cell27.translation = (-1.20206, -28.8, 0.0)
cell27.region = -surf142 & +surf903 & -surf905 & -surf999

# Ftube
cell28 = openmc.Cell(cell_id=28, fill=universe3)
cell28.translation = (-1.20206, -17.6, 0.0)
cell28.region = -surf143 & +surf903 & -surf905 & -surf999

# Ftube
cell29 = openmc.Cell(cell_id=29, fill=universe3)
cell29.translation = (-1.20206, -6.4, 0.0)
cell29.region = -surf144 & +surf903 & -surf905 & -surf999

# Ftube
cell30 = openmc.Cell(cell_id=30, fill=universe3)
cell30.translation = (-1.20206, 4.8, 0.0)
cell30.region = -surf145 & +surf903 & -surf905 & -surf999

# Ftube
cell31 = openmc.Cell(cell_id=31, fill=universe3)
cell31.translation = (-1.20206, 16.0, 0.0)
cell31.region = -surf146 & +surf903 & -surf905 & -surf999

# Ftube
cell32 = openmc.Cell(cell_id=32, fill=universe3)
cell32.translation = (8.49742, -34.4, 0.0)
cell32.region = -surf151 & +surf903 & -surf905 & -surf999

# Ftube
cell33 = openmc.Cell(cell_id=33, fill=universe3)
cell33.translation = (8.49742, -23.2, 0.0)
cell33.region = -surf152 & +surf903 & -surf905 & -surf999

# Ftube
cell34 = openmc.Cell(cell_id=34, fill=universe3)
cell34.translation = (8.49742, -12.0, 0.0)
cell34.region = -surf153 & +surf903 & -surf905 & -surf999

# Ftube
cell35 = openmc.Cell(cell_id=35, fill=universe3)
cell35.translation = (8.49742, -0.8, 0.0)
cell35.region = -surf154 & +surf903 & -surf905 & -surf999

# Ftube
cell36 = openmc.Cell(cell_id=36, fill=universe3)
cell36.translation = (8.49742, 10.4, 0.0)
cell36.region = -surf155 & +surf903 & -surf905 & -surf999

# Ftube
cell37 = openmc.Cell(cell_id=37, fill=universe3)
cell37.translation = (8.49742, 21.6, 0.0)
cell37.region = -surf156 & +surf903 & -surf905 & -surf999

# Water
cell38 = openmc.Cell(cell_id=38, fill=mat2)
cell38.region = +surf903 & -surf904 & -surf999 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106

# Air
cell39 = openmc.Cell(cell_id=39, fill=mat5)
cell39.region = +surf904 & -surf905 & -surf999 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106

# Plate
cell40 = openmc.Cell(cell_id=40, fill=mat4)
cell40.region = -surf3 & +surf902 & -surf903 & -surf999

# Water
cell41 = openmc.Cell(cell_id=41, fill=mat2)
cell41.region = +surf3 & +surf902 & -surf903 & -surf999

# Water
cell42 = openmc.Cell(cell_id=42, fill=mat2)
cell42.region = +surf901 & -surf902 & -surf999

# Water
cell43 = openmc.Cell(cell_id=43, fill=mat2)
cell43.region = +surf901 & -surf902 & -surf999

# Water
cell44 = openmc.Cell(cell_id=44, fill=mat2)
cell44.region = -surf901 & -surf999

# Water
cell57 = openmc.Cell(cell_id=57, fill=mat2)
cell57.region = -surf904 & -surf999

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell57])
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
source.space = openmc.stats.Box((-21.6, -14.6, 26.75), (-9.9, -3.8, 28.75))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
