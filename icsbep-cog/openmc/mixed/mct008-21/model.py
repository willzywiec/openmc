"""
MIX-COMP-THERM-008-21: Central H2Cd absorber rod and 232 + 14 MOX pins with 2.6670 cm pitch
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

# H2 absorber
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Hf", 9.775900e-03)
mat7.add_nuclide("O16", 2.044000e-02)
mat7.add_element("Zr", 4.439600e-04)
mat7.add_element("Al", 2.920400e-02)

# Cadmium
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Cd", 4.655500e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# MOX fuel
surf1 = openmc.ZCylinder(surface_id=1, r=0.64135)
# UO2
surf2 = openmc.ZCylinder(surface_id=2, r=0.64135)
# Zr-2
surf3 = openmc.ZCylinder(surface_id=3, r=0.71775)
surf4 = openmc.ZCylinder(surface_id=4, x0=-1.3335, y0=-2.30969, r=0.71775)
surf5 = openmc.ZCylinder(surface_id=5, x0=-1.3335, y0=2.30969, r=0.71775)
surf6 = openmc.ZCylinder(surface_id=6, x0=1.3335, y0=-2.30969, r=0.71775)
surf7 = openmc.ZCylinder(surface_id=7, x0=1.3335, y0=2.30969, r=0.71775)
# Upper  Lucite plate
surf11 = openmc.model.RectangularParallelepiped(-22.6695, 22.6695, -23.0969, 23.0969, 70.1675, 72.0725)
# Middle Lucite plate
surf12 = openmc.model.RectangularParallelepiped(-22.6695, 22.6695, -23.0969, 23.0969, 24.447499999999998, 26.3525)
# Bottom Lucite plate
surf13 = openmc.model.RectangularParallelepiped(-22.6695, 22.6695, -23.0969, 23.0969, 0.0, 1.905)
# BCD
surf14 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -16.192499999999995, 115.6335, boundary_type="vacuum")
# Top of aluminum plate
surf15 = openmc.ZPlane(surface_id=15, z0=-14.9225)
# Prism 21: 6-sided polygon
surf21_0 = openmc.Plane(a=0.8660254270, b=0.4999999597, c=0, d=21.9420532322)
surf21_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=21.9420550000)
surf21_2 = openmc.Plane(a=-0.8660254270, b=0.4999999597, c=0, d=21.9420532322)
surf21_3 = openmc.Plane(a=-0.8660254270, b=-0.4999999597, c=0, d=21.9420532322)
surf21_4 = openmc.Plane(a=-0.0000000036, b=-1.0000000000, c=0, d=21.9420550450)
surf21_5 = openmc.Plane(a=0.8660254279, b=-0.4999999582, c=0, d=21.9420532547)
surf22 = openmc.model.RectangularParallelepiped(-22.6695, 22.6695, -23.0969, 23.0969, -16.192499999999995, 115.6335)
# Absorber
surf71 = openmc.ZCylinder(surface_id=71, r=0.46736)
# Zr-2
surf72 = openmc.ZCylinder(surface_id=72, r=0.53594)
# Cd
surf73 = openmc.ZCylinder(surface_id=73, r=0.63754)
# Hole
surf74 = openmc.ZCylinder(surface_id=74, r=0.71775)
surf101 = openmc.ZCylinder(surface_id=101, x0=-12.0015, y0=20.78721, r=0.71775)
surf102 = openmc.ZCylinder(surface_id=102, x0=-9.3345, y0=20.78721, r=0.71775)
# Additional fuel rod #12
surf103 = openmc.ZCylinder(surface_id=103, x0=-6.6675, y0=20.78721, r=0.71775)
# Additional fuel rod #10
surf104 = openmc.ZCylinder(surface_id=104, x0=-4.0005, y0=20.78721, r=0.71775)
# Additional fuel rod #6
surf105 = openmc.ZCylinder(surface_id=105, x0=6.6675, y0=20.78721, r=0.71775)
surf106 = openmc.ZCylinder(surface_id=106, x0=9.3345, y0=20.78721, r=0.71775)
surf107 = openmc.ZCylinder(surface_id=107, x0=12.0015, y0=20.78721, r=0.71775)
surf108 = openmc.ZCylinder(surface_id=108, x0=-13.335, y0=18.47752, r=0.71775)
surf109 = openmc.ZCylinder(surface_id=109, x0=-10.668, y0=18.47752, r=0.71775)
# Additional fuel rod #2
surf110 = openmc.ZCylinder(surface_id=110, x0=-8.001, y0=18.47752, r=0.71775)
# Additional fuel rod #4
surf111 = openmc.ZCylinder(surface_id=111, x0=10.668, y0=18.47752, r=0.71775)
surf112 = openmc.ZCylinder(surface_id=112, x0=13.335, y0=18.47752, r=0.71775)
surf113 = openmc.ZCylinder(surface_id=113, x0=-14.6685, y0=16.16783, r=0.71775)
surf114 = openmc.ZCylinder(surface_id=114, x0=14.6685, y0=16.16783, r=0.71775)
# Additional fuel rod #8
surf115 = openmc.ZCylinder(surface_id=115, x0=-21.336, y0=4.61938, r=0.71775)
# Additional fuel rod #9
surf116 = openmc.ZCylinder(surface_id=116, x0=21.336, y0=4.61938, r=0.71775)
surf117 = openmc.ZCylinder(surface_id=117, x0=-22.6695, y0=2.30969, r=0.71775)
# Additional fuel rod #14
surf118 = openmc.ZCylinder(surface_id=118, x0=22.6695, y0=2.30969, r=0.71775)
surf119 = openmc.ZCylinder(surface_id=119, x0=-24.003, y0=0.0, r=0.71775)
surf120 = openmc.ZCylinder(surface_id=120, x0=24.003, y0=0.0, r=0.71775)
surf121 = openmc.ZCylinder(surface_id=121, x0=-22.6695, y0=-2.30969, r=0.71775)
surf122 = openmc.ZCylinder(surface_id=122, x0=22.6695, y0=-2.30969, r=0.71775)
surf123 = openmc.ZCylinder(surface_id=123, x0=-21.336, y0=-4.61938, r=0.71775)
# Additional fuel rod #7
surf124 = openmc.ZCylinder(surface_id=124, x0=21.336, y0=-4.61938, r=0.71775)
# Additional fuel rod #13
surf125 = openmc.ZCylinder(surface_id=125, x0=-14.6685, y0=-16.16783, r=0.71775)
surf126 = openmc.ZCylinder(surface_id=126, x0=14.6685, y0=-16.16783, r=0.71775)
surf127 = openmc.ZCylinder(surface_id=127, x0=-13.335, y0=-18.47752, r=0.71775)
# Additional fuel rod #3
surf128 = openmc.ZCylinder(surface_id=128, x0=-10.668, y0=-18.47752, r=0.71775)
# Additional fuel rod #1
surf129 = openmc.ZCylinder(surface_id=129, x0=8.001, y0=-18.47752, r=0.71775)
surf130 = openmc.ZCylinder(surface_id=130, x0=10.668, y0=-18.47752, r=0.71775)
surf131 = openmc.ZCylinder(surface_id=131, x0=13.335, y0=-18.47752, r=0.71775)
surf132 = openmc.ZCylinder(surface_id=132, x0=-12.0015, y0=-20.78721, r=0.71775)
surf133 = openmc.ZCylinder(surface_id=133, x0=-9.3345, y0=-20.78721, r=0.71775)
# Additional fuel rod #5
surf134 = openmc.ZCylinder(surface_id=134, x0=-6.6675, y0=-20.78721, r=0.71775)
# Additional fuel rod #11
surf135 = openmc.ZCylinder(surface_id=135, x0=4.0005, y0=-20.78721, r=0.71775)
surf136 = openmc.ZCylinder(surface_id=136, x0=6.6675, y0=-20.78721, r=0.71775)
surf137 = openmc.ZCylinder(surface_id=137, x0=9.3345, y0=-20.78721, r=0.71775)
surf138 = openmc.ZCylinder(surface_id=138, x0=12.0015, y0=-20.78721, r=0.71775)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1138, z0=3.1035)
surf1_zmax = openmc.ZPlane(surface_id=1139, z0=94.0435)
surf2_zmin = openmc.ZPlane(surface_id=1140, z0=2.6035)
surf2_zmax = openmc.ZPlane(surface_id=1141, z0=3.1035)
surf3_zmin = openmc.ZPlane(surface_id=1142, z0=1.905)
surf3_zmax = openmc.ZPlane(surface_id=1143, z0=94.869)
surf71_zmin = openmc.ZPlane(surface_id=1144, z0=2.6035)
surf71_zmax = openmc.ZPlane(surface_id=1145, z0=94.0435)
surf72_zmin = openmc.ZPlane(surface_id=1146, z0=1.905)
surf72_zmax = openmc.ZPlane(surface_id=1147, z0=94.869)
surf73_zmin = openmc.ZPlane(surface_id=1148, z0=1.905)
surf73_zmax = openmc.ZPlane(surface_id=1149, z0=94.869)
surf74_zmin = openmc.ZPlane(surface_id=1150, z0=1.905)
surf74_zmax = openmc.ZPlane(surface_id=1151, z0=94.869)

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

# Lattice 5: 27x17 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-36.0045, -39.26473]
lattice5.pitch = [2.667000, 4.619380]
lattice5.universes = [
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

# Lattice 6: 27x17 array
lattice6 = openmc.RectLattice(lattice_id=6)
lattice6.lower_left = [-36.0045, -39.26473]
lattice6.pitch = [2.667000, 4.619380]
lattice6.universes = [
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
    [universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4, universe4],
]
universe6 = openmc.Universe(universe_id=6)
universe6.add_cell(openmc.Cell(fill=lattice6))

u7_cell0 = openmc.Cell(fill=mat7)
u7_cell0.region = (-surf71 & +surf71_zmin & -surf71_zmax)
u7_cell1 = openmc.Cell(fill=mat2)
u7_cell1.region = (+surf71 | -surf71_zmin | +surf71_zmax) & (-surf72 & +surf72_zmin & -surf72_zmax) & (-surf73 & +surf73_zmin & -surf73_zmax) & (-surf74 & +surf74_zmin & -surf74_zmax)
u7_cell2 = openmc.Cell(fill=mat8)
u7_cell2.region = (+surf72 | -surf72_zmin | +surf72_zmax) & (-surf73 & +surf73_zmin & -surf73_zmax) & (-surf74 & +surf74_zmin & -surf74_zmax)
u7_cell3 = openmc.Cell(fill=mat6)
u7_cell3.region = (+surf72 | -surf72_zmin | +surf72_zmax) & (+surf73 | -surf73_zmin | +surf73_zmax) & (-surf74 & +surf74_zmin & -surf74_zmax)
universe7 = openmc.Universe(universe_id=7, cells=[u7_cell0, u7_cell1, u7_cell2, u7_cell3])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# flt5c
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & +surf101 & +surf102 & +surf106 & +surf107 & +surf108 & +surf109

# abrod
cell2 = openmc.Cell(cell_id=2, fill=universe7)
cell2.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & (-surf74 & +surf74_zmin & -surf74_zmax)

# water
cell3 = openmc.Cell(cell_id=3, fill=mat6)
cell3.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf101 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf121 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf131

# water
cell4 = openmc.Cell(cell_id=4, fill=mat6)
cell4.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf102 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf112 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf122 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf132

# water
cell5 = openmc.Cell(cell_id=5, fill=mat6)
cell5.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf113 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf123 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf133

# water
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf114

# water
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf106 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf126 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf136

# water
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf107 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf117 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf127 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf137

# water
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf108 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf138

# water
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf109 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf119

# water
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf120 & +surf6 & -surf14 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5) & -surf22 & -surf130

# elttc
cell12 = openmc.Cell(cell_id=12, fill=universe6)
cell12.region = -surf14 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5) & -surf22

# else
cell13 = openmc.Cell(cell_id=13, fill=universe2)
cell13.region = -surf14 & +surf22 & +surf118

# frod
cell14 = openmc.Cell(cell_id=14, fill=universe1)
cell14.translation = (22.6695, 2.30969, 0.0)
cell14.region = -surf14 & +surf22 & -surf118

# ZR2
cell18 = openmc.Cell(cell_id=18, fill=mat2)
cell18.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# Al6061
cell24 = openmc.Cell(cell_id=24, fill=mat3)
cell24.region = -surf14 & -surf15

# else
cell25 = openmc.Cell(cell_id=25, fill=universe2)
cell25.region = (+surf3 | -surf3_zmin | +surf3_zmax) & +surf4 & +surf5 & +surf6 & +surf7 & -surf14

# else
cell31 = openmc.Cell(cell_id=31, fill=universe2)
cell31.region = (+surf3 | -surf3_zmin | +surf3_zmax) & +surf4 & +surf5 & +surf6 & +surf7 & -surf14

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell18, cell24, cell25, cell31])
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
source.space = openmc.stats.Box((-3.667, -1.0, 47.5735), (3.667, 1.0, 49.5735))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
