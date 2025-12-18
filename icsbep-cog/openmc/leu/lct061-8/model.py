"""
LCT061-8: 762 U(4.5)O2 rods, 7 Dy rods, 1.27 cm trianglur pitch, Hc=75.41cm, water
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

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.676200e-02)
mat4.add_nuclide("O16", 3.338100e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Dysprosium
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("Dy156", 6.670700e-06)
mat5.add_nuclide("Dy158", 1.111800e-05)
mat5.add_nuclide("Dy160", 2.601600e-04)
mat5.add_nuclide("Dy161", 2.101300e-03)
mat5.add_nuclide("Dy162", 2.835100e-03)
mat5.add_nuclide("Dy163", 2.768400e-03)
mat5.add_nuclide("Dy164", 3.135200e-03)
mat5.add_nuclide("O16", 2.779500e-02)
mat5.add_element("Ti", 5.558900e-03)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Critical water height
surf1 = openmc.ZPlane(surface_id=1, z0=75.41)
# SST lower grid plate
surf2 = openmc.ZCylinder(surface_id=2, x0=-3.8, y0=-2.3, r=50.0)
# SST upper grid plate
surf3 = openmc.ZCylinder(surface_id=3, x0=126.9, y0=127.9, r=50.0)
# Boundary condition
surf4 = openmc.ZCylinder(surface_id=4, x0=-32.3, y0=133.27, r=65.0, boundary_type="vacuum")
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
# The region
# Prism 30: 6-sided polygon
surf30_0 = openmc.Plane(a=0.8660253759, b=0.5000000483, c=0, d=18.1475617522)
surf30_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=18.1475600000)
surf30_2 = openmc.Plane(a=-0.8660253759, b=0.5000000483, c=0, d=18.1475617522)
surf30_3 = openmc.Plane(a=-0.8660253759, b=-0.5000000483, c=0, d=18.1475617522)
surf30_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=18.1475600000)
surf30_5 = openmc.Plane(a=0.8660253759, b=-0.5000000483, c=0, d=18.1475617522)
# The region
# Prism 31: 6-sided polygon
surf31_0 = openmc.Plane(a=0.8660254126, b=0.4999999847, c=0, d=21.4471193435)
surf31_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=21.4471200000)
surf31_2 = openmc.Plane(a=-0.8660254126, b=0.4999999847, c=0, d=21.4471193435)
surf31_3 = openmc.Plane(a=-0.8660254126, b=-0.4999999847, c=0, d=21.4471193435)
surf31_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=21.4471200000)
surf31_5 = openmc.Plane(a=0.8660254126, b=-0.4999999847, c=0, d=21.4471193435)
# surf41: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-10.16', '17.59760', '0', '-10.16', '17.59760', '9', '-10.16', '9', '0']
# surf42: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-8.89', '17.59760', '0', '-8.89', '17.59760', '9', '-8.89', '9', '0']
# surf43: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-7.62', '17.59760', '0', '-7.62', '17.59760', '9', '-7.62', '9', '0']
# surf44: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-6.35', '17.59760', '0', '-6.35', '17.59760', '9', '-6.35', '9', '0']
# surf45: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '6.35', '17.59760', '0', '6.35', '17.59760', '9', '6.35', '9', '0']
# surf46: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '7.62', '17.59760', '0', '7.62', '17.59760', '9', '7.62', '9', '0']
# surf47: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '8.89', '17.59760', '0', '8.89', '17.59760', '9', '8.89', '9', '0']
# surf48: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '10.16', '17.59760', '0', '10.16', '17.59760', '9', '10.16', '9', '0']
# surf49: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-10.795', '16.49775', '0', '-10.795', '16.49775', '9', '-10.795', '9', '0']
# surf50: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-9.525', '16.49775', '0', '-9.525', '16.49775', '9', '-9.525', '9', '0']
# surf51: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '9.525', '16.49775', '0', '9.525', '16.49775', '9', '9.525', '9', '0']
# surf52: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '10.795', '16.49775', '0', '10.795', '16.49775', '9', '10.795', '9', '0']
# surf53: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-11.43', '15.39790', '0', '-11.43', '15.39790', '9', '-11.43', '9', '0']
# surf54: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '11.43', '15.39790', '0', '11.43', '15.39790', '9', '11.43', '9', '0']
# surf55: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-12.065', '14.29805', '0', '-12.065', '14.29805', '9', '-12.065', '9', '0']
# surf56: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '12.065', '14.29805', '0', '12.065', '14.29805', '9', '12.065', '9', '0']
# surf57: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-18.415', '3.29955', '0', '-18.415', '3.29955', '9', '-18.415', '9', '0']
# surf58: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '18.415', '3.29955', '0', '18.415', '3.29955', '9', '18.415', '9', '0']
# surf59: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-19.05', '2.19970', '0', '-19.05', '2.19970', '9', '-19.05', '9', '0']
# surf60: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '19.05', '2.19970', '0', '19.05', '2.19970', '9', '19.05', '9', '0']
# surf61: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-19.685', '1.09985', '0', '-19.685', '1.09985', '9', '-19.685', '9', '0']
# surf62: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '19.685', '1.09985', '0', '19.685', '1.09985', '9', '19.685', '9', '0']
# surf63: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-20.32', '0.0', '0', '-20.32', '0.0', '9', '-20.32', '9', '0']
# surf64: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-19.05', '0.0', '0', '-19.05', '0.0', '9', '-19.05', '9', '0']
# surf65: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '19.05', '0.0', '0', '19.05', '0.0', '9', '19.05', '9', '0']
# surf66: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '20.32', '0.0', '0', '20.32', '0.0', '9', '20.32', '9', '0']
# surf67: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-19.685', '-1.09985', '0', '-19.685', '-1.09985', '9', '-19.685', '9', '0']
# surf68: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '19.685', '-1.09985', '0', '19.685', '-1.09985', '9', '19.685', '9', '0']
# surf69: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-19.05', '-2.19970', '0', '-19.05', '-2.19970', '9', '-19.05', '9', '0']
# surf70: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '19.05', '-2.19970', '0', '19.05', '-2.19970', '9', '19.05', '9', '0']
# surf71: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-18.415', '-3.29955', '0', '-18.415', '-3.29955', '9', '-18.415', '9', '0']
# surf72: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '18.415', '-3.29955', '0', '18.415', '-3.29955', '9', '18.415', '9', '0']
# surf73: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-12.065', '-14.29805', '0', '-12.065', '-14.29805', '9', '-12.065', '9', '0']
# surf74: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '12.065', '-14.29805', '0', '12.065', '-14.29805', '9', '12.065', '9', '0']
# surf75: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-11.43', '-15.39790', '0', '-11.43', '-15.39790', '9', '-11.43', '9', '0']
# surf76: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '11.43', '-15.39790', '0', '11.43', '-15.39790', '9', '11.43', '9', '0']
# surf77: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-10.795', '-16.49775', '0', '-10.795', '-16.49775', '9', '-10.795', '9', '0']
# surf78: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-9.525', '-16.49775', '0', '-9.525', '-16.49775', '9', '-9.525', '9', '0']
# surf79: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '9.525', '-16.49775', '0', '9.525', '-16.49775', '9', '9.525', '9', '0']
# surf80: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '10.795', '-16.49775', '0', '10.795', '-16.49775', '9', '10.795', '9', '0']
# surf81: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-10.16', '-17.59760', '0', '-10.16', '-17.59760', '9', '-10.16', '9', '0']
# surf82: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-8.89', '-17.59760', '0', '-8.89', '-17.59760', '9', '-8.89', '9', '0']
# surf83: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-7.62', '-17.59760', '0', '-7.62', '-17.59760', '9', '-7.62', '9', '0']
# surf84: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-6.35', '-17.59760', '0', '-6.35', '-17.59760', '9', '-6.35', '9', '0']
# surf85: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '6.35', '-17.59760', '0', '6.35', '-17.59760', '9', '6.35', '9', '0']
# surf86: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '7.62', '-17.59760', '0', '7.62', '-17.59760', '9', '7.62', '9', '0']
# surf87: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '8.89', '-17.59760', '0', '8.89', '-17.59760', '9', '8.89', '9', '0']
# surf88: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '10.16', '-17.59760', '0', '10.16', '-17.59760', '9', '10.16', '9', '0']
# Dysprosium compound
surf90 = openmc.ZPlane(surface_id=90, z0=125.0)
# Void
surf91 = openmc.ZCylinder(surface_id=91, x0=0.0, y0=128.0, r=0.35)
# SST tube
surf92 = openmc.ZCylinder(surface_id=92, x0=-2.3, y0=130.3, r=0.4075)
# SST ends
surf93 = openmc.ZCylinder(surface_id=93, x0=-3.8, y0=131.8, r=0.3)
# surf101: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '0.0', '0.0', '0', '0.0', '0.0', '9', '0.0', '9', '0']
# surf102: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '0.0', '6.59910', '0', '0.0', '6.59910', '9', '0.0', '9', '0']
# surf103: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '0.0', '-6.59910', '0', '0.0', '-6.59910', '9', '0.0', '9', '0']
# surf104: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '5.715', '3.29955', '0', '5.715', '3.29955', '9', '5.715', '9', '0']
# surf105: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-5.715', '3.29955', '0', '-5.715', '3.29955', '9', '-5.715', '9', '0']
# surf106: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '5.715', '-3.29955', '0', '5.715', '-3.29955', '9', '5.715', '9', '0']
# surf107: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-5.715', '-3.29955', '0', '-5.715', '-3.29955', '9', '-5.715', '9', '0']

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
u4_cell0.region = -surf1
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf1
u4_cell2 = openmc.Cell(fill=mat4)
u4_cell2.region = -surf1
u4_cell3 = openmc.Cell(fill=mat4)
u4_cell3.region = -surf1
u4_cell4 = openmc.Cell(fill=mat4)
u4_cell4.region = -surf1
u4_cell5 = openmc.Cell(fill=mat4)
u4_cell5.region = -surf1
u4_cell6 = openmc.Cell(fill=mat4)
u4_cell6.region = -surf1
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4, u4_cell5, u4_cell6])

# Lattice 5: 21x21 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-26.67, -23.09685]
lattice5.pitch = [2.540000, 2.199700]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# Lattice 6: 21x21 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-26.67, -23.09685]
lattice6.pitch = [2.540000, 2.199700]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

u7_cell0 = openmc.Cell(fill=mat5)
u7_cell0.region = -surf90 & -surf91
u7_cell1 = openmc.Cell(fill=mat3)
u7_cell1.region = +surf91 & -surf92
u7_cell2 = openmc.Cell(fill=mat3)
u7_cell2.region = +surf92 & -surf93
u7_cell3 = openmc.Cell(fill=mat4)
u7_cell3.region = -surf1 & -surf4 & +surf92 & +surf93
universe7 = openmc.Universe(universe_id=7, cells=[u7_cell0, u7_cell1, u7_cell2, u7_cell3])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Frods
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = -surf4 & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5)

# H2O
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = -surf1

# H2O
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = -surf1

# H2O
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = -surf1

# H2O
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = -surf1

# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = -surf1

# H2O
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = -surf1

# H2O
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = -surf1

# DYR
cell9 = openmc.Cell(cell_id=9, fill=universe7)
cell9.translation = (0.0, 0.0, 0.0)


# DYR
cell10 = openmc.Cell(cell_id=10, fill=universe7)
cell10.translation = (0.0, 6.5991, 0.0)


# DYR
cell11 = openmc.Cell(cell_id=11, fill=universe7)
cell11.translation = (0.0, -6.5991, 0.0)


# DYR
cell12 = openmc.Cell(cell_id=12, fill=universe7)
cell12.translation = (5.715, 3.29955, 0.0)


# DYR
cell13 = openmc.Cell(cell_id=13, fill=universe7)
cell13.translation = (-5.715, 3.29955, 0.0)


# DYR
cell14 = openmc.Cell(cell_id=14, fill=universe7)
cell14.translation = (5.715, -3.29955, 0.0)


# DYR
cell15 = openmc.Cell(cell_id=15, fill=universe7)
cell15.translation = (-5.715, -3.29955, 0.0)


# Holes
cell16 = openmc.Cell(cell_id=16, fill=universe6)
cell16.region = -surf4 & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5)

# Alles
cell17 = openmc.Cell(cell_id=17, fill=universe1)
cell17.region = -surf4 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5)

# Mod
cell21 = openmc.Cell(cell_id=21, fill=mat4)
cell21.region = -surf1 & +surf2 & +surf3 & -surf4

# Mod
cell28 = openmc.Cell(cell_id=28, fill=mat4)
cell28.region = -surf1 & -surf4 & +surf16 & +surf17

# Alles
cell29 = openmc.Cell(cell_id=29, fill=universe1)
cell29.region = -surf4

# Alles
cell37 = openmc.Cell(cell_id=37, fill=universe1)
cell37.region = -surf4

# Mod
cell42 = openmc.Cell(cell_id=42, fill=mat4)
cell42.region = -surf1 & -surf4 & +surf92 & +surf93

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell21, cell28, cell29, cell37, cell42])
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
source.space = openmc.stats.Box((-2.27, -2.09985, 36.705), (2.27, 2.09985, 38.705))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
