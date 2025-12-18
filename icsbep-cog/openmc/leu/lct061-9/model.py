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

# Critical water height
surf1 = openmc.ZPlane(surface_id=1, z0=45.22)
# SST lower grid plate
surf2 = openmc.ZCylinder(surface_id=2, x0=-3.8, y0=-2.3, r=50.0)
# SST upper grid plate
surf3 = openmc.ZCylinder(surface_id=3, x0=126.9, y0=127.9, r=50.0)
# Boundary condition
surf4 = openmc.ZCylinder(surface_id=4, x0=-32.3, y0=133.5, r=65.0, boundary_type="vacuum")
# UO2
surf10 = openmc.ZCylinder(surface_id=10, x0=0.0, y0=125.0, r=0.37875)
# Zr plug, inner
surf11 = openmc.ZCylinder(surface_id=11, r=0.15)
# Zr plug, outer
surf12 = openmc.ZCylinder(surface_id=12, x0=125.0, y0=125.7, r=0.385)
# SST spring, inner
surf13 = openmc.ZCylinder(surface_id=13, r=0.29)
# SST spring, outer
surf14 = openmc.ZCylinder(surface_id=14, x0=125.7, y0=128.0, r=0.32175)
# Clad, inner
surf15 = openmc.ZCylinder(surface_id=15, x0=0.0, y0=128.0, r=0.3875)
# Clad, outer
surf16 = openmc.ZCylinder(surface_id=16, x0=-2.3, y0=130.3, r=0.45225)
# Clad, top and bottom portions
surf17 = openmc.ZCylinder(surface_id=17, x0=-3.8, y0=131.8, r=0.3)
# Hole
# surf20: Unsupported surface type "rev" with params ['4', '-3.9', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '0', '0', '0', '0', '0', '1', '0', '1', '0']
# surf21: Unsupported surface type "rev" with params ['4', '-3.9', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-0.635', '1.09985', '0', '-0.635', '1.09985', '9', '-0.635', '9', '0']
# surf22: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '0.635', '1.09985', '0', '0.635', '1.09985', '9', '0.635', '9', '0']
# surf23: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-1.270', '0', '0', '-1.270', '0', '9', '-1.270', '9', '0']
# surf24: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '1.270', '0', '0', '1.270', '0', '9', '1.270', '9', '0']
# surf25: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-0.635', '-1.09985', '0', '-0.635', '-1.09985', '9', '-0.635', '9', '0']
# surf26: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '0.635', '-1.09985', '0', '0.635', '-1.09985', '9', '0.635', '9', '0']
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
# surf41: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-8.89', '26.39640', '0', '-8.89', '26.39640', '9', '-8.89', '9', '0']
# surf42: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-7.62', '26.39640', '0', '-7.62', '26.39640', '9', '-7.62', '9', '0']
# surf43: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-6.35', '26.39640', '0', '-6.35', '26.39640', '9', '-6.35', '9', '0']
# surf44: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '6.35', '26.39640', '0', '6.35', '26.39640', '9', '6.35', '9', '0']
# surf45: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '7.62', '26.39640', '0', '7.62', '26.39640', '9', '7.62', '9', '0']
# surf46: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '8.89', '26.39640', '0', '8.89', '26.39640', '9', '8.89', '9', '0']
# surf47: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-10.795', '25.29655', '0', '-10.795', '25.29655', '9', '-10.795', '9', '0']
# surf48: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '10.795', '25.29655', '0', '10.795', '25.29655', '9', '10.795', '9', '0']
# surf49: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-12.70', '24.19670', '0', '-12.70', '24.19670', '9', '-12.70', '9', '0']
# surf50: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '12.70', '24.19670', '0', '12.70', '24.19670', '9', '12.70', '9', '0']
# surf51: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-14.605', '23.09685', '0', '-14.605', '23.09685', '9', '-14.605', '9', '0']
# surf52: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '14.605', '23.09685', '0', '14.605', '23.09685', '9', '14.605', '9', '0']
# surf53: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-16.51', '21.99700', '0', '-16.51', '21.99700', '9', '-16.51', '9', '0']
# surf54: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '16.51', '21.99700', '0', '16.51', '21.99700', '9', '16.51', '9', '0']
# surf55: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-18.415', '20.89715', '0', '-18.415', '20.89715', '9', '-18.415', '9', '0']
# surf56: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '18.415', '20.89715', '0', '18.415', '20.89715', '9', '18.415', '9', '0']
# surf57: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-19.05', '19.79730', '0', '-19.05', '19.79730', '9', '-19.05', '9', '0']
# surf58: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '19.05', '19.79730', '0', '19.05', '19.79730', '9', '19.05', '9', '0']
# surf59: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-19.685', '18.69745', '0', '-19.685', '18.69745', '9', '-19.685', '9', '0']
# surf60: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '19.685', '18.69745', '0', '19.685', '18.69745', '9', '19.685', '9', '0']
# surf61: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-26.035', '7.69895', '0', '-26.035', '7.69895', '9', '-26.035', '9', '0']
# surf62: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '26.035', '7.69895', '0', '26.035', '7.69895', '9', '26.035', '9', '0']
# surf63: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-26.67', '6.59910', '0', '-26.67', '6.59910', '9', '-26.67', '9', '0']
# surf64: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '26.67', '6.59910', '0', '26.67', '6.59910', '9', '26.67', '9', '0']
# surf65: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-27.305', '5.49925', '0', '-27.305', '5.49925', '9', '-27.305', '9', '0']
# surf66: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '27.305', '5.49925', '0', '27.305', '5.49925', '9', '27.305', '9', '0']
# surf67: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-27.305', '3.29955', '0', '-27.305', '3.29955', '9', '-27.305', '9', '0']
# surf68: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '27.305', '3.29955', '0', '27.305', '3.29955', '9', '27.305', '9', '0']
# surf69: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-27.305', '1.09985', '0', '-27.305', '1.09985', '9', '-27.305', '9', '0']
# surf70: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '27.305', '1.09985', '0', '27.305', '1.09985', '9', '27.305', '9', '0']
# surf71: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-27.305', '-1.09985', '0', '-27.305', '-1.09985', '9', '-27.305', '9', '0']
# surf72: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '27.305', '-1.09985', '0', '27.305', '-1.09985', '9', '27.305', '9', '0']
# surf73: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-27.305', '-3.29955', '0', '-27.305', '-3.29955', '9', '-27.305', '9', '0']
# surf74: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '27.305', '-3.29955', '0', '27.305', '-3.29955', '9', '27.305', '9', '0']
# surf75: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-27.305', '-5.49925', '0', '-27.305', '-5.49925', '9', '-27.305', '9', '0']
# surf76: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '27.305', '-5.49925', '0', '27.305', '-5.49925', '9', '27.305', '9', '0']
# surf77: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-26.67', '-6.59910', '0', '-26.67', '-6.59910', '9', '-26.67', '9', '0']
# surf78: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '26.67', '-6.59910', '0', '26.67', '-6.59910', '9', '26.67', '9', '0']
# surf79: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-26.035', '-7.69895', '0', '-26.035', '-7.69895', '9', '-26.035', '9', '0']
# surf80: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '26.035', '-7.69895', '0', '26.035', '-7.69895', '9', '26.035', '9', '0']
# surf81: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-19.685', '-18.69745', '0', '-19.685', '-18.69745', '9', '-19.685', '9', '0']
# surf82: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '19.685', '-18.69745', '0', '19.685', '-18.69745', '9', '19.685', '9', '0']
# surf83: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-19.05', '-19.79730', '0', '-19.05', '-19.79730', '9', '-19.05', '9', '0']
# surf84: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '19.05', '-19.79730', '0', '19.05', '-19.79730', '9', '19.05', '9', '0']
# surf85: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-18.415', '-20.89715', '0', '-18.415', '-20.89715', '9', '-18.415', '9', '0']
# surf86: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '18.415', '-20.89715', '0', '18.415', '-20.89715', '9', '18.415', '9', '0']
# surf87: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-16.51', '-21.99700', '0', '-16.51', '-21.99700', '9', '-16.51', '9', '0']
# surf88: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '16.51', '-21.99700', '0', '16.51', '-21.99700', '9', '16.51', '9', '0']
# surf89: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-14.605', '-23.09685', '0', '-14.605', '-23.09685', '9', '-14.605', '9', '0']
# surf90: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '14.605', '-23.09685', '0', '14.605', '-23.09685', '9', '14.605', '9', '0']
# surf91: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-12.70', '-24.19670', '0', '-12.70', '-24.19670', '9', '-12.70', '9', '0']
# surf92: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '12.70', '-24.19670', '0', '12.70', '-24.19670', '9', '12.70', '9', '0']
# surf93: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-10.795', '-25.29655', '0', '-10.795', '-25.29655', '9', '-10.795', '9', '0']
# surf94: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '10.795', '-25.29655', '0', '10.795', '-25.29655', '9', '10.795', '9', '0']
# surf95: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-8.89', '-26.39640', '0', '-8.89', '-26.39640', '9', '-8.89', '9', '0']
# surf96: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-7.62', '-26.39640', '0', '-7.62', '-26.39640', '9', '-7.62', '9', '0']
# surf97: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-6.35', '-26.39640', '0', '-6.35', '-26.39640', '9', '-6.35', '9', '0']
# surf98: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '6.35', '-26.39640', '0', '6.35', '-26.39640', '9', '6.35', '9', '0']
# surf99: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '7.62', '-26.39640', '0', '7.62', '-26.39640', '9', '7.62', '9', '0']
# surf100: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '8.89', '-26.39640', '0', '8.89', '-26.39640', '9', '8.89', '9', '0']
# Hole
# surf101: Unsupported surface type "rev" with params ['4', '-3.9', '0.31', '-2.3', '0.31', '-2.29999', '0.51', '133.3', '0.51', 'tr', '0', '0', '0', '0', '0', '1', '0', '1', '0']
# surf102: Unsupported surface type "rev" with params ['4', '-3.9', '0.31', '-2.3', '0.31', '-2.29999', '0.51', '133.3', '0.51', 'tr', '-0.635', '1.09985', '0', '-0.635', '1.09985', '9', '-0.635', '9', '0']
# surf103: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.51', '133.3', '0.51', 'tr', '0.635', '1.09985', '0', '0.635', '1.09985', '9', '0.635', '9', '0']
# surf104: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.51', '133.3', '0.51', 'tr', '-1.270', '0', '0', '-1.270', '0', '9', '-1.270', '9', '0']
# surf105: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.51', '133.3', '0.51', 'tr', '1.270', '0', '0', '1.270', '0', '9', '1.270', '9', '0']
# surf106: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.51', '133.3', '0.51', 'tr', '-0.635', '-1.09985', '0', '-0.635', '-1.09985', '9', '-0.635', '9', '0']
# surf107: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.51', '133.3', '0.51', 'tr', '0.635', '-1.09985', '0', '0.635', '-1.09985', '9', '0.635', '9', '0']
# Void
surf191 = openmc.ZCylinder(surface_id=191, x0=0.0, y0=133.27, r=0.45)
# Al tube
surf192 = openmc.ZCylinder(surface_id=192, x0=-2.3, y0=133.27, r=0.5)
# Al end
surf193 = openmc.ZCylinder(surface_id=193, x0=-3.8, y0=-2.3, r=0.3)
surf321 = openmc.model.RectangularParallelepiped(-27.305, 27.305, -499.95, 499.95, -499.95, 499.95)
surf322 = openmc.model.RectangularParallelepiped(-27.305, 27.305, -499.95, 499.95, -499.95, 499.95)
surf323 = openmc.model.RectangularParallelepiped(-27.305, 27.305, -499.95, 499.95, -499.95, 499.95)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = -surf2
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf3
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = -surf1 & +surf2 & +surf3 & -surf4
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf10 & -surf15
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = +surf10 & +surf11 & -surf12 & -surf15
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf12 & +surf13 & -surf14 & -surf15
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = +surf15 & -surf16
u2_cell4 = openmc.Cell(fill=mat2)
u2_cell4.region = +surf16 & -surf17
u2_cell5 = openmc.Cell(fill=mat4)
u2_cell5.region = -surf1 & -surf4 & +surf16 & +surf17
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
u7_cell0.region = +surf191 & -surf192
u7_cell1 = openmc.Cell(fill=mat5)
u7_cell1.region = +surf192 & -surf193
u7_cell2 = openmc.Cell(fill=mat4)
u7_cell2.region = -surf1 & -surf4 & +surf192 & +surf193
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
cell1.region = -surf4 & +surf41 & +surf42 & +surf43 & +surf44 & +surf45 & +surf46 & +surf47 & +surf48 & +surf49 & +surf50 & +surf51 & +surf52 & +surf53 & +surf54 & +surf55 & +surf56 & +surf57 & +surf58 & +surf59 & +surf60 & +surf61 & +surf62 & +surf63 & +surf64 & +surf65 & +surf66 & +surf67 & +surf68 & +surf69 & +surf70

