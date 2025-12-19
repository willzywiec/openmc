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
surf1 = openmc.ZCylinder(surface_id=1, r=0.208)
# void, lower
surf2 = openmc.ZCylinder(surface_id=2, r=0.1)
# void, gap
surf3 = openmc.ZCylinder(surface_id=3, r=0.215)
# void, upper
surf4 = openmc.ZCylinder(surface_id=4, r=0.1)
# SST,  lower
surf5 = openmc.ZCylinder(surface_id=5, r=0.2)
# SST,  main
surf6 = openmc.ZCylinder(surface_id=6, r=0.255)
# SST,  upper
surf7 = openmc.ZCylinder(surface_id=7, r=0.187)
# H2O,  hole
surf8 = openmc.ZCylinder(surface_id=8, r=0.26)
# Support plate
surf11 = openmc.ZCylinder(surface_id=11, r=99.9)
# Lower grid plate - w/o holes
surf12 = openmc.ZCylinder(surface_id=12, r=99.9)
# Upper grid plate - w/o holes
surf13 = openmc.ZCylinder(surface_id=13, r=99.9)
# Water and boundary condition
surf14 = openmc.ZCylinder(surface_id=14, r=47.0)
surf21 = openmc.ZCylinder(surface_id=21, x0=-0.4, y0=0.69282, r=0.26)
surf22 = openmc.ZCylinder(surface_id=22, x0=0.4, y0=0.69282, r=0.26)
surf23 = openmc.ZCylinder(surface_id=23, x0=-0.4, y0=-0.69282, r=0.26)
surf24 = openmc.ZCylinder(surface_id=24, x0=0.4, y0=-0.69282, r=0.26)
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
surf101 = openmc.ZCylinder(surface_id=101, x0=-4.4, y0=15.93486, r=0.26)
surf102 = openmc.ZCylinder(surface_id=102, x0=-3.6, y0=15.93486, r=0.26)
surf103 = openmc.ZCylinder(surface_id=103, x0=-2.8, y0=15.93486, r=0.26)
surf104 = openmc.ZCylinder(surface_id=104, x0=-2.0, y0=15.93486, r=0.26)
surf105 = openmc.ZCylinder(surface_id=105, x0=-1.2, y0=15.93486, r=0.26)
surf106 = openmc.ZCylinder(surface_id=106, x0=-0.4, y0=15.93486, r=0.26)
surf107 = openmc.ZCylinder(surface_id=107, x0=0.4, y0=15.93486, r=0.26)
surf108 = openmc.ZCylinder(surface_id=108, x0=1.2, y0=15.93486, r=0.26)
surf109 = openmc.ZCylinder(surface_id=109, x0=2.0, y0=15.93486, r=0.26)
surf110 = openmc.ZCylinder(surface_id=110, x0=2.8, y0=15.93486, r=0.26)
surf111 = openmc.ZCylinder(surface_id=111, x0=3.6, y0=15.93486, r=0.26)
surf112 = openmc.ZCylinder(surface_id=112, x0=4.4, y0=15.93486, r=0.26)
surf113 = openmc.ZCylinder(surface_id=113, x0=-5.6, y0=15.24204, r=0.26)
surf114 = openmc.ZCylinder(surface_id=114, x0=5.6, y0=15.24204, r=0.26)
surf115 = openmc.ZCylinder(surface_id=115, x0=-6.8, y0=14.54922, r=0.26)
surf116 = openmc.ZCylinder(surface_id=116, x0=6.8, y0=14.54922, r=0.26)
surf117 = openmc.ZCylinder(surface_id=117, x0=-9.2, y0=13.16358, r=0.26)
surf118 = openmc.ZCylinder(surface_id=118, x0=9.2, y0=13.16358, r=0.26)
surf119 = openmc.ZCylinder(surface_id=119, x0=-10.4, y0=12.47076, r=0.26)
surf120 = openmc.ZCylinder(surface_id=120, x0=10.4, y0=12.47076, r=0.26)
surf121 = openmc.ZCylinder(surface_id=121, x0=-11.6, y0=11.77794, r=0.26)
surf122 = openmc.ZCylinder(surface_id=122, x0=11.6, y0=11.77794, r=0.26)
surf123 = openmc.ZCylinder(surface_id=123, x0=-12.0, y0=11.08512, r=0.26)
surf124 = openmc.ZCylinder(surface_id=124, x0=12.0, y0=11.08512, r=0.26)
surf125 = openmc.ZCylinder(surface_id=125, x0=-12.4, y0=10.3923, r=0.26)
surf126 = openmc.ZCylinder(surface_id=126, x0=12.4, y0=10.3923, r=0.26)
surf127 = openmc.ZCylinder(surface_id=127, x0=-12.8, y0=9.69948, r=0.26)
surf128 = openmc.ZCylinder(surface_id=128, x0=12.8, y0=9.69948, r=0.26)
surf129 = openmc.ZCylinder(surface_id=129, x0=-13.2, y0=9.00666, r=0.26)
surf130 = openmc.ZCylinder(surface_id=130, x0=13.2, y0=9.00666, r=0.26)
surf131 = openmc.ZCylinder(surface_id=131, x0=-14.4, y0=6.9282, r=0.26)
surf132 = openmc.ZCylinder(surface_id=132, x0=14.4, y0=6.9282, r=0.26)
surf133 = openmc.ZCylinder(surface_id=133, x0=-14.8, y0=6.23538, r=0.26)
surf134 = openmc.ZCylinder(surface_id=134, x0=14.8, y0=6.23538, r=0.26)
surf135 = openmc.ZCylinder(surface_id=135, x0=-15.2, y0=5.54256, r=0.26)
surf136 = openmc.ZCylinder(surface_id=136, x0=15.2, y0=5.54256, r=0.26)
surf137 = openmc.ZCylinder(surface_id=137, x0=-15.6, y0=4.84974, r=0.26)
surf138 = openmc.ZCylinder(surface_id=138, x0=15.6, y0=4.84974, r=0.26)
surf139 = openmc.ZCylinder(surface_id=139, x0=-16.0, y0=4.15692, r=0.26)
surf140 = openmc.ZCylinder(surface_id=140, x0=16.0, y0=4.15692, r=0.26)
surf141 = openmc.ZCylinder(surface_id=141, x0=-16.0, y0=2.77128, r=0.26)
surf142 = openmc.ZCylinder(surface_id=142, x0=16.0, y0=2.77128, r=0.26)
surf143 = openmc.ZCylinder(surface_id=143, x0=-16.0, y0=1.38564, r=0.26)
surf144 = openmc.ZCylinder(surface_id=144, x0=16.0, y0=1.38564, r=0.26)
surf145 = openmc.ZCylinder(surface_id=145, x0=-16.0, y0=-1.38564, r=0.26)
surf146 = openmc.ZCylinder(surface_id=146, x0=16.0, y0=-1.38564, r=0.26)
surf147 = openmc.ZCylinder(surface_id=147, x0=-16.0, y0=-2.77128, r=0.26)
surf148 = openmc.ZCylinder(surface_id=148, x0=16.0, y0=-2.77128, r=0.26)
surf149 = openmc.ZCylinder(surface_id=149, x0=-16.0, y0=-4.15692, r=0.26)
surf150 = openmc.ZCylinder(surface_id=150, x0=16.0, y0=-4.15692, r=0.26)
surf151 = openmc.ZCylinder(surface_id=151, x0=-15.6, y0=-4.84974, r=0.26)
surf152 = openmc.ZCylinder(surface_id=152, x0=15.6, y0=-4.84974, r=0.26)
surf153 = openmc.ZCylinder(surface_id=153, x0=-15.2, y0=-5.54256, r=0.26)
surf154 = openmc.ZCylinder(surface_id=154, x0=15.2, y0=-5.54256, r=0.26)
surf155 = openmc.ZCylinder(surface_id=155, x0=-14.8, y0=-6.23538, r=0.26)
surf156 = openmc.ZCylinder(surface_id=156, x0=14.8, y0=-6.23538, r=0.26)
surf157 = openmc.ZCylinder(surface_id=157, x0=-14.4, y0=-6.9282, r=0.26)
surf158 = openmc.ZCylinder(surface_id=158, x0=14.4, y0=-6.9282, r=0.26)
surf159 = openmc.ZCylinder(surface_id=159, x0=-13.2, y0=-9.00666, r=0.26)
surf160 = openmc.ZCylinder(surface_id=160, x0=13.2, y0=-9.00666, r=0.26)
surf161 = openmc.ZCylinder(surface_id=161, x0=-12.8, y0=-9.69948, r=0.26)
surf162 = openmc.ZCylinder(surface_id=162, x0=12.8, y0=-9.69948, r=0.26)
surf163 = openmc.ZCylinder(surface_id=163, x0=-12.4, y0=-10.3923, r=0.26)
surf164 = openmc.ZCylinder(surface_id=164, x0=12.4, y0=-10.3923, r=0.26)
surf165 = openmc.ZCylinder(surface_id=165, x0=-12.0, y0=-11.08512, r=0.26)
surf166 = openmc.ZCylinder(surface_id=166, x0=12.0, y0=-11.08512, r=0.26)
surf167 = openmc.ZCylinder(surface_id=167, x0=-11.6, y0=-11.77794, r=0.26)
surf168 = openmc.ZCylinder(surface_id=168, x0=11.6, y0=-11.77794, r=0.26)
surf169 = openmc.ZCylinder(surface_id=169, x0=-10.4, y0=-12.47076, r=0.26)
surf170 = openmc.ZCylinder(surface_id=170, x0=10.4, y0=-12.47076, r=0.26)
surf171 = openmc.ZCylinder(surface_id=171, x0=-9.2, y0=-13.16358, r=0.26)
surf172 = openmc.ZCylinder(surface_id=172, x0=9.2, y0=-13.16358, r=0.26)
surf173 = openmc.ZCylinder(surface_id=173, x0=-6.8, y0=-14.54922, r=0.26)
surf174 = openmc.ZCylinder(surface_id=174, x0=6.8, y0=-14.54922, r=0.26)
surf175 = openmc.ZCylinder(surface_id=175, x0=-5.6, y0=-15.24204, r=0.26)
surf176 = openmc.ZCylinder(surface_id=176, x0=5.6, y0=-15.24204, r=0.26)
surf177 = openmc.ZCylinder(surface_id=177, x0=-4.4, y0=-15.93486, r=0.26)
surf178 = openmc.ZCylinder(surface_id=178, x0=-3.6, y0=-15.93486, r=0.26)
surf179 = openmc.ZCylinder(surface_id=179, x0=-2.8, y0=-15.93486, r=0.26)
surf180 = openmc.ZCylinder(surface_id=180, x0=-2.0, y0=-15.93486, r=0.26)
surf181 = openmc.ZCylinder(surface_id=181, x0=-1.2, y0=-15.93486, r=0.26)
surf182 = openmc.ZCylinder(surface_id=182, x0=1.2, y0=-15.93486, r=0.26)
surf183 = openmc.ZCylinder(surface_id=183, x0=2.0, y0=-15.93486, r=0.26)
surf184 = openmc.ZCylinder(surface_id=184, x0=2.8, y0=-15.93486, r=0.26)
surf185 = openmc.ZCylinder(surface_id=185, x0=3.6, y0=-15.93486, r=0.26)
surf186 = openmc.ZCylinder(surface_id=186, x0=4.4, y0=-15.93486, r=0.26)
surf201 = openmc.ZCylinder(surface_id=201, x0=-8.0, y0=13.8564, r=0.26)
surf202 = openmc.ZCylinder(surface_id=202, x0=8.0, y0=13.8564, r=0.26)
surf203 = openmc.ZCylinder(surface_id=203, x0=-13.6, y0=8.31384, r=0.26)
surf204 = openmc.ZCylinder(surface_id=204, x0=13.6, y0=8.31384, r=0.26)
surf205 = openmc.ZCylinder(surface_id=205, x0=-14.0, y0=7.62102, r=0.26)
surf206 = openmc.ZCylinder(surface_id=206, x0=14.0, y0=7.62102, r=0.26)
surf207 = openmc.ZCylinder(surface_id=207, x0=-16.0, y0=0.0, r=0.26)
surf208 = openmc.ZCylinder(surface_id=208, x0=16.0, y0=0.0, r=0.26)
surf209 = openmc.ZCylinder(surface_id=209, x0=-14.0, y0=-7.62102, r=0.26)
surf210 = openmc.ZCylinder(surface_id=210, x0=14.0, y0=-7.62102, r=0.26)
surf211 = openmc.ZCylinder(surface_id=211, x0=-13.6, y0=-8.31384, r=0.26)
surf212 = openmc.ZCylinder(surface_id=212, x0=13.6, y0=-8.31384, r=0.26)
surf213 = openmc.ZCylinder(surface_id=213, x0=-8.0, y0=-13.8564, r=0.26)
surf214 = openmc.ZCylinder(surface_id=214, x0=8.0, y0=-13.8564, r=0.26)
surf215 = openmc.ZCylinder(surface_id=215, x0=-0.4, y0=-15.93486, r=0.26)
surf216 = openmc.ZCylinder(surface_id=216, x0=0.4, y0=-15.93486, r=0.26)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=0.0)
surf1_zmax = openmc.ZPlane(z0=85.6)
surf2_zmin = openmc.ZPlane(z0=-0.8)
surf2_zmax = openmc.ZPlane(z0=0.0)
surf3_zmin = openmc.ZPlane(z0=0.0)
surf3_zmax = openmc.ZPlane(z0=85.9)
surf4_zmin = openmc.ZPlane(z0=85.9)
surf4_zmax = openmc.ZPlane(z0=86.7)
surf5_zmin = openmc.ZPlane(z0=-1.0)
surf5_zmax = openmc.ZPlane(z0=-0.1)
surf6_zmin = openmc.ZPlane(z0=-0.1)
surf6_zmax = openmc.ZPlane(z0=87.4)
surf7_zmin = openmc.ZPlane(z0=87.4)
surf7_zmax = openmc.ZPlane(z0=92.6)
surf8_zmin = openmc.ZPlane(z0=-1.0)
surf8_zmax = openmc.ZPlane(z0=999.9)
surf11_zmin = openmc.ZPlane(z0=-2.2)
surf11_zmax = openmc.ZPlane(z0=-1.0)
surf12_zmin = openmc.ZPlane(z0=0.5)
surf12_zmax = openmc.ZPlane(z0=0.8)
surf13_zmin = openmc.ZPlane(z0=81.9)
surf13_zmax = openmc.ZPlane(z0=82.2)
surf14_zmin = openmc.ZPlane(z0=-19.9, boundary_type="vacuum")
surf14_zmax = openmc.ZPlane(z0=105.6, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = (-surf13 & +surf13_zmin & -surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax)
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)
u2_cell2 = openmc.Cell(fill=mat2)
u2_cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)
u2_cell4 = openmc.Cell(fill=mat4)
u2_cell4.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

