"""
LEU-COMP-THERM-005-12: 1,185 U(4.31)O2 rods in water; 1.598 cm pitch; 0gGd/L
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

# Water (w/o Gd)
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.680500e-02)
mat6.add_nuclide("O16", 3.340300e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Boundary condition
surf1 = openmc.ZCylinder(surface_id=1, x0=-22.86, y0=109.14, r=76.014, boundary_type="vacuum")
# Acrylic base plate
surf2 = openmc.ZCylinder(surface_id=2, x0=-2.54, y0=0.0, r=99.9)
# Propylene lattice plate - bottom -
surf3 = openmc.ZCylinder(surface_id=3, x0=0.809, y0=2.159, r=45.72)
# Propylene lattice plate - middle -
surf4 = openmc.ZCylinder(surface_id=4, x0=37.639, y0=38.989, r=45.72)
# Propylene lattice plate - top    -
surf5 = openmc.ZCylinder(surface_id=5, x0=86.28, y0=87.63, r=45.72)
# Rubber
surf11 = openmc.ZCylinder(surface_id=11, x0=0.0, y0=2.2225, r=0.6415)
# U(4.31)O2 fuel
surf12 = openmc.ZCylinder(surface_id=12, x0=2.2225, y0=94.2975, r=0.6325)
# Rubber
surf13 = openmc.ZCylinder(surface_id=13, x0=94.2975, y0=96.52, r=0.6415)
# Clad inner
surf14 = openmc.ZCylinder(surface_id=14, r=0.6415)
# Clad outer
surf15 = openmc.ZCylinder(surface_id=15, x0=0.0, y0=96.52, r=0.7075)
# Hole
surf16 = openmc.ZCylinder(surface_id=16, x0=0.0, y0=96.52, r=0.714)
# surf17: Error converting surface type "c": could not convert string to float: 'tr'
# surf18: Error converting surface type "c": could not convert string to float: 'tr'
# surf19: Error converting surface type "c": could not convert string to float: 'tr'
# surf20: Error converting surface type "c": could not convert string to float: 'tr'
# Prism 21: 12-sided polygon
surf21_0 = openmc.Plane(a=0.8660254671, b=0.4999998903, c=0, d=27.6781739287)
surf21_1 = openmc.Plane(a=0.5000001097, b=0.8660253405, c=0, d=28.7640063095)
surf21_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=27.6781800000)
surf21_3 = openmc.Plane(a=-0.5000001097, b=0.8660253405, c=0, d=28.7640063095)
surf21_4 = openmc.Plane(a=-0.8660254671, b=0.4999998903, c=0, d=27.6781739287)
surf21_5 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=28.7640000000)
surf21_6 = openmc.Plane(a=-0.8660254671, b=-0.4999998903, c=0, d=27.6781739287)
surf21_7 = openmc.Plane(a=-0.5000001097, b=-0.8660253405, c=0, d=28.7640063095)
surf21_8 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=27.6781800000)
surf21_9 = openmc.Plane(a=0.5000001097, b=-0.8660253405, c=0, d=28.7640063095)
surf21_10 = openmc.Plane(a=0.8660254671, b=-0.4999998903, c=0, d=27.6781739287)
surf21_11 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=28.7640000000)
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
# surf101: Error converting surface type "c": could not convert string to float: 'tr'
# surf102: Error converting surface type "c": could not convert string to float: 'tr'
# surf103: Error converting surface type "c": could not convert string to float: 'tr'
# surf104: Error converting surface type "c": could not convert string to float: 'tr'
# surf105: Error converting surface type "c": could not convert string to float: 'tr'
# surf106: Error converting surface type "c": could not convert string to float: 'tr'
# surf107: Error converting surface type "c": could not convert string to float: 'tr'
# surf108: Error converting surface type "c": could not convert string to float: 'tr'
# surf109: Error converting surface type "c": could not convert string to float: 'tr'
# surf110: Error converting surface type "c": could not convert string to float: 'tr'
# surf111: Error converting surface type "c": could not convert string to float: 'tr'
# surf112: Error converting surface type "c": could not convert string to float: 'tr'
# surf113: Error converting surface type "c": could not convert string to float: 'tr'
# surf114: Error converting surface type "c": could not convert string to float: 'tr'
# surf115: Error converting surface type "c": could not convert string to float: 'tr'
# surf116: Error converting surface type "c": could not convert string to float: 'tr'
# surf117: Error converting surface type "c": could not convert string to float: 'tr'
# surf118: Error converting surface type "c": could not convert string to float: 'tr'
# surf119: Error converting surface type "c": could not convert string to float: 'tr'
# surf120: Error converting surface type "c": could not convert string to float: 'tr'
# surf121: Error converting surface type "c": could not convert string to float: 'tr'
# surf122: Error converting surface type "c": could not convert string to float: 'tr'
# surf123: Error converting surface type "c": could not convert string to float: 'tr'
# surf124: Error converting surface type "c": could not convert string to float: 'tr'
# surf125: Error converting surface type "c": could not convert string to float: 'tr'
# surf126: Error converting surface type "c": could not convert string to float: 'tr'
# surf127: Error converting surface type "c": could not convert string to float: 'tr'
# surf128: Error converting surface type "c": could not convert string to float: 'tr'
# surf129: Error converting surface type "c": could not convert string to float: 'tr'
# surf130: Error converting surface type "c": could not convert string to float: 'tr'
# surf131: Error converting surface type "c": could not convert string to float: 'tr'
# surf132: Error converting surface type "c": could not convert string to float: 'tr'
# surf133: Error converting surface type "c": could not convert string to float: 'tr'
# surf134: Error converting surface type "c": could not convert string to float: 'tr'
# surf135: Error converting surface type "c": could not convert string to float: 'tr'
# surf136: Error converting surface type "c": could not convert string to float: 'tr'
# surf137: Error converting surface type "c": could not convert string to float: 'tr'
# surf138: Error converting surface type "c": could not convert string to float: 'tr'
# surf139: Error converting surface type "c": could not convert string to float: 'tr'
# surf140: Error converting surface type "c": could not convert string to float: 'tr'
# surf141: Error converting surface type "c": could not convert string to float: 'tr'
# surf142: Error converting surface type "c": could not convert string to float: 'tr'
# surf143: Error converting surface type "c": could not convert string to float: 'tr'
# surf144: Error converting surface type "c": could not convert string to float: 'tr'
# surf145: Error converting surface type "c": could not convert string to float: 'tr'
# surf146: Error converting surface type "c": could not convert string to float: 'tr'
# surf147: Error converting surface type "c": could not convert string to float: 'tr'
# surf148: Error converting surface type "c": could not convert string to float: 'tr'
# surf149: Error converting surface type "c": could not convert string to float: 'tr'
# surf150: Error converting surface type "c": could not convert string to float: 'tr'
# surf151: Error converting surface type "c": could not convert string to float: 'tr'
# surf152: Error converting surface type "c": could not convert string to float: 'tr'
# surf153: Error converting surface type "c": could not convert string to float: 'tr'
# surf154: Error converting surface type "c": could not convert string to float: 'tr'
# surf155: Error converting surface type "c": could not convert string to float: 'tr'
# surf156: Error converting surface type "c": could not convert string to float: 'tr'
# surf157: Error converting surface type "c": could not convert string to float: 'tr'
# surf158: Error converting surface type "c": could not convert string to float: 'tr'
# surf159: Error converting surface type "c": could not convert string to float: 'tr'
# surf160: Error converting surface type "c": could not convert string to float: 'tr'
# surf161: Error converting surface type "c": could not convert string to float: 'tr'
# surf162: Error converting surface type "c": could not convert string to float: 'tr'
# surf163: Error converting surface type "c": could not convert string to float: 'tr'
# surf164: Error converting surface type "c": could not convert string to float: 'tr'
# surf165: Error converting surface type "c": could not convert string to float: 'tr'
# surf166: Error converting surface type "c": could not convert string to float: 'tr'
# surf167: Error converting surface type "c": could not convert string to float: 'tr'
# surf168: Error converting surface type "c": could not convert string to float: 'tr'
# surf169: Error converting surface type "c": could not convert string to float: 'tr'
# surf170: Error converting surface type "c": could not convert string to float: 'tr'
# surf171: Error converting surface type "c": could not convert string to float: 'tr'
# surf172: Error converting surface type "c": could not convert string to float: 'tr'
# surf173: Error converting surface type "c": could not convert string to float: 'tr'
# surf174: Error converting surface type "c": could not convert string to float: 'tr'
# surf175: Error converting surface type "c": could not convert string to float: 'tr'
# surf176: Error converting surface type "c": could not convert string to float: 'tr'
# surf177: Error converting surface type "c": could not convert string to float: 'tr'
# surf178: Error converting surface type "c": could not convert string to float: 'tr'
# surf179: Error converting surface type "c": could not convert string to float: 'tr'
# surf180: Error converting surface type "c": could not convert string to float: 'tr'
# surf181: Error converting surface type "c": could not convert string to float: 'tr'
# surf182: Error converting surface type "c": could not convert string to float: 'tr'
# surf183: Error converting surface type "c": could not convert string to float: 'tr'
# surf184: Error converting surface type "c": could not convert string to float: 'tr'
# surf185: Error converting surface type "c": could not convert string to float: 'tr'
# surf186: Error converting surface type "c": could not convert string to float: 'tr'
# surf187: Error converting surface type "c": could not convert string to float: 'tr'
# surf188: Error converting surface type "c": could not convert string to float: 'tr'
# surf189: Error converting surface type "c": could not convert string to float: 'tr'
# surf190: Error converting surface type "c": could not convert string to float: 'tr'
# surf191: Error converting surface type "c": could not convert string to float: 'tr'
# surf192: Error converting surface type "c": could not convert string to float: 'tr'
# surf193: Error converting surface type "c": could not convert string to float: 'tr'
# surf194: Error converting surface type "c": could not convert string to float: 'tr'
# surf195: Error converting surface type "c": could not convert string to float: 'tr'
# surf196: Error converting surface type "c": could not convert string to float: 'tr'
# surf197: Error converting surface type "c": could not convert string to float: 'tr'
# surf198: Error converting surface type "c": could not convert string to float: 'tr'
# surf201: Error converting surface type "c": could not convert string to float: 'tr'
# surf202: Error converting surface type "c": could not convert string to float: 'tr'
# surf203: Error converting surface type "c": could not convert string to float: 'tr'
# surf204: Error converting surface type "c": could not convert string to float: 'tr'
# surf205: Error converting surface type "c": could not convert string to float: 'tr'
# surf206: Error converting surface type "c": could not convert string to float: 'tr'
# surf207: Error converting surface type "c": could not convert string to float: 'tr'
# surf208: Error converting surface type "c": could not convert string to float: 'tr'
# surf209: Error converting surface type "c": could not convert string to float: 'tr'
# surf210: Error converting surface type "c": could not convert string to float: 'tr'
# surf211: Error converting surface type "c": could not convert string to float: 'tr'
# surf212: Error converting surface type "c": could not convert string to float: 'tr'
# surf213: Error converting surface type "c": could not convert string to float: 'tr'
# surf214: Error converting surface type "c": could not convert string to float: 'tr'
# surf215: Error converting surface type "c": could not convert string to float: 'tr'
# surf216: Error converting surface type "c": could not convert string to float: 'tr'
# surf217: Error converting surface type "c": could not convert string to float: 'tr'
# surf218: Error converting surface type "c": could not convert string to float: 'tr'
# surf219: Error converting surface type "c": could not convert string to float: 'tr'
# surf220: Error converting surface type "c": could not convert string to float: 'tr'
# surf221: Error converting surface type "c": could not convert string to float: 'tr'
# surf222: Error converting surface type "c": could not convert string to float: 'tr'
# surf223: Error converting surface type "c": could not convert string to float: 'tr'
# surf224: Error converting surface type "c": could not convert string to float: 'tr'
# surf225: Error converting surface type "c": could not convert string to float: 'tr'
# surf226: Error converting surface type "c": could not convert string to float: 'tr'
# surf227: Error converting surface type "c": could not convert string to float: 'tr'
# surf228: Error converting surface type "c": could not convert string to float: 'tr'
# surf229: Error converting surface type "c": could not convert string to float: 'tr'
# surf230: Error converting surface type "c": could not convert string to float: 'tr'
# surf231: Error converting surface type "c": could not convert string to float: 'tr'
# surf232: Error converting surface type "c": could not convert string to float: 'tr'
# surf233: Error converting surface type "c": could not convert string to float: 'tr'
# surf234: Error converting surface type "c": could not convert string to float: 'tr'
# surf235: Error converting surface type "c": could not convert string to float: 'tr'
# surf236: Error converting surface type "c": could not convert string to float: 'tr'
# surf237: Error converting surface type "c": could not convert string to float: 'tr'
# surf238: Error converting surface type "c": could not convert string to float: 'tr'
# surf239: Error converting surface type "c": could not convert string to float: 'tr'
# surf240: Error converting surface type "c": could not convert string to float: 'tr'
# surf241: Error converting surface type "c": could not convert string to float: 'tr'
# surf242: Error converting surface type "c": could not convert string to float: 'tr'
# surf243: Error converting surface type "c": could not convert string to float: 'tr'
# surf301: Error converting surface type "c": could not convert string to float: 'tr'
# surf302: Error converting surface type "c": could not convert string to float: 'tr'
# surf303: Error converting surface type "c": could not convert string to float: 'tr'
# surf304: Error converting surface type "c": could not convert string to float: 'tr'
# surf305: Error converting surface type "c": could not convert string to float: 'tr'
# surf306: Error converting surface type "c": could not convert string to float: 'tr'
# surf307: Error converting surface type "c": could not convert string to float: 'tr'
# surf308: Error converting surface type "c": could not convert string to float: 'tr'
# surf309: Error converting surface type "c": could not convert string to float: 'tr'
# surf310: Error converting surface type "c": could not convert string to float: 'tr'
# surf311: Error converting surface type "c": could not convert string to float: 'tr'
# surf312: Error converting surface type "c": could not convert string to float: 'tr'
# surf313: Error converting surface type "c": could not convert string to float: 'tr'
# surf314: Error converting surface type "c": could not convert string to float: 'tr'
# surf315: Error converting surface type "c": could not convert string to float: 'tr'
# surf316: Error converting surface type "c": could not convert string to float: 'tr'
# surf317: Error converting surface type "c": could not convert string to float: 'tr'
# surf318: Error converting surface type "c": could not convert string to float: 'tr'
# surf319: Error converting surface type "c": could not convert string to float: 'tr'
# surf320: Error converting surface type "c": could not convert string to float: 'tr'
# surf321: Error converting surface type "c": could not convert string to float: 'tr'
# surf322: Error converting surface type "c": could not convert string to float: 'tr'
# surf323: Error converting surface type "c": could not convert string to float: 'tr'
# surf324: Error converting surface type "c": could not convert string to float: 'tr'
# surf325: Error converting surface type "c": could not convert string to float: 'tr'
# surf326: Error converting surface type "c": could not convert string to float: 'tr'
# surf327: Error converting surface type "c": could not convert string to float: 'tr'
# surf328: Error converting surface type "c": could not convert string to float: 'tr'
# surf329: Error converting surface type "c": could not convert string to float: 'tr'
# surf330: Error converting surface type "c": could not convert string to float: 'tr'
# surf331: Error converting surface type "c": could not convert string to float: 'tr'
# surf332: Error converting surface type "c": could not convert string to float: 'tr'
# surf333: Error converting surface type "c": could not convert string to float: 'tr'
# surf334: Error converting surface type "c": could not convert string to float: 'tr'
# surf335: Error converting surface type "c": could not convert string to float: 'tr'
# surf336: Error converting surface type "c": could not convert string to float: 'tr'
# surf337: Error converting surface type "c": could not convert string to float: 'tr'
# surf338: Error converting surface type "c": could not convert string to float: 'tr'
# surf339: Error converting surface type "c": could not convert string to float: 'tr'
# surf340: Error converting surface type "c": could not convert string to float: 'tr'
# surf341: Error converting surface type "c": could not convert string to float: 'tr'
# surf701: Error converting surface type "c": could not convert string to float: 'tr'
# surf702: Error converting surface type "c": could not convert string to float: 'tr'
# surf703: Error converting surface type "c": could not convert string to float: 'tr'
# surf704: Error converting surface type "c": could not convert string to float: 'tr'
# surf705: Error converting surface type "c": could not convert string to float: 'tr'
# surf706: Error converting surface type "c": could not convert string to float: 'tr'
# surf707: Error converting surface type "c": could not convert string to float: 'tr'
# surf708: Error converting surface type "c": could not convert string to float: 'tr'
# surf709: Error converting surface type "c": could not convert string to float: 'tr'
# surf710: Error converting surface type "c": could not convert string to float: 'tr'
# surf711: Error converting surface type "c": could not convert string to float: 'tr'
# surf712: Error converting surface type "c": could not convert string to float: 'tr'
# surf713: Error converting surface type "c": could not convert string to float: 'tr'
# surf714: Error converting surface type "c": could not convert string to float: 'tr'
# surf715: Error converting surface type "c": could not convert string to float: 'tr'
# surf716: Error converting surface type "c": could not convert string to float: 'tr'
# surf717: Error converting surface type "c": could not convert string to float: 'tr'
# surf718: Error converting surface type "c": could not convert string to float: 'tr'
# surf719: Error converting surface type "c": could not convert string to float: 'tr'
# surf720: Error converting surface type "c": could not convert string to float: 'tr'
# surf721: Error converting surface type "c": could not convert string to float: 'tr'
# surf722: Error converting surface type "c": could not convert string to float: 'tr'
# surf723: Error converting surface type "c": could not convert string to float: 'tr'
# surf724: Error converting surface type "c": could not convert string to float: 'tr'
# surf725: Error converting surface type "c": could not convert string to float: 'tr'
# surf726: Error converting surface type "c": could not convert string to float: 'tr'
# surf727: Error converting surface type "c": could not convert string to float: 'tr'
# surf728: Error converting surface type "c": could not convert string to float: 'tr'
# surf729: Error converting surface type "c": could not convert string to float: 'tr'
# surf730: Error converting surface type "c": could not convert string to float: 'tr'
# surf731: Error converting surface type "c": could not convert string to float: 'tr'
# surf732: Error converting surface type "c": could not convert string to float: 'tr'
# surf733: Error converting surface type "c": could not convert string to float: 'tr'
# surf734: Error converting surface type "c": could not convert string to float: 'tr'
# surf735: Error converting surface type "c": could not convert string to float: 'tr'
# surf736: Error converting surface type "c": could not convert string to float: 'tr'

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat5)
u1_cell0.region = -surf1 & -surf2
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = -surf1 & -surf3
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = -surf1 & -surf4
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = -surf1 & -surf5
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf12 & -surf15
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = -surf11 & +surf12 & -surf15
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = -surf13 & +surf12 & -surf15
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = +surf11 & +surf12 & +surf13 & +surf14 & -surf15
u2_cell4 = openmc.Cell(fill=mat6)
u2_cell4.region = +surf15 & -surf16
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat6)
u4_cell0.region = -surf1 & -surf16
u4_cell1 = openmc.Cell(fill=mat6)
u4_cell1.region = -surf1
u4_cell2 = openmc.Cell(fill=mat6)
u4_cell2.region = -surf1
u4_cell3 = openmc.Cell(fill=mat6)
u4_cell3.region = -surf1
u4_cell4 = openmc.Cell(fill=mat6)
u4_cell4.region = -surf1
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

# Lattice 5: 37x21 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-29.563, -29.062089]
lattice5.pitch = [1.598000, 2.767818]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
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
cell1.region = -surf1 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11)

# holes
cell2 = openmc.Cell(cell_id=2, fill=universe6)
cell2.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell9 = openmc.Cell(cell_id=9, fill=universe1)
cell9.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell10 = openmc.Cell(cell_id=10, fill=universe1)
cell10.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell11 = openmc.Cell(cell_id=11, fill=universe1)
cell11.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell12 = openmc.Cell(cell_id=12, fill=universe1)
cell12.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell13 = openmc.Cell(cell_id=13, fill=universe1)
cell13.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell14 = openmc.Cell(cell_id=14, fill=universe1)
cell14.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell15 = openmc.Cell(cell_id=15, fill=universe1)
cell15.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell16 = openmc.Cell(cell_id=16, fill=universe1)
cell16.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell17 = openmc.Cell(cell_id=17, fill=universe1)
cell17.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell18 = openmc.Cell(cell_id=18, fill=universe1)
cell18.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell19 = openmc.Cell(cell_id=19, fill=universe1)
cell19.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell20 = openmc.Cell(cell_id=20, fill=universe1)
cell20.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell21 = openmc.Cell(cell_id=21, fill=universe1)
cell21.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell22 = openmc.Cell(cell_id=22, fill=universe1)
cell22.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell23 = openmc.Cell(cell_id=23, fill=universe1)
cell23.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell24 = openmc.Cell(cell_id=24, fill=universe1)
cell24.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell25 = openmc.Cell(cell_id=25, fill=universe1)
cell25.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell26 = openmc.Cell(cell_id=26, fill=universe1)
cell26.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell27 = openmc.Cell(cell_id=27, fill=universe1)
cell27.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell28 = openmc.Cell(cell_id=28, fill=universe1)
cell28.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell29 = openmc.Cell(cell_id=29, fill=universe1)
cell29.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell30 = openmc.Cell(cell_id=30, fill=universe1)
cell30.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell31 = openmc.Cell(cell_id=31, fill=universe1)
cell31.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell32 = openmc.Cell(cell_id=32, fill=universe1)
cell32.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell33 = openmc.Cell(cell_id=33, fill=universe1)
cell33.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell34 = openmc.Cell(cell_id=34, fill=universe1)
cell34.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell35 = openmc.Cell(cell_id=35, fill=universe1)
cell35.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell36 = openmc.Cell(cell_id=36, fill=universe1)
cell36.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell37 = openmc.Cell(cell_id=37, fill=universe1)
cell37.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# plates
cell38 = openmc.Cell(cell_id=38, fill=universe1)
cell38.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell39 = openmc.Cell(cell_id=39, fill=universe2)
cell39.translation = (-7.99, 27.67818, 0.0)
cell39.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell40 = openmc.Cell(cell_id=40, fill=universe2)
cell40.translation = (-6.392, 27.67818, 0.0)
cell40.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell41 = openmc.Cell(cell_id=41, fill=universe2)
cell41.translation = (-4.794, 27.67818, 0.0)
cell41.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell42 = openmc.Cell(cell_id=42, fill=universe2)
cell42.translation = (-3.196, 27.67818, 0.0)
cell42.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell43 = openmc.Cell(cell_id=43, fill=universe2)
cell43.translation = (-1.598, 27.67818, 0.0)
cell43.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell44 = openmc.Cell(cell_id=44, fill=universe2)
cell44.translation = (0.0, 27.67818, 0.0)
cell44.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell45 = openmc.Cell(cell_id=45, fill=universe2)
cell45.translation = (1.598, 27.67818, 0.0)
cell45.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell46 = openmc.Cell(cell_id=46, fill=universe2)
cell46.translation = (3.196, 27.67818, 0.0)
cell46.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell47 = openmc.Cell(cell_id=47, fill=universe2)
cell47.translation = (4.794, 27.67818, 0.0)
cell47.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell48 = openmc.Cell(cell_id=48, fill=universe2)
cell48.translation = (6.392, 27.67818, 0.0)
cell48.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell49 = openmc.Cell(cell_id=49, fill=universe2)
cell49.translation = (-11.985, 26.294271, 0.0)
cell49.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell50 = openmc.Cell(cell_id=50, fill=universe2)
cell50.translation = (11.985, 26.294271, 0.0)
cell50.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell51 = openmc.Cell(cell_id=51, fill=universe2)
cell51.translation = (-14.382, 24.910362, 0.0)
cell51.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell52 = openmc.Cell(cell_id=52, fill=universe2)
cell52.translation = (14.382, 24.910362, 0.0)
cell52.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell53 = openmc.Cell(cell_id=53, fill=universe2)
cell53.translation = (-16.779, 23.526453, 0.0)
cell53.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell54 = openmc.Cell(cell_id=54, fill=universe2)
cell54.translation = (16.779, 23.526453, 0.0)
cell54.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell55 = openmc.Cell(cell_id=55, fill=universe2)
cell55.translation = (19.975, 20.758635, 0.0)
cell55.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell56 = openmc.Cell(cell_id=56, fill=universe2)
cell56.translation = (-20.774, 19.374726, 0.0)
cell56.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell57 = openmc.Cell(cell_id=57, fill=universe2)
cell57.translation = (20.774, 19.374726, 0.0)
cell57.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell58 = openmc.Cell(cell_id=58, fill=universe2)
cell58.translation = (-21.573, 17.990817, 0.0)
cell58.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell59 = openmc.Cell(cell_id=59, fill=universe2)
cell59.translation = (21.573, 17.990817, 0.0)
cell59.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell60 = openmc.Cell(cell_id=60, fill=universe2)
cell60.translation = (-22.372, 16.606908, 0.0)
cell60.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell61 = openmc.Cell(cell_id=61, fill=universe2)
cell61.translation = (22.372, 16.606908, 0.0)
cell61.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell62 = openmc.Cell(cell_id=62, fill=universe2)
cell62.translation = (-23.171, 15.222999, 0.0)
cell62.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell63 = openmc.Cell(cell_id=63, fill=universe2)
cell63.translation = (23.171, 15.222999, 0.0)
cell63.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell64 = openmc.Cell(cell_id=64, fill=universe2)
cell64.translation = (-23.97, 13.83909, 0.0)
cell64.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell65 = openmc.Cell(cell_id=65, fill=universe2)
cell65.translation = (23.97, 13.83909, 0.0)
cell65.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell66 = openmc.Cell(cell_id=66, fill=universe2)
cell66.translation = (-24.769, 12.455181, 0.0)
cell66.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell67 = openmc.Cell(cell_id=67, fill=universe2)
cell67.translation = (24.769, 12.455181, 0.0)
cell67.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell68 = openmc.Cell(cell_id=68, fill=universe2)
cell68.translation = (-25.568, 11.071272, 0.0)
cell68.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell69 = openmc.Cell(cell_id=69, fill=universe2)
cell69.translation = (25.568, 11.071272, 0.0)
cell69.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell70 = openmc.Cell(cell_id=70, fill=universe2)
cell70.translation = (-26.367, 9.687363, 0.0)
cell70.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell71 = openmc.Cell(cell_id=71, fill=universe2)
cell71.translation = (26.367, 9.687363, 0.0)
cell71.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell72 = openmc.Cell(cell_id=72, fill=universe2)
cell72.translation = (-27.166, 8.303454, 0.0)
cell72.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell73 = openmc.Cell(cell_id=73, fill=universe2)
cell73.translation = (27.166, 8.303454, 0.0)
cell73.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell74 = openmc.Cell(cell_id=74, fill=universe2)
cell74.translation = (-27.965, 6.919545, 0.0)
cell74.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell75 = openmc.Cell(cell_id=75, fill=universe2)
cell75.translation = (-28.764, 2.767818, 0.0)
cell75.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell76 = openmc.Cell(cell_id=76, fill=universe2)
cell76.translation = (28.764, 2.767818, 0.0)
cell76.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell77 = openmc.Cell(cell_id=77, fill=universe2)
cell77.translation = (-28.764, 0.0, 0.0)
cell77.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell78 = openmc.Cell(cell_id=78, fill=universe2)
cell78.translation = (28.764, 0.0, 0.0)
cell78.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell79 = openmc.Cell(cell_id=79, fill=universe2)
cell79.translation = (-28.764, -2.767818, 0.0)
cell79.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell80 = openmc.Cell(cell_id=80, fill=universe2)
cell80.translation = (28.764, -2.767818, 0.0)
cell80.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell81 = openmc.Cell(cell_id=81, fill=universe2)
cell81.translation = (27.965, -6.919545, 0.0)
cell81.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell82 = openmc.Cell(cell_id=82, fill=universe2)
cell82.translation = (-27.166, -8.303454, 0.0)
cell82.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell83 = openmc.Cell(cell_id=83, fill=universe2)
cell83.translation = (27.166, -8.303454, 0.0)
cell83.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell84 = openmc.Cell(cell_id=84, fill=universe2)
cell84.translation = (-26.367, -9.687363, 0.0)
cell84.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell85 = openmc.Cell(cell_id=85, fill=universe2)
cell85.translation = (26.367, -9.687363, 0.0)
cell85.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell86 = openmc.Cell(cell_id=86, fill=universe2)
cell86.translation = (-25.568, -11.071272, 0.0)
cell86.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell87 = openmc.Cell(cell_id=87, fill=universe2)
cell87.translation = (25.568, -11.071272, 0.0)
cell87.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell88 = openmc.Cell(cell_id=88, fill=universe2)
cell88.translation = (-24.769, -12.455181, 0.0)
cell88.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell89 = openmc.Cell(cell_id=89, fill=universe2)
cell89.translation = (24.769, -12.455181, 0.0)
cell89.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell90 = openmc.Cell(cell_id=90, fill=universe2)
cell90.translation = (-23.97, -13.83909, 0.0)
cell90.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell91 = openmc.Cell(cell_id=91, fill=universe2)
cell91.translation = (23.97, -13.83909, 0.0)
cell91.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell92 = openmc.Cell(cell_id=92, fill=universe2)
cell92.translation = (-23.171, -15.222999, 0.0)
cell92.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell93 = openmc.Cell(cell_id=93, fill=universe2)
cell93.translation = (23.171, -15.222999, 0.0)
cell93.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell94 = openmc.Cell(cell_id=94, fill=universe2)
cell94.translation = (-22.372, -16.606908, 0.0)
cell94.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell95 = openmc.Cell(cell_id=95, fill=universe2)
cell95.translation = (22.372, -16.606908, 0.0)
cell95.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell96 = openmc.Cell(cell_id=96, fill=universe2)
cell96.translation = (-21.573, -17.990817, 0.0)
cell96.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell97 = openmc.Cell(cell_id=97, fill=universe2)
cell97.translation = (21.573, -17.990817, 0.0)
cell97.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell98 = openmc.Cell(cell_id=98, fill=universe2)
cell98.translation = (-20.774, -19.374726, 0.0)
cell98.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell99 = openmc.Cell(cell_id=99, fill=universe2)
cell99.translation = (20.774, -19.374726, 0.0)
cell99.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell100 = openmc.Cell(cell_id=100, fill=universe2)
cell100.translation = (-19.975, -20.758635, 0.0)
cell100.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell101 = openmc.Cell(cell_id=101, fill=universe2)
cell101.translation = (-16.779, -23.526453, 0.0)
cell101.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell102 = openmc.Cell(cell_id=102, fill=universe2)
cell102.translation = (16.779, -23.526453, 0.0)
cell102.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell103 = openmc.Cell(cell_id=103, fill=universe2)
cell103.translation = (-14.382, -24.910362, 0.0)
cell103.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell104 = openmc.Cell(cell_id=104, fill=universe2)
cell104.translation = (14.382, -24.910362, 0.0)
cell104.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell105 = openmc.Cell(cell_id=105, fill=universe2)
cell105.translation = (-11.985, -26.294271, 0.0)
cell105.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell106 = openmc.Cell(cell_id=106, fill=universe2)
cell106.translation = (11.985, -26.294271, 0.0)
cell106.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell107 = openmc.Cell(cell_id=107, fill=universe2)
cell107.translation = (-6.392, -27.67818, 0.0)
cell107.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell108 = openmc.Cell(cell_id=108, fill=universe2)
cell108.translation = (-4.794, -27.67818, 0.0)
cell108.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell109 = openmc.Cell(cell_id=109, fill=universe2)
cell109.translation = (-3.196, -27.67818, 0.0)
cell109.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell110 = openmc.Cell(cell_id=110, fill=universe2)
cell110.translation = (-1.598, -27.67818, 0.0)
cell110.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell111 = openmc.Cell(cell_id=111, fill=universe2)
cell111.translation = (0.0, -27.67818, 0.0)
cell111.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell112 = openmc.Cell(cell_id=112, fill=universe2)
cell112.translation = (1.598, -27.67818, 0.0)
cell112.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell113 = openmc.Cell(cell_id=113, fill=universe2)
cell113.translation = (3.196, -27.67818, 0.0)
cell113.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell114 = openmc.Cell(cell_id=114, fill=universe2)
cell114.translation = (4.794, -27.67818, 0.0)
cell114.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell115 = openmc.Cell(cell_id=115, fill=universe2)
cell115.translation = (6.392, -27.67818, 0.0)
cell115.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell116 = openmc.Cell(cell_id=116, fill=universe2)
cell116.translation = (7.99, -27.67818, 0.0)
cell116.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell117 = openmc.Cell(cell_id=117, fill=universe2)
cell117.translation = (24.769, 15.222999, 0.0)
cell117.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# frod
cell118 = openmc.Cell(cell_id=118, fill=universe2)
cell118.translation = (-25.568, 13.83909, 0.0)
cell118.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17)

# alles
cell119 = openmc.Cell(cell_id=119, fill=universe1)
cell119.region = -surf1 & (+surf22_0 | +surf22_1 | +surf22_2 | +surf22_3 | +surf22_4 | +surf22_5 | +surf22_6 | +surf22_7 | +surf22_8 | +surf22_9 | +surf22_10 | +surf22_11 | +surf22_12 | +surf22_13 | +surf22_14 | +surf22_15 | +surf22_16 | +surf22_17)

# Water
cell129 = openmc.Cell(cell_id=129, fill=mat6)
cell129.region = +surf15 & -surf16

# Alles
cell130 = openmc.Cell(cell_id=130, fill=universe1)
cell130.region = -surf1 & +surf16

# Alles
cell136 = openmc.Cell(cell_id=136, fill=universe1)
cell136.region = -surf1 & +surf16

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46, cell47, cell48, cell49, cell50, cell51, cell52, cell53, cell54, cell55, cell56, cell57, cell58, cell59, cell60, cell61, cell62, cell63, cell64, cell65, cell66, cell67, cell68, cell69, cell70, cell71, cell72, cell73, cell74, cell75, cell76, cell77, cell78, cell79, cell80, cell81, cell82, cell83, cell84, cell85, cell86, cell87, cell88, cell89, cell90, cell91, cell92, cell93, cell94, cell95, cell96, cell97, cell98, cell99, cell100, cell101, cell102, cell103, cell104, cell105, cell106, cell107, cell108, cell109, cell110, cell111, cell112, cell113, cell114, cell115, cell116, cell117, cell118, cell119, cell129, cell130, cell136])
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
