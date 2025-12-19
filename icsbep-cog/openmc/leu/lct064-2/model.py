"""
LCT064-2: Lattice of 1,495 U(2.4)O2 rods with 1.27 cm (triangular) pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(2.4)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("O16", 4.599500e-02)
mat1.add_nuclide("U234", 4.676900e-06)
mat1.add_nuclide("U235", 5.588300e-04)
mat1.add_nuclide("U238", 2.243400e-02)

# Zr-1Nb clad & plugs
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Zr", 4.279400e-02)
mat2.add_element("Nb", 4.245600e-04)
mat2.add_element("Hf", 6.629700e-06)

# SST
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.871500e-02)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Si", 1.355100e-03)
mat3.add_element("Mn", 9.525700e-04)
mat3.add_element("Ti", 6.955400e-04)
mat3.add_element("P", 5.375900e-05)
mat3.add_element("C", 4.753100e-04)
mat3.add_element("Cu", 2.246000e-04)
mat3.add_element("S", 2.966900e-05)

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("N", 4.248000e-05)
mat4.add_nuclide("O16", 1.128000e-05)

# Water
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.676200e-02)
mat5.add_nuclide("O16", 3.338100e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# UO2
surf1 = openmc.ZCylinder(surface_id=1, r=0.37875)
# Zr-Nb plug inner
surf2 = openmc.ZCylinder(surface_id=2, r=0.15)
# Zr-Nb plug outer
surf3 = openmc.ZCylinder(surface_id=3, r=0.3825)
# SST ring inner
surf4 = openmc.ZCylinder(surface_id=4, r=0.29)
# SST ring outer
surf5 = openmc.ZCylinder(surface_id=5, r=0.32)
# Zr-Nb clad inner
surf6 = openmc.ZCylinder(surface_id=6, r=0.3875)
# Zr-Nb clad outer
surf7 = openmc.ZCylinder(surface_id=7, r=0.451555)
# Zr-Nb clad top and bottom
surf8 = openmc.ZCylinder(surface_id=8, r=0.3)
# Critical moderator height
surf10 = openmc.ZPlane(surface_id=10, z0=50.87)
# Lower grid plate - hole
surf11 = openmc.ZCylinder(surface_id=11, r=0.31)
# Lower grid plate
surf12 = openmc.ZCylinder(surface_id=12, r=50.0)
# Upper grid plate - hole
surf13 = openmc.ZCylinder(surface_id=13, r=0.47)
# Upper grid plate
surf14 = openmc.ZCylinder(surface_id=14, r=50.0)
# water, air, and boundary condition
surf15 = openmc.ZCylinder(surface_id=15, r=65.0, boundary_type="vacuum")
surf21 = openmc.ZCylinder(surface_id=21, x0=-0.635, y0=1.099852, r=0.47)
surf22 = openmc.ZCylinder(surface_id=22, x0=0.635, y0=1.099852, r=0.47)
surf23 = openmc.ZCylinder(surface_id=23, x0=-0.635, y0=-1.099852, r=0.47)
surf24 = openmc.ZCylinder(surface_id=24, x0=0.635, y0=-1.099852, r=0.47)
# Prism 31: 12-sided polygon
surf31_0 = openmc.Plane(a=0.4999999862, b=-0.8660254118, c=0, d=23.4949983875)
surf31_1 = openmc.Plane(a=0.8660253521, b=-0.5000000896, c=0, d=25.2966015334)
surf31_2 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=23.4950000000)
surf31_3 = openmc.Plane(a=0.8660253521, b=0.5000000896, c=0, d=25.2966015334)
surf31_4 = openmc.Plane(a=0.4999999862, b=0.8660254118, c=0, d=23.4949983875)
surf31_5 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=25.2966000000)
surf31_6 = openmc.Plane(a=-0.4999999862, b=0.8660254118, c=0, d=23.4949983875)
surf31_7 = openmc.Plane(a=-0.8660253521, b=0.5000000896, c=0, d=25.2966015334)
surf31_8 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=23.4950000000)
surf31_9 = openmc.Plane(a=-0.8660253521, b=-0.5000000896, c=0, d=25.2966015334)
surf31_10 = openmc.Plane(a=-0.4999999862, b=-0.8660254118, c=0, d=23.4949983875)
surf31_11 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=25.2966000000)
# Prism 32: 12-sided polygon
surf32_0 = openmc.Plane(a=0.4999992285, b=-0.8660258492, c=0, d=26.0350031285)
surf32_1 = openmc.Plane(a=0.8660254764, b=-0.4999998743, c=0, d=23.0968981392)
surf32_2 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=26.0350000000)
surf32_3 = openmc.Plane(a=0.8660254764, b=0.4999998743, c=0, d=23.0968981392)
surf32_4 = openmc.Plane(a=0.4999992285, b=0.8660258492, c=0, d=26.0350031285)
surf32_5 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=23.0969000000)
surf32_6 = openmc.Plane(a=-0.4999992285, b=0.8660258492, c=0, d=26.0350031285)
surf32_7 = openmc.Plane(a=-0.8660254764, b=0.4999998743, c=0, d=23.0968981392)
surf32_8 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=26.0350000000)
surf32_9 = openmc.Plane(a=-0.8660254764, b=-0.4999998743, c=0, d=23.0968981392)
surf32_10 = openmc.Plane(a=-0.4999992285, b=-0.8660258492, c=0, d=26.0350031285)
surf32_11 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=23.0969000000)
# Prism 33: 12-sided polygon
surf33_0 = openmc.Plane(a=0.4999997967, b=-0.8660255211, c=0, d=26.6699978185)
surf33_1 = openmc.Plane(a=0.8660254505, b=-0.4999999191, c=0, d=26.3964532305)
surf33_2 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=26.6700000000)
surf33_3 = openmc.Plane(a=0.8660254505, b=0.4999999191, c=0, d=26.3964532305)
surf33_4 = openmc.Plane(a=0.4999997967, b=0.8660255211, c=0, d=26.6699978185)
surf33_5 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=26.3964500000)
surf33_6 = openmc.Plane(a=-0.5001638836, b=0.8659307649, c=0, d=26.6712477509)
surf33_7 = openmc.Plane(a=-0.8660254505, b=0.4999999191, c=0, d=26.3964532305)
surf33_8 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=26.6700000000)
surf33_9 = openmc.Plane(a=-0.8660254505, b=-0.4999999191, c=0, d=26.3964532305)
surf33_10 = openmc.Plane(a=-0.4999997967, b=-0.8660255211, c=0, d=26.6699978185)
surf33_11 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=26.3964500000)
# Prism 34: 6-sided polygon
surf34_0 = openmc.Plane(a=0.8660254126, b=-0.4999999847, c=0, d=28.5961591247)
surf34_1 = openmc.Plane(a=0.8660254126, b=0.4999999847, c=0, d=28.5961591247)
surf34_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=28.5961600000)
surf34_3 = openmc.Plane(a=-0.8660254126, b=0.4999999847, c=0, d=28.5961591247)
surf34_4 = openmc.Plane(a=-0.8660254126, b=-0.4999999847, c=0, d=28.5961591247)
surf34_5 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=28.5961600000)
surf41 = openmc.YPlane(surface_id=41, y0=0.0)
surf42 = openmc.ZPlane(surface_id=42, z0=0)
surf43 = openmc.ZPlane(surface_id=43, z0=0)
surf101 = openmc.ZCylinder(surface_id=101, x0=-16.51, y0=28.59616, r=0.47)
surf102 = openmc.ZCylinder(surface_id=102, x0=-15.24, y0=28.59616, r=0.47)
surf103 = openmc.ZCylinder(surface_id=103, x0=-13.97, y0=28.59616, r=0.47)
surf104 = openmc.ZCylinder(surface_id=104, x0=-12.7, y0=28.59616, r=0.47)
surf105 = openmc.ZCylinder(surface_id=105, x0=-11.43, y0=28.59616, r=0.47)
surf106 = openmc.ZCylinder(surface_id=106, x0=-10.16, y0=28.59616, r=0.47)
surf107 = openmc.ZCylinder(surface_id=107, x0=-8.89, y0=28.59616, r=0.47)
surf108 = openmc.ZCylinder(surface_id=108, x0=-7.62, y0=28.59616, r=0.47)
surf109 = openmc.ZCylinder(surface_id=109, x0=-6.35, y0=28.59616, r=0.47)
surf110 = openmc.ZCylinder(surface_id=110, x0=-5.08, y0=28.59616, r=0.47)
surf111 = openmc.ZCylinder(surface_id=111, x0=-3.81, y0=28.59616, r=0.47)
surf112 = openmc.ZCylinder(surface_id=112, x0=-2.54, y0=28.59616, r=0.47)
surf113 = openmc.ZCylinder(surface_id=113, x0=-1.27, y0=28.59616, r=0.47)
surf114 = openmc.ZCylinder(surface_id=114, x0=0.0, y0=28.59616, r=0.47)
surf115 = openmc.ZCylinder(surface_id=115, x0=1.27, y0=28.59616, r=0.47)
surf116 = openmc.ZCylinder(surface_id=116, x0=2.54, y0=28.59616, r=0.47)
surf117 = openmc.ZCylinder(surface_id=117, x0=3.81, y0=28.59616, r=0.47)
surf118 = openmc.ZCylinder(surface_id=118, x0=5.08, y0=28.59616, r=0.47)
surf119 = openmc.ZCylinder(surface_id=119, x0=6.35, y0=28.59616, r=0.47)
surf120 = openmc.ZCylinder(surface_id=120, x0=7.62, y0=28.59616, r=0.47)
surf121 = openmc.ZCylinder(surface_id=121, x0=8.89, y0=28.59616, r=0.47)
surf122 = openmc.ZCylinder(surface_id=122, x0=10.16, y0=28.59616, r=0.47)
surf123 = openmc.ZCylinder(surface_id=123, x0=11.43, y0=28.59616, r=0.47)
surf124 = openmc.ZCylinder(surface_id=124, x0=12.7, y0=28.59616, r=0.47)
surf125 = openmc.ZCylinder(surface_id=125, x0=13.97, y0=28.59616, r=0.47)
surf126 = openmc.ZCylinder(surface_id=126, x0=15.24, y0=28.59616, r=0.47)
surf127 = openmc.ZCylinder(surface_id=127, x0=16.51, y0=28.59616, r=0.47)
surf201 = openmc.ZCylinder(surface_id=201, x0=-7.62, y0=26.39645, r=0.47)
surf202 = openmc.ZCylinder(surface_id=202, x0=-6.35, y0=26.39645, r=0.47)
surf203 = openmc.ZCylinder(surface_id=203, x0=-5.08, y0=26.39645, r=0.47)
surf204 = openmc.ZCylinder(surface_id=204, x0=-3.81, y0=26.39645, r=0.47)
surf205 = openmc.ZCylinder(surface_id=205, x0=-2.54, y0=26.39645, r=0.47)
surf206 = openmc.ZCylinder(surface_id=206, x0=-1.27, y0=26.39645, r=0.47)
surf207 = openmc.ZCylinder(surface_id=207, x0=0.0, y0=26.39645, r=0.47)
surf208 = openmc.ZCylinder(surface_id=208, x0=1.27, y0=26.39645, r=0.47)
surf209 = openmc.ZCylinder(surface_id=209, x0=2.54, y0=26.39645, r=0.47)
surf210 = openmc.ZCylinder(surface_id=210, x0=3.81, y0=26.39645, r=0.47)
surf211 = openmc.ZCylinder(surface_id=211, x0=5.08, y0=26.39645, r=0.47)
surf212 = openmc.ZCylinder(surface_id=212, x0=6.35, y0=26.39645, r=0.47)
surf213 = openmc.ZCylinder(surface_id=213, x0=7.62, y0=26.39645, r=0.47)
surf214 = openmc.ZCylinder(surface_id=214, x0=-9.525, y0=25.2966, r=0.47)
surf215 = openmc.ZCylinder(surface_id=215, x0=-8.255, y0=25.2966, r=0.47)
surf216 = openmc.ZCylinder(surface_id=216, x0=-6.985, y0=25.2966, r=0.47)
surf217 = openmc.ZCylinder(surface_id=217, x0=-5.715, y0=25.2966, r=0.47)
surf218 = openmc.ZCylinder(surface_id=218, x0=-4.445, y0=25.2966, r=0.47)
surf219 = openmc.ZCylinder(surface_id=219, x0=4.445, y0=25.2966, r=0.47)
surf220 = openmc.ZCylinder(surface_id=220, x0=5.715, y0=25.2966, r=0.47)
surf221 = openmc.ZCylinder(surface_id=221, x0=6.985, y0=25.2966, r=0.47)
surf222 = openmc.ZCylinder(surface_id=222, x0=8.255, y0=25.2966, r=0.47)
surf223 = openmc.ZCylinder(surface_id=223, x0=9.525, y0=25.2966, r=0.47)
surf224 = openmc.ZCylinder(surface_id=224, x0=-11.43, y0=24.19675, r=0.47)
surf225 = openmc.ZCylinder(surface_id=225, x0=-10.16, y0=24.19675, r=0.47)
surf226 = openmc.ZCylinder(surface_id=226, x0=-8.89, y0=24.19675, r=0.47)
surf227 = openmc.ZCylinder(surface_id=227, x0=8.89, y0=24.19675, r=0.47)
surf228 = openmc.ZCylinder(surface_id=228, x0=10.16, y0=24.19675, r=0.47)
surf229 = openmc.ZCylinder(surface_id=229, x0=11.43, y0=24.19675, r=0.47)
surf230 = openmc.ZCylinder(surface_id=230, x0=-13.335, y0=23.0969, r=0.47)
surf231 = openmc.ZCylinder(surface_id=231, x0=13.335, y0=23.0969, r=0.47)
surf301 = openmc.ZCylinder(surface_id=301, x0=-3.175, y0=25.2966, r=0.47)
surf302 = openmc.ZCylinder(surface_id=302, x0=-1.905, y0=25.2966, r=0.47)
surf303 = openmc.ZCylinder(surface_id=303, x0=-0.635, y0=25.2966, r=0.47)
surf304 = openmc.ZCylinder(surface_id=304, x0=0.635, y0=25.2966, r=0.47)
surf305 = openmc.ZCylinder(surface_id=305, x0=1.905, y0=25.2966, r=0.47)
surf306 = openmc.ZCylinder(surface_id=306, x0=3.175, y0=25.2966, r=0.47)
surf307 = openmc.ZCylinder(surface_id=307, x0=-7.62, y0=24.19675, r=0.47)
surf308 = openmc.ZCylinder(surface_id=308, x0=-6.35, y0=24.19675, r=0.47)
surf309 = openmc.ZCylinder(surface_id=309, x0=-5.08, y0=24.19675, r=0.47)
surf310 = openmc.ZCylinder(surface_id=310, x0=5.08, y0=24.19675, r=0.47)
surf311 = openmc.ZCylinder(surface_id=311, x0=6.35, y0=24.19675, r=0.47)
surf312 = openmc.ZCylinder(surface_id=312, x0=7.62, y0=24.19675, r=0.47)
surf313 = openmc.ZCylinder(surface_id=313, x0=-12.065, y0=23.0969, r=0.47)
surf314 = openmc.ZCylinder(surface_id=314, x0=-10.795, y0=23.0969, r=0.47)
surf315 = openmc.ZCylinder(surface_id=315, x0=-9.525, y0=23.0969, r=0.47)
surf316 = openmc.ZCylinder(surface_id=316, x0=-8.255, y0=23.0969, r=0.47)
surf317 = openmc.ZCylinder(surface_id=317, x0=-6.985, y0=23.0969, r=0.47)
surf318 = openmc.ZCylinder(surface_id=318, x0=6.985, y0=23.0969, r=0.47)
surf319 = openmc.ZCylinder(surface_id=319, x0=8.255, y0=23.0969, r=0.47)
surf320 = openmc.ZCylinder(surface_id=320, x0=9.525, y0=23.0969, r=0.47)
surf321 = openmc.ZCylinder(surface_id=321, x0=10.795, y0=23.0969, r=0.47)
surf322 = openmc.ZCylinder(surface_id=322, x0=12.065, y0=23.0969, r=0.47)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1322, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1323, z0=125.0)
surf3_zmin = openmc.ZPlane(surface_id=1324, z0=125.0)
surf3_zmax = openmc.ZPlane(surface_id=1325, z0=125.7)
surf5_zmin = openmc.ZPlane(surface_id=1326, z0=125.7)
surf5_zmax = openmc.ZPlane(surface_id=1327, z0=128.0)
surf6_zmin = openmc.ZPlane(surface_id=1328, z0=0.0)
surf6_zmax = openmc.ZPlane(surface_id=1329, z0=128.0)
surf7_zmin = openmc.ZPlane(surface_id=1330, z0=-2.07)
surf7_zmax = openmc.ZPlane(surface_id=1331, z0=130.53)
surf8_zmin = openmc.ZPlane(surface_id=1332, z0=-3.57)
surf8_zmax = openmc.ZPlane(surface_id=1333, z0=132.03)
surf12_zmin = openmc.ZPlane(surface_id=1334, z0=-3.57)
surf12_zmax = openmc.ZPlane(surface_id=1335, z0=-2.07)
surf13_zmin = openmc.ZPlane(surface_id=1336, z0=-999.9)
surf13_zmax = openmc.ZPlane(surface_id=1337, z0=999.9)
surf14_zmin = openmc.ZPlane(surface_id=1338, z0=127.13)
surf14_zmax = openmc.ZPlane(surface_id=1339, z0=128.13)
surf15_zmin = openmc.ZPlane(surface_id=1340, z0=-33.57, boundary_type="vacuum")
surf15_zmax = openmc.ZPlane(surface_id=1341, z0=132.03, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
u1_cell2 = openmc.Cell(fill=mat5)
u1_cell2.region = (+surf13 | -surf13_zmin | +surf13_zmax) & -surf10 & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = (+surf13 | -surf13_zmin | +surf13_zmax) & +surf10 & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax)
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = (+surf3 | -surf3_zmin | +surf3_zmax) & +surf4 & (-surf5 & +surf5_zmin & -surf5_zmax)
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
u2_cell4 = openmc.Cell(fill=mat2)
u2_cell4.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)
u2_cell5 = openmc.Cell(fill=mat5)
u2_cell5.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax) & -surf11 & (-surf12 & +surf12_zmin & -surf12_zmax)
u2_cell6 = openmc.Cell(fill=mat3)
u2_cell6.region = +surf11 & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u2_cell7 = openmc.Cell(fill=mat5)
u2_cell7.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax) & -surf10 & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u2_cell8 = openmc.Cell(fill=mat4)
u2_cell8.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax) & +surf10 & (-surf13 & +surf13_zmin & -surf13_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8])

u3_cell0 = openmc.Cell(fill=mat5)
u3_cell0.region = -surf11 & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u3_cell1 = openmc.Cell(fill=mat3)
u3_cell1.region = +surf11 & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u3_cell2 = openmc.Cell(fill=mat5)
u3_cell2.region = -surf10 & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u3_cell3 = openmc.Cell(fill=mat4)
u3_cell3.region = +surf10 & (-surf13 & +surf13_zmin & -surf13_zmax)
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3])

universe4 = openmc.Universe(universe_id=4, cells=[])

# Lattice 5: 7x7 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-48.895, -84.68862]
lattice5.pitch = [13.970000, 24.196749]
lattice5.universes = [
    [universe50, universe50, universe50, universe50, universe50, universe50, universe50],
    [universe50, universe50, universe50, universe50, universe50, universe50, universe50],
    [universe50, universe50, universe50, universe50, universe50, universe50, universe50],
    [universe50, universe50, universe50, universe50, universe50, universe50, universe50],
    [universe50, universe50, universe50, universe50, universe50, universe50, universe50],
    [universe50, universe50, universe50, universe50, universe50, universe50, universe50],
    [universe50, universe50, universe50, universe50, universe50, universe50, universe50],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

universe6 = openmc.Universe(universe_id=6, cells=[])

# Lattice 7: 7x7 array
lattice7 = openmc.RectLattice(lattice_id=7)
lattice7.lower_left = [-48.895, -84.68862]
lattice7.pitch = [13.970000, 24.196749]
lattice7.universes = [
    [universe70, universe70, universe70, universe70, universe70, universe70, universe70],
    [universe70, universe70, universe70, universe70, universe70, universe70, universe70],
    [universe70, universe70, universe70, universe70, universe70, universe70, universe70],
    [universe70, universe70, universe70, universe70, universe70, universe70, universe70],
    [universe70, universe70, universe70, universe70, universe70, universe70, universe70],
    [universe70, universe70, universe70, universe70, universe70, universe70, universe70],
    [universe70, universe70, universe70, universe70, universe70, universe70, universe70],
]
universe7 = openmc.Universe(universe_id=7)
universe7.add_cell(openmc.Cell(fill=lattice7))

universe8 = openmc.Universe(universe_id=8, cells=[])

universe9 = openmc.Universe(universe_id=9, cells=[])

# Lattice 50: 11x11 array
lattice50 = openmc.RectLattice(lattice_id=50)
lattice50.lower_left = [-6.985, -12.098375]
lattice50.pitch = [1.270000, 2.199705]
lattice50.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe50 = openmc.Universe(universe_id=50)
universe50.add_cell(openmc.Cell(fill=lattice50))

# Lattice 70: 11x11 array
lattice70 = openmc.RectLattice(lattice_id=70)
lattice70.lower_left = [-6.985, -12.098375]
lattice70.pitch = [1.270000, 2.199705]
lattice70.universes = [
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
    [universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6],
]
universe70 = openmc.Universe(universe_id=70)
universe70.add_cell(openmc.Cell(fill=lattice70))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# F-LATT
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = (-surf15 & +surf15_zmin & -surf15_zmax) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5 & -surf31_6 & -surf31_7 & -surf31_8 & -surf31_9 & -surf31_10 & -surf31_11)

# F-LATT
cell2 = openmc.Cell(cell_id=2, fill=universe5)
cell2.region = (-surf15 & +surf15_zmin & -surf15_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5 & -surf32_6 & -surf32_7 & -surf32_8 & -surf32_9 & -surf32_10 & -surf32_11)

# Misc
cell3 = openmc.Cell(cell_id=3, fill=universe9)
cell3.region = (-surf15 & +surf15_zmin & -surf15_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5 | +surf32_6 | +surf32_7 | +surf32_8 | +surf32_9 | +surf32_10 | +surf32_11) & (-surf33_0 & -surf33_1 & -surf33_2 & -surf33_3 & -surf33_4 & -surf33_5 & -surf33_6 & -surf33_7 & -surf33_8 & -surf33_9 & -surf33_10 & -surf33_11)

# E-LATT
cell4 = openmc.Cell(cell_id=4, fill=universe7)
cell4.region = (-surf15 & +surf15_zmin & -surf15_zmax) & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5 | +surf33_6 | +surf33_7 | +surf33_8 | +surf33_9 | +surf33_10 | +surf33_11) & (-surf34_0 & -surf34_1 & -surf34_2 & -surf34_3 & -surf34_4 & -surf34_5)

# Misc
cell5 = openmc.Cell(cell_id=5, fill=universe9)
cell5.region = (-surf15 & +surf15_zmin & -surf15_zmax) & (+surf34_0 | +surf34_1 | +surf34_2 | +surf34_3 | +surf34_4 | +surf34_5)

# Air
cell10 = openmc.Cell(cell_id=10, fill=mat4)
cell10.region = (+surf13 | -surf13_zmin | +surf13_zmax) & +surf10 & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)

# Air
cell20 = openmc.Cell(cell_id=20, fill=mat4)
cell20.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax) & +surf10 & (-surf13 & +surf13_zmin & -surf13_zmax)

# Air
cell25 = openmc.Cell(cell_id=25, fill=mat4)
cell25.region = +surf10 & (-surf13 & +surf13_zmin & -surf13_zmax)

# ALLES
cell26 = openmc.Cell(cell_id=26, fill=universe1)
cell26.region = (+surf13 | -surf13_zmin | +surf13_zmax) & +surf21 & +surf22 & +surf23 & +surf24 & (-surf15 & +surf15_zmin & -surf15_zmax)

# ALLES
cell27 = openmc.Cell(cell_id=27, fill=universe1)
cell27.region = (+surf13 | -surf13_zmin | +surf13_zmax) & +surf21 & +surf22 & +surf23 & +surf24 & (-surf15 & +surf15_zmin & -surf15_zmax)

# M-LATT
cell28 = openmc.Cell(cell_id=28, fill=universe8)
cell28.translation = (0.0, 0.0, 0.0)
cell28.region = (-surf15 & +surf15_zmin & -surf15_zmax) & +surf41 & -surf42

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell10, cell20, cell25, cell26, cell27, cell28])
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
source.space = openmc.stats.Point((0.0, 0.0, 25.435))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
