"""
MIX-COMP-THERM-008-2: 286 MOX pins with 2.3622 cm pitch
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
surf4 = openmc.ZCylinder(surface_id=4, x0=-1.1811, y0=-2.045725, r=0.71775)
surf5 = openmc.ZCylinder(surface_id=5, x0=-1.1811, y0=2.045725, r=0.71775)
surf6 = openmc.ZCylinder(surface_id=6, x0=1.1811, y0=-2.045725, r=0.71775)
surf7 = openmc.ZCylinder(surface_id=7, x0=1.1811, y0=2.045725, r=0.71775)
# Upper  Lucite plate
surf11 = openmc.model.RectangularParallelepiped(-24.8031, 24.8031, -24.5487, 24.5487, 70.1675, 72.0725)
# Middle Lucite plate
surf12 = openmc.model.RectangularParallelepiped(-24.8031, 24.8031, -24.5487, 24.5487, 24.447499999999998, 26.3525)
# Bottom Lucite plate
surf13 = openmc.model.RectangularParallelepiped(-24.8031, 24.8031, -24.5487, 24.5487, 0.0, 1.905)
# BCD
surf14 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -16.192499999999995, 115.6335, boundary_type="vacuum")
# Top of aluminum plate
surf15 = openmc.ZPlane(surface_id=15, z0=-14.9225)
# Prism 20: 12-sided polygon
surf20_0 = openmc.Plane(a=0.8660253817, b=0.5000000383, c=0, d=20.4572515661)
surf20_1 = openmc.Plane(a=0.4999999617, b=0.8660254259, c=0, d=20.0786984628)
surf20_2 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=20.4572500000)
surf20_3 = openmc.Plane(a=-0.4999999617, b=0.8660254259, c=0, d=20.0786984628)
surf20_4 = openmc.Plane(a=-0.8660253817, b=0.5000000383, c=0, d=20.4572515661)
surf20_5 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=20.0787000000)
surf20_6 = openmc.Plane(a=-0.8660253817, b=-0.5000000383, c=0, d=20.4572515661)
surf20_7 = openmc.Plane(a=-0.4999999617, b=-0.8660254259, c=0, d=20.0786984628)
surf20_8 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=20.4572500000)
surf20_9 = openmc.Plane(a=0.4999999617, b=-0.8660254259, c=0, d=20.0786984628)
surf20_10 = openmc.Plane(a=0.8660253817, b=-0.5000000383, c=0, d=20.4572515661)
surf20_11 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=20.0787000000)
surf22 = openmc.model.RectangularParallelepiped(-24.8031, 24.8031, -24.5487, 24.5487, -16.192499999999995, 115.6335)
surf101 = openmc.ZCylinder(surface_id=101, x0=-4.7244, y0=20.45725, r=0.71775)
surf102 = openmc.ZCylinder(surface_id=102, x0=-2.3622, y0=20.45725, r=0.71775)
surf103 = openmc.ZCylinder(surface_id=103, x0=0.0, y0=20.45725, r=0.71775)
surf104 = openmc.ZCylinder(surface_id=104, x0=2.3622, y0=20.45725, r=0.71775)
surf105 = openmc.ZCylinder(surface_id=105, x0=4.7244, y0=20.45725, r=0.71775)
surf106 = openmc.ZCylinder(surface_id=106, x0=-8.2677, y0=18.41152, r=0.71775)
surf107 = openmc.ZCylinder(surface_id=107, x0=8.2677, y0=18.41152, r=0.71775)
surf108 = openmc.ZCylinder(surface_id=108, x0=-11.811, y0=16.3658, r=0.71775)
surf109 = openmc.ZCylinder(surface_id=109, x0=11.811, y0=16.3658, r=0.71775)
surf110 = openmc.ZCylinder(surface_id=110, x0=-15.3543, y0=14.320075, r=0.71775)
surf111 = openmc.ZCylinder(surface_id=111, x0=15.3543, y0=14.320075, r=0.71775)
surf112 = openmc.ZCylinder(surface_id=112, x0=-16.5354, y0=12.27435, r=0.71775)
surf113 = openmc.ZCylinder(surface_id=113, x0=16.5354, y0=12.27435, r=0.71775)
surf114 = openmc.ZCylinder(surface_id=114, x0=-17.7165, y0=10.22862, r=0.71775)
surf115 = openmc.ZCylinder(surface_id=115, x0=17.7165, y0=10.22862, r=0.71775)
surf116 = openmc.ZCylinder(surface_id=116, x0=-18.8976, y0=8.1829, r=0.71775)
surf117 = openmc.ZCylinder(surface_id=117, x0=18.8976, y0=8.1829, r=0.71775)
surf118 = openmc.ZCylinder(surface_id=118, x0=-20.0787, y0=6.137175, r=0.71775)
surf119 = openmc.ZCylinder(surface_id=119, x0=20.0787, y0=6.137175, r=0.71775)
surf120 = openmc.ZCylinder(surface_id=120, x0=-20.0787, y0=2.045725, r=0.71775)
surf121 = openmc.ZCylinder(surface_id=121, x0=20.0787, y0=2.045725, r=0.71775)
surf122 = openmc.ZCylinder(surface_id=122, x0=-20.0787, y0=-2.045725, r=0.71775)
surf123 = openmc.ZCylinder(surface_id=123, x0=20.0787, y0=-2.045725, r=0.71775)
surf124 = openmc.ZCylinder(surface_id=124, x0=-20.0787, y0=-6.137175, r=0.71775)
surf125 = openmc.ZCylinder(surface_id=125, x0=20.0787, y0=-6.137175, r=0.71775)
surf126 = openmc.ZCylinder(surface_id=126, x0=-18.8976, y0=-8.1829, r=0.71775)
surf127 = openmc.ZCylinder(surface_id=127, x0=18.8976, y0=-8.1829, r=0.71775)
surf128 = openmc.ZCylinder(surface_id=128, x0=-17.7165, y0=-10.22862, r=0.71775)
surf129 = openmc.ZCylinder(surface_id=129, x0=17.7165, y0=-10.22862, r=0.71775)
surf130 = openmc.ZCylinder(surface_id=130, x0=-16.5354, y0=-12.27435, r=0.71775)
surf131 = openmc.ZCylinder(surface_id=131, x0=16.5354, y0=-12.27435, r=0.71775)
surf132 = openmc.ZCylinder(surface_id=132, x0=-15.3543, y0=-14.320075, r=0.71775)
surf133 = openmc.ZCylinder(surface_id=133, x0=15.3543, y0=-14.320075, r=0.71775)
surf134 = openmc.ZCylinder(surface_id=134, x0=-11.811, y0=-16.3658, r=0.71775)
surf135 = openmc.ZCylinder(surface_id=135, x0=11.811, y0=-16.3658, r=0.71775)
surf136 = openmc.ZCylinder(surface_id=136, x0=-8.2677, y0=-18.41152, r=0.71775)
surf137 = openmc.ZCylinder(surface_id=137, x0=8.2677, y0=-18.41152, r=0.71775)
surf138 = openmc.ZCylinder(surface_id=138, x0=-4.7244, y0=-20.45725, r=0.71775)
surf139 = openmc.ZCylinder(surface_id=139, x0=-2.3622, y0=-20.45725, r=0.71775)
surf140 = openmc.ZCylinder(surface_id=140, x0=0.0, y0=-20.45725, r=0.71775)
surf141 = openmc.ZCylinder(surface_id=141, x0=2.3622, y0=-20.45725, r=0.71775)
surf142 = openmc.ZCylinder(surface_id=142, x0=4.7244, y0=-20.45725, r=0.71775)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=3.1035)
surf1_zmax = openmc.ZPlane(z0=94.0435)
surf2_zmin = openmc.ZPlane(z0=2.6035)
surf2_zmax = openmc.ZPlane(z0=3.1035)
surf3_zmin = openmc.ZPlane(z0=1.905)
surf3_zmax = openmc.ZPlane(z0=94.869)

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
lattice5.lower_left = [-31.8897, -34.777325]
lattice5.pitch = [2.362200, 4.091450]
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
lattice6.lower_left = [-31.8897, -34.777325]
lattice6.pitch = [2.362200, 4.091450]
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

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# flt5c
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = -surf14 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7 & -surf20_8 & -surf20_9 & -surf20_10 & -surf20_11) & -surf22 & +surf101 & +surf105 & +surf111 & +surf118 & +surf125 & +surf132 & +surf134 & +surf138 & +surf142

# Water
cell2 = openmc.Cell(cell_id=2, fill=mat6)
cell2.region = -surf14 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7 & -surf20_8 & -surf20_9 & -surf20_10 & -surf20_11) & -surf22 & -surf101

# Water
cell3 = openmc.Cell(cell_id=3, fill=mat6)
cell3.region = -surf14 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7 & -surf20_8 & -surf20_9 & -surf20_10 & -surf20_11) & -surf22 & -surf105

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat6)
cell4.region = -surf14 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7 & -surf20_8 & -surf20_9 & -surf20_10 & -surf20_11) & -surf22 & -surf111

# Water
cell5 = openmc.Cell(cell_id=5, fill=mat6)
cell5.region = -surf14 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7 & -surf20_8 & -surf20_9 & -surf20_10 & -surf20_11) & -surf22 & -surf118

# Water
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = -surf14 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7 & -surf20_8 & -surf20_9 & -surf20_10 & -surf20_11) & -surf22 & -surf125

# Water
cell7 = openmc.Cell(cell_id=7, fill=mat6)
cell7.region = -surf14 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7 & -surf20_8 & -surf20_9 & -surf20_10 & -surf20_11) & -surf22 & -surf132

# Water
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = -surf14 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7 & -surf20_8 & -surf20_9 & -surf20_10 & -surf20_11) & -surf22 & -surf134

# Water
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = -surf14 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7 & -surf20_8 & -surf20_9 & -surf20_10 & -surf20_11) & -surf22 & -surf138

# Water
cell10 = openmc.Cell(cell_id=10, fill=mat6)
cell10.region = -surf14 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7 & -surf20_8 & -surf20_9 & -surf20_10 & -surf20_11) & -surf22 & -surf142

# elttc
cell11 = openmc.Cell(cell_id=11, fill=universe6)
cell11.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & +surf102 & +surf103 & +surf104 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110 & +surf112 & +surf113

# frod
cell12 = openmc.Cell(cell_id=12, fill=universe1)
cell12.translation = (-2.3622, 20.45725, 0.0)
cell12.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf102

# frod
cell13 = openmc.Cell(cell_id=13, fill=universe1)
cell13.translation = (0.0, 20.45725, 0.0)
cell13.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf103

# frod
cell14 = openmc.Cell(cell_id=14, fill=universe1)
cell14.translation = (2.3622, 20.45725, 0.0)
cell14.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf104

# frod
cell15 = openmc.Cell(cell_id=15, fill=universe1)
cell15.translation = (-8.2677, 18.41152, 0.0)
cell15.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf106

# frod
cell16 = openmc.Cell(cell_id=16, fill=universe1)
cell16.translation = (8.2677, 18.41152, 0.0)
cell16.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf107

# frod
cell17 = openmc.Cell(cell_id=17, fill=universe1)
cell17.translation = (-11.811, 16.3658, 0.0)
cell17.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf108

# frod
cell18 = openmc.Cell(cell_id=18, fill=universe1)
cell18.translation = (11.811, 16.3658, 0.0)
cell18.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf109

# frod
cell19 = openmc.Cell(cell_id=19, fill=universe1)
cell19.translation = (-15.3543, 14.320075, 0.0)
cell19.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf110

# frod
cell20 = openmc.Cell(cell_id=20, fill=universe1)
cell20.translation = (-16.5354, 12.27435, 0.0)
cell20.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf112

# frod
cell21 = openmc.Cell(cell_id=21, fill=universe1)
cell21.translation = (16.5354, 12.27435, 0.0)
cell21.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf113

# frod
cell22 = openmc.Cell(cell_id=22, fill=universe1)
cell22.translation = (-17.7165, 10.22862, 0.0)
cell22.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf114

# frod
cell23 = openmc.Cell(cell_id=23, fill=universe1)
cell23.translation = (17.7165, 10.22862, 0.0)
cell23.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf115

# frod
cell24 = openmc.Cell(cell_id=24, fill=universe1)
cell24.translation = (-18.8976, 8.1829, 0.0)
cell24.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf116

# frod
cell25 = openmc.Cell(cell_id=25, fill=universe1)
cell25.translation = (18.8976, 8.1829, 0.0)
cell25.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf117

# frod
cell26 = openmc.Cell(cell_id=26, fill=universe1)
cell26.translation = (20.0787, 6.137175, 0.0)
cell26.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf119

# frod
cell27 = openmc.Cell(cell_id=27, fill=universe1)
cell27.translation = (-20.0787, 2.045725, 0.0)
cell27.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf120

# frod
cell28 = openmc.Cell(cell_id=28, fill=universe1)
cell28.translation = (20.0787, 2.045725, 0.0)
cell28.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf121

# frod
cell29 = openmc.Cell(cell_id=29, fill=universe1)
cell29.translation = (-20.0787, -2.045725, 0.0)
cell29.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf122

# frod
cell30 = openmc.Cell(cell_id=30, fill=universe1)
cell30.translation = (20.0787, -2.045725, 0.0)
cell30.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf123

# frod
cell31 = openmc.Cell(cell_id=31, fill=universe1)
cell31.translation = (-20.0787, -6.137175, 0.0)
cell31.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf124

# frod
cell32 = openmc.Cell(cell_id=32, fill=universe1)
cell32.translation = (-18.8976, -8.1829, 0.0)
cell32.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf126

# frod
cell33 = openmc.Cell(cell_id=33, fill=universe1)
cell33.translation = (18.8976, -8.1829, 0.0)
cell33.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf127

# frod
cell34 = openmc.Cell(cell_id=34, fill=universe1)
cell34.translation = (-17.7165, -10.22862, 0.0)
cell34.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf128

# frod
cell35 = openmc.Cell(cell_id=35, fill=universe1)
cell35.translation = (17.7165, -10.22862, 0.0)
cell35.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf129

# frod
cell36 = openmc.Cell(cell_id=36, fill=universe1)
cell36.translation = (-16.5354, -12.27435, 0.0)
cell36.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf130

# frod
cell37 = openmc.Cell(cell_id=37, fill=universe1)
cell37.translation = (16.5354, -12.27435, 0.0)
cell37.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf131

# frod
cell38 = openmc.Cell(cell_id=38, fill=universe1)
cell38.translation = (15.3543, -14.320075, 0.0)
cell38.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf133

# frod
cell39 = openmc.Cell(cell_id=39, fill=universe1)
cell39.translation = (11.811, -16.3658, 0.0)
cell39.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf135

# frod
cell40 = openmc.Cell(cell_id=40, fill=universe1)
cell40.translation = (-8.2677, -18.41152, 0.0)
cell40.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf136

# frod
cell41 = openmc.Cell(cell_id=41, fill=universe1)
cell41.translation = (8.2677, -18.41152, 0.0)
cell41.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf137

# frod
cell42 = openmc.Cell(cell_id=42, fill=universe1)
cell42.translation = (-2.3622, -20.45725, 0.0)
cell42.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf139

# frod
cell43 = openmc.Cell(cell_id=43, fill=universe1)
cell43.translation = (0.0, -20.45725, 0.0)
cell43.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf140

# frod
cell44 = openmc.Cell(cell_id=44, fill=universe1)
cell44.translation = (2.3622, -20.45725, 0.0)
cell44.region = -surf14 & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7 | +surf20_8 | +surf20_9 | +surf20_10 | +surf20_11) & -surf22 & -surf141

# else
cell45 = openmc.Cell(cell_id=45, fill=universe2)
cell45.region = -surf14 & +surf22

# ZR2
cell49 = openmc.Cell(cell_id=49, fill=mat2)
cell49.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# Al6061
cell55 = openmc.Cell(cell_id=55, fill=mat3)
cell55.region = -surf14 & -surf15

# else
cell56 = openmc.Cell(cell_id=56, fill=universe2)
cell56.region = (+surf3 | -surf3_zmin | +surf3_zmax) & +surf4 & +surf5 & +surf6 & +surf7 & -surf14

# else
cell62 = openmc.Cell(cell_id=62, fill=universe2)
cell62.region = (+surf3 | -surf3_zmin | +surf3_zmax) & +surf4 & +surf5 & +surf6 & +surf7 & -surf14

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell49, cell55, cell56, cell62])
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
