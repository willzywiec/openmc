"""
LCT025-1: Lattice of 2,410 U(7.5)O2 rods with 0.7 cm (triangular) pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(7.5)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 9.156100e-06)
mat1.add_nuclide("U235", 1.501300e-03)
mat1.add_nuclide("U236", 9.078300e-06)
mat1.add_nuclide("U238", 1.850400e-02)
mat1.add_nuclide("O16", 4.004600e-02)

# SST clad
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.889400e-02)
mat2.add_element("Cr", 1.646900e-02)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Si", 1.355100e-03)
mat2.add_element("Mn", 1.299000e-03)
mat2.add_element("C", 2.376600e-04)
mat2.add_element("Ti", 4.471300e-04)

# D16 aluminum
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 1.498900e-04)
mat3.add_element("Si", 2.980400e-04)
mat3.add_element("Cu", 1.146000e-03)
mat3.add_element("Al", 5.711500e-02)
mat3.add_element("Mg", 1.033200e-03)
mat3.add_element("Mn", 1.828400e-04)
mat3.add_element("Ti", 3.496500e-05)
mat3.add_element("Zn", 7.680700e-05)
mat3.add_element("Ni", 2.852500e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.673600e-02)
mat4.add_nuclide("O16", 3.336800e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# UO2
surf1 = openmc.ZCylinder(surface_id=1, r=0.208)
# void, lower
surf2 = openmc.ZCylinder(surface_id=2, r=0.1)
# void, gap
surf3 = openmc.ZCylinder(surface_id=3, r=0.215)
# void, upper
surf4 = openmc.ZCylinder(surface_id=4, r=0.1)
# SST,  lower
surf5 = openmc.ZCylinder(surface_id=5, r=0.2)
# SST,  main
surf6 = openmc.ZCylinder(surface_id=6, r=0.255)
# SST,  upper
surf7 = openmc.ZCylinder(surface_id=7, r=0.187)
# H2O,  hole
surf8 = openmc.ZCylinder(surface_id=8, r=0.26)
# Support plate
surf11 = openmc.ZCylinder(surface_id=11, r=99.9)
# Lower grid plate - w/o holes
surf12 = openmc.ZCylinder(surface_id=12, r=99.9)
# Upper grid plate - w/o holes
surf13 = openmc.ZCylinder(surface_id=13, r=99.9)
# Water and boundary condition
surf14 = openmc.ZCylinder(surface_id=14, r=48.5, boundary_type="vacuum")
surf21 = openmc.ZCylinder(surface_id=21, x0=-0.35, y0=0.606218, r=0.26)
surf22 = openmc.ZCylinder(surface_id=22, x0=0.35, y0=0.606218, r=0.26)
surf23 = openmc.ZCylinder(surface_id=23, x0=-0.35, y0=-0.606218, r=0.26)
surf24 = openmc.ZCylinder(surface_id=24, x0=0.35, y0=-0.606218, r=0.26)
# Prism 31: 12-sided polygon
surf31_0 = openmc.Plane(a=0.8660254814, b=0.4999998655, c=0, d=17.5803172726)
surf31_1 = openmc.Plane(a=0.5000001345, b=0.8660253262, c=0, d=18.2000048940)
surf31_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=17.5803220000)
surf31_3 = openmc.Plane(a=-0.5000001345, b=0.8660253262, c=0, d=18.2000048940)
surf31_4 = openmc.Plane(a=-0.8660254814, b=0.4999998655, c=0, d=17.5803172726)
surf31_5 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=18.2000000000)
surf31_6 = openmc.Plane(a=-0.8660254814, b=-0.4999998655, c=0, d=17.5803172726)
surf31_7 = openmc.Plane(a=-0.5000001345, b=-0.8660253262, c=0, d=18.2000048940)
surf31_8 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=17.5803220000)
surf31_9 = openmc.Plane(a=0.5000001345, b=-0.8660253262, c=0, d=18.2000048940)
surf31_10 = openmc.Plane(a=0.8660254814, b=-0.4999998655, c=0, d=17.5803172726)
surf31_11 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=18.2000000000)
# Prism 32: 6-sided polygon
surf32_0 = openmc.Plane(a=0.8660254814, b=0.4999998655, c=0, d=18.1865351096)
surf32_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=18.1865400000)
surf32_2 = openmc.Plane(a=-0.8660254814, b=0.4999998655, c=0, d=18.1865351096)
surf32_3 = openmc.Plane(a=-0.8660254814, b=-0.4999998655, c=0, d=18.1865351096)
surf32_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=18.1865400000)
surf32_5 = openmc.Plane(a=0.8660254814, b=-0.4999998655, c=0, d=18.1865351096)
surf101 = openmc.ZCylinder(surface_id=101, x0=-5.95, y0=17.580322, r=0.26)
surf102 = openmc.ZCylinder(surface_id=102, x0=-5.25, y0=17.580322, r=0.26)
surf103 = openmc.ZCylinder(surface_id=103, x0=-4.55, y0=17.580322, r=0.26)
surf104 = openmc.ZCylinder(surface_id=104, x0=4.55, y0=17.580322, r=0.26)
surf105 = openmc.ZCylinder(surface_id=105, x0=5.25, y0=17.580322, r=0.26)
surf106 = openmc.ZCylinder(surface_id=106, x0=5.95, y0=17.580322, r=0.26)
surf107 = openmc.ZCylinder(surface_id=107, x0=-7.0, y0=16.974104, r=0.26)
surf108 = openmc.ZCylinder(surface_id=108, x0=-6.3, y0=16.974104, r=0.26)
surf109 = openmc.ZCylinder(surface_id=109, x0=6.3, y0=16.974104, r=0.26)
surf110 = openmc.ZCylinder(surface_id=110, x0=7.0, y0=16.974104, r=0.26)
surf111 = openmc.ZCylinder(surface_id=111, x0=-8.05, y0=16.367886, r=0.26)
surf112 = openmc.ZCylinder(surface_id=112, x0=8.05, y0=16.367886, r=0.26)
surf113 = openmc.ZCylinder(surface_id=113, x0=-10.15, y0=15.15545, r=0.26)
surf114 = openmc.ZCylinder(surface_id=114, x0=10.15, y0=15.15545, r=0.26)
surf115 = openmc.ZCylinder(surface_id=115, x0=-11.2, y0=14.549232, r=0.26)
surf116 = openmc.ZCylinder(surface_id=116, x0=11.2, y0=14.549232, r=0.26)
surf117 = openmc.ZCylinder(surface_id=117, x0=-12.25, y0=13.943014, r=0.26)
surf118 = openmc.ZCylinder(surface_id=118, x0=-11.55, y0=13.943014, r=0.26)
surf119 = openmc.ZCylinder(surface_id=119, x0=11.55, y0=13.943014, r=0.26)
surf120 = openmc.ZCylinder(surface_id=120, x0=12.25, y0=13.943014, r=0.26)
surf121 = openmc.ZCylinder(surface_id=121, x0=-12.6, y0=13.336796, r=0.26)
surf122 = openmc.ZCylinder(surface_id=122, x0=12.6, y0=13.336796, r=0.26)
surf123 = openmc.ZCylinder(surface_id=123, x0=-12.95, y0=12.730578, r=0.26)
surf124 = openmc.ZCylinder(surface_id=124, x0=12.95, y0=12.730578, r=0.26)
surf125 = openmc.ZCylinder(surface_id=125, x0=-17.5, y0=4.849744, r=0.26)
surf126 = openmc.ZCylinder(surface_id=126, x0=17.5, y0=4.849744, r=0.26)
surf127 = openmc.ZCylinder(surface_id=127, x0=-17.85, y0=4.243526, r=0.26)
surf128 = openmc.ZCylinder(surface_id=128, x0=17.85, y0=4.243526, r=0.26)
surf129 = openmc.ZCylinder(surface_id=129, x0=-18.2, y0=3.637308, r=0.26)
surf130 = openmc.ZCylinder(surface_id=130, x0=18.2, y0=3.637308, r=0.26)
surf131 = openmc.ZCylinder(surface_id=131, x0=-17.85, y0=3.03109, r=0.26)
surf132 = openmc.ZCylinder(surface_id=132, x0=17.85, y0=3.03109, r=0.26)
surf133 = openmc.ZCylinder(surface_id=133, x0=-18.2, y0=2.424872, r=0.26)
surf134 = openmc.ZCylinder(surface_id=134, x0=18.2, y0=2.424872, r=0.26)
surf135 = openmc.ZCylinder(surface_id=135, x0=-18.2, y0=1.212436, r=0.26)
surf136 = openmc.ZCylinder(surface_id=136, x0=18.2, y0=1.212436, r=0.26)
surf137 = openmc.ZCylinder(surface_id=137, x0=-18.2, y0=-1.212436, r=0.26)
surf138 = openmc.ZCylinder(surface_id=138, x0=18.2, y0=-1.212436, r=0.26)
surf139 = openmc.ZCylinder(surface_id=139, x0=-18.2, y0=-2.424872, r=0.26)
surf140 = openmc.ZCylinder(surface_id=140, x0=18.2, y0=-2.424872, r=0.26)
surf141 = openmc.ZCylinder(surface_id=141, x0=-17.85, y0=-3.03109, r=0.26)
surf142 = openmc.ZCylinder(surface_id=142, x0=17.85, y0=-3.03109, r=0.26)
surf143 = openmc.ZCylinder(surface_id=143, x0=-18.2, y0=-3.637308, r=0.26)
surf144 = openmc.ZCylinder(surface_id=144, x0=18.2, y0=-3.637308, r=0.26)
surf145 = openmc.ZCylinder(surface_id=145, x0=-17.85, y0=-4.243526, r=0.26)
surf146 = openmc.ZCylinder(surface_id=146, x0=17.85, y0=-4.243526, r=0.26)
surf147 = openmc.ZCylinder(surface_id=147, x0=-17.5, y0=-4.849744, r=0.26)
surf148 = openmc.ZCylinder(surface_id=148, x0=17.5, y0=-4.849744, r=0.26)
surf149 = openmc.ZCylinder(surface_id=149, x0=-12.95, y0=-12.730578, r=0.26)
surf150 = openmc.ZCylinder(surface_id=150, x0=12.95, y0=-12.730578, r=0.26)
surf151 = openmc.ZCylinder(surface_id=151, x0=-12.6, y0=-13.336796, r=0.26)
surf152 = openmc.ZCylinder(surface_id=152, x0=12.6, y0=-13.336796, r=0.26)
surf153 = openmc.ZCylinder(surface_id=153, x0=-12.25, y0=-13.943014, r=0.26)
surf154 = openmc.ZCylinder(surface_id=154, x0=-11.55, y0=-13.943014, r=0.26)
surf155 = openmc.ZCylinder(surface_id=155, x0=11.55, y0=-13.943014, r=0.26)
surf156 = openmc.ZCylinder(surface_id=156, x0=12.25, y0=-13.943014, r=0.26)
surf157 = openmc.ZCylinder(surface_id=157, x0=-11.2, y0=-14.549232, r=0.26)
surf158 = openmc.ZCylinder(surface_id=158, x0=11.2, y0=-14.549232, r=0.26)
surf159 = openmc.ZCylinder(surface_id=159, x0=-10.15, y0=-15.15545, r=0.26)
surf160 = openmc.ZCylinder(surface_id=160, x0=10.15, y0=-15.15545, r=0.26)
surf161 = openmc.ZCylinder(surface_id=161, x0=-8.05, y0=-16.367886, r=0.26)
surf162 = openmc.ZCylinder(surface_id=162, x0=8.05, y0=-16.367886, r=0.26)
surf163 = openmc.ZCylinder(surface_id=163, x0=-7.0, y0=-16.974104, r=0.26)
surf164 = openmc.ZCylinder(surface_id=164, x0=-6.3, y0=-16.974104, r=0.26)
surf165 = openmc.ZCylinder(surface_id=165, x0=6.3, y0=-16.974104, r=0.26)
surf166 = openmc.ZCylinder(surface_id=166, x0=7.0, y0=-16.974104, r=0.26)
surf167 = openmc.ZCylinder(surface_id=167, x0=-5.95, y0=-17.580322, r=0.26)
surf168 = openmc.ZCylinder(surface_id=168, x0=-5.25, y0=-17.580322, r=0.26)
surf169 = openmc.ZCylinder(surface_id=169, x0=-4.55, y0=-17.580322, r=0.26)
surf170 = openmc.ZCylinder(surface_id=170, x0=-3.85, y0=-17.580322, r=0.26)
surf171 = openmc.ZCylinder(surface_id=171, x0=3.15, y0=-17.580322, r=0.26)
surf172 = openmc.ZCylinder(surface_id=172, x0=3.85, y0=-17.580322, r=0.26)
surf173 = openmc.ZCylinder(surface_id=173, x0=4.55, y0=-17.580322, r=0.26)
surf174 = openmc.ZCylinder(surface_id=174, x0=5.25, y0=-17.580322, r=0.26)
surf175 = openmc.ZCylinder(surface_id=175, x0=5.95, y0=-17.580322, r=0.26)
surf201 = openmc.ZCylinder(surface_id=201, x0=-3.85, y0=17.580322, r=0.26)
surf202 = openmc.ZCylinder(surface_id=202, x0=-3.15, y0=17.580322, r=0.26)
surf203 = openmc.ZCylinder(surface_id=203, x0=-2.45, y0=17.580322, r=0.26)
surf204 = openmc.ZCylinder(surface_id=204, x0=-1.75, y0=17.580322, r=0.26)
surf205 = openmc.ZCylinder(surface_id=205, x0=-1.05, y0=17.580322, r=0.26)
surf206 = openmc.ZCylinder(surface_id=206, x0=-0.35, y0=17.580322, r=0.26)
surf207 = openmc.ZCylinder(surface_id=207, x0=0.35, y0=17.580322, r=0.26)
surf208 = openmc.ZCylinder(surface_id=208, x0=1.05, y0=17.580322, r=0.26)
surf209 = openmc.ZCylinder(surface_id=209, x0=1.75, y0=17.580322, r=0.26)
surf210 = openmc.ZCylinder(surface_id=210, x0=2.45, y0=17.580322, r=0.26)
surf211 = openmc.ZCylinder(surface_id=211, x0=3.15, y0=17.580322, r=0.26)
surf212 = openmc.ZCylinder(surface_id=212, x0=3.85, y0=17.580322, r=0.26)
surf213 = openmc.ZCylinder(surface_id=213, x0=-9.1, y0=15.761668, r=0.26)
surf214 = openmc.ZCylinder(surface_id=214, x0=9.1, y0=15.761668, r=0.26)
surf215 = openmc.ZCylinder(surface_id=215, x0=-13.3, y0=12.12436, r=0.26)
surf216 = openmc.ZCylinder(surface_id=216, x0=13.3, y0=12.12436, r=0.26)
surf217 = openmc.ZCylinder(surface_id=217, x0=-13.65, y0=11.518142, r=0.26)
surf218 = openmc.ZCylinder(surface_id=218, x0=13.65, y0=11.518142, r=0.26)
surf219 = openmc.ZCylinder(surface_id=219, x0=-14.0, y0=10.911924, r=0.26)
surf220 = openmc.ZCylinder(surface_id=220, x0=14.0, y0=10.911924, r=0.26)
surf221 = openmc.ZCylinder(surface_id=221, x0=-14.35, y0=10.305706, r=0.26)
surf222 = openmc.ZCylinder(surface_id=222, x0=14.35, y0=10.305706, r=0.26)
surf223 = openmc.ZCylinder(surface_id=223, x0=-14.7, y0=9.699488, r=0.26)
surf224 = openmc.ZCylinder(surface_id=224, x0=14.7, y0=9.699488, r=0.26)
surf225 = openmc.ZCylinder(surface_id=225, x0=-15.05, y0=9.09327, r=0.26)
surf226 = openmc.ZCylinder(surface_id=226, x0=15.05, y0=9.09327, r=0.26)
surf227 = openmc.ZCylinder(surface_id=227, x0=-15.4, y0=8.487052, r=0.26)
surf228 = openmc.ZCylinder(surface_id=228, x0=15.4, y0=8.487052, r=0.26)
surf229 = openmc.ZCylinder(surface_id=229, x0=-15.75, y0=7.880834, r=0.26)
surf230 = openmc.ZCylinder(surface_id=230, x0=15.75, y0=7.880834, r=0.26)
surf231 = openmc.ZCylinder(surface_id=231, x0=-16.1, y0=7.274616, r=0.26)
surf232 = openmc.ZCylinder(surface_id=232, x0=16.1, y0=7.274616, r=0.26)
surf233 = openmc.ZCylinder(surface_id=233, x0=-16.45, y0=6.668398, r=0.26)
surf234 = openmc.ZCylinder(surface_id=234, x0=16.45, y0=6.668398, r=0.26)
surf235 = openmc.ZCylinder(surface_id=235, x0=-16.8, y0=6.06218, r=0.26)
surf236 = openmc.ZCylinder(surface_id=236, x0=16.8, y0=6.06218, r=0.26)
surf237 = openmc.ZCylinder(surface_id=237, x0=-17.15, y0=5.455962, r=0.26)
surf238 = openmc.ZCylinder(surface_id=238, x0=17.15, y0=5.455962, r=0.26)
surf239 = openmc.ZCylinder(surface_id=239, x0=-18.2, y0=0.0, r=0.26)
surf240 = openmc.ZCylinder(surface_id=240, x0=18.2, y0=0.0, r=0.26)
surf241 = openmc.ZCylinder(surface_id=241, x0=-17.15, y0=-5.455962, r=0.26)
surf242 = openmc.ZCylinder(surface_id=242, x0=17.15, y0=-5.455962, r=0.26)
surf243 = openmc.ZCylinder(surface_id=243, x0=-16.8, y0=-6.06218, r=0.26)
surf244 = openmc.ZCylinder(surface_id=244, x0=16.8, y0=-6.06218, r=0.26)
surf245 = openmc.ZCylinder(surface_id=245, x0=-16.45, y0=-6.668398, r=0.26)
surf246 = openmc.ZCylinder(surface_id=246, x0=16.45, y0=-6.668398, r=0.26)
surf247 = openmc.ZCylinder(surface_id=247, x0=-16.1, y0=-7.274616, r=0.26)
surf248 = openmc.ZCylinder(surface_id=248, x0=16.1, y0=-7.274616, r=0.26)
surf249 = openmc.ZCylinder(surface_id=249, x0=-15.75, y0=-7.880834, r=0.26)
surf250 = openmc.ZCylinder(surface_id=250, x0=15.75, y0=-7.880834, r=0.26)
surf251 = openmc.ZCylinder(surface_id=251, x0=-15.4, y0=-8.487052, r=0.26)
surf252 = openmc.ZCylinder(surface_id=252, x0=15.4, y0=-8.487052, r=0.26)
surf253 = openmc.ZCylinder(surface_id=253, x0=-15.05, y0=-9.09327, r=0.26)
surf254 = openmc.ZCylinder(surface_id=254, x0=15.05, y0=-9.09327, r=0.26)
surf255 = openmc.ZCylinder(surface_id=255, x0=-14.7, y0=-9.699488, r=0.26)
surf256 = openmc.ZCylinder(surface_id=256, x0=14.7, y0=-9.699488, r=0.26)
surf257 = openmc.ZCylinder(surface_id=257, x0=-14.35, y0=-10.305706, r=0.26)
surf258 = openmc.ZCylinder(surface_id=258, x0=14.35, y0=-10.305706, r=0.26)
surf259 = openmc.ZCylinder(surface_id=259, x0=-14.0, y0=-10.911924, r=0.26)
surf260 = openmc.ZCylinder(surface_id=260, x0=14.0, y0=-10.911924, r=0.26)
surf261 = openmc.ZCylinder(surface_id=261, x0=-13.65, y0=-11.518142, r=0.26)
surf262 = openmc.ZCylinder(surface_id=262, x0=13.65, y0=-11.518142, r=0.26)
surf263 = openmc.ZCylinder(surface_id=263, x0=-13.3, y0=-12.12436, r=0.26)
surf264 = openmc.ZCylinder(surface_id=264, x0=13.3, y0=-12.12436, r=0.26)
surf265 = openmc.ZCylinder(surface_id=265, x0=-9.1, y0=-15.761668, r=0.26)
surf266 = openmc.ZCylinder(surface_id=266, x0=9.1, y0=-15.761668, r=0.26)
surf267 = openmc.ZCylinder(surface_id=267, x0=-3.15, y0=-17.580322, r=0.26)
surf268 = openmc.ZCylinder(surface_id=268, x0=-2.45, y0=-17.580322, r=0.26)
surf269 = openmc.ZCylinder(surface_id=269, x0=-1.75, y0=-17.580322, r=0.26)
surf270 = openmc.ZCylinder(surface_id=270, x0=-1.05, y0=-17.580322, r=0.26)
surf271 = openmc.ZCylinder(surface_id=271, x0=-0.35, y0=-17.580322, r=0.26)
surf272 = openmc.ZCylinder(surface_id=272, x0=0.35, y0=-17.580322, r=0.26)
surf273 = openmc.ZCylinder(surface_id=273, x0=1.05, y0=-17.580322, r=0.26)
surf274 = openmc.ZCylinder(surface_id=274, x0=1.75, y0=-17.580322, r=0.26)
surf275 = openmc.ZCylinder(surface_id=275, x0=2.45, y0=-17.580322, r=0.26)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1275, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1276, z0=85.6)
surf2_zmin = openmc.ZPlane(surface_id=1277, z0=-0.8)
surf2_zmax = openmc.ZPlane(surface_id=1278, z0=0.0)
surf3_zmin = openmc.ZPlane(surface_id=1279, z0=0.0)
surf3_zmax = openmc.ZPlane(surface_id=1280, z0=85.9)
surf4_zmin = openmc.ZPlane(surface_id=1281, z0=85.9)
surf4_zmax = openmc.ZPlane(surface_id=1282, z0=86.7)
surf5_zmin = openmc.ZPlane(surface_id=1283, z0=-1.0)
surf5_zmax = openmc.ZPlane(surface_id=1284, z0=-0.1)
surf6_zmin = openmc.ZPlane(surface_id=1285, z0=-0.1)
surf6_zmax = openmc.ZPlane(surface_id=1286, z0=87.4)
surf7_zmin = openmc.ZPlane(surface_id=1287, z0=87.4)
surf7_zmax = openmc.ZPlane(surface_id=1288, z0=92.6)
surf8_zmin = openmc.ZPlane(surface_id=1289, z0=-1.0)
surf8_zmax = openmc.ZPlane(surface_id=1290, z0=999.9)
surf11_zmin = openmc.ZPlane(surface_id=1291, z0=-2.2)
surf11_zmax = openmc.ZPlane(surface_id=1292, z0=-1.0)
surf12_zmin = openmc.ZPlane(surface_id=1293, z0=0.5)
surf12_zmax = openmc.ZPlane(surface_id=1294, z0=0.8)
surf13_zmin = openmc.ZPlane(surface_id=1295, z0=81.9)
surf13_zmax = openmc.ZPlane(surface_id=1296, z0=82.2)
surf14_zmin = openmc.ZPlane(surface_id=1297, z0=-19.9, boundary_type="vacuum")
surf14_zmax = openmc.ZPlane(surface_id=1298, z0=105.6, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = (-surf13 & +surf13_zmin & -surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax)
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)
u2_cell2 = openmc.Cell(fill=mat2)
u2_cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)
u2_cell4 = openmc.Cell(fill=mat4)
u2_cell4.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat4)
u4_cell0.region = (-surf8 & +surf8_zmin & -surf8_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf21 & (-surf14 & +surf14_zmin & -surf14_zmax)
u4_cell2 = openmc.Cell(fill=mat4)
u4_cell2.region = -surf22 & (-surf14 & +surf14_zmin & -surf14_zmax)
u4_cell3 = openmc.Cell(fill=mat4)
u4_cell3.region = -surf23 & (-surf14 & +surf14_zmin & -surf14_zmax)
u4_cell4 = openmc.Cell(fill=mat4)
u4_cell4.region = -surf24 & (-surf14 & +surf14_zmin & -surf14_zmax)
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

# Lattice 5: 53x31 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-18.55, -18.792758]
lattice5.pitch = [0.700000, 1.212436]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# Lattice 6: 61x31 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-21.35, -18.792758]
lattice6.pitch = [0.700000, 1.212436]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# array1
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5 & -surf31_6 & -surf31_7 & -surf31_8 & -surf31_9 & -surf31_10 & -surf31_11) & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110

# array2
cell2 = openmc.Cell(cell_id=2, fill=universe6)
cell2.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & +surf201 & +surf202 & +surf203 & +surf204 & +surf205 & +surf206 & +surf207 & +surf208 & +surf209 & +surf210

# FROD
cell3 = openmc.Cell(cell_id=3, fill=universe2)
cell3.translation = (-3.85, 17.580322, 0.0)
cell3.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf201

# FROD
cell4 = openmc.Cell(cell_id=4, fill=universe2)
cell4.translation = (-3.15, 17.580322, 0.0)
cell4.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf202

# FROD
cell5 = openmc.Cell(cell_id=5, fill=universe2)
cell5.translation = (-2.45, 17.580322, 0.0)
cell5.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf203

# FROD
cell6 = openmc.Cell(cell_id=6, fill=universe2)
cell6.translation = (-1.75, 17.580322, 0.0)
cell6.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf204

# FROD
cell7 = openmc.Cell(cell_id=7, fill=universe2)
cell7.translation = (-1.05, 17.580322, 0.0)
cell7.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf205

# FROD
cell8 = openmc.Cell(cell_id=8, fill=universe2)
cell8.translation = (-0.35, 17.580322, 0.0)
cell8.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf206

# FROD
cell9 = openmc.Cell(cell_id=9, fill=universe2)
cell9.translation = (0.35, 17.580322, 0.0)
cell9.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf207

# FROD
cell10 = openmc.Cell(cell_id=10, fill=universe2)
cell10.translation = (1.05, 17.580322, 0.0)
cell10.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf208

# FROD
cell11 = openmc.Cell(cell_id=11, fill=universe2)
cell11.translation = (1.75, 17.580322, 0.0)
cell11.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf209

# FROD
cell12 = openmc.Cell(cell_id=12, fill=universe2)
cell12.translation = (2.45, 17.580322, 0.0)
cell12.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf210

# FROD
cell13 = openmc.Cell(cell_id=13, fill=universe2)
cell13.translation = (3.15, 17.580322, 0.0)
cell13.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf211

# FROD
cell14 = openmc.Cell(cell_id=14, fill=universe2)
cell14.translation = (3.85, 17.580322, 0.0)
cell14.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf212

# FROD
cell15 = openmc.Cell(cell_id=15, fill=universe2)
cell15.translation = (-9.1, 15.761668, 0.0)
cell15.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf213

# FROD
cell16 = openmc.Cell(cell_id=16, fill=universe2)
cell16.translation = (9.1, 15.761668, 0.0)
cell16.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf214

# FROD
cell17 = openmc.Cell(cell_id=17, fill=universe2)
cell17.translation = (-13.3, 12.12436, 0.0)
cell17.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf215

# FROD
cell18 = openmc.Cell(cell_id=18, fill=universe2)
cell18.translation = (13.3, 12.12436, 0.0)
cell18.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf216

# FROD
cell19 = openmc.Cell(cell_id=19, fill=universe2)
cell19.translation = (-13.65, 11.518142, 0.0)
cell19.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf217

# FROD
cell20 = openmc.Cell(cell_id=20, fill=universe2)
cell20.translation = (13.65, 11.518142, 0.0)
cell20.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf218

# FROD
cell21 = openmc.Cell(cell_id=21, fill=universe2)
cell21.translation = (-14.0, 10.911924, 0.0)
cell21.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf219

# FROD
cell22 = openmc.Cell(cell_id=22, fill=universe2)
cell22.translation = (14.0, 10.911924, 0.0)
cell22.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf220

# FROD
cell23 = openmc.Cell(cell_id=23, fill=universe2)
cell23.translation = (-14.35, 10.305706, 0.0)
cell23.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf221

# FROD
cell24 = openmc.Cell(cell_id=24, fill=universe2)
cell24.translation = (14.35, 10.305706, 0.0)
cell24.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf222

# FROD
cell25 = openmc.Cell(cell_id=25, fill=universe2)
cell25.translation = (-14.7, 9.699488, 0.0)
cell25.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf223

# FROD
cell26 = openmc.Cell(cell_id=26, fill=universe2)
cell26.translation = (14.7, 9.699488, 0.0)
cell26.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf224

# FROD
cell27 = openmc.Cell(cell_id=27, fill=universe2)
cell27.translation = (-15.05, 9.09327, 0.0)
cell27.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf225

# FROD
cell28 = openmc.Cell(cell_id=28, fill=universe2)
cell28.translation = (15.05, 9.09327, 0.0)
cell28.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf226

# FROD
cell29 = openmc.Cell(cell_id=29, fill=universe2)
cell29.translation = (-15.4, 8.487052, 0.0)
cell29.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf227

# FROD
cell30 = openmc.Cell(cell_id=30, fill=universe2)
cell30.translation = (15.4, 8.487052, 0.0)
cell30.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf228

# FROD
cell31 = openmc.Cell(cell_id=31, fill=universe2)
cell31.translation = (-15.75, 7.880834, 0.0)
cell31.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf229

# FROD
cell32 = openmc.Cell(cell_id=32, fill=universe2)
cell32.translation = (15.75, 7.880834, 0.0)
cell32.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf230

# FROD
cell33 = openmc.Cell(cell_id=33, fill=universe2)
cell33.translation = (-16.1, 7.274616, 0.0)
cell33.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf231

# FROD
cell34 = openmc.Cell(cell_id=34, fill=universe2)
cell34.translation = (16.1, 7.274616, 0.0)
cell34.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf232

# FROD
cell35 = openmc.Cell(cell_id=35, fill=universe2)
cell35.translation = (-16.45, 6.668398, 0.0)
cell35.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf233

# FROD
cell36 = openmc.Cell(cell_id=36, fill=universe2)
cell36.translation = (16.45, 6.668398, 0.0)
cell36.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf234

# FROD
cell37 = openmc.Cell(cell_id=37, fill=universe2)
cell37.translation = (-16.8, 6.06218, 0.0)
cell37.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf235

# FROD
cell38 = openmc.Cell(cell_id=38, fill=universe2)
cell38.translation = (16.8, 6.06218, 0.0)
cell38.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf236

# FROD
cell39 = openmc.Cell(cell_id=39, fill=universe2)
cell39.translation = (-17.15, 5.455962, 0.0)
cell39.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf237

# FROD
cell40 = openmc.Cell(cell_id=40, fill=universe2)
cell40.translation = (17.15, 5.455962, 0.0)
cell40.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf238

# FROD
cell41 = openmc.Cell(cell_id=41, fill=universe2)
cell41.translation = (-18.2, 0.0, 0.0)
cell41.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf239

# FROD
cell42 = openmc.Cell(cell_id=42, fill=universe2)
cell42.translation = (18.2, 0.0, 0.0)
cell42.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf240

# FROD
cell43 = openmc.Cell(cell_id=43, fill=universe2)
cell43.translation = (-17.15, -5.455962, 0.0)
cell43.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf241

# FROD
cell44 = openmc.Cell(cell_id=44, fill=universe2)
cell44.translation = (17.15, -5.455962, 0.0)
cell44.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf242

# FROD
cell45 = openmc.Cell(cell_id=45, fill=universe2)
cell45.translation = (-16.8, -6.06218, 0.0)
cell45.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf243

# FROD
cell46 = openmc.Cell(cell_id=46, fill=universe2)
cell46.translation = (16.8, -6.06218, 0.0)
cell46.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf244

# FROD
cell47 = openmc.Cell(cell_id=47, fill=universe2)
cell47.translation = (-16.45, -6.668398, 0.0)
cell47.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf245

# FROD
cell48 = openmc.Cell(cell_id=48, fill=universe2)
cell48.translation = (16.45, -6.668398, 0.0)
cell48.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf246

# FROD
cell49 = openmc.Cell(cell_id=49, fill=universe2)
cell49.translation = (-16.1, -7.274616, 0.0)
cell49.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf247

# FROD
cell50 = openmc.Cell(cell_id=50, fill=universe2)
cell50.translation = (16.1, -7.274616, 0.0)
cell50.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf248

# FROD
cell51 = openmc.Cell(cell_id=51, fill=universe2)
cell51.translation = (-15.75, -7.880834, 0.0)
cell51.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf249

# FROD
cell52 = openmc.Cell(cell_id=52, fill=universe2)
cell52.translation = (15.75, -7.880834, 0.0)
cell52.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf250

# FROD
cell53 = openmc.Cell(cell_id=53, fill=universe2)
cell53.translation = (-15.4, -8.487052, 0.0)
cell53.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf251

# FROD
cell54 = openmc.Cell(cell_id=54, fill=universe2)
cell54.translation = (15.4, -8.487052, 0.0)
cell54.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf252

# FROD
cell55 = openmc.Cell(cell_id=55, fill=universe2)
cell55.translation = (-15.05, -9.09327, 0.0)
cell55.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf253

# FROD
cell56 = openmc.Cell(cell_id=56, fill=universe2)
cell56.translation = (15.05, -9.09327, 0.0)
cell56.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf254

# FROD
cell57 = openmc.Cell(cell_id=57, fill=universe2)
cell57.translation = (-14.7, -9.699488, 0.0)
cell57.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf255

# FROD
cell58 = openmc.Cell(cell_id=58, fill=universe2)
cell58.translation = (14.7, -9.699488, 0.0)
cell58.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf256

# FROD
cell59 = openmc.Cell(cell_id=59, fill=universe2)
cell59.translation = (-14.35, -10.305706, 0.0)
cell59.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf257

# FROD
cell60 = openmc.Cell(cell_id=60, fill=universe2)
cell60.translation = (14.35, -10.305706, 0.0)
cell60.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf258

# FROD
cell61 = openmc.Cell(cell_id=61, fill=universe2)
cell61.translation = (-14.0, -10.911924, 0.0)
cell61.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf259

# FROD
cell62 = openmc.Cell(cell_id=62, fill=universe2)
cell62.translation = (14.0, -10.911924, 0.0)
cell62.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf260

# FROD
cell63 = openmc.Cell(cell_id=63, fill=universe2)
cell63.translation = (-13.65, -11.518142, 0.0)
cell63.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf261

# FROD
cell64 = openmc.Cell(cell_id=64, fill=universe2)
cell64.translation = (13.65, -11.518142, 0.0)
cell64.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf262

# FROD
cell65 = openmc.Cell(cell_id=65, fill=universe2)
cell65.translation = (-13.3, -12.12436, 0.0)
cell65.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf263

# FROD
cell66 = openmc.Cell(cell_id=66, fill=universe2)
cell66.translation = (13.3, -12.12436, 0.0)
cell66.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf264

# FROD
cell67 = openmc.Cell(cell_id=67, fill=universe2)
cell67.translation = (-9.1, -15.761668, 0.0)
cell67.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf265

# FROD
cell68 = openmc.Cell(cell_id=68, fill=universe2)
cell68.translation = (9.1, -15.761668, 0.0)
cell68.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf266

# FROD
cell69 = openmc.Cell(cell_id=69, fill=universe2)
cell69.translation = (-3.15, -17.580322, 0.0)
cell69.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf267

# FROD
cell70 = openmc.Cell(cell_id=70, fill=universe2)
cell70.translation = (-2.45, -17.580322, 0.0)
cell70.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf268

# FROD
cell71 = openmc.Cell(cell_id=71, fill=universe2)
cell71.translation = (-1.75, -17.580322, 0.0)
cell71.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf269

# FROD
cell72 = openmc.Cell(cell_id=72, fill=universe2)
cell72.translation = (-1.05, -17.580322, 0.0)
cell72.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf270

# FROD
cell73 = openmc.Cell(cell_id=73, fill=universe2)
cell73.translation = (-0.35, -17.580322, 0.0)
cell73.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf271

# FROD
cell74 = openmc.Cell(cell_id=74, fill=universe2)
cell74.translation = (0.35, -17.580322, 0.0)
cell74.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf272

# FROD
cell75 = openmc.Cell(cell_id=75, fill=universe2)
cell75.translation = (1.05, -17.580322, 0.0)
cell75.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf273

# FROD
cell76 = openmc.Cell(cell_id=76, fill=universe2)
cell76.translation = (1.75, -17.580322, 0.0)
cell76.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf274

# FROD
cell77 = openmc.Cell(cell_id=77, fill=universe2)
cell77.translation = (2.45, -17.580322, 0.0)
cell77.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf275

# D16
cell78 = openmc.Cell(cell_id=78, fill=mat3)
cell78.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5)

# water
cell79 = openmc.Cell(cell_id=79, fill=mat4)
cell79.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5)

# H2O
cell84 = openmc.Cell(cell_id=84, fill=mat4)
cell84.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)

# Water
cell90 = openmc.Cell(cell_id=90, fill=mat4)
cell90.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# ALLES
cell91 = openmc.Cell(cell_id=91, fill=universe1)
cell91.region = (+surf8 | -surf8_zmin | +surf8_zmax) & +surf21 & +surf22 & +surf23 & +surf24 & (-surf14 & +surf14_zmin & -surf14_zmax)

# ALLES
cell97 = openmc.Cell(cell_id=97, fill=universe1)
cell97.region = (+surf8 | -surf8_zmin | +surf8_zmax) & +surf21 & +surf22 & +surf23 & +surf24 & (-surf14 & +surf14_zmin & -surf14_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49, cell50, cell51, cell52, cell53, cell54, cell55, cell56, cell57, cell58, cell59, cell60, cell61, cell62, cell63, cell64, cell65, cell66, cell67, cell68, cell69, cell70, cell71, cell72, cell73, cell74, cell75, cell76, cell77, cell78, cell79, cell84, cell90, cell91, cell97])
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
source.space = openmc.stats.Point((0.0, 0.0, 42.8))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
