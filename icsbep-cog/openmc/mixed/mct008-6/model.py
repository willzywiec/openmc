"""
MIX-COMP-THERM-008-6: 365 MOX pins with 3.5204 cm pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# MOX
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.030700e-04)
mat1.add_nuclide("Pu240", 9.924800e-05)
mat1.add_nuclide("Pu241", 1.695700e-05)
mat1.add_nuclide("Pu242", 2.787400e-06)
mat1.add_nuclide("Am241", 1.638900e-06)
mat1.add_nuclide("U234", 1.144800e-06)
mat1.add_nuclide("U235", 1.498700e-04)
mat1.add_nuclide("U238", 2.066400e-02)
mat1.add_nuclide("O16", 4.309000e-02)

# Zr-2
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Zr", 4.262100e-02)
mat2.add_element("Ni", 3.033600e-05)
mat2.add_element("Cr", 7.609300e-05)
mat2.add_element("Fe", 9.564200e-05)
mat2.add_element("Sn", 4.832700e-04)

# Al-6061
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.843300e-02)
mat3.add_element("Si", 3.460700e-04)
mat3.add_element("Fe", 1.015200e-04)
mat3.add_element("Cu", 6.373100e-05)
mat3.add_element("Mn", 2.211500e-05)
mat3.add_element("Mg", 6.665100e-04)
mat3.add_element("Cr", 6.231000e-05)
mat3.add_element("Zn", 3.096700e-05)
mat3.add_element("Ti", 2.537500e-05)

# Lucite
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 5.678200e-02)
mat4.add_element("C", 3.548900e-02)
mat4.add_nuclide("O16", 1.419600e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

# UO2
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U234", 1.137100e-06)
mat5.add_nuclide("U235", 1.488600e-04)
mat5.add_nuclide("U238", 2.052500e-02)
mat5.add_nuclide("O16", 4.194400e-02)

# Water
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.666200e-02)
mat6.add_nuclide("O16", 3.333100e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# MOX fuel
surf1 = openmc.ZCylinder(surface_id=1, r=0.64135)
# UO2
surf2 = openmc.ZCylinder(surface_id=2, r=0.64135)
# Zr-2
surf3 = openmc.ZCylinder(surface_id=3, r=0.71775)
surf4 = openmc.ZCylinder(surface_id=4, x0=-1.7602, y0=-3.048756, r=0.71775)
surf5 = openmc.ZCylinder(surface_id=5, x0=-1.7602, y0=3.048756, r=0.71775)
surf6 = openmc.ZCylinder(surface_id=6, x0=1.7602, y0=-3.048756, r=0.71775)
surf7 = openmc.ZCylinder(surface_id=7, x0=1.7602, y0=3.048756, r=0.71775)
# Upper  Lucite plate
surf11 = openmc.model.RectangularParallelepiped(-36.9646, 36.9646, -36.5855, 36.5855, 70.1675, 72.0725)
# Middle Lucite plate
surf12 = openmc.model.RectangularParallelepiped(-36.9646, 36.9646, -36.5855, 36.5855, 24.447499999999998, 26.3525)
# Bottom Lucite plate
surf13 = openmc.model.RectangularParallelepiped(-36.9646, 36.9646, -36.5855, 36.5855, 0.0, 1.905)
# BCD
surf14 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -16.192499999999995, 115.6335, boundary_type="vacuum")
# Top of aluminum plate
surf15 = openmc.ZPlane(surface_id=15, z0=-14.9225)
# Prism 21: 12-sided polygon
surf21_0 = openmc.Plane(a=0.8857416501, b=0.4641785532, c=0, d=32.9326185739)
surf21_1 = openmc.Plane(a=0.5000000207, b=0.8660253918, c=0, d=36.0841014959)
surf21_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=35.0606940000)
surf21_3 = openmc.Plane(a=-0.5000000207, b=0.8660253918, c=0, d=37.8443015689)
surf21_4 = openmc.Plane(a=-0.8857416501, b=0.4641785532, c=0, d=36.0507834789)
surf21_5 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=35.9080800000)
surf21_6 = openmc.Plane(a=-0.8857416501, b=-0.4641785532, c=0, d=36.0507834789)
surf21_7 = openmc.Plane(a=-0.5000000207, b=-0.8660253918, c=0, d=37.8443015689)
surf21_8 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=35.0606940000)
surf21_9 = openmc.Plane(a=0.5000000207, b=-0.8660253918, c=0, d=36.0841014959)
surf21_10 = openmc.Plane(a=0.8857416501, b=-0.4641785532, c=0, d=32.9326185739)
surf21_11 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=32.3876800000)
surf22 = openmc.model.RectangularParallelepiped(-36.9646, 36.9646, -36.5855, 36.5855, -16.192499999999995, 115.6335)
surf101 = openmc.ZCylinder(surface_id=101, x0=-17.602, y0=33.536316, r=0.71775)
surf102 = openmc.ZCylinder(surface_id=102, x0=-14.0816, y0=33.536316, r=0.71775)
surf103 = openmc.ZCylinder(surface_id=103, x0=10.5612, y0=33.536316, r=0.71775)
surf104 = openmc.ZCylinder(surface_id=104, x0=14.0816, y0=33.536316, r=0.71775)
surf105 = openmc.ZCylinder(surface_id=105, x0=-22.8826, y0=30.48756, r=0.71775)
surf106 = openmc.ZCylinder(surface_id=106, x0=19.3622, y0=30.48756, r=0.71775)
surf107 = openmc.ZCylinder(surface_id=107, x0=-24.6428, y0=27.438804, r=0.71775)
surf108 = openmc.ZCylinder(surface_id=108, x0=21.1224, y0=27.438804, r=0.71775)
surf109 = openmc.ZCylinder(surface_id=109, x0=-24.6428, y0=-27.438804, r=0.71775)
surf110 = openmc.ZCylinder(surface_id=110, x0=21.1224, y0=-27.438804, r=0.71775)
surf111 = openmc.ZCylinder(surface_id=111, x0=-22.8826, y0=-30.48756, r=0.71775)
surf112 = openmc.ZCylinder(surface_id=112, x0=19.3622, y0=-30.48756, r=0.71775)
surf113 = openmc.ZCylinder(surface_id=113, x0=-17.602, y0=-33.536316, r=0.71775)
surf114 = openmc.ZCylinder(surface_id=114, x0=-14.0816, y0=-33.536316, r=0.71775)
surf115 = openmc.ZCylinder(surface_id=115, x0=10.5612, y0=-33.536316, r=0.71775)
surf116 = openmc.ZCylinder(surface_id=116, x0=14.0816, y0=-33.536316, r=0.71775)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1116, z0=3.1035)
surf1_zmax = openmc.ZPlane(surface_id=1117, z0=94.0435)
surf2_zmin = openmc.ZPlane(surface_id=1118, z0=2.6035)
surf2_zmax = openmc.ZPlane(surface_id=1119, z0=3.1035)
surf3_zmin = openmc.ZPlane(surface_id=1120, z0=1.905)
surf3_zmax = openmc.ZPlane(surface_id=1121, z0=94.869)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell1 = openmc.Cell(fill=mat5)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

u2_cell0 = openmc.Cell(fill=mat4)
u2_cell0.region = -surf11
u2_cell1 = openmc.Cell(fill=mat4)
u2_cell1.region = -surf12
u2_cell2 = openmc.Cell(fill=mat4)
u2_cell2.region = -surf13
u2_cell3 = openmc.Cell(fill=mat6)
u2_cell3.region = +surf11 & +surf12 & +surf13 & -surf14 & +surf15
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = -surf14 & -surf15
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat6)
u4_cell0.region = (-surf3 & +surf3_zmin & -surf3_zmax)
u4_cell1 = openmc.Cell(fill=mat6)
u4_cell1.region = -surf4
u4_cell2 = openmc.Cell(fill=mat6)
u4_cell2.region = -surf5
u4_cell3 = openmc.Cell(fill=mat6)
u4_cell3.region = -surf6
u4_cell4 = openmc.Cell(fill=mat6)
u4_cell4.region = -surf7
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

# Lattice 5: 26x17 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-45.7652, -51.828852]
lattice5.pitch = [3.520400, 6.097512]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# Lattice 6: 26x17 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-45.7652, -51.828852]
lattice6.pitch = [3.520400, 6.097512]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# flt5c
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110 & +surf111 & +surf112 & +surf113 & +surf114 & +surf115 & +surf116

# water
cell2 = openmc.Cell(cell_id=2, fill=mat6)
cell2.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf101

# water
cell3 = openmc.Cell(cell_id=3, fill=mat6)
cell3.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf102

# water
cell4 = openmc.Cell(cell_id=4, fill=mat6)
cell4.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf103

# water
cell5 = openmc.Cell(cell_id=5, fill=mat6)
cell5.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf104

# water
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf105

# water
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf106

# water
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf107

# water
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf108

# water
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf109

# water
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf110

# water
cell12 = openmc.Cell(cell_id=12, fill=mat6)
cell12.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf111

# water
cell13 = openmc.Cell(cell_id=13, fill=mat6)
cell13.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf112

# water
cell14 = openmc.Cell(cell_id=14, fill=mat6)
cell14.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf113

# water
cell15 = openmc.Cell(cell_id=15, fill=mat6)
cell15.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf114

# water
cell16 = openmc.Cell(cell_id=16, fill=mat6)
cell16.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf115

# water
cell17 = openmc.Cell(cell_id=17, fill=mat6)
cell17.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5 & -surf21_6 & -surf21_7 & -surf21_8 & -surf21_9 & -surf21_10 & -surf21_11) & -surf22 & -surf116

# elttc
cell18 = openmc.Cell(cell_id=18, fill=universe6)
cell18.region = -surf14 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5 | +surf21_6 | +surf21_7 | +surf21_8 | +surf21_9 | +surf21_10 | +surf21_11) & -surf22

# else
cell19 = openmc.Cell(cell_id=19, fill=universe2)
cell19.region = -surf14 & +surf22

# ZR2
cell23 = openmc.Cell(cell_id=23, fill=mat2)
cell23.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# Al6061
cell29 = openmc.Cell(cell_id=29, fill=mat3)
cell29.region = -surf14 & -surf15

# else
cell30 = openmc.Cell(cell_id=30, fill=universe2)
cell30.region = (+surf3 | -surf3_zmin | +surf3_zmax) & +surf4 & +surf5 & +surf6 & +surf7 & -surf14

# else
cell36 = openmc.Cell(cell_id=36, fill=universe2)
cell36.region = (+surf3 | -surf3_zmin | +surf3_zmax) & +surf4 & +surf5 & +surf6 & +surf7 & -surf14

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell23, cell29, cell30, cell36])
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
source.space = openmc.stats.Point((0.0, 0.0, 48.5735))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