# Mod
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = -surf1 & -surf4 & -surf41 & -surf1 & -surf42 & -surf1 & -surf43 & -surf1 & -surf44 & -surf1 & -surf45 & -surf1 & -surf46 & -surf1 & -surf47 & -surf1 & -surf48 & -surf1 & -surf49 & -surf1 & -surf50

# Mod
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = -surf1 & -surf4 & -surf51 & -surf1 & -surf52 & -surf1 & -surf53 & -surf1 & -surf54 & -surf1 & -surf55 & -surf1 & -surf56 & -surf1 & -surf57 & -surf1 & -surf58 & -surf1 & -surf59 & -surf1 & -surf60

# Mod
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = -surf1 & -surf4 & -surf61 & -surf1 & -surf62 & -surf1 & -surf63 & -surf1 & -surf64 & -surf1 & -surf65 & -surf1 & -surf66 & -surf1 & -surf67 & -surf1 & -surf68 & -surf1 & -surf69 & -surf1 & -surf70

# Mod
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = -surf1 & -surf4 & -surf71 & -surf1 & -surf72 & -surf1 & -surf73 & -surf1 & -surf74 & -surf1 & -surf75 & -surf1 & -surf76 & -surf1 & -surf77 & -surf1 & -surf78 & -surf1 & -surf79 & -surf1 & -surf80

