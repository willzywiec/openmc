"""
ICT003-2: TRIGA Mark II Reactor with U(20) Fuel - Core 132
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Fuel in fuel rod
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 5.525300e-02)
mat1.add_element("Zr", 3.453000e-02)
mat1.add_nuclide("U238", 1.462500e-03)
mat1.add_nuclide("U235", 3.680100e-04)
mat1.add_s_alpha_beta("c_H_in_ZrH")
mat1.add_s_alpha_beta("c_Zr_in_ZrH")

# Fuel in control rod
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 5.628400e-02)
mat2.add_element("Zr", 3.517500e-02)
mat2.add_nuclide("U238", 1.489800e-03)
mat2.add_nuclide("U235", 3.748700e-04)
mat2.add_s_alpha_beta("c_H_in_ZrH")
mat2.add_s_alpha_beta("c_Zr_in_ZrH")

# Zr rod
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Zr", 4.284300e-02)

# B4C in absorber rod
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("B10", 2.144300e-02)
mat4.add_nuclide("B11", 8.631000e-02)
mat4.add_element("C", 2.735500e-02)

# SS404 in clad, ends
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 5.686000e-02)
mat5.add_element("Cr", 1.736000e-02)
mat5.add_element("Ni", 8.094800e-03)
mat5.add_element("Mn", 1.729500e-03)
mat5.add_element("Si", 3.383100e-03)
mat5.add_element("C", 3.164300e-04)
mat5.add_element("P", 6.135300e-05)
mat5.add_element("S", 5.925600e-05)

# Al in clad, grids, transient rod
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Al", 6.026200e-02)

# Support disc in fuel rod
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Mo", 6.402500e-02)

# Graphite
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("C", 8.022100e-02)

# Water
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_nuclide("H1", 6.668900e-02)
mat9.add_nuclide("O16", 3.334400e-02)
mat9.add_s_alpha_beta("c_H_in_H2O")

# Air
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_element("N", 4.347900e-05)
mat10.add_nuclide("O16", 1.086800e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZCylinder(surface_id=1, x0=-36.83, y0=74.295, r=1.87706)
# surf2: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf3: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf4: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf5: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf6: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf7: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf8: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf9: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf10: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf11: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf12: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf13: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf14: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf15: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf16: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf17: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf18: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf19: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf20: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf21: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf22: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf23: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf24: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf25: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf26: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf27: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf28: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf29: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf30: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf31: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf32: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf33: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf34: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf35: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf36: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf37: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf38: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf39: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf40: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf41: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf42: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf43: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf44: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf45: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf46: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf47: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf48: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf49: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf50: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf51: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf52: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf53: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf54: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf55: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf56: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf57: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf58: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf59: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf60: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf61: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf62: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf63: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf64: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf65: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf66: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf67: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf68: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf69: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf70: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf71: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf72: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf73: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf74: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf75: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf76: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf77: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf78: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf79: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf80: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf81: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf82: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf83: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf84: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf85: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf86: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf87: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf88: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf89: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf90: Error converting surface type "cylinder": could not convert string to float: 'tr'
# surf91: Error converting surface type "cylinder": could not convert string to float: 'tr'
# Lower aluminum support grid
surf100 = openmc.ZCylinder(surface_id=100, x0=-36.20, y0=-34.295, r=22.06)
# Upper aluminum support grid
surf101 = openmc.ZCylinder(surface_id=101, x0=28.88, y0=30.785, r=22.06)
# Cladding/inner
surf110 = openmc.ZCylinder(surface_id=110, r=22.098)
# Graphite/inner
surf111 = openmc.ZCylinder(surface_id=111, r=22.733)
# Groove/inner
surf112 = openmc.ZCylinder(surface_id=112, r=29.883)
# Groove/outer
surf113 = openmc.ZCylinder(surface_id=113, r=36.957)
# Groove/lower
surf114 = openmc.ZPlane(surface_id=114, z0=0.851)
# Graphite/outer
surf115 = openmc.ZCylinder(surface_id=115, x0=-26.975, y0=26.975, r=53.14)
# Cladding/outer
surf116 = openmc.ZCylinder(surface_id=116, x0=-28.245, y0=28.245, r=54.41)
# Water/outer/bcd
surf199 = openmc.ZCylinder(surface_id=199, x0=-100.0, y0=100.0, r=98.4, boundary_type="vacuum")
# Graphite/lower
surf201 = openmc.ZCylinder(surface_id=201, x0=-28.527375, y0=-19.129375, r=1.8161)
# Mo disc
surf202 = openmc.ZCylinder(surface_id=202, x0=-19.129375, y0=-19.05, r=1.82626)
# Zr Rod
surf203 = openmc.ZCylinder(surface_id=203, r=0.3175)
# U-ZrH Fuel
surf204 = openmc.ZCylinder(surface_id=204, x0=-19.05, y0=19.05, r=1.82245)
# Graphite/upper
surf205 = openmc.ZCylinder(surface_id=205, x0=19.05, y0=25.654, r=1.8161)
# Clad/inner
surf206 = openmc.ZCylinder(surface_id=206, x0=-28.527375, y0=25.654, r=1.82626)
# Clad/outer
surf207 = openmc.ZCylinder(surface_id=207, x0=-36.030, y0=36.030, r=1.87706)
# Void/lower
surf301 = openmc.ZCylinder(surface_id=301, x0=-35.56, y0=-21.59, r=1.69545)
# SS304/lower
surf302 = openmc.ZCylinder(surface_id=302, x0=-21.59, y0=-19.05, r=1.69545)
# Zr Rod
surf303 = openmc.ZCylinder(surface_id=303, r=0.3175)
# U-ZrH Fuel
surf304 = openmc.ZCylinder(surface_id=304, x0=-19.05, y0=19.05, r=1.666875)
# Void
surf305 = openmc.ZCylinder(surface_id=305, x0=19.05, y0=19.84375, r=1.69545)
# SS304/middle
surf306 = openmc.ZCylinder(surface_id=306, x0=19.84375, y0=21.11375, r=1.69545)
# B4C Absorber
surf307 = openmc.ZCylinder(surface_id=307, x0=21.11375, y0=59.69, r=1.666875)
# SS304/upper
surf308 = openmc.ZCylinder(surface_id=308, x0=59.69, y0=60.96, r=1.69545)
# Void
surf309 = openmc.ZCylinder(surface_id=309, x0=60.96, y0=70.485, r=1.69545)
# Clad/inner
surf310 = openmc.ZCylinder(surface_id=310, x0=-35.56, y0=70.485, r=1.69545)
# Clad/outer
surf311 = openmc.ZCylinder(surface_id=311, x0=-36.83, y0=74.295, r=1.74625)
# Void/lower
surf401 = openmc.ZCylinder(surface_id=401, x0=-35.56, y0=19.84375, r=1.51638)
# B4C Absorber
surf402 = openmc.ZCylinder(surface_id=402, x0=21.11375, y0=59.21375, r=1.51638)
# Void/middle
surf403 = openmc.ZCylinder(surface_id=403, x0=59.21375, y0=59.69, r=1.51638)
# Void/upper
surf404 = openmc.ZCylinder(surface_id=404, x0=60.96, y0=70.485, r=1.51638)
# Al clad/outer
surf405 = openmc.ZCylinder(surface_id=405, x0=-36.83, y0=74.295, r=1.87706)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat8)
u1_cell0.region = -surf201
u1_cell1 = openmc.Cell(fill=mat7)
u1_cell1.region = +surf201 & -surf202
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = +surf202 & -surf203 & -surf204
u1_cell3 = openmc.Cell(fill=mat1)
u1_cell3.region = +surf202 & +surf203 & -surf204
u1_cell4 = openmc.Cell(fill=mat8)
u1_cell4.region = +surf204 & -surf205
u1_cell5 = openmc.Cell(fill=mat10)
u1_cell5.region = +surf201 & +surf202 & +surf204 & +surf205 & -surf206
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = +surf206 & -surf207
u1_cell7 = openmc.Cell(fill=mat9)
u1_cell7.region = +surf207 & -surf199
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7])

u2_cell0 = openmc.Cell(fill=mat10)
u2_cell0.region = -surf301 & -surf310
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = +surf301 & -surf302 & -surf310
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf302 & -surf303 & -surf304 & -surf310
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = +surf302 & +surf303 & -surf304 & -surf310
u2_cell4 = openmc.Cell(fill=mat10)
u2_cell4.region = +surf304 & -surf305 & -surf310
u2_cell5 = openmc.Cell(fill=mat5)
u2_cell5.region = +surf305 & -surf306 & -surf310
u2_cell6 = openmc.Cell(fill=mat4)
u2_cell6.region = +surf306 & -surf307 & -surf310
u2_cell7 = openmc.Cell(fill=mat5)
u2_cell7.region = +surf307 & -surf308 & -surf310
u2_cell8 = openmc.Cell(fill=mat10)
u2_cell8.region = +surf308 & -surf309 & -surf310
u2_cell9 = openmc.Cell(fill=mat10)
u2_cell9.region = +surf301 & +surf302 & +surf304 & +surf305 & +surf306
u2_cell10 = openmc.Cell(fill=mat5)
u2_cell10.region = +surf310 & -surf311
u2_cell11 = openmc.Cell(fill=mat9)
u2_cell11.region = +surf311 & -surf199
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8, u2_cell9, u2_cell10, u2_cell11])

u3_cell0 = openmc.Cell(fill=mat10)
u3_cell0.region = -surf401
u3_cell1 = openmc.Cell(fill=mat4)
u3_cell1.region = -surf402
u3_cell2 = openmc.Cell(fill=mat10)
u3_cell2.region = +surf402 & -surf403
u3_cell3 = openmc.Cell(fill=mat10)
u3_cell3.region = -surf404
u3_cell4 = openmc.Cell(fill=mat6)
u3_cell4.region = +surf401 & +surf402 & +surf403 & +surf404 & -surf405
u3_cell5 = openmc.Cell(fill=mat9)
u3_cell5.region = +surf405 & -surf199
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4, u3_cell5])

u4_cell0 = openmc.Cell(fill=mat9)
u4_cell1 = openmc.Cell(fill=mat9)
u4_cell2 = openmc.Cell(fill=mat9)
u4_cell3 = openmc.Cell(fill=mat9)
u4_cell4 = openmc.Cell(fill=mat9)
u4_cell5 = openmc.Cell(fill=mat9)
u4_cell6 = openmc.Cell(fill=mat9)
u4_cell7 = openmc.Cell(fill=mat9)
u4_cell8 = openmc.Cell(fill=mat9)
u4_cell9 = openmc.Cell(fill=mat9)
u4_cell10 = openmc.Cell(fill=mat9)
u4_cell11 = openmc.Cell(fill=mat9)
u4_cell12 = openmc.Cell(fill=mat9)
u4_cell13 = openmc.Cell(fill=mat6)
u4_cell13.region = -surf100 & +surf1
u4_cell14 = openmc.Cell(fill=mat6)
u4_cell14.region = -surf101 & +surf1
u4_cell15 = openmc.Cell(fill=mat6)
u4_cell15.region = +surf110 & -surf111 & -surf116
u4_cell16 = openmc.Cell(fill=mat6)
u4_cell16.region = +surf111 & +surf115 & -surf116
u4_cell17 = openmc.Cell(fill=mat8)
u4_cell17.region = +surf111 & -surf112 & -surf115
u4_cell18 = openmc.Cell(fill=mat10)
u4_cell18.region = +surf112 & -surf113 & +surf114 & -surf115
u4_cell19 = openmc.Cell(fill=mat8)
u4_cell19.region = +surf112 & -surf113 & -surf114 & -surf115
u4_cell20 = openmc.Cell(fill=mat8)
u4_cell20.region = +surf113 & -surf115
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4, u4_cell5, u4_cell6, u4_cell7, u4_cell8, u4_cell9, u4_cell10, u4_cell11, u4_cell12, u4_cell13, u4_cell14, u4_cell15, u4_cell16, u4_cell17, u4_cell18, u4_cell19, u4_cell20])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# RX
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = -surf199

# Water
cell31 = openmc.Cell(cell_id=31, fill=mat9)
cell31.region = +surf207 & -surf199

# Water
cell44 = openmc.Cell(cell_id=44, fill=mat9)
cell44.region = +surf311 & -surf199

# Water
cell51 = openmc.Cell(cell_id=51, fill=mat9)
cell51.region = +surf405 & -surf199

root_universe = openmc.Universe(cells=[cell1, cell31, cell44, cell51])
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