universe3 = openmc.Universe(universe_id=3, cells=[])

u4_cell0 = openmc.Cell(fill=mat4)
u4_cell0.region = (-surf8 & +surf8_zmin & -surf8_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf21 & (-surf14 & +surf14_zmin & -surf14_zmax)
u4_cell2 = openmc.Cell(fill=mat4)
u4_cell2.region = -surf22 & (-surf14 & +surf14_zmin & -surf14_zmax)
u4_cell3 = openmc.Cell(fill=mat4)
u4_cell3.region = -surf23 & (-surf14 & +surf14_zmin & -surf14_zmax)
u4_cell4 = openmc.Cell(fill=mat4)
u4_cell4.region = -surf24 & (-surf14 & +surf14_zmin & -surf14_zmax)
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
cell1.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5 & -surf31_6 & -surf31_7 & -surf31_8 & -surf31_9 & -surf31_10 & -surf31_11) & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110

# array2
cell2 = openmc.Cell(cell_id=2, fill=universe6)
cell2.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & +surf201 & +surf202 & +surf203 & +surf204 & +surf205 & +surf206 & +surf207 & +surf208 & +surf209 & +surf210

# FROD
cell3 = openmc.Cell(cell_id=3, fill=universe3)
cell3.translation = (-8.0, 13.8564, 0.0)
cell3.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf201

