"""
LCT025-2: Lattice of 1,433 U(7.5)O2 rods with 0.80 cm (triangular) pitch
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
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0, y0=85.6, r=0.208)
# void, lower
surf2 = openmc.ZCylinder(surface_id=2, x0=-0.8, y0=0.0, r=0.1)
# void, gap
surf3 = openmc.ZCylinder(surface_id=3, x0=0.0, y0=85.9, r=0.215)
# void, upper
surf4 = openmc.ZCylinder(surface_id=4, x0=85.9, y0=86.7, r=0.1)
# SST,  lower
surf5 = openmc.ZCylinder(surface_id=5, x0=-1.0, y0=-0.1, r=0.2)
# SST,  main
surf6 = openmc.ZCylinder(surface_id=6, x0=-0.1, y0=87.4, r=0.255)
# SST,  upper
surf7 = openmc.ZCylinder(surface_id=7, x0=87.4, y0=92.6, r=0.187)
# H2O,  hole
surf8 = openmc.ZCylinder(surface_id=8, x0=-1.0, y0=999.9, r=0.26)
# Support plate
surf11 = openmc.ZCylinder(surface_id=11, x0=-2.2, y0=-1.0, r=99.9)
# Lower grid plate - w/o holes
surf12 = openmc.ZCylinder(surface_id=12, x0=0.5, y0=0.8, r=99.9)
# Upper grid plate - w/o holes
surf13 = openmc.ZCylinder(surface_id=13, x0=81.9, y0=82.2, r=99.9)
# Water and boundary condition
surf14 = openmc.ZCylinder(surface_id=14, x0=-19.9, y0=105.6, r=47.0, boundary_type="vacuum")
# surf21: Error converting surface type "c": could not convert string to float: 'tr'
# surf22: Error converting surface type "c": could not convert string to float: 'tr'
# surf23: Error converting surface type "c": could not convert string to float: 'tr'
# surf24: Error converting surface type "c": could not convert string to float: 'tr'
# Prism 31: 12-sided polygon
surf31_0 = openmc.Plane(a=0.8660253028, b=0.5000001748, c=0, d=15.9348655722)
surf31_1 = openmc.Plane(a=0.4999998252, b=0.8660255047, c=0, d=15.9999944050)
surf31_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=15.9348600000)
surf31_3 = openmc.Plane(a=-0.4999998252, b=0.8660255047, c=0, d=15.9999944050)
surf31_4 = openmc.Plane(a=-0.8660253028, b=0.5000001748, c=0, d=15.9348655722)
surf31_5 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=16.0000000000)
surf31_6 = openmc.Plane(a=-0.8660253028, b=-0.5000001748, c=0, d=15.9348655722)
surf31_7 = openmc.Plane(a=-0.4999998252, b=-0.8660255047, c=0, d=15.9999944050)
surf31_8 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=15.9348600000)
surf31_9 = openmc.Plane(a=0.4999998252, b=-0.8660255047, c=0, d=15.9999944050)
surf31_10 = openmc.Plane(a=0.8660253028, b=-0.5000001748, c=0, d=15.9348655722)
surf31_11 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=16.0000000000)
# Prism 32: 6-sided polygon
surf32_0 = openmc.Plane(a=0.8660253028, b=0.5000001748, c=0, d=16.6276858145)
surf32_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=16.6276800000)
surf32_2 = openmc.Plane(a=-0.8660253028, b=0.5000001748, c=0, d=16.6276858145)
surf32_3 = openmc.Plane(a=-0.8660253028, b=-0.5000001748, c=0, d=16.6276858145)
surf32_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=16.6276800000)
surf32_5 = openmc.Plane(a=0.8660253028, b=-0.5000001748, c=0, d=16.6276858145)
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

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = -surf11 & -surf14
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf12 & -surf14
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = -surf13 & -surf14
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = +surf11 & +surf12 & +surf13 & -surf14
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf1
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = +surf1 & +surf2 & +surf3 & +surf4 & -surf5 & -surf8
u2_cell2 = openmc.Cell(fill=mat2)
u2_cell2.region = +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & -surf6 & -surf8
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & +surf6 & -surf7 & -surf8
u2_cell4 = openmc.Cell(fill=mat4)
u2_cell4.region = +surf5 & +surf6 & +surf7 & -surf8
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat4)
u4_cell0.region = -surf8 & -surf14
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf14
u4_cell2 = openmc.Cell(fill=mat4)
u4_cell2.region = -surf14
u4_cell3 = openmc.Cell(fill=mat4)
u4_cell3.region = -surf14
u4_cell4 = openmc.Cell(fill=mat4)
u4_cell4.region = -surf14
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

# Lattice 5: 41x23 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-16.4, -15.93486]
lattice5.pitch = [0.800000, 1.385640]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# Lattice 6: 49x25 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-19.6, -17.3205]
lattice6.pitch = [0.800000, 1.385640]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# array1
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = -surf14 & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5 & -surf31_6 & -surf31_7 & -surf31_8 & -surf31_9 & -surf31_10 & -surf31_11)

# array2
cell2 = openmc.Cell(cell_id=2, fill=universe6)
cell2.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell3 = openmc.Cell(cell_id=3, fill=universe3)
cell3.translation = (-8.0, 13.8564, 0.0)
cell3.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell4 = openmc.Cell(cell_id=4, fill=universe3)
cell4.translation = (8.0, 13.8564, 0.0)
cell4.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell5 = openmc.Cell(cell_id=5, fill=universe3)
cell5.translation = (-13.6, 8.31384, 0.0)
cell5.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell6 = openmc.Cell(cell_id=6, fill=universe3)
cell6.translation = (13.6, 8.31384, 0.0)
cell6.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell7 = openmc.Cell(cell_id=7, fill=universe3)
cell7.translation = (-14.0, 7.62102, 0.0)
cell7.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell8 = openmc.Cell(cell_id=8, fill=universe3)
cell8.translation = (14.0, 7.62102, 0.0)
cell8.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell9 = openmc.Cell(cell_id=9, fill=universe3)
cell9.translation = (-16.0, 0.0, 0.0)
cell9.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell10 = openmc.Cell(cell_id=10, fill=universe3)
cell10.translation = (16.0, 0.0, 0.0)
cell10.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell11 = openmc.Cell(cell_id=11, fill=universe3)
cell11.translation = (-14.0, -7.62102, 0.0)
cell11.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell12 = openmc.Cell(cell_id=12, fill=universe3)
cell12.translation = (14.0, -7.62102, 0.0)
cell12.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell13 = openmc.Cell(cell_id=13, fill=universe3)
cell13.translation = (-13.6, -8.31384, 0.0)
cell13.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell14 = openmc.Cell(cell_id=14, fill=universe3)
cell14.translation = (13.6, -8.31384, 0.0)
cell14.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell15 = openmc.Cell(cell_id=15, fill=universe3)
cell15.translation = (-8.0, -13.8564, 0.0)
cell15.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell16 = openmc.Cell(cell_id=16, fill=universe3)
cell16.translation = (8.0, -13.8564, 0.0)
cell16.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell17 = openmc.Cell(cell_id=17, fill=universe3)
cell17.translation = (-0.4, -15.93486, 0.0)
cell17.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# FROD
cell18 = openmc.Cell(cell_id=18, fill=universe3)
cell18.translation = (0.4, -15.93486, 0.0)
cell18.region = -surf14 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5)

# D16
cell19 = openmc.Cell(cell_id=19, fill=mat3)
cell19.region = -surf11 & -surf14 & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5)

# water
cell20 = openmc.Cell(cell_id=20, fill=mat4)
cell20.region = +surf11 & -surf14 & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5)

# H2O
cell25 = openmc.Cell(cell_id=25, fill=mat4)
cell25.region = +surf11 & +surf12 & +surf13 & -surf14

# Water
cell31 = openmc.Cell(cell_id=31, fill=mat4)
cell31.region = +surf5 & +surf6 & +surf7 & -surf8

# ALLES
cell32 = openmc.Cell(cell_id=32, fill=universe1)
cell32.region = +surf8 & -surf14

# ALLES
cell38 = openmc.Cell(cell_id=38, fill=universe1)
cell38.region = +surf8 & -surf14

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell25, cell31, cell32, cell38])
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
