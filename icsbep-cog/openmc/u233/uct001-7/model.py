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
# surf101: Unsupported surface type "sameas" with params ['17', 'tr', '-5.80136', '10.04825', '0', '102', 'sameas', '17', 'tr', '-4.35102', '10.04825', '0']
# surf103: Unsupported surface type "sameas" with params ['17', 'tr', '-2.90068', '10.04825', '0', '104', 'sameas', '17', 'tr', '-1.45034', '10.04825', '0']
# surf105: Unsupported surface type "sameas" with params ['17', 'tr', '0', '10.04825', '0', '106', 'sameas', '17', 'tr', '1.45034', '10.04825', '0']
# surf107: Unsupported surface type "sameas" with params ['17', 'tr', '2.90068', '10.04825', '0', '108', 'sameas', '17', 'tr', '4.35102', '10.04825', '0']
# surf109: Unsupported surface type "sameas" with params ['17', 'tr', '5.80136', '10.04825', '0']
# surf110: Unsupported surface type "sameas" with params ['17', 'tr', '-6.52653', '8.79222', '0', '111', 'sameas', '17', 'tr', '-5.07619', '8.79222', '0']
# surf112: Unsupported surface type "sameas" with params ['17', 'tr', '-3.62585', '8.79222', '0', '113', 'sameas', '17', 'tr', '-2.17551', '8.79222', '0']
# surf114: Unsupported surface type "sameas" with params ['17', 'tr', '-0.72517', '8.79222', '0', '115', 'sameas', '17', 'tr', '0.72517', '8.79222', '0']
# surf116: Unsupported surface type "sameas" with params ['17', 'tr', '2.17551', '8.79222', '0', '117', 'sameas', '17', 'tr', '3.62585', '8.79222', '0']
# surf118: Unsupported surface type "sameas" with params ['17', 'tr', '5.07619', '8.79222', '0', '119', 'sameas', '17', 'tr', '6.52653', '8.79222', '0']
# surf120: Unsupported surface type "sameas" with params ['17', 'tr', '-7.25170', '7.53619', '0', '121', 'sameas', '17', 'tr', '-5.80136', '7.53619', '0']
# surf122: Unsupported surface type "sameas" with params ['17', 'tr', '-4.35102', '7.53619', '0', '123', 'sameas', '17', 'tr', '-2.90068', '7.53619', '0']
# surf124: Unsupported surface type "sameas" with params ['17', 'tr', '-1.45034', '7.53619', '0', '125', 'sameas', '17', 'tr', '0', '7.53619', '0']
# surf126: Unsupported surface type "sameas" with params ['17', 'tr', '1.45034', '7.53619', '0', '127', 'sameas', '17', 'tr', '2.90068', '7.53619', '0']
# surf128: Unsupported surface type "sameas" with params ['17', 'tr', '4.35102', '7.53619', '0', '129', 'sameas', '17', 'tr', '5.80136', '7.53619', '0']
# surf130: Unsupported surface type "sameas" with params ['17', 'tr', '7.25170', '7.53619', '0']
# surf131: Unsupported surface type "sameas" with params ['17', 'tr', '-7.97687', '6.28016', '0', '132', 'sameas', '17', 'tr', '-6.52653', '6.28016', '0']
# surf133: Unsupported surface type "sameas" with params ['17', 'tr', '-5.07619', '6.28016', '0', '134', 'sameas', '17', 'tr', '-3.62585', '6.28016', '0']
# surf135: Unsupported surface type "sameas" with params ['17', 'tr', '-2.17551', '6.28016', '0', '136', 'sameas', '17', 'tr', '-0.72517', '6.28016', '0']
# surf137: Unsupported surface type "sameas" with params ['17', 'tr', '0.72517', '6.28016', '0', '138', 'sameas', '17', 'tr', '2.17551', '6.28016', '0']
# surf139: Unsupported surface type "sameas" with params ['17', 'tr', '3.62585', '6.28016', '0', '140', 'sameas', '17', 'tr', '5.07619', '6.28016', '0']
# surf141: Unsupported surface type "sameas" with params ['17', 'tr', '6.52653', '6.28016', '0', '142', 'sameas', '17', 'tr', '7.97687', '6.28016', '0']
# surf143: Unsupported surface type "sameas" with params ['17', 'tr', '-8.70204', '5.02413', '0', '144', 'sameas', '17', 'tr', '-7.25170', '5.02413', '0']
# surf145: Unsupported surface type "sameas" with params ['17', 'tr', '-5.80136', '5.02413', '0', '146', 'sameas', '17', 'tr', '-4.35102', '5.02413', '0']
# surf147: Unsupported surface type "sameas" with params ['17', 'tr', '-2.90068', '5.02413', '0', '148', 'sameas', '17', 'tr', '-1.45034', '5.02413', '0']
# surf149: Unsupported surface type "sameas" with params ['17', 'tr', '0', '5.02413', '0', '150', 'sameas', '17', 'tr', '1.45034', '5.02413', '0']
# surf151: Unsupported surface type "sameas" with params ['17', 'tr', '2.90068', '5.02413', '0', '152', 'sameas', '17', 'tr', '4.35102', '5.02413', '0']
# surf153: Unsupported surface type "sameas" with params ['17', 'tr', '5.80136', '5.02413', '0', '154', 'sameas', '17', 'tr', '7.25170', '5.02413', '0']
# surf155: Unsupported surface type "sameas" with params ['17', 'tr', '8.70204', '5.02413', '0']
# surf156: Unsupported surface type "sameas" with params ['17', 'tr', '-9.42721', '3.76809', '0', '157', 'sameas', '17', 'tr', '-7.97687', '3.76809', '0']
# surf158: Unsupported surface type "sameas" with params ['17', 'tr', '-6.52653', '3.76809', '0', '159', 'sameas', '17', 'tr', '-5.07619', '3.76809', '0']
# surf160: Unsupported surface type "sameas" with params ['17', 'tr', '-3.62585', '3.76809', '0', '161', 'sameas', '17', 'tr', '-2.17551', '3.76809', '0']
# surf162: Unsupported surface type "sameas" with params ['17', 'tr', '-0.72517', '3.76809', '0', '163', 'sameas', '17', 'tr', '0.72517', '3.76809', '0']
# surf164: Unsupported surface type "sameas" with params ['17', 'tr', '2.17551', '3.76809', '0', '165', 'sameas', '17', 'tr', '3.62585', '3.76809', '0']
# surf166: Unsupported surface type "sameas" with params ['17', 'tr', '5.07619', '3.76809', '0', '167', 'sameas', '17', 'tr', '6.52653', '3.76809', '0']
# surf168: Unsupported surface type "sameas" with params ['17', 'tr', '7.97687', '3.76809', '0', '169', 'sameas', '17', 'tr', '9.42721', '3.76809', '0']
# surf170: Unsupported surface type "sameas" with params ['17', 'tr', '-10.15238', '2.51206', '0', '171', 'sameas', '17', 'tr', '-8.70204', '2.51206', '0']
# surf172: Unsupported surface type "sameas" with params ['17', 'tr', '-7.25170', '2.51206', '0', '173', 'sameas', '17', 'tr', '-5.80136', '2.51206', '0']
# surf174: Unsupported surface type "sameas" with params ['17', 'tr', '-4.35102', '2.51206', '0', '175', 'sameas', '17', 'tr', '-2.90068', '2.51206', '0']
# surf176: Unsupported surface type "sameas" with params ['17', 'tr', '-1.45034', '2.51206', '0', '177', 'sameas', '17', 'tr', '0', '2.51206', '0']
# surf178: Unsupported surface type "sameas" with params ['17', 'tr', '1.45034', '2.51206', '0', '179', 'sameas', '17', 'tr', '2.90068', '2.51206', '0']
# surf180: Unsupported surface type "sameas" with params ['17', 'tr', '4.35102', '2.51206', '0', '181', 'sameas', '17', 'tr', '5.80136', '2.51206', '0']
# surf182: Unsupported surface type "sameas" with params ['17', 'tr', '7.25170', '2.51206', '0', '183', 'sameas', '17', 'tr', '8.70204', '2.51206', '0']
# surf184: Unsupported surface type "sameas" with params ['17', 'tr', '10.15238', '2.51206', '0']
# surf185: Unsupported surface type "sameas" with params ['17', 'tr', '-10.87755', '1.25603', '0', '186', 'sameas', '17', 'tr', '-9.42721', '1.25603', '0']
# surf187: Unsupported surface type "sameas" with params ['17', 'tr', '-7.97687', '1.25603', '0', '188', 'sameas', '17', 'tr', '-6.52653', '1.25603', '0']
# surf189: Unsupported surface type "sameas" with params ['17', 'tr', '-5.07619', '1.25603', '0', '190', 'sameas', '17', 'tr', '-3.62585', '1.25603', '0']
# surf191: Unsupported surface type "sameas" with params ['17', 'tr', '-2.17551', '1.25603', '0', '192', 'sameas', '17', 'tr', '-0.72517', '1.25603', '0']
# surf193: Unsupported surface type "sameas" with params ['17', 'tr', '0.72517', '1.25603', '0', '194', 'sameas', '17', 'tr', '2.17551', '1.25603', '0']
# surf195: Unsupported surface type "sameas" with params ['17', 'tr', '3.62585', '1.25603', '0', '196', 'sameas', '17', 'tr', '5.07619', '1.25603', '0']
# surf197: Unsupported surface type "sameas" with params ['17', 'tr', '6.52653', '1.25603', '0', '198', 'sameas', '17', 'tr', '7.97687', '1.25603', '0']
# surf199: Unsupported surface type "sameas" with params ['17', 'tr', '9.42721', '1.25603', '0', '200', 'sameas', '17', 'tr', '10.87755', '1.25603', '0']
# surf201: Unsupported surface type "sameas" with params ['17', 'tr', '-11.60272', '0', '0', '202', 'sameas', '17', 'tr', '-10.15238', '0', '0']
# surf203: Unsupported surface type "sameas" with params ['17', 'tr', '-8.70204', '0', '0', '204', 'sameas', '17', 'tr', '-7.25170', '0', '0']
# surf205: Unsupported surface type "sameas" with params ['17', 'tr', '-5.80136', '0', '0', '206', 'sameas', '17', 'tr', '-4.35102', '0', '0']
# surf207: Unsupported surface type "sameas" with params ['17', 'tr', '-2.90068', '0', '0', '208', 'sameas', '17', 'tr', '-1.45034', '0', '0']
# surf209: Unsupported surface type "sameas" with params ['17', 'tr', '0', '0', '0', '210', 'sameas', '17', 'tr', '1.45034', '0', '0']
# surf211: Unsupported surface type "sameas" with params ['17', 'tr', '2.90068', '0', '0', '212', 'sameas', '17', 'tr', '4.35102', '0', '0']
# surf213: Unsupported surface type "sameas" with params ['17', 'tr', '5.80136', '0', '0', '214', 'sameas', '17', 'tr', '7.25170', '0', '0']
# surf215: Unsupported surface type "sameas" with params ['17', 'tr', '8.70204', '0', '0', '216', 'sameas', '17', 'tr', '10.15238', '0', '0']
# surf217: Unsupported surface type "sameas" with params ['17', 'tr', '11.60272', '0', '0', '1218', 'sameas', '17', 'tr', '13.05306', '0', '0']
# surf218: Unsupported surface type "sameas" with params ['17', 'tr', '-10.87755', '-1.25603', '0', '219', 'sameas', '17', 'tr', '-9.42721', '-1.25603', '0']
# surf220: Unsupported surface type "sameas" with params ['17', 'tr', '-7.97687', '-1.25603', '0', '221', 'sameas', '17', 'tr', '-6.52653', '-1.25603', '0']
# surf222: Unsupported surface type "sameas" with params ['17', 'tr', '-5.07619', '-1.25603', '0', '223', 'sameas', '17', 'tr', '-3.62585', '-1.25603', '0']
# surf224: Unsupported surface type "sameas" with params ['17', 'tr', '-2.17551', '-1.25603', '0', '225', 'sameas', '17', 'tr', '-0.72517', '-1.25603', '0']
# surf226: Unsupported surface type "sameas" with params ['17', 'tr', '0.72517', '-1.25603', '0', '227', 'sameas', '17', 'tr', '2.17551', '-1.25603', '0']
# surf228: Unsupported surface type "sameas" with params ['17', 'tr', '3.62585', '-1.25603', '0', '229', 'sameas', '17', 'tr', '5.07619', '-1.25603', '0']
# surf230: Unsupported surface type "sameas" with params ['17', 'tr', '6.52653', '-1.25603', '0', '231', 'sameas', '17', 'tr', '7.97687', '-1.25603', '0']
# surf232: Unsupported surface type "sameas" with params ['17', 'tr', '9.42721', '-1.25603', '0', '233', 'sameas', '17', 'tr', '10.87755', '-1.25603', '0']
# surf234: Unsupported surface type "sameas" with params ['17', 'tr', '-10.15238', '-2.51206', '0', '235', 'sameas', '17', 'tr', '-8.70204', '-2.51206', '0']
# surf236: Unsupported surface type "sameas" with params ['17', 'tr', '-7.25170', '-2.51206', '0', '237', 'sameas', '17', 'tr', '-5.80136', '-2.51206', '0']
# surf238: Unsupported surface type "sameas" with params ['17', 'tr', '-4.35102', '-2.51206', '0', '239', 'sameas', '17', 'tr', '-2.90068', '-2.51206', '0']
# surf240: Unsupported surface type "sameas" with params ['17', 'tr', '-1.45034', '-2.51206', '0', '241', 'sameas', '17', 'tr', '0', '-2.51206', '0']
# surf242: Unsupported surface type "sameas" with params ['17', 'tr', '1.45034', '-2.51206', '0', '243', 'sameas', '17', 'tr', '2.90068', '-2.51206', '0']
# surf244: Unsupported surface type "sameas" with params ['17', 'tr', '4.35102', '-2.51206', '0', '245', 'sameas', '17', 'tr', '5.80136', '-2.51206', '0']
# surf246: Unsupported surface type "sameas" with params ['17', 'tr', '7.25170', '-2.51206', '0', '247', 'sameas', '17', 'tr', '8.70204', '-2.51206', '0']
# surf248: Unsupported surface type "sameas" with params ['17', 'tr', '10.15238', '-2.51206', '0']
# surf249: Unsupported surface type "sameas" with params ['17', 'tr', '-9.42721', '-3.76809', '0', '250', 'sameas', '17', 'tr', '-7.97687', '-3.76809', '0']
# surf251: Unsupported surface type "sameas" with params ['17', 'tr', '-6.52653', '-3.76809', '0', '252', 'sameas', '17', 'tr', '-5.07619', '-3.76809', '0']
# surf253: Unsupported surface type "sameas" with params ['17', 'tr', '-3.62585', '-3.76809', '0', '254', 'sameas', '17', 'tr', '-2.17551', '-3.76809', '0']
# surf255: Unsupported surface type "sameas" with params ['17', 'tr', '-0.72517', '-3.76809', '0', '256', 'sameas', '17', 'tr', '0.72517', '-3.76809', '0']
# surf257: Unsupported surface type "sameas" with params ['17', 'tr', '2.17551', '-3.76809', '0', '258', 'sameas', '17', 'tr', '3.62585', '-3.76809', '0']
# surf259: Unsupported surface type "sameas" with params ['17', 'tr', '5.07619', '-3.76809', '0', '260', 'sameas', '17', 'tr', '6.52653', '-3.76809', '0']
# surf261: Unsupported surface type "sameas" with params ['17', 'tr', '7.97687', '-3.76809', '0', '262', 'sameas', '17', 'tr', '9.42721', '-3.76809', '0']
# surf263: Unsupported surface type "sameas" with params ['17', 'tr', '-8.70204', '-5.02413', '0', '264', 'sameas', '17', 'tr', '-7.25170', '-5.02413', '0']
# surf265: Unsupported surface type "sameas" with params ['17', 'tr', '-5.80136', '-5.02413', '0', '266', 'sameas', '17', 'tr', '-4.35102', '-5.02413', '0']
# surf267: Unsupported surface type "sameas" with params ['17', 'tr', '-2.90068', '-5.02413', '0', '268', 'sameas', '17', 'tr', '-1.45034', '-5.02413', '0']
# surf269: Unsupported surface type "sameas" with params ['17', 'tr', '0', '-5.02413', '0', '270', 'sameas', '17', 'tr', '1.45034', '-5.02413', '0']
# surf271: Unsupported surface type "sameas" with params ['17', 'tr', '2.90068', '-5.02413', '0', '272', 'sameas', '17', 'tr', '4.35102', '-5.02413', '0']
# surf273: Unsupported surface type "sameas" with params ['17', 'tr', '5.80136', '-5.02413', '0', '274', 'sameas', '17', 'tr', '7.25170', '-5.02413', '0']
# surf275: Unsupported surface type "sameas" with params ['17', 'tr', '8.70204', '-5.02413', '0']
# surf276: Unsupported surface type "sameas" with params ['17', 'tr', '-7.97687', '-6.28016', '0', '277', 'sameas', '17', 'tr', '-6.52653', '-6.28016', '0']
# surf278: Unsupported surface type "sameas" with params ['17', 'tr', '-5.07619', '-6.28016', '0', '279', 'sameas', '17', 'tr', '-3.62585', '-6.28016', '0']
# surf280: Unsupported surface type "sameas" with params ['17', 'tr', '-2.17551', '-6.28016', '0', '281', 'sameas', '17', 'tr', '-0.72517', '-6.28016', '0']
# surf282: Unsupported surface type "sameas" with params ['17', 'tr', '0.72517', '-6.28016', '0', '283', 'sameas', '17', 'tr', '2.17551', '-6.28016', '0']
# surf284: Unsupported surface type "sameas" with params ['17', 'tr', '3.62585', '-6.28016', '0', '285', 'sameas', '17', 'tr', '5.07619', '-6.28016', '0']
# surf286: Unsupported surface type "sameas" with params ['17', 'tr', '6.52653', '-6.28016', '0', '287', 'sameas', '17', 'tr', '7.97687', '-6.28016', '0']
# surf288: Unsupported surface type "sameas" with params ['17', 'tr', '-7.25170', '-7.53619', '0', '289', 'sameas', '17', 'tr', '-5.80136', '-7.53619', '0']
# surf290: Unsupported surface type "sameas" with params ['17', 'tr', '-4.35102', '-7.53619', '0', '291', 'sameas', '17', 'tr', '-2.90068', '-7.53619', '0']
# surf292: Unsupported surface type "sameas" with params ['17', 'tr', '-1.45034', '-7.53619', '0', '293', 'sameas', '17', 'tr', '0', '-7.53619', '0']
# surf294: Unsupported surface type "sameas" with params ['17', 'tr', '1.45034', '-7.53619', '0', '295', 'sameas', '17', 'tr', '2.90068', '-7.53619', '0']
# surf296: Unsupported surface type "sameas" with params ['17', 'tr', '4.35102', '-7.53619', '0', '297', 'sameas', '17', 'tr', '5.80136', '-7.53619', '0']
# surf298: Unsupported surface type "sameas" with params ['17', 'tr', '7.25170', '-7.53619', '0']
# surf299: Unsupported surface type "sameas" with params ['17', 'tr', '-6.52653', '-8.79222', '0', '300', 'sameas', '17', 'tr', '-5.07619', '-8.79222', '0']
# surf301: Unsupported surface type "sameas" with params ['17', 'tr', '-3.62585', '-8.79222', '0', '302', 'sameas', '17', 'tr', '-2.17551', '-8.79222', '0']
# surf303: Unsupported surface type "sameas" with params ['17', 'tr', '-0.72517', '-8.79222', '0', '304', 'sameas', '17', 'tr', '0.72517', '-8.79222', '0']
# surf305: Unsupported surface type "sameas" with params ['17', 'tr', '2.17551', '-8.79222', '0', '306', 'sameas', '17', 'tr', '3.62585', '-8.79222', '0']
# surf307: Unsupported surface type "sameas" with params ['17', 'tr', '5.07619', '-8.79222', '0', '308', 'sameas', '17', 'tr', '6.52653', '-8.79222', '0']
# surf309: Unsupported surface type "sameas" with params ['17', 'tr', '-5.80136', '-10.04825', '0', '310', 'sameas', '17', 'tr', '-4.35102', '-10.04825', '0']
# surf311: Unsupported surface type "sameas" with params ['17', 'tr', '-2.90068', '-10.04825', '0', '312', 'sameas', '17', 'tr', '-1.45034', '-10.04825', '0']
# surf313: Unsupported surface type "sameas" with params ['17', 'tr', '0', '-10.04825', '0', '314', 'sameas', '17', 'tr', '1.45034', '-10.04825', '0']
# surf315: Unsupported surface type "sameas" with params ['17', 'tr', '2.90068', '-10.04825', '0', '316', 'sameas', '17', 'tr', '4.35102', '-10.04825', '0']
# surf317: Unsupported surface type "sameas" with params ['17', 'tr', '5.80136', '-10.04825', '0']
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
# surf1201: Unsupported surface type "sameas" with params ['17', 'tr', '12.32789', '1.25603', '0', '1202', 'sameas', '17', 'tr', '13.77823', '1.25603', '0']
# surf1203: Unsupported surface type "sameas" with params ['17', 'tr', '15.22857', '1.25603', '0', '1204', 'sameas', '17', 'tr', '16.67891', '1.25603', '0']
# surf1205: Unsupported surface type "sameas" with params ['17', 'tr', '18.12925', '1.25603', '0', '1206', 'sameas', '17', 'tr', '19.57959', '1.25603', '0']
# surf1207: Unsupported surface type "sameas" with params ['17', 'tr', '21.02993', '1.25603', '0', '1208', 'sameas', '17', 'tr', '22.48027', '1.25603', '0']
# surf1209: Unsupported surface type "sameas" with params ['17', 'tr', '23.93061', '1.25603', '0', '1210', 'sameas', '17', 'tr', '25.38095', '1.25603', '0']
# surf1211: Unsupported surface type "sameas" with params ['17', 'tr', '26.83129', '1.25603', '0', '1212', 'sameas', '17', 'tr', '28.28163', '1.25603', '0']
# surf1219: Unsupported surface type "sameas" with params ['17', 'tr', '14.50340', '0', '0', '1220', 'sameas', '17', 'tr', '15.95374', '0', '0']
# surf1221: Unsupported surface type "sameas" with params ['17', 'tr', '17.40408', '0', '0', '1222', 'sameas', '17', 'tr', '18.85442', '0', '0']
# surf1223: Unsupported surface type "sameas" with params ['17', 'tr', '20.30476', '0', '0', '1224', 'sameas', '17', 'tr', '21.75510', '0', '0']
# surf1225: Unsupported surface type "sameas" with params ['17', 'tr', '23.20544', '0', '0', '1226', 'sameas', '17', 'tr', '24.65578', '0', '0']
# surf1227: Unsupported surface type "sameas" with params ['17', 'tr', '26.10612', '0', '0', '1228', 'sameas', '17', 'tr', '27.55646', '0', '0']
# surf1229: Unsupported surface type "sameas" with params ['17', 'tr', '29.00680', '0', '0']

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