# FROD
cell4 = openmc.Cell(cell_id=4, fill=universe3)
cell4.translation = (8.0, 13.8564, 0.0)
cell4.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf202

# FROD
cell5 = openmc.Cell(cell_id=5, fill=universe3)
cell5.translation = (-13.6, 8.31384, 0.0)
cell5.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf203

# FROD
cell6 = openmc.Cell(cell_id=6, fill=universe3)
cell6.translation = (13.6, 8.31384, 0.0)
cell6.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf204

# FROD
cell7 = openmc.Cell(cell_id=7, fill=universe3)
cell7.translation = (-14.0, 7.62102, 0.0)
cell7.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf205

# FROD
cell8 = openmc.Cell(cell_id=8, fill=universe3)
cell8.translation = (14.0, 7.62102, 0.0)
cell8.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf206

# FROD
cell9 = openmc.Cell(cell_id=9, fill=universe3)
cell9.translation = (-16.0, 0.0, 0.0)
cell9.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf207

# FROD
cell10 = openmc.Cell(cell_id=10, fill=universe3)
cell10.translation = (16.0, 0.0, 0.0)
cell10.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf208

# FROD
cell11 = openmc.Cell(cell_id=11, fill=universe3)
cell11.translation = (-14.0, -7.62102, 0.0)
cell11.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf209

