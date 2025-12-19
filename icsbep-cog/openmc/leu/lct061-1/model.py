"""
LCT061-1: 762 U(4.5)O2 rods, 7 B4C rods, 1.27 cm trianglur pitch, Hc=96.60cm, water
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

# B4C
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 1.852800e-02)
mat5.add_nuclide("B10", 1.474800e-02)
mat5.add_nuclide("B11", 5.936300e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Critical water height
surf1 = openmc.ZPlane(surface_id=1, z0=96.60)
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
# B4C
surf90 = openmc.ZPlane(surface_id=90, z0=125.0)
# Clad, inner
surf91 = openmc.ZCylinder(surface_id=91, r=0.35)
# Clad, outer
surf92 = openmc.ZCylinder(surface_id=92, r=0.4075)
# Clad, top and bottom portions
surf93 = openmc.ZCylinder(surface_id=93, r=0.3)
# surf101: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '0.0', '0.0', '0', '0.0', '0.0', '9', '0.0', '9', '0']
# surf102: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '2.54', '2.19970', '0', '2.54', '2.19970', '9', '2.54', '9', '0']
# surf103: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-0.635', '3.29955', '0', '-0.635', '3.29955', '9', '-0.635', '9', '0']
# surf104: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-3.175', '1.09985', '0', '-3.175', '1.09985', '9', '-3.175', '9', '0']
# surf105: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '-2.54', '-2.19970', '0', '-2.54', '-2.19970', '9', '-2.54', '9', '0']
# surf106: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '0.635', '-3.29955', '0', '0.635', '-3.29955', '9', '0.635', '9', '0']
# surf107: Unsupported surface type "rev" with params ['4', '-3.8', '0.31', '-2.3', '0.31', '-2.29999', '0.47', '131.8', '0.47', 'tr', '3.175', '-1.09985', '0', '3.175', '-1.09985', '9', '3.175', '9', '0']

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(surface_id=1107, z0=-3.8)
surf2_zmax = openmc.ZPlane(surface_id=1108, z0=-2.3)
surf3_zmin = openmc.ZPlane(surface_id=1109, z0=126.9)
surf3_zmax = openmc.ZPlane(surface_id=1110, z0=127.9)
surf4_zmin = openmc.ZPlane(surface_id=1111, z0=-32.3, boundary_type="vacuum")
surf4_zmax = openmc.ZPlane(surface_id=1112, z0=133.27, boundary_type="vacuum")
surf10_zmin = openmc.ZPlane(surface_id=1113, z0=0.0)
surf10_zmax = openmc.ZPlane(surface_id=1114, z0=125.0)
surf12_zmin = openmc.ZPlane(surface_id=1115, z0=125.0)
surf12_zmax = openmc.ZPlane(surface_id=1116, z0=125.7)
surf14_zmin = openmc.ZPlane(surface_id=1117, z0=125.7)
surf14_zmax = openmc.ZPlane(surface_id=1118, z0=128.0)
surf15_zmin = openmc.ZPlane(surface_id=1119, z0=0.0)
surf15_zmax = openmc.ZPlane(surface_id=1120, z0=128.0)
surf16_zmin = openmc.ZPlane(surface_id=1121, z0=-2.3)
surf16_zmax = openmc.ZPlane(surface_id=1122, z0=130.3)
surf17_zmin = openmc.ZPlane(surface_id=1123, z0=-3.8)
surf17_zmax = openmc.ZPlane(surface_id=1124, z0=131.8)
surf91_zmin = openmc.ZPlane(surface_id=1125, z0=0.0)
surf91_zmax = openmc.ZPlane(surface_id=1126, z0=128.0)
surf92_zmin = openmc.ZPlane(surface_id=1127, z0=-2.3)
surf92_zmax = openmc.ZPlane(surface_id=1128, z0=130.3)
surf93_zmin = openmc.ZPlane(surface_id=1129, z0=-3.8)
surf93_zmax = openmc.ZPlane(surface_id=1130, z0=131.8)

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
u7_cell0.region = -surf90 & (-surf91 & +surf91_zmin & -surf91_zmax)
u7_cell1 = openmc.Cell(fill=mat3)
u7_cell1.region = (+surf91 | -surf91_zmin | +surf91_zmax) & (-surf92 & +surf92_zmin & -surf92_zmax)
u7_cell2 = openmc.Cell(fill=mat3)
u7_cell2.region = (+surf92 | -surf92_zmin | +surf92_zmax) & (-surf93 & +surf93_zmin & -surf93_zmax)
u7_cell3 = openmc.Cell(fill=mat4)
u7_cell3.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf92 | -surf92_zmin | +surf92_zmax) & (+surf93 | -surf93_zmin | +surf93_zmax)
universe7 = openmc.Universe(universe_id=7, cells=[u7_cell0, u7_cell1, u7_cell2, u7_cell3])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Frods
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf30_0 & -surf30_1 & -surf30_2 & -surf30_3 & -surf30_4 & -surf30_5) & +surf41 & +surf42 & +surf43 & +surf44 & +surf45 & +surf46 & +surf47 & +surf48 & +surf49 & +surf50 & +surf51 & +surf52 & +surf53 & +surf54 & +surf55 & +surf56 & +surf57 & +surf58 & +surf59 & +surf60

# H2O
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = -surf1 & -surf41 & -surf1 & -surf42 & -surf1 & -surf43 & -surf1 & -surf44 & -surf1 & -surf45 & -surf1 & -surf46 & -surf1 & -surf47

# H2O
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = -surf1 & -surf48 & -surf1 & -surf49 & -surf1 & -surf50 & -surf1 & -surf51 & -surf1 & -surf52 & -surf1 & -surf53 & -surf1 & -surf54

# H2O
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = -surf1 & -surf55 & -surf1 & -surf56 & -surf1 & -surf57 & -surf1 & -surf58 & -surf1 & -surf59 & -surf1 & -surf60 & -surf1 & -surf61

# H2O
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = -surf1 & -surf62 & -surf1 & -surf63 & -surf1 & -surf64 & -surf1 & -surf65 & -surf1 & -surf66 & -surf1 & -surf67 & -surf1 & -surf68

# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = -surf1 & -surf69 & -surf1 & -surf70 & -surf1 & -surf71 & -surf1 & -surf72 & -surf1 & -surf73 & -surf1 & -surf74 & -surf1 & -surf75

# H2O
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = -surf1 & -surf76 & -surf1 & -surf77 & -surf1 & -surf78 & -surf1 & -surf79 & -surf1 & -surf80 & -surf1 & -surf81 & -surf1 & -surf82

# H2O
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = -surf1 & -surf83 & -surf1 & -surf84 & -surf1 & -surf85 & -surf1 & -surf86 & -surf1 & -surf87 & -surf1 & -surf88

# B4C
cell9 = openmc.Cell(cell_id=9, fill=universe7)
cell9.translation = (0.0, 0.0, 0.0)
cell9.region = -surf101

# B4C
cell10 = openmc.Cell(cell_id=10, fill=universe7)
cell10.translation = (2.54, 2.1997, 0.0)
cell10.region = -surf102

# B4C
cell11 = openmc.Cell(cell_id=11, fill=universe7)
cell11.translation = (-0.635, 3.29955, 0.0)
cell11.region = -surf103

# B4C
cell12 = openmc.Cell(cell_id=12, fill=universe7)
cell12.translation = (-3.175, 1.09985, 0.0)
cell12.region = -surf104

# B4C
cell13 = openmc.Cell(cell_id=13, fill=universe7)
cell13.translation = (-2.54, -2.1997, 0.0)
cell13.region = -surf105

# B4C
cell14 = openmc.Cell(cell_id=14, fill=universe7)
cell14.translation = (0.635, -3.29955, 0.0)
cell14.region = -surf106

# B4C
cell15 = openmc.Cell(cell_id=15, fill=universe7)
cell15.translation = (3.175, -1.09985, 0.0)
cell15.region = -surf107

# Holes
cell16 = openmc.Cell(cell_id=16, fill=universe6)
cell16.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf30_0 | +surf30_1 | +surf30_2 | +surf30_3 | +surf30_4 | +surf30_5) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5)

# Alles
cell17 = openmc.Cell(cell_id=17, fill=universe1)
cell17.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5)

# Mod
cell21 = openmc.Cell(cell_id=21, fill=mat4)
cell21.region = -surf1 & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# Mod
cell28 = openmc.Cell(cell_id=28, fill=mat4)
cell28.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax)

# Alles
cell29 = openmc.Cell(cell_id=29, fill=universe1)
cell29.region = (-surf4 & +surf4_zmin & -surf4_zmax) & +surf20 & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

# Alles
cell37 = openmc.Cell(cell_id=37, fill=universe1)
cell37.region = (-surf4 & +surf4_zmin & -surf4_zmax) & +surf20 & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

# Mod
cell42 = openmc.Cell(cell_id=42, fill=mat4)
cell42.region = -surf1 & (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf92 | -surf92_zmin | +surf92_zmax) & (+surf93 | -surf93_zmin | +surf93_zmax)

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
source.space = openmc.stats.Box((-2.27, -2.09985, 47.3), (2.27, 2.09985, 49.3))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
