"""
U233-COMP-THERM-001-7: SB-6
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Water at 20C
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 6.673500e-02)
mat1.add_nuclide("O16", 3.336800e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Borated SST
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.925900e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Mn", 8.681600e-04)
mat2.add_element("Ni", 7.517100e-03)
mat2.add_nuclide("B10", 3.748800e-03)

# 233UO2-ZrO2 Seed
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U233", 3.989100e-03)
mat3.add_nuclide("U234", 6.369000e-05)
mat3.add_nuclide("U238", 4.575900e-05)
mat3.add_nuclide("O16", 5.393200e-02)
mat3.add_element("Zr", 2.286700e-02)

# Zircalloy-2
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Zr", 4.253700e-02)
mat4.add_element("Sn", 4.991800e-04)

# ThO2 Blanket with Gd
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Th", 2.164100e-02)
mat5.add_nuclide("O16", 4.328200e-02)
mat5.add_element("Gd", 9.260700e-08)

# Polyethylene
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 7.885400e-02)
mat6.add_element("C", 3.942700e-02)
mat6.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Water/OR
surf1 = openmc.ZCylinder(surface_id=1, r=91.44, boundary_type="vacuum")
# Z-Lo = -200/2 + 115.765 = 15.765 cm
surf2 = openmc.model.RectangularParallelepiped(-3.81, 3.81, -5.605779999999999, -5.42798, 15.765, 215.765)
surf3 = openmc.model.RectangularParallelepiped(-3.81, 3.81, -1.92786, -1.75006, 15.765, 215.765)
surf4 = openmc.model.RectangularParallelepiped(-3.81, 3.81, 1.75006, 1.92786, 15.765, 215.765)
surf5 = openmc.model.RectangularParallelepiped(-3.81, 3.81, 5.42798, 5.605779999999999, 15.765, 215.765)
# Really big (dummy) box
surf9 = openmc.model.RectangularParallelepiped(-500.0, 500.0, -500.0, 500.0, -500.0, 500.0)
# Fuel/OR
surf10 = openmc.ZCylinder(surface_id=10, r=0.26797)
# Clad/IR
surf11 = openmc.ZCylinder(surface_id=11, r=0.2794)
# Clad/OR
surf12 = openmc.ZCylinder(surface_id=12, r=0.32385)
# Fuel/Lower
surf13 = openmc.ZPlane(surface_id=13, z0=-19.05)
# Fuel/Upper
surf14 = openmc.ZPlane(surface_id=14, z0=19.05)
# Poly/Lower
surf15 = openmc.ZPlane(surface_id=15, z0=-0.3175)
# Poly/Upper
surf16 = openmc.ZPlane(surface_id=16, z0=0.3175)
# Poly/OR
surf17 = openmc.ZCylinder(surface_id=17, x0=0.0, y0=0.0, r=0.72517)
# Fuel/OR
surf21 = openmc.ZCylinder(surface_id=21, r=0.62103)
# Clad/IR
surf22 = openmc.ZCylinder(surface_id=22, r=0.63373)
# Clad/OR
surf23 = openmc.ZCylinder(surface_id=23, r=0.7239)
# Prism 100: 6-sided polygon
surf100_0 = openmc.Plane(a=-0.8660253979, b=-0.5000000102, c=0, d=10.0482502047)
surf100_1 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=10.0482500000)
surf100_2 = openmc.Plane(a=0.8660253979, b=-0.5000000102, c=0, d=10.0482502047)
surf100_3 = openmc.Plane(a=0.8660253979, b=0.5000000102, c=0, d=10.0482502047)
surf100_4 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=10.0482500000)
surf100_5 = openmc.Plane(a=-0.8660253979, b=0.5000000102, c=0, d=10.0482502047)
surf101 = openmc.ZCylinder(surface_id=101, x0=-5.80136, y0=10.04825, r=0.72517)
surf102 = openmc.ZCylinder(surface_id=102, x0=-4.35102, y0=10.04825, r=0.72517)
surf103 = openmc.ZCylinder(surface_id=103, x0=-2.90068, y0=10.04825, r=0.72517)
surf104 = openmc.ZCylinder(surface_id=104, x0=-1.45034, y0=10.04825, r=0.72517)
surf105 = openmc.ZCylinder(surface_id=105, x0=0.0, y0=10.04825, r=0.72517)
surf106 = openmc.ZCylinder(surface_id=106, x0=1.45034, y0=10.04825, r=0.72517)
surf107 = openmc.ZCylinder(surface_id=107, x0=2.90068, y0=10.04825, r=0.72517)
surf108 = openmc.ZCylinder(surface_id=108, x0=4.35102, y0=10.04825, r=0.72517)
surf109 = openmc.ZCylinder(surface_id=109, x0=5.80136, y0=10.04825, r=0.72517)
surf110 = openmc.ZCylinder(surface_id=110, x0=-6.52653, y0=8.79222, r=0.72517)
surf111 = openmc.ZCylinder(surface_id=111, x0=-5.07619, y0=8.79222, r=0.72517)
surf112 = openmc.ZCylinder(surface_id=112, x0=-3.62585, y0=8.79222, r=0.72517)
surf113 = openmc.ZCylinder(surface_id=113, x0=-2.17551, y0=8.79222, r=0.72517)
surf114 = openmc.ZCylinder(surface_id=114, x0=-0.72517, y0=8.79222, r=0.72517)
surf115 = openmc.ZCylinder(surface_id=115, x0=0.72517, y0=8.79222, r=0.72517)
surf116 = openmc.ZCylinder(surface_id=116, x0=2.17551, y0=8.79222, r=0.72517)
surf117 = openmc.ZCylinder(surface_id=117, x0=3.62585, y0=8.79222, r=0.72517)
surf118 = openmc.ZCylinder(surface_id=118, x0=5.07619, y0=8.79222, r=0.72517)
surf119 = openmc.ZCylinder(surface_id=119, x0=6.52653, y0=8.79222, r=0.72517)
surf120 = openmc.ZCylinder(surface_id=120, x0=-7.2517, y0=7.53619, r=0.72517)
surf121 = openmc.ZCylinder(surface_id=121, x0=-5.80136, y0=7.53619, r=0.72517)
surf122 = openmc.ZCylinder(surface_id=122, x0=-4.35102, y0=7.53619, r=0.72517)
surf123 = openmc.ZCylinder(surface_id=123, x0=-2.90068, y0=7.53619, r=0.72517)
surf124 = openmc.ZCylinder(surface_id=124, x0=-1.45034, y0=7.53619, r=0.72517)
surf125 = openmc.ZCylinder(surface_id=125, x0=0.0, y0=7.53619, r=0.72517)
surf126 = openmc.ZCylinder(surface_id=126, x0=1.45034, y0=7.53619, r=0.72517)
surf127 = openmc.ZCylinder(surface_id=127, x0=2.90068, y0=7.53619, r=0.72517)
surf128 = openmc.ZCylinder(surface_id=128, x0=4.35102, y0=7.53619, r=0.72517)
surf129 = openmc.ZCylinder(surface_id=129, x0=5.80136, y0=7.53619, r=0.72517)
surf130 = openmc.ZCylinder(surface_id=130, x0=7.2517, y0=7.53619, r=0.72517)
surf131 = openmc.ZCylinder(surface_id=131, x0=-7.97687, y0=6.28016, r=0.72517)
surf132 = openmc.ZCylinder(surface_id=132, x0=-6.52653, y0=6.28016, r=0.72517)
surf133 = openmc.ZCylinder(surface_id=133, x0=-5.07619, y0=6.28016, r=0.72517)
surf134 = openmc.ZCylinder(surface_id=134, x0=-3.62585, y0=6.28016, r=0.72517)
surf135 = openmc.ZCylinder(surface_id=135, x0=-2.17551, y0=6.28016, r=0.72517)
surf136 = openmc.ZCylinder(surface_id=136, x0=-0.72517, y0=6.28016, r=0.72517)
surf137 = openmc.ZCylinder(surface_id=137, x0=0.72517, y0=6.28016, r=0.72517)
surf138 = openmc.ZCylinder(surface_id=138, x0=2.17551, y0=6.28016, r=0.72517)
surf139 = openmc.ZCylinder(surface_id=139, x0=3.62585, y0=6.28016, r=0.72517)
surf140 = openmc.ZCylinder(surface_id=140, x0=5.07619, y0=6.28016, r=0.72517)
surf141 = openmc.ZCylinder(surface_id=141, x0=6.52653, y0=6.28016, r=0.72517)
surf142 = openmc.ZCylinder(surface_id=142, x0=7.97687, y0=6.28016, r=0.72517)
surf143 = openmc.ZCylinder(surface_id=143, x0=-8.70204, y0=5.02413, r=0.72517)
surf144 = openmc.ZCylinder(surface_id=144, x0=-7.2517, y0=5.02413, r=0.72517)
surf145 = openmc.ZCylinder(surface_id=145, x0=-5.80136, y0=5.02413, r=0.72517)
surf146 = openmc.ZCylinder(surface_id=146, x0=-4.35102, y0=5.02413, r=0.72517)
surf147 = openmc.ZCylinder(surface_id=147, x0=-2.90068, y0=5.02413, r=0.72517)
surf148 = openmc.ZCylinder(surface_id=148, x0=-1.45034, y0=5.02413, r=0.72517)
surf149 = openmc.ZCylinder(surface_id=149, x0=0.0, y0=5.02413, r=0.72517)
surf150 = openmc.ZCylinder(surface_id=150, x0=1.45034, y0=5.02413, r=0.72517)
surf151 = openmc.ZCylinder(surface_id=151, x0=2.90068, y0=5.02413, r=0.72517)
surf152 = openmc.ZCylinder(surface_id=152, x0=4.35102, y0=5.02413, r=0.72517)
surf153 = openmc.ZCylinder(surface_id=153, x0=5.80136, y0=5.02413, r=0.72517)
surf154 = openmc.ZCylinder(surface_id=154, x0=7.2517, y0=5.02413, r=0.72517)
surf155 = openmc.ZCylinder(surface_id=155, x0=8.70204, y0=5.02413, r=0.72517)
surf156 = openmc.ZCylinder(surface_id=156, x0=-9.42721, y0=3.76809, r=0.72517)
surf157 = openmc.ZCylinder(surface_id=157, x0=-7.97687, y0=3.76809, r=0.72517)
surf158 = openmc.ZCylinder(surface_id=158, x0=-6.52653, y0=3.76809, r=0.72517)
surf159 = openmc.ZCylinder(surface_id=159, x0=-5.07619, y0=3.76809, r=0.72517)
surf160 = openmc.ZCylinder(surface_id=160, x0=-3.62585, y0=3.76809, r=0.72517)
surf161 = openmc.ZCylinder(surface_id=161, x0=-2.17551, y0=3.76809, r=0.72517)
surf162 = openmc.ZCylinder(surface_id=162, x0=-0.72517, y0=3.76809, r=0.72517)
surf163 = openmc.ZCylinder(surface_id=163, x0=0.72517, y0=3.76809, r=0.72517)
surf164 = openmc.ZCylinder(surface_id=164, x0=2.17551, y0=3.76809, r=0.72517)
surf165 = openmc.ZCylinder(surface_id=165, x0=3.62585, y0=3.76809, r=0.72517)
surf166 = openmc.ZCylinder(surface_id=166, x0=5.07619, y0=3.76809, r=0.72517)
surf167 = openmc.ZCylinder(surface_id=167, x0=6.52653, y0=3.76809, r=0.72517)
surf168 = openmc.ZCylinder(surface_id=168, x0=7.97687, y0=3.76809, r=0.72517)
surf169 = openmc.ZCylinder(surface_id=169, x0=9.42721, y0=3.76809, r=0.72517)
surf170 = openmc.ZCylinder(surface_id=170, x0=-10.15238, y0=2.51206, r=0.72517)
surf171 = openmc.ZCylinder(surface_id=171, x0=-8.70204, y0=2.51206, r=0.72517)
surf172 = openmc.ZCylinder(surface_id=172, x0=-7.2517, y0=2.51206, r=0.72517)
surf173 = openmc.ZCylinder(surface_id=173, x0=-5.80136, y0=2.51206, r=0.72517)
surf174 = openmc.ZCylinder(surface_id=174, x0=-4.35102, y0=2.51206, r=0.72517)
surf175 = openmc.ZCylinder(surface_id=175, x0=-2.90068, y0=2.51206, r=0.72517)
surf176 = openmc.ZCylinder(surface_id=176, x0=-1.45034, y0=2.51206, r=0.72517)
surf177 = openmc.ZCylinder(surface_id=177, x0=0.0, y0=2.51206, r=0.72517)
surf178 = openmc.ZCylinder(surface_id=178, x0=1.45034, y0=2.51206, r=0.72517)
surf179 = openmc.ZCylinder(surface_id=179, x0=2.90068, y0=2.51206, r=0.72517)
surf180 = openmc.ZCylinder(surface_id=180, x0=4.35102, y0=2.51206, r=0.72517)
surf181 = openmc.ZCylinder(surface_id=181, x0=5.80136, y0=2.51206, r=0.72517)
surf182 = openmc.ZCylinder(surface_id=182, x0=7.2517, y0=2.51206, r=0.72517)
surf183 = openmc.ZCylinder(surface_id=183, x0=8.70204, y0=2.51206, r=0.72517)
surf184 = openmc.ZCylinder(surface_id=184, x0=10.15238, y0=2.51206, r=0.72517)
surf185 = openmc.ZCylinder(surface_id=185, x0=-10.87755, y0=1.25603, r=0.72517)
surf186 = openmc.ZCylinder(surface_id=186, x0=-9.42721, y0=1.25603, r=0.72517)
surf187 = openmc.ZCylinder(surface_id=187, x0=-7.97687, y0=1.25603, r=0.72517)
surf188 = openmc.ZCylinder(surface_id=188, x0=-6.52653, y0=1.25603, r=0.72517)
surf189 = openmc.ZCylinder(surface_id=189, x0=-5.07619, y0=1.25603, r=0.72517)
surf190 = openmc.ZCylinder(surface_id=190, x0=-3.62585, y0=1.25603, r=0.72517)
surf191 = openmc.ZCylinder(surface_id=191, x0=-2.17551, y0=1.25603, r=0.72517)
surf192 = openmc.ZCylinder(surface_id=192, x0=-0.72517, y0=1.25603, r=0.72517)
surf193 = openmc.ZCylinder(surface_id=193, x0=0.72517, y0=1.25603, r=0.72517)
surf194 = openmc.ZCylinder(surface_id=194, x0=2.17551, y0=1.25603, r=0.72517)
surf195 = openmc.ZCylinder(surface_id=195, x0=3.62585, y0=1.25603, r=0.72517)
surf196 = openmc.ZCylinder(surface_id=196, x0=5.07619, y0=1.25603, r=0.72517)
surf197 = openmc.ZCylinder(surface_id=197, x0=6.52653, y0=1.25603, r=0.72517)
surf198 = openmc.ZCylinder(surface_id=198, x0=7.97687, y0=1.25603, r=0.72517)
surf199 = openmc.ZCylinder(surface_id=199, x0=9.42721, y0=1.25603, r=0.72517)
surf200 = openmc.ZCylinder(surface_id=200, x0=10.87755, y0=1.25603, r=0.72517)
surf201 = openmc.ZCylinder(surface_id=201, x0=-11.60272, y0=0.0, r=0.72517)
surf202 = openmc.ZCylinder(surface_id=202, x0=-10.15238, y0=0.0, r=0.72517)
surf203 = openmc.ZCylinder(surface_id=203, x0=-8.70204, y0=0.0, r=0.72517)
surf204 = openmc.ZCylinder(surface_id=204, x0=-7.2517, y0=0.0, r=0.72517)
surf205 = openmc.ZCylinder(surface_id=205, x0=-5.80136, y0=0.0, r=0.72517)
surf206 = openmc.ZCylinder(surface_id=206, x0=-4.35102, y0=0.0, r=0.72517)
surf207 = openmc.ZCylinder(surface_id=207, x0=-2.90068, y0=0.0, r=0.72517)
surf208 = openmc.ZCylinder(surface_id=208, x0=-1.45034, y0=0.0, r=0.72517)
surf209 = openmc.ZCylinder(surface_id=209, x0=0.0, y0=0.0, r=0.72517)
surf210 = openmc.ZCylinder(surface_id=210, x0=1.45034, y0=0.0, r=0.72517)
surf211 = openmc.ZCylinder(surface_id=211, x0=2.90068, y0=0.0, r=0.72517)
surf212 = openmc.ZCylinder(surface_id=212, x0=4.35102, y0=0.0, r=0.72517)
surf213 = openmc.ZCylinder(surface_id=213, x0=5.80136, y0=0.0, r=0.72517)
surf214 = openmc.ZCylinder(surface_id=214, x0=7.2517, y0=0.0, r=0.72517)
surf215 = openmc.ZCylinder(surface_id=215, x0=8.70204, y0=0.0, r=0.72517)
surf216 = openmc.ZCylinder(surface_id=216, x0=10.15238, y0=0.0, r=0.72517)
surf217 = openmc.ZCylinder(surface_id=217, x0=11.60272, y0=0.0, r=0.72517)
surf218 = openmc.ZCylinder(surface_id=218, x0=-10.87755, y0=-1.25603, r=0.72517)
surf219 = openmc.ZCylinder(surface_id=219, x0=-9.42721, y0=-1.25603, r=0.72517)
surf220 = openmc.ZCylinder(surface_id=220, x0=-7.97687, y0=-1.25603, r=0.72517)
surf221 = openmc.ZCylinder(surface_id=221, x0=-6.52653, y0=-1.25603, r=0.72517)
surf222 = openmc.ZCylinder(surface_id=222, x0=-5.07619, y0=-1.25603, r=0.72517)
surf223 = openmc.ZCylinder(surface_id=223, x0=-3.62585, y0=-1.25603, r=0.72517)
surf224 = openmc.ZCylinder(surface_id=224, x0=-2.17551, y0=-1.25603, r=0.72517)
surf225 = openmc.ZCylinder(surface_id=225, x0=-0.72517, y0=-1.25603, r=0.72517)
surf226 = openmc.ZCylinder(surface_id=226, x0=0.72517, y0=-1.25603, r=0.72517)
surf227 = openmc.ZCylinder(surface_id=227, x0=2.17551, y0=-1.25603, r=0.72517)
surf228 = openmc.ZCylinder(surface_id=228, x0=3.62585, y0=-1.25603, r=0.72517)
surf229 = openmc.ZCylinder(surface_id=229, x0=5.07619, y0=-1.25603, r=0.72517)
surf230 = openmc.ZCylinder(surface_id=230, x0=6.52653, y0=-1.25603, r=0.72517)
surf231 = openmc.ZCylinder(surface_id=231, x0=7.97687, y0=-1.25603, r=0.72517)
surf232 = openmc.ZCylinder(surface_id=232, x0=9.42721, y0=-1.25603, r=0.72517)
surf233 = openmc.ZCylinder(surface_id=233, x0=10.87755, y0=-1.25603, r=0.72517)
surf234 = openmc.ZCylinder(surface_id=234, x0=-10.15238, y0=-2.51206, r=0.72517)
surf235 = openmc.ZCylinder(surface_id=235, x0=-8.70204, y0=-2.51206, r=0.72517)
surf236 = openmc.ZCylinder(surface_id=236, x0=-7.2517, y0=-2.51206, r=0.72517)
surf237 = openmc.ZCylinder(surface_id=237, x0=-5.80136, y0=-2.51206, r=0.72517)
surf238 = openmc.ZCylinder(surface_id=238, x0=-4.35102, y0=-2.51206, r=0.72517)
surf239 = openmc.ZCylinder(surface_id=239, x0=-2.90068, y0=-2.51206, r=0.72517)
surf240 = openmc.ZCylinder(surface_id=240, x0=-1.45034, y0=-2.51206, r=0.72517)
surf241 = openmc.ZCylinder(surface_id=241, x0=0.0, y0=-2.51206, r=0.72517)
surf242 = openmc.ZCylinder(surface_id=242, x0=1.45034, y0=-2.51206, r=0.72517)
surf243 = openmc.ZCylinder(surface_id=243, x0=2.90068, y0=-2.51206, r=0.72517)
surf244 = openmc.ZCylinder(surface_id=244, x0=4.35102, y0=-2.51206, r=0.72517)
surf245 = openmc.ZCylinder(surface_id=245, x0=5.80136, y0=-2.51206, r=0.72517)
surf246 = openmc.ZCylinder(surface_id=246, x0=7.2517, y0=-2.51206, r=0.72517)
surf247 = openmc.ZCylinder(surface_id=247, x0=8.70204, y0=-2.51206, r=0.72517)
surf248 = openmc.ZCylinder(surface_id=248, x0=10.15238, y0=-2.51206, r=0.72517)
surf249 = openmc.ZCylinder(surface_id=249, x0=-9.42721, y0=-3.76809, r=0.72517)
surf250 = openmc.ZCylinder(surface_id=250, x0=-7.97687, y0=-3.76809, r=0.72517)
surf251 = openmc.ZCylinder(surface_id=251, x0=-6.52653, y0=-3.76809, r=0.72517)
surf252 = openmc.ZCylinder(surface_id=252, x0=-5.07619, y0=-3.76809, r=0.72517)
surf253 = openmc.ZCylinder(surface_id=253, x0=-3.62585, y0=-3.76809, r=0.72517)
surf254 = openmc.ZCylinder(surface_id=254, x0=-2.17551, y0=-3.76809, r=0.72517)
surf255 = openmc.ZCylinder(surface_id=255, x0=-0.72517, y0=-3.76809, r=0.72517)
surf256 = openmc.ZCylinder(surface_id=256, x0=0.72517, y0=-3.76809, r=0.72517)
surf257 = openmc.ZCylinder(surface_id=257, x0=2.17551, y0=-3.76809, r=0.72517)
surf258 = openmc.ZCylinder(surface_id=258, x0=3.62585, y0=-3.76809, r=0.72517)
surf259 = openmc.ZCylinder(surface_id=259, x0=5.07619, y0=-3.76809, r=0.72517)
surf260 = openmc.ZCylinder(surface_id=260, x0=6.52653, y0=-3.76809, r=0.72517)
surf261 = openmc.ZCylinder(surface_id=261, x0=7.97687, y0=-3.76809, r=0.72517)
surf262 = openmc.ZCylinder(surface_id=262, x0=9.42721, y0=-3.76809, r=0.72517)
surf263 = openmc.ZCylinder(surface_id=263, x0=-8.70204, y0=-5.02413, r=0.72517)
surf264 = openmc.ZCylinder(surface_id=264, x0=-7.2517, y0=-5.02413, r=0.72517)
surf265 = openmc.ZCylinder(surface_id=265, x0=-5.80136, y0=-5.02413, r=0.72517)
surf266 = openmc.ZCylinder(surface_id=266, x0=-4.35102, y0=-5.02413, r=0.72517)
surf267 = openmc.ZCylinder(surface_id=267, x0=-2.90068, y0=-5.02413, r=0.72517)
surf268 = openmc.ZCylinder(surface_id=268, x0=-1.45034, y0=-5.02413, r=0.72517)
surf269 = openmc.ZCylinder(surface_id=269, x0=0.0, y0=-5.02413, r=0.72517)
surf270 = openmc.ZCylinder(surface_id=270, x0=1.45034, y0=-5.02413, r=0.72517)
surf271 = openmc.ZCylinder(surface_id=271, x0=2.90068, y0=-5.02413, r=0.72517)
surf272 = openmc.ZCylinder(surface_id=272, x0=4.35102, y0=-5.02413, r=0.72517)
surf273 = openmc.ZCylinder(surface_id=273, x0=5.80136, y0=-5.02413, r=0.72517)
surf274 = openmc.ZCylinder(surface_id=274, x0=7.2517, y0=-5.02413, r=0.72517)
surf275 = openmc.ZCylinder(surface_id=275, x0=8.70204, y0=-5.02413, r=0.72517)
surf276 = openmc.ZCylinder(surface_id=276, x0=-7.97687, y0=-6.28016, r=0.72517)
surf277 = openmc.ZCylinder(surface_id=277, x0=-6.52653, y0=-6.28016, r=0.72517)
surf278 = openmc.ZCylinder(surface_id=278, x0=-5.07619, y0=-6.28016, r=0.72517)
surf279 = openmc.ZCylinder(surface_id=279, x0=-3.62585, y0=-6.28016, r=0.72517)
surf280 = openmc.ZCylinder(surface_id=280, x0=-2.17551, y0=-6.28016, r=0.72517)
surf281 = openmc.ZCylinder(surface_id=281, x0=-0.72517, y0=-6.28016, r=0.72517)
surf282 = openmc.ZCylinder(surface_id=282, x0=0.72517, y0=-6.28016, r=0.72517)
surf283 = openmc.ZCylinder(surface_id=283, x0=2.17551, y0=-6.28016, r=0.72517)
surf284 = openmc.ZCylinder(surface_id=284, x0=3.62585, y0=-6.28016, r=0.72517)
surf285 = openmc.ZCylinder(surface_id=285, x0=5.07619, y0=-6.28016, r=0.72517)
surf286 = openmc.ZCylinder(surface_id=286, x0=6.52653, y0=-6.28016, r=0.72517)
surf287 = openmc.ZCylinder(surface_id=287, x0=7.97687, y0=-6.28016, r=0.72517)
surf288 = openmc.ZCylinder(surface_id=288, x0=-7.2517, y0=-7.53619, r=0.72517)
surf289 = openmc.ZCylinder(surface_id=289, x0=-5.80136, y0=-7.53619, r=0.72517)
surf290 = openmc.ZCylinder(surface_id=290, x0=-4.35102, y0=-7.53619, r=0.72517)
surf291 = openmc.ZCylinder(surface_id=291, x0=-2.90068, y0=-7.53619, r=0.72517)
surf292 = openmc.ZCylinder(surface_id=292, x0=-1.45034, y0=-7.53619, r=0.72517)
surf293 = openmc.ZCylinder(surface_id=293, x0=0.0, y0=-7.53619, r=0.72517)
surf294 = openmc.ZCylinder(surface_id=294, x0=1.45034, y0=-7.53619, r=0.72517)
surf295 = openmc.ZCylinder(surface_id=295, x0=2.90068, y0=-7.53619, r=0.72517)
surf296 = openmc.ZCylinder(surface_id=296, x0=4.35102, y0=-7.53619, r=0.72517)
surf297 = openmc.ZCylinder(surface_id=297, x0=5.80136, y0=-7.53619, r=0.72517)
surf298 = openmc.ZCylinder(surface_id=298, x0=7.2517, y0=-7.53619, r=0.72517)
surf299 = openmc.ZCylinder(surface_id=299, x0=-6.52653, y0=-8.79222, r=0.72517)
surf300 = openmc.ZCylinder(surface_id=300, x0=-5.07619, y0=-8.79222, r=0.72517)
surf301 = openmc.ZCylinder(surface_id=301, x0=-3.62585, y0=-8.79222, r=0.72517)
surf302 = openmc.ZCylinder(surface_id=302, x0=-2.17551, y0=-8.79222, r=0.72517)
surf303 = openmc.ZCylinder(surface_id=303, x0=-0.72517, y0=-8.79222, r=0.72517)
surf304 = openmc.ZCylinder(surface_id=304, x0=0.72517, y0=-8.79222, r=0.72517)
surf305 = openmc.ZCylinder(surface_id=305, x0=2.17551, y0=-8.79222, r=0.72517)
surf306 = openmc.ZCylinder(surface_id=306, x0=3.62585, y0=-8.79222, r=0.72517)
surf307 = openmc.ZCylinder(surface_id=307, x0=5.07619, y0=-8.79222, r=0.72517)
surf308 = openmc.ZCylinder(surface_id=308, x0=6.52653, y0=-8.79222, r=0.72517)
surf309 = openmc.ZCylinder(surface_id=309, x0=-5.80136, y0=-10.04825, r=0.72517)
surf310 = openmc.ZCylinder(surface_id=310, x0=-4.35102, y0=-10.04825, r=0.72517)
surf311 = openmc.ZCylinder(surface_id=311, x0=-2.90068, y0=-10.04825, r=0.72517)
surf312 = openmc.ZCylinder(surface_id=312, x0=-1.45034, y0=-10.04825, r=0.72517)
surf313 = openmc.ZCylinder(surface_id=313, x0=0.0, y0=-10.04825, r=0.72517)
surf314 = openmc.ZCylinder(surface_id=314, x0=1.45034, y0=-10.04825, r=0.72517)
surf315 = openmc.ZCylinder(surface_id=315, x0=2.90068, y0=-10.04825, r=0.72517)
surf316 = openmc.ZCylinder(surface_id=316, x0=4.35102, y0=-10.04825, r=0.72517)
surf317 = openmc.ZCylinder(surface_id=317, x0=5.80136, y0=-10.04825, r=0.72517)
surf399 = openmc.YPlane(surface_id=399, y0=0.0)
surf400 = openmc.XPlane(surface_id=400, x0=0.0)
surf401 = openmc.YPlane(surface_id=401, y0=1.25603)
surf402 = openmc.YPlane(surface_id=402, y0=2.51206)
surf403 = openmc.YPlane(surface_id=403, y0=3.76809)
surf404 = openmc.YPlane(surface_id=404, y0=5.02413)
surf405 = openmc.YPlane(surface_id=405, y0=6.28016)
surf406 = openmc.YPlane(surface_id=406, y0=7.53619)
surf407 = openmc.YPlane(surface_id=407, y0=8.79222)
surf408 = openmc.YPlane(surface_id=408, y0=10.04825)
surf409 = openmc.YPlane(surface_id=409, y0=11.30428)
surf410 = openmc.YPlane(surface_id=410, y0=12.56031)
surf411 = openmc.YPlane(surface_id=411, y0=13.81634)
surf412 = openmc.YPlane(surface_id=412, y0=15.07238)
surf413 = openmc.YPlane(surface_id=413, y0=16.32841)
surf414 = openmc.YPlane(surface_id=414, y0=17.58444)
surf415 = openmc.YPlane(surface_id=415, y0=18.84047)
surf416 = openmc.YPlane(surface_id=416, y0=20.09650)
surf417 = openmc.YPlane(surface_id=417, y0=21.35253)
surf418 = openmc.YPlane(surface_id=418, y0=22.60856)
surf419 = openmc.YPlane(surface_id=419, y0=23.86459)
surf420 = openmc.YPlane(surface_id=420, y0=25.12063)
surf1201 = openmc.ZCylinder(surface_id=1201, x0=12.32789, y0=1.25603, r=0.72517)
surf1202 = openmc.ZCylinder(surface_id=1202, x0=13.77823, y0=1.25603, r=0.72517)
surf1203 = openmc.ZCylinder(surface_id=1203, x0=15.22857, y0=1.25603, r=0.72517)
surf1204 = openmc.ZCylinder(surface_id=1204, x0=16.67891, y0=1.25603, r=0.72517)
surf1205 = openmc.ZCylinder(surface_id=1205, x0=18.12925, y0=1.25603, r=0.72517)
surf1206 = openmc.ZCylinder(surface_id=1206, x0=19.57959, y0=1.25603, r=0.72517)
surf1207 = openmc.ZCylinder(surface_id=1207, x0=21.02993, y0=1.25603, r=0.72517)
surf1208 = openmc.ZCylinder(surface_id=1208, x0=22.48027, y0=1.25603, r=0.72517)
surf1209 = openmc.ZCylinder(surface_id=1209, x0=23.93061, y0=1.25603, r=0.72517)
surf1210 = openmc.ZCylinder(surface_id=1210, x0=25.38095, y0=1.25603, r=0.72517)
surf1211 = openmc.ZCylinder(surface_id=1211, x0=26.83129, y0=1.25603, r=0.72517)
surf1212 = openmc.ZCylinder(surface_id=1212, x0=28.28163, y0=1.25603, r=0.72517)
surf1218 = openmc.ZCylinder(surface_id=1218, x0=13.05306, y0=0.0, r=0.72517)
surf1219 = openmc.ZCylinder(surface_id=1219, x0=14.5034, y0=0.0, r=0.72517)
surf1220 = openmc.ZCylinder(surface_id=1220, x0=15.95374, y0=0.0, r=0.72517)
surf1221 = openmc.ZCylinder(surface_id=1221, x0=17.40408, y0=0.0, r=0.72517)
surf1222 = openmc.ZCylinder(surface_id=1222, x0=18.85442, y0=0.0, r=0.72517)
surf1223 = openmc.ZCylinder(surface_id=1223, x0=20.30476, y0=0.0, r=0.72517)
surf1224 = openmc.ZCylinder(surface_id=1224, x0=21.7551, y0=0.0, r=0.72517)
surf1225 = openmc.ZCylinder(surface_id=1225, x0=23.20544, y0=0.0, r=0.72517)
surf1226 = openmc.ZCylinder(surface_id=1226, x0=24.65578, y0=0.0, r=0.72517)
surf1227 = openmc.ZCylinder(surface_id=1227, x0=26.10612, y0=0.0, r=0.72517)
surf1228 = openmc.ZCylinder(surface_id=1228, x0=27.55646, y0=0.0, r=0.72517)
surf1229 = openmc.ZCylinder(surface_id=1229, x0=29.0068, y0=0.0, r=0.72517)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=2229, z0=-56.2991, boundary_type="vacuum")
surf1_zmax = openmc.ZPlane(surface_id=2230, z0=56.2991, boundary_type="vacuum")
surf23_zmin = openmc.ZPlane(surface_id=2231, z0=-25.8191)
surf23_zmax = openmc.ZPlane(surface_id=2232, z0=25.8191)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = -surf10 & +surf13 & -surf14 & -surf17
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = -surf10 & -surf13 & -surf17
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = -surf10 & +surf14 & -surf17
u1_cell3 = openmc.Cell()
u1_cell3.region = +surf10 & -surf11 & -surf17
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = +surf11 & -surf12 & -surf17
u1_cell5 = openmc.Cell(fill=mat6)
u1_cell5.region = +surf12 & +surf15 & -surf16 & -surf17
u1_cell6 = openmc.Cell(fill=mat1)
u1_cell6.region = +surf12 & -surf15 & -surf17
u1_cell7 = openmc.Cell(fill=mat1)
u1_cell7.region = +surf12 & +surf16 & -surf17
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = -surf21 & (-surf23 & +surf23_zmin & -surf23_zmax) & +surf13 & -surf14
u2_cell1 = openmc.Cell(fill=mat4)
u2_cell1.region = -surf21 & (-surf23 & +surf23_zmin & -surf23_zmax) & -surf13
u2_cell2 = openmc.Cell(fill=mat4)
u2_cell2.region = -surf21 & (-surf23 & +surf23_zmin & -surf23_zmax) & +surf14
u2_cell3 = openmc.Cell()
u2_cell3.region = +surf21 & -surf22 & (-surf23 & +surf23_zmin & -surf23_zmax)
u2_cell4 = openmc.Cell(fill=mat4)
u2_cell4.region = +surf22 & (-surf23 & +surf23_zmin & -surf23_zmax)
u2_cell5 = openmc.Cell(fill=mat1)
u2_cell5.region = (+surf23 | -surf23_zmin | +surf23_zmax) & -surf17
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5])

u3_cell0 = openmc.Cell(fill=mat1)
u3_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax)
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0])

u4_cell0 = openmc.Cell(fill=mat1)
u4_cell0.region = -surf9
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0])

universe5 = openmc.Universe(universe_id=5, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Cntrl
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf100_0 & -surf100_1 & -surf100_2 & -surf100_3 & -surf100_4 & -surf100_5) & -surf2

# Cntrl
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf100_0 & -surf100_1 & -surf100_2 & -surf100_3 & -surf100_4 & -surf100_5) & -surf3

# Cntrl
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf100_0 & -surf100_1 & -surf100_2 & -surf100_3 & -surf100_4 & -surf100_5) & -surf4

# Cntrl
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf100_0 & -surf100_1 & -surf100_2 & -surf100_3 & -surf100_4 & -surf100_5) & -surf5

# H2O
cell21 = openmc.Cell(cell_id=21, fill=mat1)
cell21.region = +surf12 & +surf16 & -surf17

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell21])
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
