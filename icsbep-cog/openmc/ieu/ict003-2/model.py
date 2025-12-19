"""
ICT003-2: TRIGA Mark II Reactor with U(20) Fuel - Core 133
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

surf1 = openmc.ZCylinder(surface_id=1, r=1.87706)
surf2 = openmc.ZCylinder(surface_id=2, x0=4.0538, y0=0.0, r=1.87706)
surf3 = openmc.ZCylinder(surface_id=3, x0=2.0269, y0=3.510694, r=1.87706)
surf4 = openmc.ZCylinder(surface_id=4, x0=-2.0269, y0=3.510694, r=1.87706)
surf5 = openmc.ZCylinder(surface_id=5, x0=-4.0538, y0=0.0, r=1.87706)
surf6 = openmc.ZCylinder(surface_id=6, x0=-2.0269, y0=-3.510694, r=1.87706)
surf7 = openmc.ZCylinder(surface_id=7, x0=2.0269, y0=-3.510694, r=1.87706)
surf8 = openmc.ZCylinder(surface_id=8, x0=7.9807, y0=0.0, r=1.87706)
surf9 = openmc.ZCylinder(surface_id=9, x0=6.911489, y0=3.99035, r=1.87706)
surf10 = openmc.ZCylinder(surface_id=10, x0=3.99035, y0=6.911489, r=1.87706)
surf11 = openmc.ZCylinder(surface_id=11, x0=0.0, y0=7.9807, r=1.87706)
surf12 = openmc.ZCylinder(surface_id=12, x0=-3.99035, y0=6.911489, r=1.87706)
surf13 = openmc.ZCylinder(surface_id=13, x0=-6.911489, y0=3.99035, r=1.87706)
surf14 = openmc.ZCylinder(surface_id=14, x0=-7.9807, y0=0.0, r=1.87706)
surf15 = openmc.ZCylinder(surface_id=15, x0=-6.911489, y0=-3.99035, r=1.87706)
surf16 = openmc.ZCylinder(surface_id=16, x0=-3.99035, y0=-6.911489, r=1.87706)
surf17 = openmc.ZCylinder(surface_id=17, x0=0.0, y0=-7.9807, r=1.87706)
surf18 = openmc.ZCylinder(surface_id=18, x0=3.99035, y0=-6.911489, r=1.87706)
surf19 = openmc.ZCylinder(surface_id=19, x0=6.911489, y0=-3.99035, r=1.87706)
surf20 = openmc.ZCylinder(surface_id=20, x0=11.9456, y0=0.0, r=1.87706)
surf21 = openmc.ZCylinder(surface_id=21, x0=11.225192, y0=4.085636, r=1.87706)
surf22 = openmc.ZCylinder(surface_id=22, x0=9.15086, y0=7.678484, r=1.87706)
surf23 = openmc.ZCylinder(surface_id=23, x0=5.9728, y0=10.345193, r=1.87706)
surf24 = openmc.ZCylinder(surface_id=24, x0=2.074332, y0=11.764119, r=1.87706)
surf25 = openmc.ZCylinder(surface_id=25, x0=-2.074332, y0=11.764119, r=1.87706)
surf26 = openmc.ZCylinder(surface_id=26, x0=-5.9728, y0=10.345193, r=1.87706)
surf27 = openmc.ZCylinder(surface_id=27, x0=-9.15086, y0=7.678484, r=1.87706)
surf28 = openmc.ZCylinder(surface_id=28, x0=-11.225192, y0=4.085636, r=1.87706)
surf29 = openmc.ZCylinder(surface_id=29, x0=-11.9456, y0=0.0, r=1.87706)
surf30 = openmc.ZCylinder(surface_id=30, x0=-11.225192, y0=-4.085636, r=1.87706)
surf31 = openmc.ZCylinder(surface_id=31, x0=-9.15086, y0=-7.678484, r=1.87706)
surf32 = openmc.ZCylinder(surface_id=32, x0=-5.9728, y0=-10.345193, r=1.87706)
surf33 = openmc.ZCylinder(surface_id=33, x0=-2.074332, y0=-11.764119, r=1.87706)
surf34 = openmc.ZCylinder(surface_id=34, x0=2.074332, y0=-11.764119, r=1.87706)
surf35 = openmc.ZCylinder(surface_id=35, x0=5.9728, y0=-10.345193, r=1.87706)
surf36 = openmc.ZCylinder(surface_id=36, x0=9.15086, y0=-7.678484, r=1.87706)
surf37 = openmc.ZCylinder(surface_id=37, x0=11.225192, y0=-4.085636, r=1.87706)
surf38 = openmc.ZCylinder(surface_id=38, x0=15.9156, y0=0.0, r=1.87706)
surf39 = openmc.ZCylinder(surface_id=39, x0=15.373289, y0=4.11926, r=1.87706)
surf40 = openmc.ZCylinder(surface_id=40, x0=13.78331, y0=7.9578, r=1.87706)
surf41 = openmc.ZCylinder(surface_id=41, x0=11.254029, y0=11.254029, r=1.87706)
surf42 = openmc.ZCylinder(surface_id=42, x0=7.9578, y0=13.78331, r=1.87706)
surf43 = openmc.ZCylinder(surface_id=43, x0=4.11926, y0=15.373289, r=1.87706)
surf44 = openmc.ZCylinder(surface_id=44, x0=0.0, y0=15.9156, r=1.87706)
surf45 = openmc.ZCylinder(surface_id=45, x0=-4.11926, y0=15.373289, r=1.87706)
surf46 = openmc.ZCylinder(surface_id=46, x0=-7.9578, y0=13.78331, r=1.87706)
surf47 = openmc.ZCylinder(surface_id=47, x0=-11.254029, y0=11.254029, r=1.87706)
surf48 = openmc.ZCylinder(surface_id=48, x0=-13.78331, y0=7.9578, r=1.87706)
surf49 = openmc.ZCylinder(surface_id=49, x0=-15.373289, y0=4.11926, r=1.87706)
surf50 = openmc.ZCylinder(surface_id=50, x0=-15.9156, y0=0.0, r=1.87706)
surf51 = openmc.ZCylinder(surface_id=51, x0=-15.373289, y0=-4.11926, r=1.87706)
surf52 = openmc.ZCylinder(surface_id=52, x0=-13.78331, y0=-7.9578, r=1.87706)
surf53 = openmc.ZCylinder(surface_id=53, x0=-11.254029, y0=-11.254029, r=1.87706)
surf54 = openmc.ZCylinder(surface_id=54, x0=-7.9578, y0=-13.78331, r=1.87706)
surf55 = openmc.ZCylinder(surface_id=55, x0=-4.11926, y0=-15.373289, r=1.87706)
surf56 = openmc.ZCylinder(surface_id=56, x0=0.0, y0=-15.9156, r=1.87706)
surf57 = openmc.ZCylinder(surface_id=57, x0=4.11926, y0=-15.373289, r=1.87706)
surf58 = openmc.ZCylinder(surface_id=58, x0=7.9578, y0=-13.78331, r=1.87706)
surf59 = openmc.ZCylinder(surface_id=59, x0=11.254029, y0=-11.254029, r=1.87706)
surf60 = openmc.ZCylinder(surface_id=60, x0=13.78331, y0=-7.9578, r=1.87706)
surf61 = openmc.ZCylinder(surface_id=61, x0=15.373289, y0=-4.11926, r=1.87706)
surf62 = openmc.ZCylinder(surface_id=62, x0=19.8882, y0=0.0, r=1.87706)
surf63 = openmc.ZCylinder(surface_id=63, x0=19.453595, y0=4.134989, r=1.87706)
surf64 = openmc.ZCylinder(surface_id=64, x0=18.168775, y0=8.08926, r=1.87706)
surf65 = openmc.ZCylinder(surface_id=65, x0=16.089892, y0=11.689991, r=1.87706)
surf66 = openmc.ZCylinder(surface_id=66, x0=13.307803, y0=14.779813, r=1.87706)
surf67 = openmc.ZCylinder(surface_id=67, x0=9.9441, y0=17.223686, r=1.87706)
surf68 = openmc.ZCylinder(surface_id=68, x0=6.145792, y0=18.914802, r=1.87706)
surf69 = openmc.ZCylinder(surface_id=69, x0=2.078883, y0=19.77925, r=1.87706)
surf70 = openmc.ZCylinder(surface_id=70, x0=-2.078883, y0=19.77925, r=1.87706)
surf71 = openmc.ZCylinder(surface_id=71, x0=-6.145792, y0=18.914802, r=1.87706)
surf72 = openmc.ZCylinder(surface_id=72, x0=-9.9441, y0=17.223686, r=1.87706)
surf73 = openmc.ZCylinder(surface_id=73, x0=-13.307803, y0=14.779813, r=1.87706)
surf74 = openmc.ZCylinder(surface_id=74, x0=-16.089892, y0=11.689991, r=1.87706)
surf75 = openmc.ZCylinder(surface_id=75, x0=-18.168775, y0=8.08926, r=1.87706)
surf76 = openmc.ZCylinder(surface_id=76, x0=-19.453595, y0=4.134989, r=1.87706)
surf77 = openmc.ZCylinder(surface_id=77, x0=-19.8882, y0=0.0, r=1.87706)
surf78 = openmc.ZCylinder(surface_id=78, x0=-19.453595, y0=-4.134989, r=1.87706)
surf79 = openmc.ZCylinder(surface_id=79, x0=-18.168775, y0=-8.08926, r=1.87706)
surf80 = openmc.ZCylinder(surface_id=80, x0=-16.089892, y0=-11.689991, r=1.87706)
surf81 = openmc.ZCylinder(surface_id=81, x0=-13.307803, y0=-14.779813, r=1.87706)
surf82 = openmc.ZCylinder(surface_id=82, x0=-9.9441, y0=-17.223686, r=1.87706)
surf83 = openmc.ZCylinder(surface_id=83, x0=-6.145792, y0=-18.914802, r=1.87706)
surf84 = openmc.ZCylinder(surface_id=84, x0=-2.078883, y0=-19.77925, r=1.87706)
surf85 = openmc.ZCylinder(surface_id=85, x0=2.078883, y0=-19.77925, r=1.87706)
surf86 = openmc.ZCylinder(surface_id=86, x0=6.145792, y0=-18.914802, r=1.87706)
surf87 = openmc.ZCylinder(surface_id=87, x0=9.9441, y0=-17.223686, r=1.87706)
surf88 = openmc.ZCylinder(surface_id=88, x0=13.307803, y0=-14.779813, r=1.87706)
surf89 = openmc.ZCylinder(surface_id=89, x0=16.089892, y0=-11.689991, r=1.87706)
surf90 = openmc.ZCylinder(surface_id=90, x0=18.168775, y0=-8.08926, r=1.87706)
surf91 = openmc.ZCylinder(surface_id=91, x0=19.453595, y0=-4.134989, r=1.87706)
# Lower aluminum support grid
surf100 = openmc.ZCylinder(surface_id=100, r=22.06)
# Upper aluminum support grid
surf101 = openmc.ZCylinder(surface_id=101, r=22.06)
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
surf115 = openmc.ZCylinder(surface_id=115, r=53.14)
# Cladding/outer
surf116 = openmc.ZCylinder(surface_id=116, r=54.41)
# Water/outer/bcd
surf199 = openmc.ZCylinder(surface_id=199, r=98.4)
# Graphite/lower
surf201 = openmc.ZCylinder(surface_id=201, r=1.8161)
# Mo disc
surf202 = openmc.ZCylinder(surface_id=202, r=1.82626)
# Zr Rod
surf203 = openmc.ZCylinder(surface_id=203, r=0.3175)
# U-ZrH Fuel
surf204 = openmc.ZCylinder(surface_id=204, r=1.82245)
# Graphite/upper
surf205 = openmc.ZCylinder(surface_id=205, r=1.8161)
# Clad/inner
surf206 = openmc.ZCylinder(surface_id=206, r=1.82626)
# Clad/outer
surf207 = openmc.ZCylinder(surface_id=207, r=1.87706)
# Void/lower
surf301 = openmc.ZCylinder(surface_id=301, r=1.69545)
# SS304/lower
surf302 = openmc.ZCylinder(surface_id=302, r=1.69545)
# Zr Rod
surf303 = openmc.ZCylinder(surface_id=303, r=0.3175)
# U-ZrH Fuel
surf304 = openmc.ZCylinder(surface_id=304, r=1.666875)
# Void
surf305 = openmc.ZCylinder(surface_id=305, r=1.69545)
# SS304/middle
surf306 = openmc.ZCylinder(surface_id=306, r=1.69545)
# B4C Absorber
surf307 = openmc.ZCylinder(surface_id=307, r=1.666875)
# SS304/upper
surf308 = openmc.ZCylinder(surface_id=308, r=1.69545)
# Void
surf309 = openmc.ZCylinder(surface_id=309, r=1.69545)
# Clad/inner
surf310 = openmc.ZCylinder(surface_id=310, r=1.69545)
# Clad/outer
surf311 = openmc.ZCylinder(surface_id=311, r=1.74625)
# Void/lower
surf401 = openmc.ZCylinder(surface_id=401, r=1.51638)
# B4C Absorber
surf402 = openmc.ZCylinder(surface_id=402, r=1.51638)
# Void/middle
surf403 = openmc.ZCylinder(surface_id=403, r=1.51638)
# Void/upper
surf404 = openmc.ZCylinder(surface_id=404, r=1.51638)
# Al clad/outer
surf405 = openmc.ZCylinder(surface_id=405, r=1.87706)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=-36.83)
surf1_zmax = openmc.ZPlane(z0=74.295)
surf100_zmin = openmc.ZPlane(z0=-36.2)
surf100_zmax = openmc.ZPlane(z0=-34.295)
surf101_zmin = openmc.ZPlane(z0=28.88)
surf101_zmax = openmc.ZPlane(z0=30.785)
surf115_zmin = openmc.ZPlane(z0=-26.975)
surf115_zmax = openmc.ZPlane(z0=26.975)
surf116_zmin = openmc.ZPlane(z0=-28.245)
surf116_zmax = openmc.ZPlane(z0=28.245)
surf199_zmin = openmc.ZPlane(z0=-100.0, boundary_type="vacuum")
surf199_zmax = openmc.ZPlane(z0=100.0, boundary_type="vacuum")
surf201_zmin = openmc.ZPlane(z0=-28.527375)
surf201_zmax = openmc.ZPlane(z0=-19.129375)
surf202_zmin = openmc.ZPlane(z0=-19.129375)
surf202_zmax = openmc.ZPlane(z0=-19.05)
surf204_zmin = openmc.ZPlane(z0=-19.05)
surf204_zmax = openmc.ZPlane(z0=19.05)
surf205_zmin = openmc.ZPlane(z0=19.05)
surf205_zmax = openmc.ZPlane(z0=25.654)
surf206_zmin = openmc.ZPlane(z0=-28.527375)
surf206_zmax = openmc.ZPlane(z0=25.654)
surf207_zmin = openmc.ZPlane(z0=-36.03)
surf207_zmax = openmc.ZPlane(z0=36.03)
surf301_zmin = openmc.ZPlane(z0=-35.56)
surf301_zmax = openmc.ZPlane(z0=-21.59)
surf302_zmin = openmc.ZPlane(z0=-21.59)
surf302_zmax = openmc.ZPlane(z0=-19.05)
surf304_zmin = openmc.ZPlane(z0=-19.05)
surf304_zmax = openmc.ZPlane(z0=19.05)
surf305_zmin = openmc.ZPlane(z0=19.05)
surf305_zmax = openmc.ZPlane(z0=19.84375)
surf306_zmin = openmc.ZPlane(z0=19.84375)
surf306_zmax = openmc.ZPlane(z0=21.11375)
surf307_zmin = openmc.ZPlane(z0=21.11375)
surf307_zmax = openmc.ZPlane(z0=59.69)
surf308_zmin = openmc.ZPlane(z0=59.69)
surf308_zmax = openmc.ZPlane(z0=60.96)
surf309_zmin = openmc.ZPlane(z0=60.96)
surf309_zmax = openmc.ZPlane(z0=70.485)
surf310_zmin = openmc.ZPlane(z0=-35.56)
surf310_zmax = openmc.ZPlane(z0=70.485)
surf311_zmin = openmc.ZPlane(z0=-36.83)
surf311_zmax = openmc.ZPlane(z0=74.295)
surf401_zmin = openmc.ZPlane(z0=-35.56)
surf401_zmax = openmc.ZPlane(z0=19.84375)
surf402_zmin = openmc.ZPlane(z0=21.11375)
surf402_zmax = openmc.ZPlane(z0=59.21375)
surf403_zmin = openmc.ZPlane(z0=59.21375)
surf403_zmax = openmc.ZPlane(z0=59.69)
surf404_zmin = openmc.ZPlane(z0=60.96)
surf404_zmax = openmc.ZPlane(z0=70.485)
surf405_zmin = openmc.ZPlane(z0=-36.83)
surf405_zmax = openmc.ZPlane(z0=74.295)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat8)
u1_cell0.region = (-surf201 & +surf201_zmin & -surf201_zmax)
u1_cell1 = openmc.Cell(fill=mat7)
u1_cell1.region = (+surf201 | -surf201_zmin | +surf201_zmax) & (-surf202 & +surf202_zmin & -surf202_zmax)
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = (+surf202 | -surf202_zmin | +surf202_zmax) & -surf203 & (-surf204 & +surf204_zmin & -surf204_zmax)
u1_cell3 = openmc.Cell(fill=mat1)
u1_cell3.region = (+surf202 | -surf202_zmin | +surf202_zmax) & +surf203 & (-surf204 & +surf204_zmin & -surf204_zmax)
u1_cell4 = openmc.Cell(fill=mat8)
u1_cell4.region = (+surf204 | -surf204_zmin | +surf204_zmax) & (-surf205 & +surf205_zmin & -surf205_zmax)
u1_cell5 = openmc.Cell(fill=mat10)
u1_cell5.region = (+surf201 | -surf201_zmin | +surf201_zmax) & (+surf202 | -surf202_zmin | +surf202_zmax) & (+surf204 | -surf204_zmin | +surf204_zmax) & (+surf205 | -surf205_zmin | +surf205_zmax) & (-surf206 & +surf206_zmin & -surf206_zmax)
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = (+surf206 | -surf206_zmin | +surf206_zmax) & (-surf207 & +surf207_zmin & -surf207_zmax)
u1_cell7 = openmc.Cell(fill=mat9)
u1_cell7.region = (+surf207 | -surf207_zmin | +surf207_zmax) & (-surf199 & +surf199_zmin & -surf199_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7])

u2_cell0 = openmc.Cell(fill=mat10)
u2_cell0.region = (-surf301 & +surf301_zmin & -surf301_zmax) & (-surf310 & +surf310_zmin & -surf310_zmax)
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = (+surf301 | -surf301_zmin | +surf301_zmax) & (-surf302 & +surf302_zmin & -surf302_zmax) & (-surf310 & +surf310_zmin & -surf310_zmax)
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = (+surf302 | -surf302_zmin | +surf302_zmax) & -surf303 & (-surf304 & +surf304_zmin & -surf304_zmax) & (-surf310 & +surf310_zmin & -surf310_zmax)
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = (+surf302 | -surf302_zmin | +surf302_zmax) & +surf303 & (-surf304 & +surf304_zmin & -surf304_zmax) & (-surf310 & +surf310_zmin & -surf310_zmax)
u2_cell4 = openmc.Cell(fill=mat10)
u2_cell4.region = (+surf304 | -surf304_zmin | +surf304_zmax) & (-surf305 & +surf305_zmin & -surf305_zmax) & (-surf310 & +surf310_zmin & -surf310_zmax)
u2_cell5 = openmc.Cell(fill=mat5)
u2_cell5.region = (+surf305 | -surf305_zmin | +surf305_zmax) & (-surf306 & +surf306_zmin & -surf306_zmax) & (-surf310 & +surf310_zmin & -surf310_zmax)
u2_cell6 = openmc.Cell(fill=mat4)
u2_cell6.region = (+surf306 | -surf306_zmin | +surf306_zmax) & (-surf307 & +surf307_zmin & -surf307_zmax) & (-surf310 & +surf310_zmin & -surf310_zmax)
u2_cell7 = openmc.Cell(fill=mat5)
u2_cell7.region = (+surf307 | -surf307_zmin | +surf307_zmax) & (-surf308 & +surf308_zmin & -surf308_zmax) & (-surf310 & +surf310_zmin & -surf310_zmax)
u2_cell8 = openmc.Cell(fill=mat10)
u2_cell8.region = (+surf308 | -surf308_zmin | +surf308_zmax) & (-surf309 & +surf309_zmin & -surf309_zmax) & (-surf310 & +surf310_zmin & -surf310_zmax)
u2_cell9 = openmc.Cell(fill=mat10)
u2_cell9.region = (+surf301 | -surf301_zmin | +surf301_zmax) & (+surf302 | -surf302_zmin | +surf302_zmax) & (+surf304 | -surf304_zmin | +surf304_zmax) & (+surf305 | -surf305_zmin | +surf305_zmax) & (+surf306 | -surf306_zmin | +surf306_zmax)
u2_cell10 = openmc.Cell(fill=mat5)
u2_cell10.region = (+surf310 | -surf310_zmin | +surf310_zmax) & (-surf311 & +surf311_zmin & -surf311_zmax)
u2_cell11 = openmc.Cell(fill=mat9)
u2_cell11.region = (+surf311 | -surf311_zmin | +surf311_zmax) & (-surf199 & +surf199_zmin & -surf199_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8, u2_cell9, u2_cell10, u2_cell11])

u3_cell0 = openmc.Cell(fill=mat10)
u3_cell0.region = (-surf401 & +surf401_zmin & -surf401_zmax)
u3_cell1 = openmc.Cell(fill=mat4)
u3_cell1.region = (-surf402 & +surf402_zmin & -surf402_zmax)
u3_cell2 = openmc.Cell(fill=mat10)
u3_cell2.region = (+surf402 | -surf402_zmin | +surf402_zmax) & (-surf403 & +surf403_zmin & -surf403_zmax)
u3_cell3 = openmc.Cell(fill=mat10)
u3_cell3.region = (-surf404 & +surf404_zmin & -surf404_zmax)
u3_cell4 = openmc.Cell(fill=mat6)
u3_cell4.region = (+surf401 | -surf401_zmin | +surf401_zmax) & (+surf402 | -surf402_zmin | +surf402_zmax) & (+surf403 | -surf403_zmin | +surf403_zmax) & (+surf404 | -surf404_zmin | +surf404_zmax) & (-surf405 & +surf405_zmin & -surf405_zmax)
u3_cell5 = openmc.Cell(fill=mat9)
u3_cell5.region = (+surf405 | -surf405_zmin | +surf405_zmax) & (-surf199 & +surf199_zmin & -surf199_zmax)
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4, u3_cell5])

u4_cell0 = openmc.Cell(fill=mat9)
u4_cell0.region = -surf38 & +surf9 & -surf39 & +surf9 & -surf40
u4_cell1 = openmc.Cell(fill=mat9)
u4_cell1.region = -surf48 & +surf9 & -surf49 & +surf9 & -surf50
u4_cell2 = openmc.Cell(fill=mat9)
u4_cell2.region = -surf51 & +surf9 & -surf52 & +surf9 & -surf53
u4_cell3 = openmc.Cell(fill=mat9)
u4_cell3.region = -surf54 & +surf9 & -surf55 & +surf9 & -surf56
u4_cell4 = openmc.Cell(fill=mat9)
u4_cell4.region = -surf57 & +surf9 & -surf58 & +surf9 & -surf59
u4_cell5 = openmc.Cell(fill=mat9)
u4_cell5.region = -surf60 & +surf9 & -surf61
u4_cell6 = openmc.Cell(fill=mat9)
u4_cell6.region = -surf62 & +surf9 & -surf63 & +surf9 & -surf64 & +surf9 & -surf65
u4_cell7 = openmc.Cell(fill=mat9)
u4_cell7.region = -surf66 & +surf9 & -surf67 & +surf9 & -surf68 & +surf9 & -surf69
u4_cell8 = openmc.Cell(fill=mat9)
u4_cell8.region = -surf70 & +surf9 & -surf71 & +surf9 & -surf72 & +surf9 & -surf73
u4_cell9 = openmc.Cell(fill=mat9)
u4_cell9.region = -surf74 & +surf9 & -surf75 & +surf9 & -surf76 & +surf9 & -surf77
u4_cell10 = openmc.Cell(fill=mat9)
u4_cell10.region = -surf78 & +surf9 & -surf79 & +surf9 & -surf80 & +surf9 & -surf81
u4_cell11 = openmc.Cell(fill=mat9)
u4_cell11.region = -surf82 & +surf9 & -surf83 & +surf9 & -surf84 & +surf9 & -surf85
u4_cell12 = openmc.Cell(fill=mat9)
u4_cell12.region = -surf86 & +surf9 & -surf87 & +surf9 & -surf88 & +surf9 & -surf89
u4_cell13 = openmc.Cell(fill=mat9)
u4_cell13.region = -surf90 & +surf9 & -surf91
u4_cell14 = openmc.Cell(fill=mat6)
u4_cell14.region = (-surf100 & +surf100_zmin & -surf100_zmax) & (+surf1 | -surf1_zmin | +surf1_zmax) & +surf2 & +surf3 & +surf4 & +surf5 & +surf6 & +surf7 & +surf8 & +surf9 & +surf10 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & +surf17 & +surf18 & +surf19 & +surf20
u4_cell15 = openmc.Cell(fill=mat6)
u4_cell15.region = (-surf101 & +surf101_zmin & -surf101_zmax) & (+surf1 | -surf1_zmin | +surf1_zmax) & +surf2 & +surf3 & +surf4 & +surf5 & +surf6 & +surf7 & +surf8 & +surf9 & +surf10 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & +surf16 & +surf17 & +surf18 & +surf19 & +surf20
u4_cell16 = openmc.Cell(fill=mat6)
u4_cell16.region = +surf110 & -surf111 & (-surf116 & +surf116_zmin & -surf116_zmax)
u4_cell17 = openmc.Cell(fill=mat6)
u4_cell17.region = +surf111 & (+surf115 | -surf115_zmin | +surf115_zmax) & (-surf116 & +surf116_zmin & -surf116_zmax)
u4_cell18 = openmc.Cell(fill=mat8)
u4_cell18.region = +surf111 & -surf112 & (-surf115 & +surf115_zmin & -surf115_zmax)
u4_cell19 = openmc.Cell(fill=mat10)
u4_cell19.region = +surf112 & -surf113 & +surf114 & (-surf115 & +surf115_zmin & -surf115_zmax)
u4_cell20 = openmc.Cell(fill=mat8)
u4_cell20.region = +surf112 & -surf113 & -surf114 & (-surf115 & +surf115_zmin & -surf115_zmax)
u4_cell21 = openmc.Cell(fill=mat8)
u4_cell21.region = +surf113 & (-surf115 & +surf115_zmin & -surf115_zmax)
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4, u4_cell5, u4_cell6, u4_cell7, u4_cell8, u4_cell9, u4_cell10, u4_cell11, u4_cell12, u4_cell13, u4_cell14, u4_cell15, u4_cell16, u4_cell17, u4_cell18, u4_cell19, u4_cell20, u4_cell21])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# RX
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = (-surf199 & +surf199_zmin & -surf199_zmax)

# Water
cell32 = openmc.Cell(cell_id=32, fill=mat9)
cell32.region = (+surf207 | -surf207_zmin | +surf207_zmax) & (-surf199 & +surf199_zmin & -surf199_zmax)

# Water
cell45 = openmc.Cell(cell_id=45, fill=mat9)
cell45.region = (+surf311 | -surf311_zmin | +surf311_zmax) & (-surf199 & +surf199_zmin & -surf199_zmax)

# Water
cell52 = openmc.Cell(cell_id=52, fill=mat9)
cell52.region = (+surf405 | -surf405_zmin | +surf405_zmax) & (-surf199 & +surf199_zmin & -surf199_zmax)

root_universe = openmc.Universe(cells=[cell1, cell32, cell45, cell52])
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
