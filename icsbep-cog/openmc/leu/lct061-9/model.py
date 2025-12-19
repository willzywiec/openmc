"""
LCT061-9: 1309 U(4.5)O2 rods, 342 Al displacer rods, 1.27 cm trianglur pitch, Hc=45.22cm, 0.500 g(H3BO3)/L
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(4.5)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 7.957300e-06)
mat1.add_nuclide("U235", 1.025400e-03)
mat1.add_nuclide("U238", 2.198900e-02)
mat1.add_nuclide("O16", 4.604600e-02)

# Zr alloy clad, plugs and ends
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Zr", 4.279400e-02)
mat2.add_element("Nb", 4.245600e-04)
mat2.add_element("Hf", 6.629700e-06)

# Stainless
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.860900e-02)
mat3.add_element("Cr", 1.628600e-02)
mat3.add_element("Ni", 8.754600e-03)
mat3.add_element("Mn", 1.299000e-03)
mat3.add_element("Ti", 5.961700e-04)
mat3.add_element("Si", 4.065400e-04)
mat3.add_element("S", 1.631800e-04)
mat3.add_element("C", 3.564800e-04)
mat3.add_element("P", 5.068700e-05)
mat3.add_element("Cu", 2.246000e-04)
mat3.add_element("S", 2.966900e-05)

# 0.500 g(H3BO3)/L solution
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.675900e-02)
mat4.add_nuclide("O16", 3.338700e-02)
mat4.add_nuclide("B10", 9.690600e-07)
mat4.add_nuclide("B11", 3.900600e-06)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Aluminum displacer
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 6.026200e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Critical water height
surf1 = openmc.ZPlane(surface_id=1, z0=45.22)
# SST lower grid plate
surf2 = openmc.ZCylinder(surface_id=2, r=50.0)
# SST upper grid plate
surf3 = openmc.ZCylinder(surface_id=3, r=50.0)
# Boundary condition
surf4 = openmc.ZCylinder(surface_id=4, r=65.0, boundary_type="vacuum")
# UO2
surf10 = openmc.ZCylinder(surface_id=10, r=0.37875)
# Zr plug, inner
surf11 = openmc.ZCylinder(surface_id=11, r=0.15)
# Zr plug, outer
surf12 = openmc.ZCylinder(surface_id=12, r=0.385)
# SST spring, inner
surf13 = openmc.ZCylinder(surface_id=13, r=0.29)
# SST spring, outer
surf14 = openmc.ZCylinder(surface_id=14, r=0.32175)
# Clad, inner
surf15 = openmc.ZCylinder(surface_id=15, r=0.3875)
# Clad, outer
surf16 = openmc.ZCylinder(surface_id=16, r=0.45225)
# Clad, top and bottom portions
surf17 = openmc.ZCylinder(surface_id=17, r=0.3)
# Hole
surf20 = openmc.Revolution(surface_id=20, rz=[(-3.9, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf21 = openmc.Revolution(surface_id=21, rz=[(-3.9, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf22 = openmc.Revolution(surface_id=22, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf23 = openmc.Revolution(surface_id=23, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf24 = openmc.Revolution(surface_id=24, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf25 = openmc.Revolution(surface_id=25, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf26 = openmc.Revolution(surface_id=26, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
# The inner region
# Prism 30: 6-sided polygon
surf30_0 = openmc.Plane(a=0.8660251098, b=0.5000005092, c=0, d=7.1490372812)
surf30_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=7.1490300000)
surf30_2 = openmc.Plane(a=-0.8660251098, b=0.5000005092, c=0, d=7.1490372812)
surf30_3 = openmc.Plane(a=-0.8660251098, b=-0.5000005092, c=0, d=7.1490372812)
surf30_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=7.1490300000)
surf30_5 = openmc.Plane(a=0.8660251098, b=-0.5000005092, c=0, d=7.1490372812)
# The inner region
# Prism 31: 6-sided polygon
surf31_0 = openmc.Plane(a=0.8660250371, b=0.5000006351, c=0, d=13.7481474638)
surf31_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=13.7481300000)
surf31_2 = openmc.Plane(a=-0.8660250371, b=0.5000006351, c=0, d=13.7481474638)
surf31_3 = openmc.Plane(a=-0.8660250371, b=-0.5000006351, c=0, d=13.7481474638)
surf31_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=13.7481300000)
surf31_5 = openmc.Plane(a=0.8660250371, b=-0.5000006351, c=0, d=13.7481474638)
# The outer region
# Prism 32: 6-sided polygon
surf32_0 = openmc.Plane(a=0.8660247575, b=0.5000011194, c=0, d=26.9463603290)
surf32_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=26.9463000000)
surf32_2 = openmc.Plane(a=-0.8660247575, b=0.5000011194, c=0, d=26.9463603290)
surf32_3 = openmc.Plane(a=-0.8660247575, b=-0.5000011194, c=0, d=26.9463603290)
surf32_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=26.9463000000)
surf32_5 = openmc.Plane(a=0.8660247575, b=-0.5000011194, c=0, d=26.9463603290)
# The region
# Prism 33: 6-sided polygon
surf33_0 = openmc.Plane(a=0.8660249941, b=0.5000007095, c=0, d=30.2459229203)
surf33_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=30.2458800000)
surf33_2 = openmc.Plane(a=-0.8660249941, b=0.5000007095, c=0, d=30.2459229203)
surf33_3 = openmc.Plane(a=-0.8660249941, b=-0.5000007095, c=0, d=30.2459229203)
surf33_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=30.2458800000)
surf33_5 = openmc.Plane(a=0.8660249941, b=-0.5000007095, c=0, d=30.2459229203)
surf41 = openmc.Revolution(surface_id=41, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf42 = openmc.Revolution(surface_id=42, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf43 = openmc.Revolution(surface_id=43, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf44 = openmc.Revolution(surface_id=44, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf45 = openmc.Revolution(surface_id=45, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf46 = openmc.Revolution(surface_id=46, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf47 = openmc.Revolution(surface_id=47, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf48 = openmc.Revolution(surface_id=48, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf49 = openmc.Revolution(surface_id=49, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf50 = openmc.Revolution(surface_id=50, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf51 = openmc.Revolution(surface_id=51, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf52 = openmc.Revolution(surface_id=52, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf53 = openmc.Revolution(surface_id=53, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf54 = openmc.Revolution(surface_id=54, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf55 = openmc.Revolution(surface_id=55, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf56 = openmc.Revolution(surface_id=56, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf57 = openmc.Revolution(surface_id=57, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf58 = openmc.Revolution(surface_id=58, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf59 = openmc.Revolution(surface_id=59, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf60 = openmc.Revolution(surface_id=60, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf61 = openmc.Revolution(surface_id=61, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf62 = openmc.Revolution(surface_id=62, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf63 = openmc.Revolution(surface_id=63, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf64 = openmc.Revolution(surface_id=64, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf65 = openmc.Revolution(surface_id=65, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf66 = openmc.Revolution(surface_id=66, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf67 = openmc.Revolution(surface_id=67, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf68 = openmc.Revolution(surface_id=68, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf69 = openmc.Revolution(surface_id=69, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf70 = openmc.Revolution(surface_id=70, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf71 = openmc.Revolution(surface_id=71, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf72 = openmc.Revolution(surface_id=72, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf73 = openmc.Revolution(surface_id=73, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf74 = openmc.Revolution(surface_id=74, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf75 = openmc.Revolution(surface_id=75, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf76 = openmc.Revolution(surface_id=76, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf77 = openmc.Revolution(surface_id=77, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf78 = openmc.Revolution(surface_id=78, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf79 = openmc.Revolution(surface_id=79, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf80 = openmc.Revolution(surface_id=80, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf81 = openmc.Revolution(surface_id=81, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf82 = openmc.Revolution(surface_id=82, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf83 = openmc.Revolution(surface_id=83, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf84 = openmc.Revolution(surface_id=84, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf85 = openmc.Revolution(surface_id=85, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf86 = openmc.Revolution(surface_id=86, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf87 = openmc.Revolution(surface_id=87, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf88 = openmc.Revolution(surface_id=88, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf89 = openmc.Revolution(surface_id=89, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf90 = openmc.Revolution(surface_id=90, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf91 = openmc.Revolution(surface_id=91, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf92 = openmc.Revolution(surface_id=92, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf93 = openmc.Revolution(surface_id=93, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf94 = openmc.Revolution(surface_id=94, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf95 = openmc.Revolution(surface_id=95, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf96 = openmc.Revolution(surface_id=96, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf97 = openmc.Revolution(surface_id=97, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf98 = openmc.Revolution(surface_id=98, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf99 = openmc.Revolution(surface_id=99, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf100 = openmc.Revolution(surface_id=100, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
# Hole
surf101 = openmc.Revolution(surface_id=101, rz=[(-3.9, 0.31), (-2.3, 0.31), (-2.29999, 0.51), (133.3, 0.51)], axis="x")
surf102 = openmc.Revolution(surface_id=102, rz=[(-3.9, 0.31), (-2.3, 0.31), (-2.29999, 0.51), (133.3, 0.51)], axis="x")
surf103 = openmc.Revolution(surface_id=103, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.51), (133.3, 0.51)], axis="x")
surf104 = openmc.Revolution(surface_id=104, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.51), (133.3, 0.51)], axis="x")
surf105 = openmc.Revolution(surface_id=105, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.51), (133.3, 0.51)], axis="x")
surf106 = openmc.Revolution(surface_id=106, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.51), (133.3, 0.51)], axis="x")
surf107 = openmc.Revolution(surface_id=107, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.51), (133.3, 0.51)], axis="x")
# Void
surf191 = openmc.ZCylinder(surface_id=191, r=0.45)
# Al tube
surf192 = openmc.ZCylinder(surface_id=192, r=0.5)
# Al end
surf193 = openmc.ZCylinder(surface_id=193, r=0.3)
surf321 = openmc.model.RectangularParallelepiped(-27.305, 27.305, -499.95, 499.95, -499.95, 499.95)
surf322 = openmc.model.RectangularParallelepiped(-27.305, 27.305, -499.95, 499.95, -499.95, 499.95)
surf323 = openmc.model.RectangularParallelepiped(-27.305, 27.305, -499.95, 499.95, -499.95, 499.95)

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(surface_id=1323, z0=-3.8)
surf2_zmax = openmc.ZPlane(surface_id=1324, z0=-2.3)
surf3_zmin = openmc.ZPlane(surface_id=1325, z0=126.9)
surf3_zmax = openmc.ZPlane(surface_id=1326, z0=127.9)
surf4_zmin = openmc.ZPlane(surface_id=1327, z0=-32.3, boundary_type="vacuum")
surf4_zmax = openmc.ZPlane(surface_id=1328, z0=133.5, boundary_type="vacuum")
surf10_zmin = openmc.ZPlane(surface_id=1329, z0=0.0)
surf10_zmax = openmc.ZPlane(surface_id=1330, z0=125.0)
surf12_zmin = openmc.ZPlane(surface_id=1331, z0=125.0)
surf12_zmax = openmc.ZPlane(surface_id=1332, z0=125.7)
surf14_zmin = openmc.ZPlane(surface_id=1333, z0=125.7)
surf14_zmax = openmc.ZPlane(surface_id=1334, z0=128.0)
surf15_zmin = openmc.ZPlane(surface_id=1335, z0=0.0)
surf15_zmax = openmc.ZPlane(surface_id=1336, z0=128.0)
surf16_zmin = openmc.ZPlane(surface_id=1337, z0=-2.3)
surf16_zmax = openmc.ZPlane(surface_id=1338, z0=130.3)
surf17_zmin = openmc.ZPlane(surface_id=1339, z0=-3.8)
surf17_zmax = openmc.ZPlane(surface_id=1340, z0=131.8)
surf191_zmin = openmc.ZPlane(surface_id=1341, z0=0.0)
surf191_zmax = openmc.ZPlane(surface_id=1342, z0=133.27)
surf192_zmin = openmc.ZPlane(surface_id=1343, z0=-2.3)
surf192_zmax = openmc.ZPlane(surface_id=1344, z0=133.27)
surf193_zmin = openmc.ZPlane(surface_id=1345, z0=-3.8)
surf193_zmax = openmc.ZPlane(surface_id=1346, z0=-2.3)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = -surf1 & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = (+surf10 | -surf10_zmin | +surf10_zmax) & +surf11 & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = (+surf12 | -surf12_zmin | +surf12_zmax) & +surf13 & (-surf14 & +surf14_zmin & -surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = (+surf15 | -surf15_zmin | +surf15_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)
u2_cell4 = openmc.Cell(fill=mat2)
u2_cell4.region = (+surf16 | -surf16_zmin | +surf16_zmax) & (-surf17 & +surf17_zmin & -surf17_zmax)
u2_cell5 = openmc.Cell(fill=mat4)
u2_cell5.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat4)
u4_cell0.region = -surf1 & -surf20
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf1 & -surf21
u4_cell2 = openmc.Cell(fill=mat4)
u4_cell2.region = -surf1 & -surf22
u4_cell3 = openmc.Cell(fill=mat4)
u4_cell3.region = -surf1 & -surf23
u4_cell4 = openmc.Cell(fill=mat4)
u4_cell4.region = -surf1 & -surf24
u4_cell5 = openmc.Cell(fill=mat4)
u4_cell5.region = -surf1 & -surf25
u4_cell6 = openmc.Cell(fill=mat4)
u4_cell6.region = -surf1 & -surf26
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4, u4_cell5, u4_cell6])

# Lattice 5: 29x25 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-36.83, -27.49625]
lattice5.pitch = [2.540000, 2.199700]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# Lattice 6: 29x29 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-36.83, -31.89565]
lattice6.pitch = [2.540000, 2.199700]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

u7_cell0 = openmc.Cell(fill=mat5)
u7_cell0.region = (+surf191 | -surf191_zmin | +surf191_zmax) & (-surf192 & +surf192_zmin & -surf192_zmax)
u7_cell1 = openmc.Cell(fill=mat5)
u7_cell1.region = (+surf192 | -surf192_zmin | +surf192_zmax) & (-surf193 & +surf193_zmin & -surf193_zmax)
u7_cell2 = openmc.Cell(fill=mat4)
u7_cell2.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf192 | -surf192_zmin | +surf192_zmax) & (+surf193 | -surf193_zmin | +surf193_zmax)
universe7 = openmc.Universe(universe_id=7, cells=[u7_cell0, u7_cell1, u7_cell2])

universe8 = openmc.Universe(universe_id=8, cells=[])

# Lattice 9: 21x21 array
lattice9 = openmc.RectLattice(lattice_id=9)
lattice9.lower_left = [-26.67, -23.09685]
lattice9.pitch = [2.540000, 2.199700]
lattice9.universes = [
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
    [universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8, universe8],
]
universe9 = openmc.Universe(universe_id=9)
universe9.add_cell(openmc.Cell(fill=lattice9))

universe10 = openmc.Universe(universe_id=10, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# All
cell1 = openmc.Cell(cell_id=1, fill=universe10)
cell1.region = (-surf4 & +surf4_zmin & -surf4_zmax) & +surf41 & +surf42 & +surf43 & +surf44 & +surf45 & +surf46 & +surf47 & +surf48 & +surf49 & +surf50 & +surf51 & +surf52 & +surf53 & +surf54 & +surf55 & +surf56 & +surf57 & +surf58 & +surf59 & +surf60 & +surf61 & +surf62 & +surf63 & +surf64 & +surf65 & +surf66 & +surf67 & +surf68 & +surf69 & +surf70

# Mod
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf41 & -surf1 & -surf42 & -surf1 & -surf43 & -surf1 & -surf44 & -surf1 & -surf45 & -surf1 & -surf46 & -surf1 & -surf47 & -surf1 & -surf48 & -surf1 & -surf49 & -surf1 & -surf50

# Mod
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf51 & -surf1 & -surf52 & -surf1 & -surf53 & -surf1 & -surf54 & -surf1 & -surf55 & -surf1 & -surf56 & -surf1 & -surf57 & -surf1 & -surf58 & -surf1 & -surf59 & -surf1 & -surf60

# Mod
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf61 & -surf1 & -surf62 & -surf1 & -surf63 & -surf1 & -surf64 & -surf1 & -surf65 & -surf1 & -surf66 & -surf1 & -surf67 & -surf1 & -surf68 & -surf1 & -surf69 & -surf1 & -surf70

# Mod
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf71 & -surf1 & -surf72 & -surf1 & -surf73 & -surf1 & -surf74 & -surf1 & -surf75 & -surf1 & -surf76 & -surf1 & -surf77 & -surf1 & -surf78 & -surf1 & -surf79 & -surf1 & -surf80

# Mod
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf81 & -surf1 & -surf82 & -surf1 & -surf83 & -surf1 & -surf84 & -surf1 & -surf85 & -surf1 & -surf86 & -surf1 & -surf87 & -surf1 & -surf88 & -surf1 & -surf89 & -surf1 & -surf90

# Mod
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf91 & -surf1 & -surf92 & -surf1 & -surf93 & -surf1 & -surf94 & -surf1 & -surf95 & -surf1 & -surf96 & -surf1 & -surf97 & -surf1 & -surf98 & -surf1 & -surf99 & -surf1 & -surf100

# Alles
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5)

# Mod
cell12 = openmc.Cell(cell_id=12, fill=mat4)
cell12.region = -surf1 & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# Mod
cell19 = openmc.Cell(cell_id=19, fill=mat4)
cell19.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)

# Alles
cell20 = openmc.Cell(cell_id=20, fill=universe1)
cell20.region = (-surf4 & +surf4_zmin & -surf4_zmax) & +surf20 & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

# Alles
cell28 = openmc.Cell(cell_id=28, fill=universe1)
cell28.region = (-surf4 & +surf4_zmin & -surf4_zmax) & +surf20 & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

# Mod
cell32 = openmc.Cell(cell_id=32, fill=mat4)
cell32.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf192 | -surf192_zmin | +surf192_zmax) & (+surf193 | -surf193_zmin | +surf193_zmax)

# Alles
cell33 = openmc.Cell(cell_id=33, fill=universe1)
cell33.region = (-surf4 & +surf4_zmin & -surf4_zmax) & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell12, cell19, cell20, cell28, cell32, cell33])
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
source.space = openmc.stats.Box((-2.27, -2.09985, 21.61), (2.27, 2.09985, 23.61))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
