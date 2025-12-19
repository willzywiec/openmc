"""
PU-SOL-THERM-033-23: 202.67 gPu(3.13)/L at H/X=116.4 with 37 (3x60) pyrex tubes at 3.23cm pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.490300e-10)
mat1.add_nuclide("U238", 2.087400e-08)
mat1.add_nuclide("Pu239", 4.938800e-04)
mat1.add_nuclide("Pu240", 1.593900e-05)
mat1.add_nuclide("Pu241", 6.075700e-07)
mat1.add_nuclide("Pu242", 6.050600e-08)
mat1.add_nuclide("Am241", 7.088400e-08)
mat1.add_nuclide("H1", 5.749200e-02)
mat1.add_nuclide("O16", 3.866400e-02)
mat1.add_element("N", 3.554800e-03)
mat1.add_element("Fe", 2.943800e-06)
mat1.add_element("Cr", 3.520900e-07)
mat1.add_element("Ni", 4.159100e-07)
mat1.add_element("Mn", 1.332900e-07)
mat1.add_element("Ca", 1.827200e-06)
mat1.add_element("Cu", 2.496800e-07)
mat1.add_element("Mg", 1.004300e-06)
mat1.add_element("Zn", 2.799700e-07)
mat1.add_element("Na", 1.327200e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.954600e-02)
mat2.add_element("Si", 1.646900e-03)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Mn", 8.659700e-04)
mat2.add_element("Si", 1.693900e-03)
mat2.add_element("S", 4.450400e-05)
mat2.add_element("P", 6.143900e-05)
mat2.add_element("C", 1.188300e-04)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.670600e-02)
mat3.add_nuclide("O16", 3.335300e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("N", 4.198500e-05)
mat4.add_nuclide("O16", 1.126300e-05)

# Polyethylene
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 8.310400e-02)
mat5.add_element("C", 4.155200e-02)
mat5.add_s_alpha_beta("c_H_in_CH2")

# Borated
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("B10", 1.039600e-03)
mat6.add_nuclide("B11", 4.184400e-03)
mat6.add_element("Al", 5.334600e-04)
mat6.add_element("Fe", 3.705600e-06)
mat6.add_element("Na", 1.482700e-03)
mat6.add_element("K", 3.061000e-04)
mat6.add_element("Si", 1.789200e-02)
mat6.add_nuclide("O16", 4.532300e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Critical solution height, Hc
surf1 = openmc.ZPlane(surface_id=1, z0=48.89)
# SST solution tank, inner
# surf2: Unsupported surface type "rev" with params ['3', '0.0', '0.0', '0.6', '17.98', '80.7', '17.98']
# SST solution  tank, outer
surf3 = openmc.ZCylinder(surface_id=3, r=18.28)
# SST reflector tank, inner
surf4 = openmc.ZCylinder(surface_id=4, r=54.6)
# SST refelctor tank, top
surf5 = openmc.ZPlane(surface_id=5, z0=63.2)
# SST reflector tank, outer, and BCD
surf6 = openmc.ZCylinder(surface_id=6, r=55.0, boundary_type="vacuum")
# Basket outer boundary
surf10 = openmc.ZCylinder(surface_id=10, r=17.8)
# SST bottom plate
surf11 = openmc.ZCylinder(surface_id=11, r=17.5)
# SST annular top plate, inner
surf12 = openmc.ZCylinder(surface_id=12, r=13.75)
# SST annular top plate, outer
surf13 = openmc.ZCylinder(surface_id=13, r=17.8)
# Tie rod, inner
surf14 = openmc.ZCylinder(surface_id=14, r=0.3)
# Tie rod, outer
surf15 = openmc.ZCylinder(surface_id=15, r=0.4)
# Tie rod #1
surf16 = openmc.ZCylinder(surface_id=16, x0=0.0, y0=-16.9, r=0.4)
# Tie rod #2
surf17 = openmc.ZCylinder(surface_id=17, x0=-14.63583, y0=8.45, r=0.4)
# Tie rod #3
surf18 = openmc.ZCylinder(surface_id=18, x0=14.63583, y0=8.45, r=0.4)
# Lower polyethylene grid plate, inner region
surf19 = openmc.ZCylinder(surface_id=19, r=17.5)
# Upper polyethylene grid plate, inner region
surf20 = openmc.ZCylinder(surface_id=20, r=17.5)
# Lower polyethylene grid plate, outer region
surf21 = openmc.ZCylinder(surface_id=21, r=17.5)
# Upper polyethylene grid plate, outer region
surf22 = openmc.ZCylinder(surface_id=22, r=17.5)
# 3x60 pyrex tube, inner
surf23 = openmc.ZCylinder(surface_id=23, r=1.3)
# 3x60 pyrex tube, outer
surf24 = openmc.ZCylinder(surface_id=24, r=1.5)
# Unit cell #1
# Prism 101: 6-sided polygon
surf101_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf101_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf101_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf101_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf101_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf101_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #2
# Prism 102: 6-sided polygon
surf102_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf102_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf102_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf102_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf102_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf102_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #3
# Prism 103: 6-sided polygon
surf103_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf103_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf103_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf103_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf103_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf103_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #4
# Prism 104: 6-sided polygon
surf104_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf104_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf104_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf104_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf104_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf104_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #5
# Prism 105: 6-sided polygon
surf105_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf105_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf105_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf105_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf105_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf105_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #6
# Prism 106: 6-sided polygon
surf106_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf106_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf106_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf106_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf106_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf106_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #7
# Prism 107: 6-sided polygon
surf107_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf107_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf107_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf107_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf107_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf107_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #8
# Prism 108: 6-sided polygon
surf108_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf108_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf108_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf108_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf108_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf108_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #9
# Prism 109: 6-sided polygon
surf109_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf109_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf109_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf109_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf109_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf109_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #10
# Prism 110: 6-sided polygon
surf110_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf110_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf110_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf110_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf110_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf110_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #11
# Prism 111: 6-sided polygon
surf111_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf111_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf111_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf111_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf111_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf111_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #12
# Prism 112: 6-sided polygon
surf112_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf112_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf112_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf112_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf112_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf112_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #13
# Prism 113: 6-sided polygon
surf113_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf113_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf113_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf113_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf113_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf113_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #14
# Prism 114: 6-sided polygon
surf114_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf114_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf114_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf114_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf114_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf114_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #15
# Prism 115: 6-sided polygon
surf115_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf115_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf115_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf115_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf115_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf115_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #16
# Prism 116: 6-sided polygon
surf116_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf116_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf116_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf116_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf116_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf116_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #17
# Prism 117: 6-sided polygon
surf117_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf117_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf117_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf117_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf117_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf117_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #18
# Prism 118: 6-sided polygon
surf118_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf118_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf118_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf118_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf118_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf118_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #19
# Prism 119: 6-sided polygon
surf119_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf119_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf119_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf119_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf119_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf119_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #20
# Prism 120: 6-sided polygon
surf120_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf120_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf120_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf120_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf120_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf120_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #21
# Prism 121: 6-sided polygon
surf121_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf121_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf121_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf121_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf121_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf121_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #22
# Prism 122: 6-sided polygon
surf122_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf122_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf122_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf122_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf122_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf122_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #23
# Prism 123: 6-sided polygon
surf123_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf123_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf123_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf123_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf123_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf123_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #24
# Prism 124: 6-sided polygon
surf124_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf124_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf124_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf124_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf124_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf124_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #25
# Prism 125: 6-sided polygon
surf125_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf125_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf125_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf125_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf125_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf125_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #26
# Prism 126: 6-sided polygon
surf126_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf126_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf126_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf126_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf126_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf126_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #27
# Prism 127: 6-sided polygon
surf127_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf127_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf127_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf127_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf127_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf127_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #28
# Prism 128: 6-sided polygon
surf128_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf128_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf128_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf128_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf128_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf128_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #29
# Prism 129: 6-sided polygon
surf129_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf129_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf129_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf129_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf129_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf129_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #30
# Prism 130: 6-sided polygon
surf130_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf130_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf130_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf130_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf130_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf130_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #31
# Prism 131: 6-sided polygon
surf131_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf131_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf131_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf131_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf131_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf131_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #32
# Prism 132: 6-sided polygon
surf132_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf132_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf132_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf132_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf132_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf132_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #33
# Prism 133: 6-sided polygon
surf133_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf133_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf133_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf133_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf133_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf133_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #34
# Prism 134: 6-sided polygon
surf134_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf134_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf134_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf134_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf134_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf134_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #35
# Prism 135: 6-sided polygon
surf135_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf135_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf135_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf135_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf135_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf135_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #36
# Prism 136: 6-sided polygon
surf136_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf136_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf136_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf136_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf136_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf136_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
# Unit cell #37
# Prism 137: 6-sided polygon
surf137_0 = openmc.Plane(a=0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf137_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=1.6100000000)
surf137_2 = openmc.Plane(a=-0.8660253883, b=0.5000000269, c=0, d=1.6100000865)
surf137_3 = openmc.Plane(a=-0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)
surf137_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=1.6100000000)
surf137_5 = openmc.Plane(a=0.8660253883, b=-0.5000000269, c=0, d=1.6100000865)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1137, z0=-0.3)
surf3_zmax = openmc.ZPlane(surface_id=1138, z0=80.7)
surf4_zmin = openmc.ZPlane(surface_id=1139, z0=-25.9)
surf4_zmax = openmc.ZPlane(surface_id=1140, z0=62.8)
surf6_zmin = openmc.ZPlane(surface_id=1141, z0=-26.3, boundary_type="vacuum")
surf6_zmax = openmc.ZPlane(surface_id=1142, z0=85.7, boundary_type="vacuum")
surf10_zmin = openmc.ZPlane(surface_id=1143, z0=1.2)
surf10_zmax = openmc.ZPlane(surface_id=1144, z0=82.2)
surf11_zmin = openmc.ZPlane(surface_id=1145, z0=1.2)
surf11_zmax = openmc.ZPlane(surface_id=1146, z0=1.38)
surf13_zmin = openmc.ZPlane(surface_id=1147, z0=81.8)
surf13_zmax = openmc.ZPlane(surface_id=1148, z0=82.2)
surf15_zmin = openmc.ZPlane(surface_id=1149, z0=1.38)
surf15_zmax = openmc.ZPlane(surface_id=1150, z0=81.8)
surf19_zmin = openmc.ZPlane(surface_id=1151, z0=2.5)
surf19_zmax = openmc.ZPlane(surface_id=1152, z0=2.7)
surf20_zmin = openmc.ZPlane(surface_id=1153, z0=59.314)
surf20_zmax = openmc.ZPlane(surface_id=1154, z0=59.514)
surf21_zmin = openmc.ZPlane(surface_id=1155, z0=2.5)
surf21_zmax = openmc.ZPlane(surface_id=1156, z0=2.565)
surf22_zmin = openmc.ZPlane(surface_id=1157, z0=59.449)
surf22_zmax = openmc.ZPlane(surface_id=1158, z0=59.514)
surf24_zmin = openmc.ZPlane(surface_id=1159, z0=1.5)
surf24_zmax = openmc.ZPlane(surface_id=1160, z0=61.514)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = +surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = -surf1 & +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = +surf1 & +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell5 = openmc.Cell(fill=mat2)
u1_cell5.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf1 & -surf14 & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell1 = openmc.Cell(fill=mat4)
u2_cell1.region = +surf1 & -surf14 & (-surf15 & +surf15_zmin & -surf15_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1])

u3_cell0 = openmc.Cell(fill=mat1)
u3_cell0.region = -surf1 & -surf23 & (-surf24 & +surf24_zmin & -surf24_zmax) & (-surf119_0 & -surf119_1 & -surf119_2 & -surf119_3 & -surf119_4 & -surf119_5)
u3_cell1 = openmc.Cell(fill=mat6)
u3_cell1.region = +surf23 & (-surf24 & +surf24_zmin & -surf24_zmax) & (-surf119_0 & -surf119_1 & -surf119_2 & -surf119_3 & -surf119_4 & -surf119_5)
u3_cell2 = openmc.Cell(fill=mat1)
u3_cell2.region = -surf1 & (+surf24 | -surf24_zmin | +surf24_zmax) & (+surf19 | -surf19_zmin | +surf19_zmax) & (+surf20 | -surf20_zmin | +surf20_zmax) & (-surf119_0 & -surf119_1 & -surf119_2 & -surf119_3 & -surf119_4 & -surf119_5)
u3_cell3 = openmc.Cell(fill=mat5)
u3_cell3.region = (+surf24 | -surf24_zmin | +surf24_zmax) & (-surf19 & +surf19_zmin & -surf19_zmax) & (-surf119_0 & -surf119_1 & -surf119_2 & -surf119_3 & -surf119_4 & -surf119_5)
u3_cell4 = openmc.Cell(fill=mat5)
u3_cell4.region = (+surf24 | -surf24_zmin | +surf24_zmax) & (-surf20 & +surf20_zmin & -surf20_zmax) & (-surf119_0 & -surf119_1 & -surf119_2 & -surf119_3 & -surf119_4 & -surf119_5)
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4])

u4_cell0 = openmc.Cell(fill=mat2)
u4_cell0.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf11 & +surf11_zmin & -surf11_zmax) & +surf16 & +surf17 & +surf18
u4_cell1 = openmc.Cell(fill=mat5)
u4_cell1.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf21 & +surf21_zmin & -surf21_zmax) & +surf16 & +surf17 & +surf18 & (+surf101_0 | +surf101_1 | +surf101_2 | +surf101_3 | +surf101_4 | +surf101_5) & (+surf102_0 | +surf102_1 | +surf102_2 | +surf102_3 | +surf102_4 | +surf102_5) & (+surf103_0 | +surf103_1 | +surf103_2 | +surf103_3 | +surf103_4 | +surf103_5) & (+surf104_0 | +surf104_1 | +surf104_2 | +surf104_3 | +surf104_4 | +surf104_5) & (+surf105_0 | +surf105_1 | +surf105_2 | +surf105_3 | +surf105_4 | +surf105_5) & (+surf106_0 | +surf106_1 | +surf106_2 | +surf106_3 | +surf106_4 | +surf106_5) & (+surf107_0 | +surf107_1 | +surf107_2 | +surf107_3 | +surf107_4 | +surf107_5) & (+surf108_0 | +surf108_1 | +surf108_2 | +surf108_3 | +surf108_4 | +surf108_5) & (+surf109_0 | +surf109_1 | +surf109_2 | +surf109_3 | +surf109_4 | +surf109_5) & (+surf110_0 | +surf110_1 | +surf110_2 | +surf110_3 | +surf110_4 | +surf110_5) & (+surf111_0 | +surf111_1 | +surf111_2 | +surf111_3 | +surf111_4 | +surf111_5) & (+surf112_0 | +surf112_1 | +surf112_2 | +surf112_3 | +surf112_4 | +surf112_5) & (+surf113_0 | +surf113_1 | +surf113_2 | +surf113_3 | +surf113_4 | +surf113_5) & (+surf114_0 | +surf114_1 | +surf114_2 | +surf114_3 | +surf114_4 | +surf114_5) & (+surf115_0 | +surf115_1 | +surf115_2 | +surf115_3 | +surf115_4 | +surf115_5) & (+surf116_0 | +surf116_1 | +surf116_2 | +surf116_3 | +surf116_4 | +surf116_5) & (+surf117_0 | +surf117_1 | +surf117_2 | +surf117_3 | +surf117_4 | +surf117_5) & (+surf118_0 | +surf118_1 | +surf118_2 | +surf118_3 | +surf118_4 | +surf118_5) & (+surf119_0 | +surf119_1 | +surf119_2 | +surf119_3 | +surf119_4 | +surf119_5) & (+surf120_0 | +surf120_1 | +surf120_2 | +surf120_3 | +surf120_4 | +surf120_5)
u4_cell2 = openmc.Cell(fill=mat5)
u4_cell2.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf22 & +surf22_zmin & -surf22_zmax) & +surf16 & +surf17 & +surf18 & (+surf101_0 | +surf101_1 | +surf101_2 | +surf101_3 | +surf101_4 | +surf101_5) & (+surf102_0 | +surf102_1 | +surf102_2 | +surf102_3 | +surf102_4 | +surf102_5) & (+surf103_0 | +surf103_1 | +surf103_2 | +surf103_3 | +surf103_4 | +surf103_5) & (+surf104_0 | +surf104_1 | +surf104_2 | +surf104_3 | +surf104_4 | +surf104_5) & (+surf105_0 | +surf105_1 | +surf105_2 | +surf105_3 | +surf105_4 | +surf105_5) & (+surf106_0 | +surf106_1 | +surf106_2 | +surf106_3 | +surf106_4 | +surf106_5) & (+surf107_0 | +surf107_1 | +surf107_2 | +surf107_3 | +surf107_4 | +surf107_5) & (+surf108_0 | +surf108_1 | +surf108_2 | +surf108_3 | +surf108_4 | +surf108_5) & (+surf109_0 | +surf109_1 | +surf109_2 | +surf109_3 | +surf109_4 | +surf109_5) & (+surf110_0 | +surf110_1 | +surf110_2 | +surf110_3 | +surf110_4 | +surf110_5) & (+surf111_0 | +surf111_1 | +surf111_2 | +surf111_3 | +surf111_4 | +surf111_5) & (+surf112_0 | +surf112_1 | +surf112_2 | +surf112_3 | +surf112_4 | +surf112_5) & (+surf113_0 | +surf113_1 | +surf113_2 | +surf113_3 | +surf113_4 | +surf113_5) & (+surf114_0 | +surf114_1 | +surf114_2 | +surf114_3 | +surf114_4 | +surf114_5) & (+surf115_0 | +surf115_1 | +surf115_2 | +surf115_3 | +surf115_4 | +surf115_5) & (+surf116_0 | +surf116_1 | +surf116_2 | +surf116_3 | +surf116_4 | +surf116_5) & (+surf117_0 | +surf117_1 | +surf117_2 | +surf117_3 | +surf117_4 | +surf117_5) & (+surf118_0 | +surf118_1 | +surf118_2 | +surf118_3 | +surf118_4 | +surf118_5) & (+surf119_0 | +surf119_1 | +surf119_2 | +surf119_3 | +surf119_4 | +surf119_5) & (+surf120_0 | +surf120_1 | +surf120_2 | +surf120_3 | +surf120_4 | +surf120_5)
u4_cell3 = openmc.Cell(fill=mat2)
u4_cell3.region = (-surf10 & +surf10_zmin & -surf10_zmax) & +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax) & +surf16 & +surf17 & +surf18
u4_cell4 = openmc.Cell(fill=mat1)
u4_cell4.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & +surf16 & +surf17 & +surf18 & (+surf21 | -surf21_zmin | +surf21_zmax) & (+surf22 | -surf22_zmin | +surf22_zmax)
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# inside
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = (-surf10 & +surf10_zmin & -surf10_zmax)

# outside
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.region = (-surf6 & +surf6_zmin & -surf6_zmax) & (+surf10 | -surf10_zmin | +surf10_zmax)

# Air
cell15 = openmc.Cell(cell_id=15, fill=mat4)
cell15.region = +surf1 & -surf14 & (-surf15 & +surf15_zmin & -surf15_zmax)

# Air
cell23 = openmc.Cell(cell_id=23, fill=mat4)
cell23.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell15, cell23])
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
source.space = openmc.stats.Box((-2.6100000000000003, -2.8600000000000003, 23.445), (2.6100000000000003, 2.8600000000000003, 25.445))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
