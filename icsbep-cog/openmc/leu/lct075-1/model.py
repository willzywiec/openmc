"""
LCT075-1: 1,195 VVER U(6.5)O2 rods, 1.10 cm trianglur pitch, 4 B4C rods 15.4 from core center, Hc=93.83cm
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(6.5)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.229800e-05)
mat1.add_nuclide("U235", 1.592000e-03)
mat1.add_nuclide("U238", 2.259800e-02)
mat1.add_nuclide("O16", 4.840500e-02)

# Clad, plugs, ends
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Zr", 4.279400e-02)
mat2.add_element("Nb", 4.245600e-04)
mat2.add_element("Hf", 6.629700e-06)

# B4C
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 1.911500e-02)
mat3.add_nuclide("B10", 1.521600e-02)
mat3.add_nuclide("B11", 6.124600e-02)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.676200e-02)
mat4.add_nuclide("O16", 3.338100e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# 12X18H10T
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 5.871500e-02)
mat5.add_element("Cr", 1.646900e-02)
mat5.add_element("Ni", 8.106100e-03)
mat5.add_element("Si", 1.355100e-03)
mat5.add_element("Mn", 9.525700e-04)
mat5.add_element("Ti", 6.955400e-04)
mat5.add_element("P", 5.375900e-05)
mat5.add_element("C", 4.753100e-04)
mat5.add_element("Cu", 2.246000e-04)
mat5.add_element("S", 2.966900e-05)

# AVT
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Cu", 2.558700e-05)
mat6.add_element("Mg", 3.010400e-04)
mat6.add_element("Mn", 4.439500e-05)
mat6.add_element("Zn", 4.973100e-05)
mat6.add_element("Fe", 1.455700e-04)
mat6.add_element("Si", 2.894700e-04)
mat6.add_element("Ti", 5.093900e-05)
mat6.add_element("Cr", 7.817800e-05)
mat6.add_element("Al", 5.881600e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Critical water height
surf1 = openmc.ZPlane(surface_id=1, z0=93.83)
# SST lower grid plate
surf2 = openmc.ZCylinder(surface_id=2, r=50.0)
# AVT grid plate
surf3 = openmc.ZCylinder(surface_id=3, r=50.0)
# SST upper grid plate
surf4 = openmc.ZCylinder(surface_id=4, r=50.0)
# Boundary condition
surf5 = openmc.ZCylinder(surface_id=5, r=65.0, boundary_type="vacuum")
# UO2, inner
surf10 = openmc.ZCylinder(surface_id=10, r=0.06)
# UO2, outer
surf11 = openmc.ZCylinder(surface_id=11, r=0.37825)
# Zr plug, inner
surf12 = openmc.ZCylinder(surface_id=12, r=0.15)
# Zr plug, outer
surf13 = openmc.ZCylinder(surface_id=13, r=0.385)
# SST spring, inner
surf14 = openmc.ZCylinder(surface_id=14, r=0.29)
# SST spring, outer
surf15 = openmc.ZCylinder(surface_id=15, r=0.32175)
# Clad, inner
surf16 = openmc.ZCylinder(surface_id=16, r=0.388)
# Clad, outer
surf17 = openmc.ZCylinder(surface_id=17, r=0.4525)
# Clad, lower
surf18 = openmc.ZCylinder(surface_id=18, r=0.3)
# Clad, upper
surf19 = openmc.ZCylinder(surface_id=19, r=0.3)
# Hole
surf20 = openmc.Revolution(surface_id=20, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf21 = openmc.Revolution(surface_id=21, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf22 = openmc.Revolution(surface_id=22, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf23 = openmc.Revolution(surface_id=23, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf24 = openmc.Revolution(surface_id=24, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf25 = openmc.Revolution(surface_id=25, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf26 = openmc.Revolution(surface_id=26, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
# The
# Prism 30: 12-sided polygon
surf30_0 = openmc.Plane(a=0.8660254165, b=0.4999999780, c=0, d=19.0525591624)
surf30_1 = openmc.Plane(a=0.5000000220, b=0.8660253911, c=0, d=20.3500008946)
surf30_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=19.0525600000)
surf30_3 = openmc.Plane(a=-0.5000000220, b=0.8660253911, c=0, d=20.3500008946)
surf30_4 = openmc.Plane(a=-0.8660254165, b=0.4999999780, c=0, d=19.0525591624)
surf30_5 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=20.3500000000)
surf30_6 = openmc.Plane(a=-0.8660254165, b=-0.4999999780, c=0, d=19.0525591624)
surf30_7 = openmc.Plane(a=-0.5000000220, b=-0.8660253911, c=0, d=20.3500008946)
surf30_8 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=19.0525600000)
surf30_9 = openmc.Plane(a=0.5000000220, b=-0.8660253911, c=0, d=20.3500008946)
surf30_10 = openmc.Plane(a=0.8660254165, b=-0.4999999780, c=0, d=19.0525591624)
surf30_11 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=20.3500000000)
# The region
# Prism 31: 6-sided polygon
surf31_0 = openmc.Plane(a=0.8660254165, b=0.4999999780, c=0, d=21.9104430368)
surf31_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=21.9104440000)
surf31_2 = openmc.Plane(a=-0.8660254165, b=0.4999999780, c=0, d=21.9104430368)
surf31_3 = openmc.Plane(a=-0.8660254165, b=-0.4999999780, c=0, d=21.9104430368)
surf31_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=21.9104440000)
surf31_5 = openmc.Plane(a=0.8660254165, b=-0.4999999780, c=0, d=21.9104430368)
# B4C
surf41 = openmc.ZCylinder(surface_id=41, r=0.3765)
# Void
surf42 = openmc.ZCylinder(surface_id=42, r=0.388)
# Clad, outer
surf43 = openmc.ZCylinder(surface_id=43, r=0.452)
# Clad, lower
surf44 = openmc.ZCylinder(surface_id=44, r=0.3)
# Clad, upper
surf45 = openmc.ZCylinder(surface_id=45, r=0.3)
surf101 = openmc.Revolution(surface_id=101, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf102 = openmc.Revolution(surface_id=102, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf103 = openmc.Revolution(surface_id=103, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf104 = openmc.Revolution(surface_id=104, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf105 = openmc.Revolution(surface_id=105, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf106 = openmc.Revolution(surface_id=106, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf107 = openmc.Revolution(surface_id=107, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf108 = openmc.Revolution(surface_id=108, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf109 = openmc.Revolution(surface_id=109, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf110 = openmc.Revolution(surface_id=110, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf111 = openmc.Revolution(surface_id=111, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf112 = openmc.Revolution(surface_id=112, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf113 = openmc.Revolution(surface_id=113, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf114 = openmc.Revolution(surface_id=114, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf115 = openmc.Revolution(surface_id=115, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf116 = openmc.Revolution(surface_id=116, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf117 = openmc.Revolution(surface_id=117, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf118 = openmc.Revolution(surface_id=118, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf119 = openmc.Revolution(surface_id=119, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf120 = openmc.Revolution(surface_id=120, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf121 = openmc.Revolution(surface_id=121, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf122 = openmc.Revolution(surface_id=122, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf123 = openmc.Revolution(surface_id=123, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf124 = openmc.Revolution(surface_id=124, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf201 = openmc.Revolution(surface_id=201, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf202 = openmc.Revolution(surface_id=202, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf203 = openmc.Revolution(surface_id=203, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf204 = openmc.Revolution(surface_id=204, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf205 = openmc.Revolution(surface_id=205, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf206 = openmc.Revolution(surface_id=206, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf207 = openmc.Revolution(surface_id=207, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf208 = openmc.Revolution(surface_id=208, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf209 = openmc.Revolution(surface_id=209, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf210 = openmc.Revolution(surface_id=210, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf211 = openmc.Revolution(surface_id=211, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf212 = openmc.Revolution(surface_id=212, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf213 = openmc.Revolution(surface_id=213, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf214 = openmc.Revolution(surface_id=214, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf215 = openmc.Revolution(surface_id=215, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf216 = openmc.Revolution(surface_id=216, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf217 = openmc.Revolution(surface_id=217, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf218 = openmc.Revolution(surface_id=218, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf219 = openmc.Revolution(surface_id=219, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf220 = openmc.Revolution(surface_id=220, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf221 = openmc.Revolution(surface_id=221, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf222 = openmc.Revolution(surface_id=222, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf223 = openmc.Revolution(surface_id=223, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf224 = openmc.Revolution(surface_id=224, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf225 = openmc.Revolution(surface_id=225, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf226 = openmc.Revolution(surface_id=226, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf227 = openmc.Revolution(surface_id=227, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf228 = openmc.Revolution(surface_id=228, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf229 = openmc.Revolution(surface_id=229, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf230 = openmc.Revolution(surface_id=230, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf231 = openmc.Revolution(surface_id=231, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf232 = openmc.Revolution(surface_id=232, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf233 = openmc.Revolution(surface_id=233, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf234 = openmc.Revolution(surface_id=234, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf235 = openmc.Revolution(surface_id=235, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf236 = openmc.Revolution(surface_id=236, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf237 = openmc.Revolution(surface_id=237, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf238 = openmc.Revolution(surface_id=238, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf239 = openmc.Revolution(surface_id=239, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf240 = openmc.Revolution(surface_id=240, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf241 = openmc.Revolution(surface_id=241, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf242 = openmc.Revolution(surface_id=242, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf243 = openmc.Revolution(surface_id=243, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf244 = openmc.Revolution(surface_id=244, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf245 = openmc.Revolution(surface_id=245, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf246 = openmc.Revolution(surface_id=246, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf247 = openmc.Revolution(surface_id=247, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf248 = openmc.Revolution(surface_id=248, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf249 = openmc.Revolution(surface_id=249, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf250 = openmc.Revolution(surface_id=250, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf251 = openmc.Revolution(surface_id=251, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf252 = openmc.Revolution(surface_id=252, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf253 = openmc.Revolution(surface_id=253, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf254 = openmc.Revolution(surface_id=254, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf255 = openmc.Revolution(surface_id=255, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf256 = openmc.Revolution(surface_id=256, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf257 = openmc.Revolution(surface_id=257, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf258 = openmc.Revolution(surface_id=258, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf259 = openmc.Revolution(surface_id=259, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf260 = openmc.Revolution(surface_id=260, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf261 = openmc.Revolution(surface_id=261, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf262 = openmc.Revolution(surface_id=262, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf263 = openmc.Revolution(surface_id=263, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf264 = openmc.Revolution(surface_id=264, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf265 = openmc.Revolution(surface_id=265, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf266 = openmc.Revolution(surface_id=266, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf267 = openmc.Revolution(surface_id=267, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf268 = openmc.Revolution(surface_id=268, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf269 = openmc.Revolution(surface_id=269, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf270 = openmc.Revolution(surface_id=270, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf271 = openmc.Revolution(surface_id=271, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf272 = openmc.Revolution(surface_id=272, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf273 = openmc.Revolution(surface_id=273, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf274 = openmc.Revolution(surface_id=274, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf275 = openmc.Revolution(surface_id=275, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf276 = openmc.Revolution(surface_id=276, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf277 = openmc.Revolution(surface_id=277, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf278 = openmc.Revolution(surface_id=278, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf301 = openmc.Revolution(surface_id=301, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf302 = openmc.Revolution(surface_id=302, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf303 = openmc.Revolution(surface_id=303, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf304 = openmc.Revolution(surface_id=304, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf305 = openmc.Revolution(surface_id=305, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf306 = openmc.Revolution(surface_id=306, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf307 = openmc.Revolution(surface_id=307, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf308 = openmc.Revolution(surface_id=308, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf309 = openmc.Revolution(surface_id=309, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf310 = openmc.Revolution(surface_id=310, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf311 = openmc.Revolution(surface_id=311, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf312 = openmc.Revolution(surface_id=312, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf313 = openmc.Revolution(surface_id=313, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf314 = openmc.Revolution(surface_id=314, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf315 = openmc.Revolution(surface_id=315, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf316 = openmc.Revolution(surface_id=316, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf317 = openmc.Revolution(surface_id=317, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf318 = openmc.Revolution(surface_id=318, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf319 = openmc.Revolution(surface_id=319, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf320 = openmc.Revolution(surface_id=320, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf321 = openmc.Revolution(surface_id=321, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf322 = openmc.Revolution(surface_id=322, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf323 = openmc.Revolution(surface_id=323, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf324 = openmc.Revolution(surface_id=324, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf325 = openmc.Revolution(surface_id=325, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf326 = openmc.Revolution(surface_id=326, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf327 = openmc.Revolution(surface_id=327, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf328 = openmc.Revolution(surface_id=328, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf329 = openmc.Revolution(surface_id=329, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf330 = openmc.Revolution(surface_id=330, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf331 = openmc.Revolution(surface_id=331, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf332 = openmc.Revolution(surface_id=332, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf333 = openmc.Revolution(surface_id=333, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf334 = openmc.Revolution(surface_id=334, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf335 = openmc.Revolution(surface_id=335, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf336 = openmc.Revolution(surface_id=336, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf337 = openmc.Revolution(surface_id=337, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf338 = openmc.Revolution(surface_id=338, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf339 = openmc.Revolution(surface_id=339, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf340 = openmc.Revolution(surface_id=340, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf341 = openmc.Revolution(surface_id=341, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf342 = openmc.Revolution(surface_id=342, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf343 = openmc.Revolution(surface_id=343, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf344 = openmc.Revolution(surface_id=344, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf345 = openmc.Revolution(surface_id=345, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf346 = openmc.Revolution(surface_id=346, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf347 = openmc.Revolution(surface_id=347, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf348 = openmc.Revolution(surface_id=348, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf349 = openmc.Revolution(surface_id=349, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf350 = openmc.Revolution(surface_id=350, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf351 = openmc.Revolution(surface_id=351, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf352 = openmc.Revolution(surface_id=352, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf353 = openmc.Revolution(surface_id=353, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf354 = openmc.Revolution(surface_id=354, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf355 = openmc.Revolution(surface_id=355, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf356 = openmc.Revolution(surface_id=356, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf357 = openmc.Revolution(surface_id=357, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf358 = openmc.Revolution(surface_id=358, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf359 = openmc.Revolution(surface_id=359, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf360 = openmc.Revolution(surface_id=360, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf361 = openmc.Revolution(surface_id=361, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf362 = openmc.Revolution(surface_id=362, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf363 = openmc.Revolution(surface_id=363, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf364 = openmc.Revolution(surface_id=364, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf365 = openmc.Revolution(surface_id=365, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf366 = openmc.Revolution(surface_id=366, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf367 = openmc.Revolution(surface_id=367, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf368 = openmc.Revolution(surface_id=368, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf369 = openmc.Revolution(surface_id=369, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf370 = openmc.Revolution(surface_id=370, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf371 = openmc.Revolution(surface_id=371, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf372 = openmc.Revolution(surface_id=372, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf373 = openmc.Revolution(surface_id=373, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf374 = openmc.Revolution(surface_id=374, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf375 = openmc.Revolution(surface_id=375, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf376 = openmc.Revolution(surface_id=376, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf377 = openmc.Revolution(surface_id=377, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf378 = openmc.Revolution(surface_id=378, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf379 = openmc.Revolution(surface_id=379, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf380 = openmc.Revolution(surface_id=380, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf381 = openmc.Revolution(surface_id=381, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf382 = openmc.Revolution(surface_id=382, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf383 = openmc.Revolution(surface_id=383, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf384 = openmc.Revolution(surface_id=384, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf385 = openmc.Revolution(surface_id=385, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf386 = openmc.Revolution(surface_id=386, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf387 = openmc.Revolution(surface_id=387, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf388 = openmc.Revolution(surface_id=388, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf389 = openmc.Revolution(surface_id=389, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf390 = openmc.Revolution(surface_id=390, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf391 = openmc.Revolution(surface_id=391, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf392 = openmc.Revolution(surface_id=392, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf393 = openmc.Revolution(surface_id=393, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf394 = openmc.Revolution(surface_id=394, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf395 = openmc.Revolution(surface_id=395, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf396 = openmc.Revolution(surface_id=396, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf397 = openmc.Revolution(surface_id=397, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf398 = openmc.Revolution(surface_id=398, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf399 = openmc.Revolution(surface_id=399, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf400 = openmc.Revolution(surface_id=400, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf401 = openmc.Revolution(surface_id=401, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf402 = openmc.Revolution(surface_id=402, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf403 = openmc.Revolution(surface_id=403, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf404 = openmc.Revolution(surface_id=404, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf405 = openmc.Revolution(surface_id=405, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf406 = openmc.Revolution(surface_id=406, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf407 = openmc.Revolution(surface_id=407, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf408 = openmc.Revolution(surface_id=408, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf409 = openmc.Revolution(surface_id=409, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf410 = openmc.Revolution(surface_id=410, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf411 = openmc.Revolution(surface_id=411, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf412 = openmc.Revolution(surface_id=412, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf413 = openmc.Revolution(surface_id=413, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf414 = openmc.Revolution(surface_id=414, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf415 = openmc.Revolution(surface_id=415, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf416 = openmc.Revolution(surface_id=416, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf417 = openmc.Revolution(surface_id=417, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf418 = openmc.Revolution(surface_id=418, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf419 = openmc.Revolution(surface_id=419, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf420 = openmc.Revolution(surface_id=420, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf421 = openmc.Revolution(surface_id=421, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf422 = openmc.Revolution(surface_id=422, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf423 = openmc.Revolution(surface_id=423, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf424 = openmc.Revolution(surface_id=424, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf425 = openmc.Revolution(surface_id=425, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf426 = openmc.Revolution(surface_id=426, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf427 = openmc.Revolution(surface_id=427, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf428 = openmc.Revolution(surface_id=428, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf429 = openmc.Revolution(surface_id=429, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf430 = openmc.Revolution(surface_id=430, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf431 = openmc.Revolution(surface_id=431, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf432 = openmc.Revolution(surface_id=432, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf433 = openmc.Revolution(surface_id=433, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf434 = openmc.Revolution(surface_id=434, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf435 = openmc.Revolution(surface_id=435, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf436 = openmc.Revolution(surface_id=436, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf437 = openmc.Revolution(surface_id=437, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf438 = openmc.Revolution(surface_id=438, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf501 = openmc.Revolution(surface_id=501, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf502 = openmc.Revolution(surface_id=502, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf503 = openmc.Revolution(surface_id=503, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf504 = openmc.Revolution(surface_id=504, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf505 = openmc.Revolution(surface_id=505, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")
surf506 = openmc.Revolution(surface_id=506, rz=[(-3.8, 0.31), (-2.3, 0.31), (-2.29999, 0.47), (131.8, 0.47)], axis="x")

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(surface_id=1506, z0=-3.8)
surf2_zmax = openmc.ZPlane(surface_id=1507, z0=-2.3)
surf3_zmin = openmc.ZPlane(surface_id=1508, z0=63.7)
surf3_zmax = openmc.ZPlane(surface_id=1509, z0=64.1)
surf4_zmin = openmc.ZPlane(surface_id=1510, z0=126.9)
surf4_zmax = openmc.ZPlane(surface_id=1511, z0=127.9)
surf5_zmin = openmc.ZPlane(surface_id=1512, z0=-32.3, boundary_type="vacuum")
surf5_zmax = openmc.ZPlane(surface_id=1513, z0=131.8, boundary_type="vacuum")
surf11_zmin = openmc.ZPlane(surface_id=1514, z0=0.0)
surf11_zmax = openmc.ZPlane(surface_id=1515, z0=125.0)
surf13_zmin = openmc.ZPlane(surface_id=1516, z0=125.0)
surf13_zmax = openmc.ZPlane(surface_id=1517, z0=125.7)
surf15_zmin = openmc.ZPlane(surface_id=1518, z0=125.7)
surf15_zmax = openmc.ZPlane(surface_id=1519, z0=128.0)
surf16_zmin = openmc.ZPlane(surface_id=1520, z0=0.0)
surf16_zmax = openmc.ZPlane(surface_id=1521, z0=128.0)
surf17_zmin = openmc.ZPlane(surface_id=1522, z0=-2.3)
surf17_zmax = openmc.ZPlane(surface_id=1523, z0=130.3)
surf18_zmin = openmc.ZPlane(surface_id=1524, z0=-3.8)
surf18_zmax = openmc.ZPlane(surface_id=1525, z0=-2.3)
surf19_zmin = openmc.ZPlane(surface_id=1526, z0=130.3)
surf19_zmax = openmc.ZPlane(surface_id=1527, z0=131.8)
surf41_zmin = openmc.ZPlane(surface_id=1528, z0=-0.2)
surf41_zmax = openmc.ZPlane(surface_id=1529, z0=123.4)
surf42_zmin = openmc.ZPlane(surface_id=1530, z0=-0.2)
surf42_zmax = openmc.ZPlane(surface_id=1531, z0=127.0)
surf43_zmin = openmc.ZPlane(surface_id=1532, z0=-2.3)
surf43_zmax = openmc.ZPlane(surface_id=1533, z0=129.1)
surf44_zmin = openmc.ZPlane(surface_id=1534, z0=-3.8)
surf44_zmax = openmc.ZPlane(surface_id=1535, z0=-2.3)
surf45_zmin = openmc.ZPlane(surface_id=1536, z0=129.1)
surf45_zmax = openmc.ZPlane(surface_id=1537, z0=130.6)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat5)
u1_cell0.region = (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell1 = openmc.Cell(fill=mat6)
u1_cell1.region = (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat5)
u1_cell2.region = (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = -surf1 & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = +surf10 & (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf17 & +surf17_zmin & -surf17_zmax)
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = (+surf11 | -surf11_zmin | +surf11_zmax) & +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax) & (-surf17 & +surf17_zmin & -surf17_zmax)
u2_cell2 = openmc.Cell(fill=mat5)
u2_cell2.region = (+surf13 | -surf13_zmin | +surf13_zmax) & +surf14 & (-surf15 & +surf15_zmin & -surf15_zmax) & (-surf17 & +surf17_zmin & -surf17_zmax)
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = (+surf16 | -surf16_zmin | +surf16_zmax) & (-surf17 & +surf17_zmin & -surf17_zmax)
u2_cell4 = openmc.Cell(fill=mat2)
u2_cell4.region = (+surf17 | -surf17_zmin | +surf17_zmax) & (-surf18 & +surf18_zmin & -surf18_zmax)
u2_cell5 = openmc.Cell(fill=mat2)
u2_cell5.region = (+surf17 | -surf17_zmin | +surf17_zmax) & (-surf19 & +surf19_zmin & -surf19_zmax)
u2_cell6 = openmc.Cell(fill=mat4)
u2_cell6.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax) & (+surf18 | -surf18_zmin | +surf18_zmax) & (+surf19 | -surf19_zmin | +surf19_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6])

u3_cell0 = openmc.Cell(fill=mat4)
u3_cell0.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax)
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0])

universe4 = openmc.Universe(universe_id=4, cells=[])

universe5 = openmc.Universe(universe_id=5, cells=[])

# Lattice 6: 23x23 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-25.3, -21.910444]
lattice6.pitch = [2.200000, 1.905256]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

# Lattice 7: 23x23 array
lattice7 = openmc.RectLattice(lattice_id=7)
lattice7.lower_left = [-25.3, -21.910444]
lattice7.pitch = [2.200000, 1.905256]
lattice7.universes = [
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
]
universe7 = openmc.Universe(universe_id=7)
universe7.add_cell(openmc.Cell(fill=lattice7))

u8_cell0 = openmc.Cell(fill=mat3)
u8_cell0.region = (-surf41 & +surf41_zmin & -surf41_zmax) & (-surf42 & +surf42_zmin & -surf42_zmax)
u8_cell1 = openmc.Cell()
u8_cell1.region = (+surf41 | -surf41_zmin | +surf41_zmax) & (-surf42 & +surf42_zmin & -surf42_zmax)
u8_cell2 = openmc.Cell(fill=mat2)
u8_cell2.region = (+surf42 | -surf42_zmin | +surf42_zmax) & (-surf43 & +surf43_zmin & -surf43_zmax)
u8_cell3 = openmc.Cell(fill=mat2)
u8_cell3.region = (+surf43 | -surf43_zmin | +surf43_zmax) & (-surf44 & +surf44_zmin & -surf44_zmax)
u8_cell4 = openmc.Cell(fill=mat2)
u8_cell4.region = (+surf43 | -surf43_zmin | +surf43_zmax) & (-surf45 & +surf45_zmin & -surf45_zmax)
u8_cell5 = openmc.Cell(fill=mat4)
u8_cell5.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf43 | -surf43_zmin | +surf43_zmax) & (+surf44 | -surf44_zmin | +surf44_zmax) & (+surf45 | -surf45_zmin | +surf45_zmax)
universe8 = openmc.Universe(universe_id=8, cells=[u8_cell0, u8_cell1, u8_cell2, u8_cell3, u8_cell4, u8_cell5])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Frods
cell1 = openmc.Cell(cell_id=1, fill=universe6)
cell1.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110

# Arod
cell2 = openmc.Cell(cell_id=2, fill=universe8)
cell2.translation = (-7.7, 13.336792, 0.0)
cell2.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf501

# Arod
cell3 = openmc.Cell(cell_id=3, fill=universe8)
cell3.translation = (7.7, 13.336792, 0.0)
cell3.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf502

# Arod
cell4 = openmc.Cell(cell_id=4, fill=universe8)
cell4.translation = (-15.4, 0.0, 0.0)
cell4.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf503

# Arod
cell5 = openmc.Cell(cell_id=5, fill=universe8)
cell5.translation = (15.4, 0.0, 0.0)
cell5.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf504

# Arod
cell6 = openmc.Cell(cell_id=6, fill=universe8)
cell6.translation = (-7.7, -13.336792, 0.0)
cell6.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf505

# Arod
cell7 = openmc.Cell(cell_id=7, fill=universe8)
cell7.translation = (7.7, -13.336792, 0.0)
cell7.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf506

# Hole
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf101 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf102 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf103

# Hole
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf104 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf105 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf106

# Hole
cell10 = openmc.Cell(cell_id=10, fill=mat4)
cell10.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf107 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf108 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf109

# Hole
cell11 = openmc.Cell(cell_id=11, fill=mat4)
cell11.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf110 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf111 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf112

# Hole
cell12 = openmc.Cell(cell_id=12, fill=mat4)
cell12.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf113 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf114 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf115

# Hole
cell13 = openmc.Cell(cell_id=13, fill=mat4)
cell13.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf116 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf117 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf118

# Hole
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf119 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf120 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf121

# Hole
cell15 = openmc.Cell(cell_id=15, fill=mat4)
cell15.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf122 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf123 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5 & -surf30_6 & -surf30_7 & -surf30_8 & -surf30_9 & -surf30_10 & -surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf124

# Holes
cell16 = openmc.Cell(cell_id=16, fill=universe7)
cell16.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & +surf201 & +surf202 & +surf203 & +surf204 & +surf205 & +surf206 & +surf207 & +surf208 & +surf209 & +surf210

# Frod
cell17 = openmc.Cell(cell_id=17, fill=universe2)
cell17.translation = (-6.6, 19.05256, 0.0)
cell17.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf201

# Frod
cell18 = openmc.Cell(cell_id=18, fill=universe2)
cell18.translation = (-5.5, 19.05256, 0.0)
cell18.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf202

# Frod
cell19 = openmc.Cell(cell_id=19, fill=universe2)
cell19.translation = (-4.4, 19.05256, 0.0)
cell19.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf203

# Frod
cell20 = openmc.Cell(cell_id=20, fill=universe2)
cell20.translation = (-3.3, 19.05256, 0.0)
cell20.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf204

# Frod
cell21 = openmc.Cell(cell_id=21, fill=universe2)
cell21.translation = (-2.2, 19.05256, 0.0)
cell21.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf205

# Frod
cell22 = openmc.Cell(cell_id=22, fill=universe2)
cell22.translation = (-1.1, 19.05256, 0.0)
cell22.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf206

# Frod
cell23 = openmc.Cell(cell_id=23, fill=universe2)
cell23.translation = (0.0, 19.05256, 0.0)
cell23.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf207

# Frod
cell24 = openmc.Cell(cell_id=24, fill=universe2)
cell24.translation = (1.1, 19.05256, 0.0)
cell24.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf208

# Frod
cell25 = openmc.Cell(cell_id=25, fill=universe2)
cell25.translation = (2.2, 19.05256, 0.0)
cell25.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf209

# Frod
cell26 = openmc.Cell(cell_id=26, fill=universe2)
cell26.translation = (3.3, 19.05256, 0.0)
cell26.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf210

# Frod
cell27 = openmc.Cell(cell_id=27, fill=universe2)
cell27.translation = (4.4, 19.05256, 0.0)
cell27.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf211

# Frod
cell28 = openmc.Cell(cell_id=28, fill=universe2)
cell28.translation = (5.5, 19.05256, 0.0)
cell28.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf212

# Frod
cell29 = openmc.Cell(cell_id=29, fill=universe2)
cell29.translation = (6.6, 19.05256, 0.0)
cell29.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf213

# Frod
cell30 = openmc.Cell(cell_id=30, fill=universe2)
cell30.translation = (-13.2, 15.242048, 0.0)
cell30.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf214

# Frod
cell31 = openmc.Cell(cell_id=31, fill=universe2)
cell31.translation = (-13.75, 14.28942, 0.0)
cell31.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf215

# Frod
cell32 = openmc.Cell(cell_id=32, fill=universe2)
cell32.translation = (-14.3, 13.336792, 0.0)
cell32.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf216

# Frod
cell33 = openmc.Cell(cell_id=33, fill=universe2)
cell33.translation = (-14.85, 12.384164, 0.0)
cell33.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf217

# Frod
cell34 = openmc.Cell(cell_id=34, fill=universe2)
cell34.translation = (-15.4, 11.431536, 0.0)
cell34.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf218

# Frod
cell35 = openmc.Cell(cell_id=35, fill=universe2)
cell35.translation = (-15.95, 10.478908, 0.0)
cell35.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf219

# Frod
cell36 = openmc.Cell(cell_id=36, fill=universe2)
cell36.translation = (-16.5, 9.52628, 0.0)
cell36.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf220

# Frod
cell37 = openmc.Cell(cell_id=37, fill=universe2)
cell37.translation = (-17.05, 8.573652, 0.0)
cell37.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf221

# Frod
cell38 = openmc.Cell(cell_id=38, fill=universe2)
cell38.translation = (-17.6, 7.621024, 0.0)
cell38.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf222

# Frod
cell39 = openmc.Cell(cell_id=39, fill=universe2)
cell39.translation = (-18.15, 6.668396, 0.0)
cell39.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf223

# Frod
cell40 = openmc.Cell(cell_id=40, fill=universe2)
cell40.translation = (-18.7, 5.715768, 0.0)
cell40.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf224

# Frod
cell41 = openmc.Cell(cell_id=41, fill=universe2)
cell41.translation = (-19.25, 4.76314, 0.0)
cell41.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf225

# Frod
cell42 = openmc.Cell(cell_id=42, fill=universe2)
cell42.translation = (-19.8, 3.810512, 0.0)
cell42.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf226

# Frod
cell43 = openmc.Cell(cell_id=43, fill=universe2)
cell43.translation = (13.2, 15.242048, 0.0)
cell43.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf227

# Frod
cell44 = openmc.Cell(cell_id=44, fill=universe2)
cell44.translation = (13.75, 14.28942, 0.0)
cell44.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf228

# Frod
cell45 = openmc.Cell(cell_id=45, fill=universe2)
cell45.translation = (14.3, 13.336792, 0.0)
cell45.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf229

# Frod
cell46 = openmc.Cell(cell_id=46, fill=universe2)
cell46.translation = (14.85, 12.384164, 0.0)
cell46.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf230

# Frod
cell47 = openmc.Cell(cell_id=47, fill=universe2)
cell47.translation = (15.4, 11.431536, 0.0)
cell47.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf231

# Frod
cell48 = openmc.Cell(cell_id=48, fill=universe2)
cell48.translation = (15.95, 10.478908, 0.0)
cell48.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf232

# Frod
cell49 = openmc.Cell(cell_id=49, fill=universe2)
cell49.translation = (16.5, 9.52628, 0.0)
cell49.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf233

# Frod
cell50 = openmc.Cell(cell_id=50, fill=universe2)
cell50.translation = (17.05, 8.573652, 0.0)
cell50.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf234

# Frod
cell51 = openmc.Cell(cell_id=51, fill=universe2)
cell51.translation = (17.6, 7.621024, 0.0)
cell51.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf235

# Frod
cell52 = openmc.Cell(cell_id=52, fill=universe2)
cell52.translation = (18.15, 6.668396, 0.0)
cell52.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf236

# Frod
cell53 = openmc.Cell(cell_id=53, fill=universe2)
cell53.translation = (18.7, 5.715768, 0.0)
cell53.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf237

# Frod
cell54 = openmc.Cell(cell_id=54, fill=universe2)
cell54.translation = (19.25, 4.76314, 0.0)
cell54.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf238

# Frod
cell55 = openmc.Cell(cell_id=55, fill=universe2)
cell55.translation = (19.8, 3.810512, 0.0)
cell55.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf239

# Frod
cell56 = openmc.Cell(cell_id=56, fill=universe2)
cell56.translation = (-13.2, -15.242048, 0.0)
cell56.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf240

# Frod
cell57 = openmc.Cell(cell_id=57, fill=universe2)
cell57.translation = (-13.75, -14.28942, 0.0)
cell57.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf241

# Frod
cell58 = openmc.Cell(cell_id=58, fill=universe2)
cell58.translation = (-14.3, -13.336792, 0.0)
cell58.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf242

# Frod
cell59 = openmc.Cell(cell_id=59, fill=universe2)
cell59.translation = (-14.85, -12.384164, 0.0)
cell59.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf243

# Frod
cell60 = openmc.Cell(cell_id=60, fill=universe2)
cell60.translation = (-15.4, -11.431536, 0.0)
cell60.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf244

# Frod
cell61 = openmc.Cell(cell_id=61, fill=universe2)
cell61.translation = (-15.95, -10.478908, 0.0)
cell61.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf245

# Frod
cell62 = openmc.Cell(cell_id=62, fill=universe2)
cell62.translation = (-16.5, -9.52628, 0.0)
cell62.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf246

# Frod
cell63 = openmc.Cell(cell_id=63, fill=universe2)
cell63.translation = (-17.05, -8.573652, 0.0)
cell63.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf247

# Frod
cell64 = openmc.Cell(cell_id=64, fill=universe2)
cell64.translation = (-17.6, -7.621024, 0.0)
cell64.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf248

# Frod
cell65 = openmc.Cell(cell_id=65, fill=universe2)
cell65.translation = (-18.15, -6.668396, 0.0)
cell65.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf249

# Frod
cell66 = openmc.Cell(cell_id=66, fill=universe2)
cell66.translation = (-18.7, -5.715768, 0.0)
cell66.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf250

# Frod
cell67 = openmc.Cell(cell_id=67, fill=universe2)
cell67.translation = (-19.25, -4.76314, 0.0)
cell67.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf251

# Frod
cell68 = openmc.Cell(cell_id=68, fill=universe2)
cell68.translation = (-19.8, -3.810512, 0.0)
cell68.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf252

# Frod
cell69 = openmc.Cell(cell_id=69, fill=universe2)
cell69.translation = (13.2, -15.242048, 0.0)
cell69.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf253

# Frod
cell70 = openmc.Cell(cell_id=70, fill=universe2)
cell70.translation = (13.75, -14.28942, 0.0)
cell70.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf254

# Frod
cell71 = openmc.Cell(cell_id=71, fill=universe2)
cell71.translation = (14.3, -13.336792, 0.0)
cell71.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf255

# Frod
cell72 = openmc.Cell(cell_id=72, fill=universe2)
cell72.translation = (14.85, -12.384164, 0.0)
cell72.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf256

# Frod
cell73 = openmc.Cell(cell_id=73, fill=universe2)
cell73.translation = (15.4, -11.431536, 0.0)
cell73.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf257

# Frod
cell74 = openmc.Cell(cell_id=74, fill=universe2)
cell74.translation = (15.95, -10.478908, 0.0)
cell74.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf258

# Frod
cell75 = openmc.Cell(cell_id=75, fill=universe2)
cell75.translation = (16.5, -9.52628, 0.0)
cell75.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf259

# Frod
cell76 = openmc.Cell(cell_id=76, fill=universe2)
cell76.translation = (17.05, -8.573652, 0.0)
cell76.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf260

# Frod
cell77 = openmc.Cell(cell_id=77, fill=universe2)
cell77.translation = (17.6, -7.621024, 0.0)
cell77.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf261

# Frod
cell78 = openmc.Cell(cell_id=78, fill=universe2)
cell78.translation = (18.15, -6.668396, 0.0)
cell78.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf262

# Frod
cell79 = openmc.Cell(cell_id=79, fill=universe2)
cell79.translation = (18.7, -5.715768, 0.0)
cell79.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf263

# Frod
cell80 = openmc.Cell(cell_id=80, fill=universe2)
cell80.translation = (19.25, -4.76314, 0.0)
cell80.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf264

# Frod
cell81 = openmc.Cell(cell_id=81, fill=universe2)
cell81.translation = (19.8, -3.810512, 0.0)
cell81.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf265

# Frod
cell82 = openmc.Cell(cell_id=82, fill=universe2)
cell82.translation = (-6.6, -19.05256, 0.0)
cell82.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf266

# Frod
cell83 = openmc.Cell(cell_id=83, fill=universe2)
cell83.translation = (-5.5, -19.05256, 0.0)
cell83.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf267

# Frod
cell84 = openmc.Cell(cell_id=84, fill=universe2)
cell84.translation = (-4.4, -19.05256, 0.0)
cell84.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf268

# Frod
cell85 = openmc.Cell(cell_id=85, fill=universe2)
cell85.translation = (-3.3, -19.05256, 0.0)
cell85.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf269

# Frod
cell86 = openmc.Cell(cell_id=86, fill=universe2)
cell86.translation = (-2.2, -19.05256, 0.0)
cell86.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf270

# Frod
cell87 = openmc.Cell(cell_id=87, fill=universe2)
cell87.translation = (-1.1, -19.05256, 0.0)
cell87.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf271

# Frod
cell88 = openmc.Cell(cell_id=88, fill=universe2)
cell88.translation = (0.0, -19.05256, 0.0)
cell88.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf272

# Frod
cell89 = openmc.Cell(cell_id=89, fill=universe2)
cell89.translation = (1.1, -19.05256, 0.0)
cell89.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf273

# Frod
cell90 = openmc.Cell(cell_id=90, fill=universe2)
cell90.translation = (2.2, -19.05256, 0.0)
cell90.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf274

# Frod
cell91 = openmc.Cell(cell_id=91, fill=universe2)
cell91.translation = (3.3, -19.05256, 0.0)
cell91.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf275

# Frod
cell92 = openmc.Cell(cell_id=92, fill=universe2)
cell92.translation = (4.4, -19.05256, 0.0)
cell92.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf276

# Frod
cell93 = openmc.Cell(cell_id=93, fill=universe2)
cell93.translation = (5.5, -19.05256, 0.0)
cell93.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf277

# Frod
cell94 = openmc.Cell(cell_id=94, fill=universe2)
cell94.translation = (6.6, -19.05256, 0.0)
cell94.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf278

# Alles
cell95 = openmc.Cell(cell_id=95, fill=universe1)
cell95.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & +surf301 & +surf302 & +surf303 & +surf304 & +surf305 & +surf306 & +surf307 & +surf308 & +surf309 & +surf310

# Hole
cell96 = openmc.Cell(cell_id=96, fill=mat4)
cell96.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf301 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf302 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf303

# Hole
cell97 = openmc.Cell(cell_id=97, fill=mat4)
cell97.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf304 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf305 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf306

# Hole
cell98 = openmc.Cell(cell_id=98, fill=mat4)
cell98.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf307 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf308 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf309

# Hole
cell99 = openmc.Cell(cell_id=99, fill=mat4)
cell99.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf310 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf311 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf312

# Hole
cell100 = openmc.Cell(cell_id=100, fill=mat4)
cell100.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf313 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf314 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf315

# Hole
cell101 = openmc.Cell(cell_id=101, fill=mat4)
cell101.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf316 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf317 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf318

# Hole
cell102 = openmc.Cell(cell_id=102, fill=mat4)
cell102.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf319 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf320 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf321

# Hole
cell103 = openmc.Cell(cell_id=103, fill=mat4)
cell103.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf322 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf323 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf324

# Hole
cell104 = openmc.Cell(cell_id=104, fill=mat4)
cell104.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf325 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf326 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf327

# Hole
cell105 = openmc.Cell(cell_id=105, fill=mat4)
cell105.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf328 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf329 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf330

# Hole
cell106 = openmc.Cell(cell_id=106, fill=mat4)
cell106.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf331 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf332 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf333

# Hole
cell107 = openmc.Cell(cell_id=107, fill=mat4)
cell107.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf334 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf335 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf336

# Hole
cell108 = openmc.Cell(cell_id=108, fill=mat4)
cell108.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf337 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf338 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf339

# Hole
cell109 = openmc.Cell(cell_id=109, fill=mat4)
cell109.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf340 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf341 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf342

# Hole
cell110 = openmc.Cell(cell_id=110, fill=mat4)
cell110.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf343 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf344 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf345

# Hole
cell111 = openmc.Cell(cell_id=111, fill=mat4)
cell111.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf346 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf347 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf348

# Hole
cell112 = openmc.Cell(cell_id=112, fill=mat4)
cell112.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf349 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf350 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf351

# Hole
cell113 = openmc.Cell(cell_id=113, fill=mat4)
cell113.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf352 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf353 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf354

# Hole
cell114 = openmc.Cell(cell_id=114, fill=mat4)
cell114.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf355 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf356 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf357

# Hole
cell115 = openmc.Cell(cell_id=115, fill=mat4)
cell115.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf358 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf359 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf360

# Hole
cell116 = openmc.Cell(cell_id=116, fill=mat4)
cell116.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf361 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf362 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf363

# Hole
cell117 = openmc.Cell(cell_id=117, fill=mat4)
cell117.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf364 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf365 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf366

# Hole
cell118 = openmc.Cell(cell_id=118, fill=mat4)
cell118.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf367 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf368 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf369

# Hole
cell119 = openmc.Cell(cell_id=119, fill=mat4)
cell119.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf370 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf371 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf372

# Hole
cell120 = openmc.Cell(cell_id=120, fill=mat4)
cell120.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf373 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf374 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf375

# Hole
cell121 = openmc.Cell(cell_id=121, fill=mat4)
cell121.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf376 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf377 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf378

# Hole
cell122 = openmc.Cell(cell_id=122, fill=mat4)
cell122.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf379 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf380 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf381

# Hole
cell123 = openmc.Cell(cell_id=123, fill=mat4)
cell123.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf382 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf383 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf384

# Hole
cell124 = openmc.Cell(cell_id=124, fill=mat4)
cell124.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf385 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf386 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf387

# Hole
cell125 = openmc.Cell(cell_id=125, fill=mat4)
cell125.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf388 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf389 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf390

# Hole
cell126 = openmc.Cell(cell_id=126, fill=mat4)
cell126.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf391 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf392 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf393

# Hole
cell127 = openmc.Cell(cell_id=127, fill=mat4)
cell127.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf394 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf395 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf396

# Hole
cell128 = openmc.Cell(cell_id=128, fill=mat4)
cell128.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf397 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf398 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf399

# Hole
cell129 = openmc.Cell(cell_id=129, fill=mat4)
cell129.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf400 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf401 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf402

# Hole
cell130 = openmc.Cell(cell_id=130, fill=mat4)
cell130.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf403 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf404 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf405

# Hole
cell131 = openmc.Cell(cell_id=131, fill=mat4)
cell131.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf406 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf407 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf408

# Hole
cell132 = openmc.Cell(cell_id=132, fill=mat4)
cell132.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf409 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf410 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf411

# Hole
cell133 = openmc.Cell(cell_id=133, fill=mat4)
cell133.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf412 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf413 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf414

# Hole
cell134 = openmc.Cell(cell_id=134, fill=mat4)
cell134.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf415 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf416 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf417

# Hole
cell135 = openmc.Cell(cell_id=135, fill=mat4)
cell135.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf418 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf419 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf420

# Hole
cell136 = openmc.Cell(cell_id=136, fill=mat4)
cell136.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf421 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf422 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf423

# Hole
cell137 = openmc.Cell(cell_id=137, fill=mat4)
cell137.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf424 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf425 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf426

# Hole
cell138 = openmc.Cell(cell_id=138, fill=mat4)
cell138.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf427 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf428 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf429

# Hole
cell139 = openmc.Cell(cell_id=139, fill=mat4)
cell139.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf430 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf431 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf432

# Hole
cell140 = openmc.Cell(cell_id=140, fill=mat4)
cell140.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf433 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf434 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf435

# Hole
cell141 = openmc.Cell(cell_id=141, fill=mat4)
cell141.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf436 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf437 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5 | +surf30_6 | +surf30_7 | +surf30_8 | +surf30_9 | +surf30_10 | +surf30_11) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & -surf438

# Water
cell146 = openmc.Cell(cell_id=146, fill=mat4)
cell146.region = -surf1 & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# Water
cell154 = openmc.Cell(cell_id=154, fill=mat4)
cell154.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax) & (+surf18 | -surf18_zmin | +surf18_zmax) & (+surf19 | -surf19_zmin | +surf19_zmax)

# Water
cell156 = openmc.Cell(cell_id=156, fill=mat4)
cell156.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax)

# Alles
cell157 = openmc.Cell(cell_id=157, fill=universe1)
cell157.region = (-surf5 & +surf5_zmin & -surf5_zmax) & +surf20 & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

# Alles
cell158 = openmc.Cell(cell_id=158, fill=universe1)
cell158.region = (-surf5 & +surf5_zmin & -surf5_zmax) & +surf20 & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

# Water
cell165 = openmc.Cell(cell_id=165, fill=mat4)
cell165.region = -surf1 & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf43 | -surf43_zmin | +surf43_zmax) & (+surf44 | -surf44_zmin | +surf44_zmax) & (+surf45 | -surf45_zmin | +surf45_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49, cell50, cell51, cell52, cell53, cell54, cell55, cell56, cell57, cell58, cell59, cell60, cell61, cell62, cell63, cell64, cell65, cell66, cell67, cell68, cell69, cell70, cell71, cell72, cell73, cell74, cell75, cell76, cell77, cell78, cell79, cell80, cell81, cell82, cell83, cell84, cell85, cell86, cell87, cell88, cell89, cell90, cell91, cell92, cell93, cell94, cell95, cell96, cell97, cell98, cell99, cell100, cell101, cell102, cell103, cell104, cell105, cell106, cell107, cell108, cell109, cell110, cell111, cell112, cell113, cell114, cell115, cell116, cell117, cell118, cell119, cell120, cell121, cell122, cell123, cell124, cell125, cell126, cell127, cell128, cell129, cell130, cell131, cell132, cell133, cell134, cell135, cell136, cell137, cell138, cell139, cell140, cell141, cell146, cell154, cell156, cell157, cell158, cell165])
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
source.space = openmc.stats.Point((0.0, 0.0, 46.915))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
