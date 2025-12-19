"""
LEU-COMP-THERM-005-13: 1,495 U(4.31)O2 rods in water; 1.598 cm pitch; 0.121gGd/L
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(4.31)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 5.183500e-06)
mat1.add_nuclide("U235", 1.010200e-03)
mat1.add_nuclide("U236", 5.139500e-06)
mat1.add_nuclide("U238", 2.215700e-02)
mat1.add_nuclide("O16", 4.675300e-02)

# Al-6061
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.843300e-02)
mat2.add_element("Cr", 6.231000e-05)
mat2.add_element("Cu", 6.373100e-05)
mat2.add_element("Mg", 6.665100e-04)
mat2.add_element("Mn", 2.211500e-05)
mat2.add_element("Ti", 2.537500e-05)
mat2.add_element("Zn", 3.096700e-05)
mat2.add_element("Si", 3.460700e-04)
mat2.add_element("Fe", 1.015200e-04)

# Rubber
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 5.817800e-02)
mat3.add_element("C", 4.356200e-02)
mat3.add_element("Ca", 2.566000e-03)
mat3.add_element("S", 4.782000e-04)
mat3.add_element("Si", 9.636000e-05)
mat3.add_nuclide("O16", 1.246100e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

# Polypropylene
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 7.770800e-02)
mat4.add_element("C", 3.885400e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

# Acrylic
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 5.702300e-02)
mat5.add_element("C", 3.563900e-02)
mat5.add_nuclide("O16", 1.425600e-02)
mat5.add_s_alpha_beta("c_H_in_CH2")

# Water with 0.121 gGd/L
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.679500e-02)
mat6.add_nuclide("O16", 3.340200e-02)
mat6.add_element("Gd", 4.633900e-07)
mat6.add_element("N", 1.390200e-06)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Boundary condition
surf1 = openmc.ZCylinder(surface_id=1, r=76.014, boundary_type="vacuum")
# Acrylic base plate
surf2 = openmc.ZCylinder(surface_id=2, r=99.9)
# Propylene lattice plate - bottom -
surf3 = openmc.ZCylinder(surface_id=3, r=45.72)
# Propylene lattice plate - middle -
surf4 = openmc.ZCylinder(surface_id=4, r=45.72)
# Propylene lattice plate - top    -
surf5 = openmc.ZCylinder(surface_id=5, r=45.72)
# Rubber
surf11 = openmc.ZCylinder(surface_id=11, r=0.6415)
# U(4.31)O2 fuel
surf12 = openmc.ZCylinder(surface_id=12, r=0.6325)
# Rubber
surf13 = openmc.ZCylinder(surface_id=13, r=0.6415)
# Clad inner
surf14 = openmc.ZCylinder(surface_id=14, r=0.6415)
# Clad outer
surf15 = openmc.ZCylinder(surface_id=15, r=0.7075)
# Hole
surf16 = openmc.ZCylinder(surface_id=16, r=0.714)
surf17 = openmc.ZCylinder(surface_id=17, x0=-0.799, y0=1.383909, r=0.714)
surf18 = openmc.ZCylinder(surface_id=18, x0=-0.799, y0=-1.383909, r=0.714)
surf19 = openmc.ZCylinder(surface_id=19, x0=0.799, y0=1.383909, r=0.714)
surf20 = openmc.ZCylinder(surface_id=20, x0=0.799, y0=-1.383909, r=0.714)
# Prism 21: 12-sided polygon
surf21_0 = openmc.Plane(a=0.8660254671, b=0.4999998903, c=0, d=31.8299000180)
surf21_1 = openmc.Plane(a=0.5000001097, b=0.8660253405, c=0, d=31.9600070105)
surf21_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=31.8299070000)
surf21_3 = openmc.Plane(a=-0.5000001097, b=0.8660253405, c=0, d=31.9600070105)
surf21_4 = openmc.Plane(a=-0.8660254671, b=0.4999998903, c=0, d=31.8299000180)
surf21_5 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=31.9600000000)
surf21_6 = openmc.Plane(a=-0.8660254671, b=-0.4999998903, c=0, d=31.8299000180)
surf21_7 = openmc.Plane(a=-0.5000001097, b=-0.8660253405, c=0, d=31.9600070105)
surf21_8 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=31.8299070000)
surf21_9 = openmc.Plane(a=0.5000001097, b=-0.8660253405, c=0, d=31.9600070105)
surf21_10 = openmc.Plane(a=0.8660254671, b=-0.4999998903, c=0, d=31.8299000180)
surf21_11 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=31.9600000000)
# Prism 22: 18-sided polygon
surf22_0 = openmc.Plane(a=0.9819790177, b=0.1889899699, c=0, d=36.2723409569)
surf22_1 = openmc.Plane(a=0.8660313503, b=0.4999897002, c=0, d=36.1615675717)
surf22_2 = openmc.Plane(a=0.6546527387, b=0.7559297532, c=0, d=36.2722183049)
surf22_3 = openmc.Plane(a=0.3273611282, b=0.9448993024, c=0, d=36.2724164623)
surf22_4 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=36.1620000000)
surf22_5 = openmc.Plane(a=-0.3273611282, b=0.9448993024, c=0, d=36.2724164623)
surf22_6 = openmc.Plane(a=-0.6546348070, b=0.7559452820, c=0, d=36.2723838780)
surf22_7 = openmc.Plane(a=-0.8660371872, b=0.4999795899, c=0, d=36.1616925629)
surf22_8 = openmc.Plane(a=-0.9819792979, b=0.1889885140, c=0, d=36.2723513071)
surf22_9 = openmc.Plane(a=-0.9819790177, b=-0.1889899699, c=0, d=36.2723409569)
surf22_10 = openmc.Plane(a=-0.8660313503, b=-0.4999897002, c=0, d=36.1615675717)
surf22_11 = openmc.Plane(a=-0.6546527387, b=-0.7559297532, c=0, d=36.2722183049)
surf22_12 = openmc.Plane(a=-0.3273611282, b=-0.9448993024, c=0, d=36.2724164623)
surf22_13 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=36.1620000000)
surf22_14 = openmc.Plane(a=0.3273611282, b=-0.9448993024, c=0, d=36.2724164623)
surf22_15 = openmc.Plane(a=0.6546527387, b=-0.7559297532, c=0, d=36.2722183049)
surf22_16 = openmc.Plane(a=0.8660313503, b=-0.4999897002, c=0, d=36.1615675717)
surf22_17 = openmc.Plane(a=0.9819790177, b=-0.1889899699, c=0, d=36.2723409569)
# Prism 23: 18-sided polygon
surf23_0 = openmc.Plane(a=0.9819805163, b=0.1889821832, c=0, d=36.0917118968)
surf23_1 = openmc.Plane(a=0.8660254671, b=0.4999998903, c=0, d=35.9816261073)
surf23_2 = openmc.Plane(a=0.6546537801, b=0.7559288513, c=0, d=36.0917175517)
surf23_3 = openmc.Plane(a=0.3273269208, b=0.9449111529, c=0, d=36.0917209446)
surf23_4 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=35.9816340000)
surf23_5 = openmc.Plane(a=-0.3273269208, b=0.9449111529, c=0, d=36.0917209446)
surf23_6 = openmc.Plane(a=-0.6546537801, b=0.7559288513, c=0, d=36.0917175517)
surf23_7 = openmc.Plane(a=-0.8660254671, b=0.4999998903, c=0, d=35.9816261073)
surf23_8 = openmc.Plane(a=-0.9819805163, b=0.1889821832, c=0, d=36.0917118968)
surf23_9 = openmc.Plane(a=-0.9819805163, b=-0.1889821832, c=0, d=36.0917118968)
surf23_10 = openmc.Plane(a=-0.8660254671, b=-0.4999998903, c=0, d=35.9816261073)
surf23_11 = openmc.Plane(a=-0.6546537801, b=-0.7559288513, c=0, d=36.0917175517)
surf23_12 = openmc.Plane(a=-0.3273269208, b=-0.9449111529, c=0, d=36.0917209446)
surf23_13 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=35.9816340000)
surf23_14 = openmc.Plane(a=0.3273269208, b=-0.9449111529, c=0, d=36.0917209446)
surf23_15 = openmc.Plane(a=0.6546537801, b=-0.7559288513, c=0, d=36.0917175517)
surf23_16 = openmc.Plane(a=0.8660254671, b=-0.4999998903, c=0, d=35.9816261073)
surf23_17 = openmc.Plane(a=0.9819805163, b=-0.1889821832, c=0, d=36.0917118968)
surf91 = openmc.ZCylinder(surface_id=91, x0=5.593, y0=-31.829907, r=0.714)
surf92 = openmc.ZCylinder(surface_id=92, x0=7.191, y0=-31.829907, r=0.714)
surf93 = openmc.ZCylinder(surface_id=93, x0=8.789, y0=-31.829907, r=0.714)
surf101 = openmc.ZCylinder(surface_id=101, x0=-8.789, y0=31.829907, r=0.714)
surf102 = openmc.ZCylinder(surface_id=102, x0=-7.191, y0=31.829907, r=0.714)
surf103 = openmc.ZCylinder(surface_id=103, x0=-5.593, y0=31.829907, r=0.714)
surf104 = openmc.ZCylinder(surface_id=104, x0=-3.995, y0=31.829907, r=0.714)
surf105 = openmc.ZCylinder(surface_id=105, x0=-2.397, y0=31.829907, r=0.714)
surf106 = openmc.ZCylinder(surface_id=106, x0=-0.799, y0=31.829907, r=0.714)
surf107 = openmc.ZCylinder(surface_id=107, x0=0.799, y0=31.829907, r=0.714)
surf108 = openmc.ZCylinder(surface_id=108, x0=2.397, y0=31.829907, r=0.714)
surf109 = openmc.ZCylinder(surface_id=109, x0=3.995, y0=31.829907, r=0.714)
surf110 = openmc.ZCylinder(surface_id=110, x0=5.593, y0=31.829907, r=0.714)
surf111 = openmc.ZCylinder(surface_id=111, x0=7.191, y0=31.829907, r=0.714)
surf112 = openmc.ZCylinder(surface_id=112, x0=8.789, y0=31.829907, r=0.714)
surf113 = openmc.ZCylinder(surface_id=113, x0=-11.186, y0=30.445998, r=0.714)
surf114 = openmc.ZCylinder(surface_id=114, x0=11.186, y0=30.445998, r=0.714)
surf115 = openmc.ZCylinder(surface_id=115, x0=-13.583, y0=29.062089, r=0.714)
surf116 = openmc.ZCylinder(surface_id=116, x0=13.583, y0=29.062089, r=0.714)
surf117 = openmc.ZCylinder(surface_id=117, x0=-15.98, y0=27.67818, r=0.714)
surf118 = openmc.ZCylinder(surface_id=118, x0=15.98, y0=27.67818, r=0.714)
surf119 = openmc.ZCylinder(surface_id=119, x0=-18.377, y0=26.294271, r=0.714)
surf120 = openmc.ZCylinder(surface_id=120, x0=18.377, y0=26.294271, r=0.714)
surf121 = openmc.ZCylinder(surface_id=121, x0=-20.774, y0=24.910362, r=0.714)
surf122 = openmc.ZCylinder(surface_id=122, x0=20.774, y0=24.910362, r=0.714)
surf123 = openmc.ZCylinder(surface_id=123, x0=-23.171, y0=23.526453, r=0.714)
surf124 = openmc.ZCylinder(surface_id=124, x0=23.171, y0=23.526453, r=0.714)
surf125 = openmc.ZCylinder(surface_id=125, x0=-23.97, y0=22.142544, r=0.714)
surf126 = openmc.ZCylinder(surface_id=126, x0=23.97, y0=22.142544, r=0.714)
surf127 = openmc.ZCylinder(surface_id=127, x0=-24.769, y0=20.758635, r=0.714)
surf128 = openmc.ZCylinder(surface_id=128, x0=24.769, y0=20.758635, r=0.714)
surf129 = openmc.ZCylinder(surface_id=129, x0=-25.568, y0=19.374726, r=0.714)
surf130 = openmc.ZCylinder(surface_id=130, x0=25.568, y0=19.374726, r=0.714)
surf131 = openmc.ZCylinder(surface_id=131, x0=-26.367, y0=17.990817, r=0.714)
surf132 = openmc.ZCylinder(surface_id=132, x0=26.367, y0=17.990817, r=0.714)
surf133 = openmc.ZCylinder(surface_id=133, x0=-27.166, y0=16.606908, r=0.714)
surf134 = openmc.ZCylinder(surface_id=134, x0=27.166, y0=16.606908, r=0.714)
surf135 = openmc.ZCylinder(surface_id=135, x0=-27.965, y0=15.222999, r=0.714)
surf136 = openmc.ZCylinder(surface_id=136, x0=27.965, y0=15.222999, r=0.714)
surf137 = openmc.ZCylinder(surface_id=137, x0=-28.764, y0=13.83909, r=0.714)
surf138 = openmc.ZCylinder(surface_id=138, x0=28.764, y0=13.83909, r=0.714)
surf139 = openmc.ZCylinder(surface_id=139, x0=-29.563, y0=12.455181, r=0.714)
surf140 = openmc.ZCylinder(surface_id=140, x0=29.563, y0=12.455181, r=0.714)
surf141 = openmc.ZCylinder(surface_id=141, x0=-30.362, y0=11.071272, r=0.714)
surf142 = openmc.ZCylinder(surface_id=142, x0=30.362, y0=11.071272, r=0.714)
surf143 = openmc.ZCylinder(surface_id=143, x0=-31.161, y0=9.687363, r=0.714)
surf144 = openmc.ZCylinder(surface_id=144, x0=31.161, y0=9.687363, r=0.714)
surf145 = openmc.ZCylinder(surface_id=145, x0=-31.96, y0=8.303454, r=0.714)
surf146 = openmc.ZCylinder(surface_id=146, x0=31.96, y0=8.303454, r=0.714)
surf147 = openmc.ZCylinder(surface_id=147, x0=-31.96, y0=5.535636, r=0.714)
surf148 = openmc.ZCylinder(surface_id=148, x0=31.96, y0=5.535636, r=0.714)
surf149 = openmc.ZCylinder(surface_id=149, x0=-31.96, y0=2.767818, r=0.714)
surf150 = openmc.ZCylinder(surface_id=150, x0=31.96, y0=2.767818, r=0.714)
surf151 = openmc.ZCylinder(surface_id=151, x0=-31.96, y0=0.0, r=0.714)
surf152 = openmc.ZCylinder(surface_id=152, x0=31.96, y0=0.0, r=0.714)
surf153 = openmc.ZCylinder(surface_id=153, x0=-31.96, y0=-2.767818, r=0.714)
surf154 = openmc.ZCylinder(surface_id=154, x0=31.96, y0=-2.767818, r=0.714)
surf155 = openmc.ZCylinder(surface_id=155, x0=-31.96, y0=-5.535636, r=0.714)
surf156 = openmc.ZCylinder(surface_id=156, x0=31.96, y0=-5.535636, r=0.714)
surf157 = openmc.ZCylinder(surface_id=157, x0=-31.96, y0=-8.303454, r=0.714)
surf158 = openmc.ZCylinder(surface_id=158, x0=31.96, y0=-8.303454, r=0.714)
surf159 = openmc.ZCylinder(surface_id=159, x0=-31.161, y0=-9.687363, r=0.714)
surf160 = openmc.ZCylinder(surface_id=160, x0=31.161, y0=-9.687363, r=0.714)
surf161 = openmc.ZCylinder(surface_id=161, x0=-30.362, y0=-11.071272, r=0.714)
surf162 = openmc.ZCylinder(surface_id=162, x0=30.362, y0=-11.071272, r=0.714)
surf163 = openmc.ZCylinder(surface_id=163, x0=-29.563, y0=-12.455181, r=0.714)
surf164 = openmc.ZCylinder(surface_id=164, x0=29.563, y0=-12.455181, r=0.714)
surf165 = openmc.ZCylinder(surface_id=165, x0=-28.764, y0=-13.83909, r=0.714)
surf166 = openmc.ZCylinder(surface_id=166, x0=28.764, y0=-13.83909, r=0.714)
surf167 = openmc.ZCylinder(surface_id=167, x0=-27.965, y0=-15.222999, r=0.714)
surf168 = openmc.ZCylinder(surface_id=168, x0=27.965, y0=-15.222999, r=0.714)
surf169 = openmc.ZCylinder(surface_id=169, x0=-27.166, y0=-16.606908, r=0.714)
surf170 = openmc.ZCylinder(surface_id=170, x0=27.166, y0=-16.606908, r=0.714)
surf171 = openmc.ZCylinder(surface_id=171, x0=-26.367, y0=-17.990817, r=0.714)
surf172 = openmc.ZCylinder(surface_id=172, x0=26.367, y0=-17.990817, r=0.714)
surf173 = openmc.ZCylinder(surface_id=173, x0=-25.568, y0=-19.374726, r=0.714)
surf174 = openmc.ZCylinder(surface_id=174, x0=25.568, y0=-19.374726, r=0.714)
surf175 = openmc.ZCylinder(surface_id=175, x0=-24.769, y0=-20.758635, r=0.714)
surf176 = openmc.ZCylinder(surface_id=176, x0=24.769, y0=-20.758635, r=0.714)
surf177 = openmc.ZCylinder(surface_id=177, x0=-23.97, y0=-22.142544, r=0.714)
surf178 = openmc.ZCylinder(surface_id=178, x0=23.97, y0=-22.142544, r=0.714)
surf179 = openmc.ZCylinder(surface_id=179, x0=-23.171, y0=-23.526453, r=0.714)
surf180 = openmc.ZCylinder(surface_id=180, x0=23.171, y0=-23.526453, r=0.714)
surf181 = openmc.ZCylinder(surface_id=181, x0=-20.774, y0=-24.910362, r=0.714)
surf182 = openmc.ZCylinder(surface_id=182, x0=20.774, y0=-24.910362, r=0.714)
surf183 = openmc.ZCylinder(surface_id=183, x0=-18.377, y0=-26.294271, r=0.714)
surf184 = openmc.ZCylinder(surface_id=184, x0=18.377, y0=-26.294271, r=0.714)
surf185 = openmc.ZCylinder(surface_id=185, x0=-15.98, y0=-27.67818, r=0.714)
surf186 = openmc.ZCylinder(surface_id=186, x0=15.98, y0=-27.67818, r=0.714)
surf187 = openmc.ZCylinder(surface_id=187, x0=-13.583, y0=-29.062089, r=0.714)
surf188 = openmc.ZCylinder(surface_id=188, x0=13.583, y0=-29.062089, r=0.714)
surf189 = openmc.ZCylinder(surface_id=189, x0=-11.186, y0=-30.445998, r=0.714)
surf190 = openmc.ZCylinder(surface_id=190, x0=11.186, y0=-30.445998, r=0.714)
surf191 = openmc.ZCylinder(surface_id=191, x0=-8.789, y0=-31.829907, r=0.714)
surf192 = openmc.ZCylinder(surface_id=192, x0=-7.191, y0=-31.829907, r=0.714)
surf193 = openmc.ZCylinder(surface_id=193, x0=-5.593, y0=-31.829907, r=0.714)
surf194 = openmc.ZCylinder(surface_id=194, x0=-3.995, y0=-31.829907, r=0.714)
surf195 = openmc.ZCylinder(surface_id=195, x0=-2.397, y0=-31.829907, r=0.714)
surf196 = openmc.ZCylinder(surface_id=196, x0=-0.799, y0=-31.829907, r=0.714)
surf197 = openmc.ZCylinder(surface_id=197, x0=0.799, y0=-31.829907, r=0.714)
surf198 = openmc.ZCylinder(surface_id=198, x0=2.397, y0=-31.829907, r=0.714)
surf199 = openmc.ZCylinder(surface_id=199, x0=3.995, y0=-31.829907, r=0.714)
surf201 = openmc.ZCylinder(surface_id=201, x0=-6.392, y0=35.981634, r=0.714)
surf202 = openmc.ZCylinder(surface_id=202, x0=-4.794, y0=35.981634, r=0.714)
surf203 = openmc.ZCylinder(surface_id=203, x0=-3.196, y0=35.981634, r=0.714)
surf204 = openmc.ZCylinder(surface_id=204, x0=-1.598, y0=35.981634, r=0.714)
surf205 = openmc.ZCylinder(surface_id=205, x0=0.0, y0=35.981634, r=0.714)
surf206 = openmc.ZCylinder(surface_id=206, x0=1.598, y0=35.981634, r=0.714)
surf207 = openmc.ZCylinder(surface_id=207, x0=3.196, y0=35.981634, r=0.714)
surf208 = openmc.ZCylinder(surface_id=208, x0=4.794, y0=35.981634, r=0.714)
surf209 = openmc.ZCylinder(surface_id=209, x0=6.392, y0=35.981634, r=0.714)
surf210 = openmc.ZCylinder(surface_id=210, x0=-10.387, y0=34.597725, r=0.714)
surf211 = openmc.ZCylinder(surface_id=211, x0=10.387, y0=34.597725, r=0.714)
surf212 = openmc.ZCylinder(surface_id=212, x0=-14.382, y0=33.213816, r=0.714)
surf213 = openmc.ZCylinder(surface_id=213, x0=14.382, y0=33.213816, r=0.714)
surf214 = openmc.ZCylinder(surface_id=214, x0=-18.377, y0=31.829907, r=0.714)
surf215 = openmc.ZCylinder(surface_id=215, x0=18.377, y0=31.829907, r=0.714)
surf216 = openmc.ZCylinder(surface_id=216, x0=-21.573, y0=29.062089, r=0.714)
surf217 = openmc.ZCylinder(surface_id=217, x0=21.573, y0=29.062089, r=0.714)
surf218 = openmc.ZCylinder(surface_id=218, x0=-24.769, y0=26.294271, r=0.714)
surf219 = openmc.ZCylinder(surface_id=219, x0=24.769, y0=26.294271, r=0.714)
surf220 = openmc.ZCylinder(surface_id=220, x0=-27.965, y0=23.526453, r=0.714)
surf221 = openmc.ZCylinder(surface_id=221, x0=27.965, y0=23.526453, r=0.714)
surf222 = openmc.ZCylinder(surface_id=222, x0=-28.764, y0=22.142544, r=0.714)
surf223 = openmc.ZCylinder(surface_id=223, x0=28.764, y0=22.142544, r=0.714)
surf224 = openmc.ZCylinder(surface_id=224, x0=-29.563, y0=20.758635, r=0.714)
surf225 = openmc.ZCylinder(surface_id=225, x0=29.563, y0=20.758635, r=0.714)
surf226 = openmc.ZCylinder(surface_id=226, x0=-30.362, y0=19.374726, r=0.714)
surf227 = openmc.ZCylinder(surface_id=227, x0=30.362, y0=19.374726, r=0.714)
surf228 = openmc.ZCylinder(surface_id=228, x0=-31.161, y0=17.990817, r=0.714)
surf229 = openmc.ZCylinder(surface_id=229, x0=31.161, y0=17.990817, r=0.714)
surf230 = openmc.ZCylinder(surface_id=230, x0=-31.96, y0=16.606908, r=0.714)
surf231 = openmc.ZCylinder(surface_id=231, x0=31.96, y0=16.606908, r=0.714)
surf232 = openmc.ZCylinder(surface_id=232, x0=-32.759, y0=15.22299, r=0.714)
surf233 = openmc.ZCylinder(surface_id=233, x0=32.759, y0=15.22299, r=0.714)
surf234 = openmc.ZCylinder(surface_id=234, x0=-33.558, y0=13.83909, r=0.714)
surf235 = openmc.ZCylinder(surface_id=235, x0=33.558, y0=13.83909, r=0.714)
surf236 = openmc.ZCylinder(surface_id=236, x0=-34.357, y0=12.455181, r=0.714)
surf237 = openmc.ZCylinder(surface_id=237, x0=34.357, y0=12.455181, r=0.714)
surf238 = openmc.ZCylinder(surface_id=238, x0=-35.156, y0=8.303454, r=0.714)
surf239 = openmc.ZCylinder(surface_id=239, x0=35.156, y0=8.303454, r=0.714)
surf240 = openmc.ZCylinder(surface_id=240, x0=-35.955, y0=4.151727, r=0.714)
surf241 = openmc.ZCylinder(surface_id=241, x0=35.955, y0=4.151727, r=0.714)
surf242 = openmc.ZCylinder(surface_id=242, x0=-36.754, y0=0.0, r=0.714)
surf243 = openmc.ZCylinder(surface_id=243, x0=36.754, y0=0.0, r=0.714)
surf301 = openmc.ZCylinder(surface_id=301, x0=-6.392, y0=-35.981634, r=0.714)
surf302 = openmc.ZCylinder(surface_id=302, x0=-4.794, y0=-35.981634, r=0.714)
surf303 = openmc.ZCylinder(surface_id=303, x0=-3.196, y0=-35.981634, r=0.714)
surf304 = openmc.ZCylinder(surface_id=304, x0=-1.598, y0=-35.981634, r=0.714)
surf305 = openmc.ZCylinder(surface_id=305, x0=0.0, y0=-35.981634, r=0.714)
surf306 = openmc.ZCylinder(surface_id=306, x0=1.598, y0=-35.981634, r=0.714)
surf307 = openmc.ZCylinder(surface_id=307, x0=3.196, y0=-35.981634, r=0.714)
surf308 = openmc.ZCylinder(surface_id=308, x0=4.794, y0=-35.981634, r=0.714)
surf309 = openmc.ZCylinder(surface_id=309, x0=6.392, y0=-35.981634, r=0.714)
surf310 = openmc.ZCylinder(surface_id=310, x0=-10.387, y0=-34.597725, r=0.714)
surf311 = openmc.ZCylinder(surface_id=311, x0=10.387, y0=-34.597725, r=0.714)
surf312 = openmc.ZCylinder(surface_id=312, x0=-14.382, y0=-33.213816, r=0.714)
surf313 = openmc.ZCylinder(surface_id=313, x0=14.382, y0=-33.213816, r=0.714)
surf314 = openmc.ZCylinder(surface_id=314, x0=-18.377, y0=-31.829907, r=0.714)
surf315 = openmc.ZCylinder(surface_id=315, x0=18.377, y0=-31.829907, r=0.714)
surf316 = openmc.ZCylinder(surface_id=316, x0=-21.573, y0=-29.062089, r=0.714)
surf317 = openmc.ZCylinder(surface_id=317, x0=21.573, y0=-29.062089, r=0.714)
surf318 = openmc.ZCylinder(surface_id=318, x0=-24.769, y0=-26.294271, r=0.714)
surf319 = openmc.ZCylinder(surface_id=319, x0=24.769, y0=-26.294271, r=0.714)
surf320 = openmc.ZCylinder(surface_id=320, x0=-27.965, y0=-23.526453, r=0.714)
surf321 = openmc.ZCylinder(surface_id=321, x0=27.965, y0=-23.526453, r=0.714)
surf322 = openmc.ZCylinder(surface_id=322, x0=-28.764, y0=-22.142544, r=0.714)
surf323 = openmc.ZCylinder(surface_id=323, x0=28.764, y0=-22.142544, r=0.714)
surf324 = openmc.ZCylinder(surface_id=324, x0=-29.563, y0=-20.758635, r=0.714)
surf325 = openmc.ZCylinder(surface_id=325, x0=29.563, y0=-20.758635, r=0.714)
surf326 = openmc.ZCylinder(surface_id=326, x0=-30.362, y0=-19.374726, r=0.714)
surf327 = openmc.ZCylinder(surface_id=327, x0=30.362, y0=-19.374726, r=0.714)
surf328 = openmc.ZCylinder(surface_id=328, x0=-31.161, y0=-17.990817, r=0.714)
surf329 = openmc.ZCylinder(surface_id=329, x0=31.161, y0=-17.990817, r=0.714)
surf330 = openmc.ZCylinder(surface_id=330, x0=-31.96, y0=-16.606908, r=0.714)
surf331 = openmc.ZCylinder(surface_id=331, x0=31.96, y0=-16.606908, r=0.714)
surf332 = openmc.ZCylinder(surface_id=332, x0=-32.759, y0=-15.22299, r=0.714)
surf333 = openmc.ZCylinder(surface_id=333, x0=32.759, y0=-15.22299, r=0.714)
surf334 = openmc.ZCylinder(surface_id=334, x0=-33.558, y0=-13.83909, r=0.714)
surf335 = openmc.ZCylinder(surface_id=335, x0=33.558, y0=-13.83909, r=0.714)
surf336 = openmc.ZCylinder(surface_id=336, x0=-34.357, y0=-12.455181, r=0.714)
surf337 = openmc.ZCylinder(surface_id=337, x0=34.357, y0=-12.455181, r=0.714)
surf338 = openmc.ZCylinder(surface_id=338, x0=-35.156, y0=-8.303454, r=0.714)
surf339 = openmc.ZCylinder(surface_id=339, x0=35.156, y0=-8.303454, r=0.714)
surf340 = openmc.ZCylinder(surface_id=340, x0=-35.955, y0=-4.151727, r=0.714)
surf341 = openmc.ZCylinder(surface_id=341, x0=35.955, y0=-4.151727, r=0.714)
surf701 = openmc.ZCylinder(surface_id=701, x0=-7.99, y0=35.981634, r=0.7141)
surf702 = openmc.ZCylinder(surface_id=702, x0=7.99, y0=35.981634, r=0.7141)
surf703 = openmc.ZCylinder(surface_id=703, x0=-11.985, y0=34.597725, r=0.7141)
surf704 = openmc.ZCylinder(surface_id=704, x0=11.985, y0=34.597725, r=0.7141)
surf705 = openmc.ZCylinder(surface_id=705, x0=-15.98, y0=33.213816, r=0.7141)
surf706 = openmc.ZCylinder(surface_id=706, x0=15.98, y0=33.213816, r=0.7141)
surf707 = openmc.ZCylinder(surface_id=707, x0=-20.774, y0=30.445998, r=0.7141)
surf708 = openmc.ZCylinder(surface_id=708, x0=20.774, y0=30.445998, r=0.7141)
surf709 = openmc.ZCylinder(surface_id=709, x0=-23.97, y0=27.67818, r=0.7141)
surf710 = openmc.ZCylinder(surface_id=710, x0=23.97, y0=27.67818, r=0.7141)
surf711 = openmc.ZCylinder(surface_id=711, x0=-27.166, y0=24.910362, r=0.7141)
surf712 = openmc.ZCylinder(surface_id=712, x0=27.166, y0=24.910362, r=0.7141)
surf713 = openmc.ZCylinder(surface_id=713, x0=-35.156, y0=11.071272, r=0.7141)
surf714 = openmc.ZCylinder(surface_id=714, x0=35.156, y0=11.071272, r=0.7141)
surf715 = openmc.ZCylinder(surface_id=715, x0=-35.955, y0=6.919545, r=0.7141)
surf716 = openmc.ZCylinder(surface_id=716, x0=35.955, y0=6.919545, r=0.7141)
surf717 = openmc.ZCylinder(surface_id=717, x0=-36.754, y0=2.767818, r=0.7141)
surf718 = openmc.ZCylinder(surface_id=718, x0=36.754, y0=2.767818, r=0.7141)
surf719 = openmc.ZCylinder(surface_id=719, x0=-36.754, y0=-2.767818, r=0.7141)
surf720 = openmc.ZCylinder(surface_id=720, x0=36.754, y0=-2.767818, r=0.7141)
surf721 = openmc.ZCylinder(surface_id=721, x0=-35.955, y0=-6.919545, r=0.7141)
surf722 = openmc.ZCylinder(surface_id=722, x0=35.955, y0=-6.919545, r=0.7141)
surf723 = openmc.ZCylinder(surface_id=723, x0=-35.156, y0=-11.071272, r=0.7141)
surf724 = openmc.ZCylinder(surface_id=724, x0=35.156, y0=-11.071272, r=0.7141)
surf725 = openmc.ZCylinder(surface_id=725, x0=-27.166, y0=-24.910362, r=0.7141)
surf726 = openmc.ZCylinder(surface_id=726, x0=27.166, y0=-24.910362, r=0.7141)
surf727 = openmc.ZCylinder(surface_id=727, x0=-23.97, y0=-27.67818, r=0.7141)
surf728 = openmc.ZCylinder(surface_id=728, x0=23.97, y0=-27.67818, r=0.7141)
surf729 = openmc.ZCylinder(surface_id=729, x0=-20.774, y0=-30.445998, r=0.7141)
surf730 = openmc.ZCylinder(surface_id=730, x0=20.774, y0=-30.445998, r=0.7141)
surf731 = openmc.ZCylinder(surface_id=731, x0=-15.98, y0=-33.213816, r=0.7141)
surf732 = openmc.ZCylinder(surface_id=732, x0=15.98, y0=-33.213816, r=0.7141)
surf733 = openmc.ZCylinder(surface_id=733, x0=-11.985, y0=-34.597725, r=0.7141)
surf734 = openmc.ZCylinder(surface_id=734, x0=11.985, y0=-34.597725, r=0.7141)
surf735 = openmc.ZCylinder(surface_id=735, x0=-7.99, y0=-35.981634, r=0.7141)
surf736 = openmc.ZCylinder(surface_id=736, x0=7.99, y0=-35.981634, r=0.7141)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1736, z0=-22.86, boundary_type="vacuum")
surf1_zmax = openmc.ZPlane(surface_id=1737, z0=109.14, boundary_type="vacuum")
surf2_zmin = openmc.ZPlane(surface_id=1738, z0=-2.54)
surf2_zmax = openmc.ZPlane(surface_id=1739, z0=0.0)
surf3_zmin = openmc.ZPlane(surface_id=1740, z0=0.809)
surf3_zmax = openmc.ZPlane(surface_id=1741, z0=2.159)
surf4_zmin = openmc.ZPlane(surface_id=1742, z0=37.639)
surf4_zmax = openmc.ZPlane(surface_id=1743, z0=38.989)
surf5_zmin = openmc.ZPlane(surface_id=1744, z0=86.28)
surf5_zmax = openmc.ZPlane(surface_id=1745, z0=87.63)
surf11_zmin = openmc.ZPlane(surface_id=1746, z0=0.0)
surf11_zmax = openmc.ZPlane(surface_id=1747, z0=2.2225)
surf12_zmin = openmc.ZPlane(surface_id=1748, z0=2.2225)
surf12_zmax = openmc.ZPlane(surface_id=1749, z0=94.2975)
surf13_zmin = openmc.ZPlane(surface_id=1750, z0=94.2975)
surf13_zmax = openmc.ZPlane(surface_id=1751, z0=96.52)
surf15_zmin = openmc.ZPlane(surface_id=1752, z0=0.0)
surf15_zmax = openmc.ZPlane(surface_id=1753, z0=96.52)
surf16_zmin = openmc.ZPlane(surface_id=1754, z0=0.0)
surf16_zmax = openmc.ZPlane(surface_id=1755, z0=96.52)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat5)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = (-surf13 & +surf13_zmin & -surf13_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & +surf14 & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell4 = openmc.Cell(fill=mat6)
u2_cell4.region = (+surf15 | -surf15_zmin | +surf15_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat6)
u4_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)
u4_cell1 = openmc.Cell(fill=mat6)
u4_cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf17
u4_cell2 = openmc.Cell(fill=mat6)
u4_cell2.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf18
u4_cell3 = openmc.Cell(fill=mat6)
u4_cell3.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf19
u4_cell4 = openmc.Cell(fill=mat6)
u4_cell4.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf20
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

# Lattice 5: 47x27 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-37.553, -37.365543]
lattice5.pitch = [1.598000, 2.767818]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# Lattice 6: 47x27 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-37.553, -37.365543]
lattice6.pitch = [1.598000, 2.767818]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# core
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & +surf101 & +surf102 & +surf111 & +surf112 & +surf113 & +surf114 & +surf121 & +surf122 & +surf123 & +surf124

# holes
cell2 = openmc.Cell(cell_id=2, fill=universe6)
cell2.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & +surf701 & +surf702 & +surf703 & +surf704 & +surf705 & +surf706 & +surf707 & +surf708 & +surf709 & +surf710

# plates
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf701

# plates
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf702

# plates
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf703

# plates
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf704

# plates
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf705

# plates
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf706

# plates
cell9 = openmc.Cell(cell_id=9, fill=universe1)
cell9.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf707

# plates
cell10 = openmc.Cell(cell_id=10, fill=universe1)
cell10.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf708

# plates
cell11 = openmc.Cell(cell_id=11, fill=universe1)
cell11.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf709

# plates
cell12 = openmc.Cell(cell_id=12, fill=universe1)
cell12.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf710

# plates
cell13 = openmc.Cell(cell_id=13, fill=universe1)
cell13.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf711

# plates
cell14 = openmc.Cell(cell_id=14, fill=universe1)
cell14.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf712

# plates
cell15 = openmc.Cell(cell_id=15, fill=universe1)
cell15.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf713

# plates
cell16 = openmc.Cell(cell_id=16, fill=universe1)
cell16.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf714

# plates
cell17 = openmc.Cell(cell_id=17, fill=universe1)
cell17.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf715

# plates
cell18 = openmc.Cell(cell_id=18, fill=universe1)
cell18.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf716

# plates
cell19 = openmc.Cell(cell_id=19, fill=universe1)
cell19.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf717

# plates
cell20 = openmc.Cell(cell_id=20, fill=universe1)
cell20.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf718

# plates
cell21 = openmc.Cell(cell_id=21, fill=universe1)
cell21.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf719

# plates
cell22 = openmc.Cell(cell_id=22, fill=universe1)
cell22.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf720

# plates
cell23 = openmc.Cell(cell_id=23, fill=universe1)
cell23.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf721

# plates
cell24 = openmc.Cell(cell_id=24, fill=universe1)
cell24.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf722

# plates
cell25 = openmc.Cell(cell_id=25, fill=universe1)
cell25.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf723

# plates
cell26 = openmc.Cell(cell_id=26, fill=universe1)
cell26.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf724

# plates
cell27 = openmc.Cell(cell_id=27, fill=universe1)
cell27.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf725

# plates
cell28 = openmc.Cell(cell_id=28, fill=universe1)
cell28.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf726

# plates
cell29 = openmc.Cell(cell_id=29, fill=universe1)
cell29.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf727

# plates
cell30 = openmc.Cell(cell_id=30, fill=universe1)
cell30.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf728

# plates
cell31 = openmc.Cell(cell_id=31, fill=universe1)
cell31.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf729

# plates
cell32 = openmc.Cell(cell_id=32, fill=universe1)
cell32.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf730

# plates
cell33 = openmc.Cell(cell_id=33, fill=universe1)
cell33.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf731

# plates
cell34 = openmc.Cell(cell_id=34, fill=universe1)
cell34.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf732

# plates
cell35 = openmc.Cell(cell_id=35, fill=universe1)
cell35.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf733

# plates
cell36 = openmc.Cell(cell_id=36, fill=universe1)
cell36.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf734

# plates
cell37 = openmc.Cell(cell_id=37, fill=universe1)
cell37.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf735

# plates
cell38 = openmc.Cell(cell_id=38, fill=universe1)
cell38.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf736

# frod
cell39 = openmc.Cell(cell_id=39, fill=universe2)
cell39.translation = (-5.593, 31.829907, 0.0)
cell39.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf103

# frod
cell40 = openmc.Cell(cell_id=40, fill=universe2)
cell40.translation = (-3.995, 31.829907, 0.0)
cell40.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf104

# frod
cell41 = openmc.Cell(cell_id=41, fill=universe2)
cell41.translation = (-2.397, 31.829907, 0.0)
cell41.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf105

# frod
cell42 = openmc.Cell(cell_id=42, fill=universe2)
cell42.translation = (-0.799, 31.829907, 0.0)
cell42.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf106

# frod
cell43 = openmc.Cell(cell_id=43, fill=universe2)
cell43.translation = (0.799, 31.829907, 0.0)
cell43.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf107

# frod
cell44 = openmc.Cell(cell_id=44, fill=universe2)
cell44.translation = (2.397, 31.829907, 0.0)
cell44.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf108

# frod
cell45 = openmc.Cell(cell_id=45, fill=universe2)
cell45.translation = (3.995, 31.829907, 0.0)
cell45.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf109

# frod
cell46 = openmc.Cell(cell_id=46, fill=universe2)
cell46.translation = (5.593, 31.829907, 0.0)
cell46.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf110

# frod
cell47 = openmc.Cell(cell_id=47, fill=universe2)
cell47.translation = (-13.583, 29.062089, 0.0)
cell47.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf115

# frod
cell48 = openmc.Cell(cell_id=48, fill=universe2)
cell48.translation = (13.583, 29.062089, 0.0)
cell48.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf116

# frod
cell49 = openmc.Cell(cell_id=49, fill=universe2)
cell49.translation = (-15.98, 27.67818, 0.0)
cell49.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf117

# frod
cell50 = openmc.Cell(cell_id=50, fill=universe2)
cell50.translation = (15.98, 27.67818, 0.0)
cell50.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf118

# frod
cell51 = openmc.Cell(cell_id=51, fill=universe2)
cell51.translation = (-18.377, 26.294271, 0.0)
cell51.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf119

# frod
cell52 = openmc.Cell(cell_id=52, fill=universe2)
cell52.translation = (18.377, 26.294271, 0.0)
cell52.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf120

# frod
cell53 = openmc.Cell(cell_id=53, fill=universe2)
cell53.translation = (-24.769, 20.758635, 0.0)
cell53.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf127

# frod
cell54 = openmc.Cell(cell_id=54, fill=universe2)
cell54.translation = (24.769, 20.758635, 0.0)
cell54.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf128

# frod
cell55 = openmc.Cell(cell_id=55, fill=universe2)
cell55.translation = (-25.568, 19.374726, 0.0)
cell55.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf129

# frod
cell56 = openmc.Cell(cell_id=56, fill=universe2)
cell56.translation = (25.568, 19.374726, 0.0)
cell56.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf130

# frod
cell57 = openmc.Cell(cell_id=57, fill=universe2)
cell57.translation = (-26.367, 17.990817, 0.0)
cell57.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf131

# frod
cell58 = openmc.Cell(cell_id=58, fill=universe2)
cell58.translation = (26.367, 17.990817, 0.0)
cell58.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf132

# frod
cell59 = openmc.Cell(cell_id=59, fill=universe2)
cell59.translation = (-27.166, 16.606908, 0.0)
cell59.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf133

# frod
cell60 = openmc.Cell(cell_id=60, fill=universe2)
cell60.translation = (27.166, 16.606908, 0.0)
cell60.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf134

# frod
cell61 = openmc.Cell(cell_id=61, fill=universe2)
cell61.translation = (-27.965, 15.222999, 0.0)
cell61.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf135

# frod
cell62 = openmc.Cell(cell_id=62, fill=universe2)
cell62.translation = (27.965, 15.222999, 0.0)
cell62.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf136

# frod
cell63 = openmc.Cell(cell_id=63, fill=universe2)
cell63.translation = (-28.764, 13.83909, 0.0)
cell63.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf137

# frod
cell64 = openmc.Cell(cell_id=64, fill=universe2)
cell64.translation = (28.764, 13.83909, 0.0)
cell64.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf138

# frod
cell65 = openmc.Cell(cell_id=65, fill=universe2)
cell65.translation = (-29.563, 12.455181, 0.0)
cell65.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf139

# frod
cell66 = openmc.Cell(cell_id=66, fill=universe2)
cell66.translation = (29.563, 12.455181, 0.0)
cell66.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf140

# frod
cell67 = openmc.Cell(cell_id=67, fill=universe2)
cell67.translation = (-30.362, 11.071272, 0.0)
cell67.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf141

# frod
cell68 = openmc.Cell(cell_id=68, fill=universe2)
cell68.translation = (30.362, 11.071272, 0.0)
cell68.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf142

# frod
cell69 = openmc.Cell(cell_id=69, fill=universe2)
cell69.translation = (-31.96, 2.767818, 0.0)
cell69.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf149

# frod
cell70 = openmc.Cell(cell_id=70, fill=universe2)
cell70.translation = (31.96, 2.767818, 0.0)
cell70.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf150

# frod
cell71 = openmc.Cell(cell_id=71, fill=universe2)
cell71.translation = (-31.96, 0.0, 0.0)
cell71.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf151

# frod
cell72 = openmc.Cell(cell_id=72, fill=universe2)
cell72.translation = (31.96, 0.0, 0.0)
cell72.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf152

# frod
cell73 = openmc.Cell(cell_id=73, fill=universe2)
cell73.translation = (-31.96, -2.767818, 0.0)
cell73.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf153

# frod
cell74 = openmc.Cell(cell_id=74, fill=universe2)
cell74.translation = (31.96, -2.767818, 0.0)
cell74.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf154

# frod
cell75 = openmc.Cell(cell_id=75, fill=universe2)
cell75.translation = (-30.362, -11.071272, 0.0)
cell75.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf161

# frod
cell76 = openmc.Cell(cell_id=76, fill=universe2)
cell76.translation = (30.362, -11.071272, 0.0)
cell76.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf162

# frod
cell77 = openmc.Cell(cell_id=77, fill=universe2)
cell77.translation = (-29.563, -12.455181, 0.0)
cell77.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf163

# frod
cell78 = openmc.Cell(cell_id=78, fill=universe2)
cell78.translation = (29.563, -12.455181, 0.0)
cell78.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf164

# frod
cell79 = openmc.Cell(cell_id=79, fill=universe2)
cell79.translation = (-28.764, -13.83909, 0.0)
cell79.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf165

# frod
cell80 = openmc.Cell(cell_id=80, fill=universe2)
cell80.translation = (28.764, -13.83909, 0.0)
cell80.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf166

# frod
cell81 = openmc.Cell(cell_id=81, fill=universe2)
cell81.translation = (-27.965, -15.222999, 0.0)
cell81.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf167

# frod
cell82 = openmc.Cell(cell_id=82, fill=universe2)
cell82.translation = (27.965, -15.222999, 0.0)
cell82.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf168

# frod
cell83 = openmc.Cell(cell_id=83, fill=universe2)
cell83.translation = (-27.166, -16.606908, 0.0)
cell83.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf169

# frod
cell84 = openmc.Cell(cell_id=84, fill=universe2)
cell84.translation = (27.166, -16.606908, 0.0)
cell84.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf170

# frod
cell85 = openmc.Cell(cell_id=85, fill=universe2)
cell85.translation = (-26.367, -17.990817, 0.0)
cell85.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf171

# frod
cell86 = openmc.Cell(cell_id=86, fill=universe2)
cell86.translation = (26.367, -17.990817, 0.0)
cell86.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf172

# frod
cell87 = openmc.Cell(cell_id=87, fill=universe2)
cell87.translation = (-25.568, -19.374726, 0.0)
cell87.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf173

# frod
cell88 = openmc.Cell(cell_id=88, fill=universe2)
cell88.translation = (25.568, -19.374726, 0.0)
cell88.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf174

# frod
cell89 = openmc.Cell(cell_id=89, fill=universe2)
cell89.translation = (-24.769, -20.758635, 0.0)
cell89.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf175

# frod
cell90 = openmc.Cell(cell_id=90, fill=universe2)
cell90.translation = (24.769, -20.758635, 0.0)
cell90.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf176

# frod
cell91 = openmc.Cell(cell_id=91, fill=universe2)
cell91.translation = (-18.377, -26.294271, 0.0)
cell91.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf183

# frod
cell92 = openmc.Cell(cell_id=92, fill=universe2)
cell92.translation = (18.377, -26.294271, 0.0)
cell92.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf184

# frod
cell93 = openmc.Cell(cell_id=93, fill=universe2)
cell93.translation = (-15.98, -27.67818, 0.0)
cell93.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf185

# frod
cell94 = openmc.Cell(cell_id=94, fill=universe2)
cell94.translation = (15.98, -27.67818, 0.0)
cell94.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf186

# frod
cell95 = openmc.Cell(cell_id=95, fill=universe2)
cell95.translation = (-13.583, -29.062089, 0.0)
cell95.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf187

# frod
cell96 = openmc.Cell(cell_id=96, fill=universe2)
cell96.translation = (13.583, -29.062089, 0.0)
cell96.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf188

# frod
cell97 = openmc.Cell(cell_id=97, fill=universe2)
cell97.translation = (-5.593, -31.829907, 0.0)
cell97.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf193

# frod
cell98 = openmc.Cell(cell_id=98, fill=universe2)
cell98.translation = (-3.995, -31.829907, 0.0)
cell98.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf194

# frod
cell99 = openmc.Cell(cell_id=99, fill=universe2)
cell99.translation = (-2.397, -31.829907, 0.0)
cell99.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf195

# frod
cell100 = openmc.Cell(cell_id=100, fill=universe2)
cell100.translation = (-0.799, -31.829907, 0.0)
cell100.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf196

# frod
cell101 = openmc.Cell(cell_id=101, fill=universe2)
cell101.translation = (0.799, -31.829907, 0.0)
cell101.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf197

# frod
cell102 = openmc.Cell(cell_id=102, fill=universe2)
cell102.translation = (2.397, -31.829907, 0.0)
cell102.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf198

# frod
cell103 = openmc.Cell(cell_id=103, fill=universe2)
cell103.translation = (3.995, -31.829907, 0.0)
cell103.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf199

# frod
cell104 = openmc.Cell(cell_id=104, fill=universe2)
cell104.translation = (5.593, -31.829907, 0.0)
cell104.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf91

# alles
cell105 = openmc.Cell(cell_id=105, fill=universe1)
cell105.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf22_0 | +surf22_1 | +surf22_2 | +surf22_3 | +surf22_4 | +surf22_5 | +surf22_6 | +surf22_7 | +surf22_8 | +surf22_9 | +surf22_10 | +surf22_11 | +surf22_12 | +surf22_13 | +surf22_14 | +surf22_15 | +surf22_16 | +surf22_17) & +surf201 & +surf202 & +surf203 & +surf204 & +surf205 & +surf206 & +surf207 & +surf208 & +surf209 & +surf210

# Water
cell115 = openmc.Cell(cell_id=115, fill=mat6)
cell115.region = (+surf15 | -surf15_zmin | +surf15_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)

# Alles
cell116 = openmc.Cell(cell_id=116, fill=universe1)
cell116.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & +surf17 & +surf18 & +surf19 & +surf20

# Alles
cell122 = openmc.Cell(cell_id=122, fill=universe1)
cell122.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & +surf17 & +surf18 & +surf19 & +surf20

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49, cell50, cell51, cell52, cell53, cell54, cell55, cell56, cell57, cell58, cell59, cell60, cell61, cell62, cell63, cell64, cell65, cell66, cell67, cell68, cell69, cell70, cell71, cell72, cell73, cell74, cell75, cell76, cell77, cell78, cell79, cell80, cell81, cell82, cell83, cell84, cell85, cell86, cell87, cell88, cell89, cell90, cell91, cell92, cell93, cell94, cell95, cell96, cell97, cell98, cell99, cell100, cell101, cell102, cell103, cell104, cell105, cell115, cell116, cell122])
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
source.space = openmc.stats.Point((0.0, 0.0, 48.26))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
