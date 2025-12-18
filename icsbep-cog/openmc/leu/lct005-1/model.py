"""
LEU-COMP-THERM-005-1: 132 U(4.31)O2 rods in water; 2.398 cm pitch; 0gGd/L
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

# Water
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.674900e-02)
mat6.add_nuclide("O16", 3.337500e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Boundary condition
surf1 = openmc.ZCylinder(surface_id=1, x0=-22.86, y0=109.14, r=76.014, boundary_type="vacuum")
# Acrylic base plate
surf2 = openmc.ZCylinder(surface_id=2, x0=-2.54, y0=0.0, r=99.9)
# Propylene lattice plate - bottom - *** BENCHMARK RADIUS IS 45.72 ***
surf3 = openmc.ZCylinder(surface_id=3, x0=0.809, y0=2.159, r=58.42)
# Propylene lattice plate - middle - *** BENCHMARK RADIUS IS 45.72 ***
surf4 = openmc.ZCylinder(surface_id=4, x0=37.639, y0=38.989, r=58.42)
# Propylene lattice plate - top    - *** BENCHMARK RADIUS IS 45.72 ***
surf5 = openmc.ZCylinder(surface_id=5, x0=86.28, y0=87.63, r=58.42)
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
# Prism 21: 6-sided polygon
surf21_0 = openmc.Plane(a=0.8660254123, b=0.4999999852, c=0, d=12.4603736322)
surf21_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=12.4603740000)
surf21_2 = openmc.Plane(a=-0.8660254123, b=0.4999999852, c=0, d=12.4603736322)
surf21_3 = openmc.Plane(a=-0.8660254123, b=-0.4999999852, c=0, d=12.4603736322)
surf21_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=12.4603740000)
surf21_5 = openmc.Plane(a=0.8660254123, b=-0.4999999852, c=0, d=12.4603736322)
# Prism 22: 18-sided polygon
surf22_0 = openmc.Plane(a=0.9819805074, b=0.1889822293, c=0, d=54.1601529075)
surf22_1 = openmc.Plane(a=0.8660254123, b=0.4999999852, c=0, d=53.9949524064)
surf22_2 = openmc.Plane(a=0.6546534753, b=0.7559291153, c=0, d=54.1601516555)
surf22_3 = openmc.Plane(a=0.3273271752, b=0.9449110648, c=0, d=54.1601517421)
surf22_4 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=53.9949540000)
surf22_5 = openmc.Plane(a=-0.3273271752, b=0.9449110648, c=0, d=54.1601517421)
surf22_6 = openmc.Plane(a=-0.6546534753, b=0.7559291153, c=0, d=54.1601516555)
surf22_7 = openmc.Plane(a=-0.8660254123, b=0.4999999852, c=0, d=53.9949524064)
surf22_8 = openmc.Plane(a=-0.9819805074, b=0.1889822293, c=0, d=54.1601529075)
surf22_9 = openmc.Plane(a=-0.9819805074, b=-0.1889822293, c=0, d=54.1601529075)
surf22_10 = openmc.Plane(a=-0.8660254123, b=-0.4999999852, c=0, d=53.9949524064)
surf22_11 = openmc.Plane(a=-0.6546534753, b=-0.7559291153, c=0, d=54.1601516555)
surf22_12 = openmc.Plane(a=-0.3273271752, b=-0.9449110648, c=0, d=54.1601517421)
surf22_13 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=53.9949540000)
surf22_14 = openmc.Plane(a=0.3273271752, b=-0.9449110648, c=0, d=54.1601517421)
surf22_15 = openmc.Plane(a=0.6546534753, b=-0.7559291153, c=0, d=54.1601516555)
surf22_16 = openmc.Plane(a=0.8660254123, b=-0.4999999852, c=0, d=53.9949524064)
surf22_17 = openmc.Plane(a=0.9819805074, b=-0.1889822293, c=0, d=54.1601529075)
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
u4_cell1.region = -surf1 & -surf17
u4_cell2 = openmc.Cell(fill=mat6)
u4_cell2.region = -surf1 & -surf18
u4_cell3 = openmc.Cell(fill=mat6)
u4_cell3.region = -surf1 & -surf19
u4_cell4 = openmc.Cell(fill=mat6)
u4_cell4.region = -surf1 & -surf20
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

# Lattice 5: 13x7 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-15.587, -14.537103]
lattice5.pitch = [2.398000, 4.153458]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# Lattice 6: 47x27 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-56.353, -56.071683]
lattice6.pitch = [2.398000, 4.153458]
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
cell1.region = -surf1 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5)

# holes
cell2 = openmc.Cell(cell_id=2, fill=universe6)
cell2.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110

# frod
cell3 = openmc.Cell(cell_id=3, fill=universe2)
cell3.translation = (-1.199, 14.537103, 0.0)
cell3.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf101

# frod
cell4 = openmc.Cell(cell_id=4, fill=universe2)
cell4.translation = (-7.194, 12.460374, 0.0)
cell4.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf102

# frod
cell5 = openmc.Cell(cell_id=5, fill=universe2)
cell5.translation = (-4.796, 12.460374, 0.0)
cell5.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf103

# frod
cell6 = openmc.Cell(cell_id=6, fill=universe2)
cell6.translation = (-2.398, 12.460374, 0.0)
cell6.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf104

# frod
cell7 = openmc.Cell(cell_id=7, fill=universe2)
cell7.translation = (0.0, 12.460374, 0.0)
cell7.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf105

# frod
cell8 = openmc.Cell(cell_id=8, fill=universe2)
cell8.translation = (2.398, 12.460374, 0.0)
cell8.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf106

# frod
cell9 = openmc.Cell(cell_id=9, fill=universe2)
cell9.translation = (4.796, 12.460374, 0.0)
cell9.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf107

# frod
cell10 = openmc.Cell(cell_id=10, fill=universe2)
cell10.translation = (7.194, 12.460374, 0.0)
cell10.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf108

# frod
cell11 = openmc.Cell(cell_id=11, fill=universe2)
cell11.translation = (-8.393, 10.383645, 0.0)
cell11.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf109

# frod
cell12 = openmc.Cell(cell_id=12, fill=universe2)
cell12.translation = (8.393, 10.383645, 0.0)
cell12.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf110

# frod
cell13 = openmc.Cell(cell_id=13, fill=universe2)
cell13.translation = (-9.592, 8.306916, 0.0)
cell13.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf111

# frod
cell14 = openmc.Cell(cell_id=14, fill=universe2)
cell14.translation = (9.592, 8.306916, 0.0)
cell14.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf112

# frod
cell15 = openmc.Cell(cell_id=15, fill=universe2)
cell15.translation = (11.99, 8.306916, 0.0)
cell15.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf113

# frod
cell16 = openmc.Cell(cell_id=16, fill=universe2)
cell16.translation = (-13.189, 6.230187, 0.0)
cell16.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf114

# frod
cell17 = openmc.Cell(cell_id=17, fill=universe2)
cell17.translation = (-10.791, 6.230187, 0.0)
cell17.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf115

# frod
cell18 = openmc.Cell(cell_id=18, fill=universe2)
cell18.translation = (10.791, 6.230187, 0.0)
cell18.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf116

# frod
cell19 = openmc.Cell(cell_id=19, fill=universe2)
cell19.translation = (-11.99, 4.153458, 0.0)
cell19.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf117

# frod
cell20 = openmc.Cell(cell_id=20, fill=universe2)
cell20.translation = (11.99, 4.153458, 0.0)
cell20.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf118

# frod
cell21 = openmc.Cell(cell_id=21, fill=universe2)
cell21.translation = (-13.189, 2.076729, 0.0)
cell21.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf119

# frod
cell22 = openmc.Cell(cell_id=22, fill=universe2)
cell22.translation = (13.189, 2.076729, 0.0)
cell22.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf120

# frod
cell23 = openmc.Cell(cell_id=23, fill=universe2)
cell23.translation = (-14.388, 0.0, 0.0)
cell23.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf121

# frod
cell24 = openmc.Cell(cell_id=24, fill=universe2)
cell24.translation = (14.388, 0.0, 0.0)
cell24.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf122

# frod
cell25 = openmc.Cell(cell_id=25, fill=universe2)
cell25.translation = (-13.189, -2.076729, 0.0)
cell25.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf123

# frod
cell26 = openmc.Cell(cell_id=26, fill=universe2)
cell26.translation = (13.189, -2.076729, 0.0)
cell26.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf124

# frod
cell27 = openmc.Cell(cell_id=27, fill=universe2)
cell27.translation = (-11.99, -4.153458, 0.0)
cell27.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf125

# frod
cell28 = openmc.Cell(cell_id=28, fill=universe2)
cell28.translation = (11.99, -4.153458, 0.0)
cell28.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf126

# frod
cell29 = openmc.Cell(cell_id=29, fill=universe2)
cell29.translation = (-10.791, -6.230187, 0.0)
cell29.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf127

# frod
cell30 = openmc.Cell(cell_id=30, fill=universe2)
cell30.translation = (10.791, -6.230187, 0.0)
cell30.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf128

# frod
cell31 = openmc.Cell(cell_id=31, fill=universe2)
cell31.translation = (13.189, -6.230187, 0.0)
cell31.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf129

# frod
cell32 = openmc.Cell(cell_id=32, fill=universe2)
cell32.translation = (-9.592, -8.306916, 0.0)
cell32.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf130

# frod
cell33 = openmc.Cell(cell_id=33, fill=universe2)
cell33.translation = (9.592, -8.306916, 0.0)
cell33.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf131

# frod
cell34 = openmc.Cell(cell_id=34, fill=universe2)
cell34.translation = (-8.393, -10.383645, 0.0)
cell34.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf132

# frod
cell35 = openmc.Cell(cell_id=35, fill=universe2)
cell35.translation = (8.393, -10.383645, 0.0)
cell35.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf133

# frod
cell36 = openmc.Cell(cell_id=36, fill=universe2)
cell36.translation = (-7.194, -12.460374, 0.0)
cell36.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf134

# frod
cell37 = openmc.Cell(cell_id=37, fill=universe2)
cell37.translation = (-4.796, -12.460374, 0.0)
cell37.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf135

# frod
cell38 = openmc.Cell(cell_id=38, fill=universe2)
cell38.translation = (-2.398, -12.460374, 0.0)
cell38.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf136

# frod
cell39 = openmc.Cell(cell_id=39, fill=universe2)
cell39.translation = (0.0, -12.460374, 0.0)
cell39.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf137

# frod
cell40 = openmc.Cell(cell_id=40, fill=universe2)
cell40.translation = (2.398, -12.460374, 0.0)
cell40.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf138

# frod
cell41 = openmc.Cell(cell_id=41, fill=universe2)
cell41.translation = (4.796, -12.460374, 0.0)
cell41.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf139

# frod
cell42 = openmc.Cell(cell_id=42, fill=universe2)
cell42.translation = (7.194, -12.460374, 0.0)
cell42.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf140

# frod
cell43 = openmc.Cell(cell_id=43, fill=universe2)
cell43.translation = (1.199, -14.537103, 0.0)
cell43.region = -surf1 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & (-surf22_0 & -surf22_1 & -surf22_2 & -surf22_3 & -surf22_4 & -surf22_5 & -surf22_6 & -surf22_7 & -surf22_8 & -surf22_9 & -surf22_10 & -surf22_11 & -surf22_12 & -surf22_13 & -surf22_14 & -surf22_15 & -surf22_16 & -surf22_17) & -surf141

# alles
cell44 = openmc.Cell(cell_id=44, fill=universe1)
cell44.region = -surf1 & (+surf22_0 | +surf22_1 | +surf22_2 | +surf22_3 | +surf22_4 | +surf22_5 | +surf22_6 | +surf22_7 | +surf22_8 | +surf22_9 | +surf22_10 | +surf22_11 | +surf22_12 | +surf22_13 | +surf22_14 | +surf22_15 | +surf22_16 | +surf22_17) & +surf201 & +surf202 & +surf203 & +surf204 & +surf205 & +surf206 & +surf207 & +surf208 & +surf209 & +surf210

# Water
cell54 = openmc.Cell(cell_id=54, fill=mat6)
cell54.region = +surf15 & -surf16

# Alles
cell55 = openmc.Cell(cell_id=55, fill=universe1)
cell55.region = -surf1 & +surf16 & +surf17 & +surf18 & +surf19 & +surf20

# Alles
cell61 = openmc.Cell(cell_id=61, fill=universe1)
cell61.region = -surf1 & +surf16 & +surf17 & +surf18 & +surf19 & +surf20

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell54, cell55, cell61])
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