# Mod
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = -surf1 & -surf4 & -surf81 & -surf1 & -surf82 & -surf1 & -surf83 & -surf1 & -surf84 & -surf1 & -surf85 & -surf1 & -surf86 & -surf1 & -surf87 & -surf1 & -surf88 & -surf1 & -surf89 & -surf1 & -surf90

# Mod
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = -surf1 & -surf4 & -surf91 & -surf1 & -surf92 & -surf1 & -surf93 & -surf1 & -surf94 & -surf1 & -surf95 & -surf1 & -surf96 & -surf1 & -surf97 & -surf1 & -surf98 & -surf1 & -surf99 & -surf1 & -surf100

# Alles
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.region = -surf4 & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5)

# Mod
cell12 = openmc.Cell(cell_id=12, fill=mat4)
cell12.region = -surf1 & +surf2 & +surf3 & -surf4

# Mod
cell19 = openmc.Cell(cell_id=19, fill=mat4)
cell19.region = -surf1 & -surf4 & +surf16 & +surf17

# Alles
cell20 = openmc.Cell(cell_id=20, fill=universe1)
cell20.region = -surf4 & +surf20 & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

# Alles
cell28 = openmc.Cell(cell_id=28, fill=universe1)
cell28.region = -surf4 & +surf20 & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

# Mod
cell32 = openmc.Cell(cell_id=32, fill=mat4)
cell32.region = -surf1 & -surf4 & +surf192 & +surf193

# Alles
cell33 = openmc.Cell(cell_id=33, fill=universe1)
cell33.region = -surf4 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107

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