# FROD
cell12 = openmc.Cell(cell_id=12, fill=universe3)
cell12.translation = (14.0, -7.62102, 0.0)
cell12.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf210

# FROD
cell13 = openmc.Cell(cell_id=13, fill=universe3)
cell13.translation = (-13.6, -8.31384, 0.0)
cell13.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf211

# FROD
cell14 = openmc.Cell(cell_id=14, fill=universe3)
cell14.translation = (13.6, -8.31384, 0.0)
cell14.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf212

# FROD
cell15 = openmc.Cell(cell_id=15, fill=universe3)
cell15.translation = (-8.0, -13.8564, 0.0)
cell15.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf213

# FROD
cell16 = openmc.Cell(cell_id=16, fill=universe3)
cell16.translation = (8.0, -13.8564, 0.0)
cell16.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf214

# FROD
cell17 = openmc.Cell(cell_id=17, fill=universe3)
cell17.translation = (-0.4, -15.93486, 0.0)
cell17.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf215

# FROD
cell18 = openmc.Cell(cell_id=18, fill=universe3)
cell18.translation = (0.4, -15.93486, 0.0)
cell18.region = (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5 | +surf31_6 | +surf31_7 | +surf31_8 | +surf31_9 | +surf31_10 | +surf31_11) & (-surf32_0 & -surf32_1 & -surf32_2 & -surf32_3 & -surf32_4 & -surf32_5) & -surf216

# D16
cell19 = openmc.Cell(cell_id=19, fill=mat3)
cell19.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5)

# water
cell20 = openmc.Cell(cell_id=20, fill=mat4)
cell20.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5)

# H2O
cell25 = openmc.Cell(cell_id=25, fill=mat4)
cell25.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)

# Water
cell31 = openmc.Cell(cell_id=31, fill=mat4)
cell31.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

# ALLES
cell32 = openmc.Cell(cell_id=32, fill=universe1)
cell32.region = (+surf8 | -surf8_zmin | +surf8_zmax) & +surf21 & +surf22 & +surf23 & +surf24 & (-surf14 & +surf14_zmin & -surf14_zmax)

# ALLES
cell38 = openmc.Cell(cell_id=38, fill=universe1)
cell38.region = (+surf8 | -surf8_zmin | +surf8_zmax) & +surf21 & +surf22 & +surf23 & +surf24 & (-surf14 & +surf14_zmin & -surf14_zmax)

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
