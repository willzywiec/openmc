"""
LMCT002-4: STACY run 385 with U(5)O2 rods immersed in 52.07cm of U(6) uranyl nitrate solution, unreflected
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Uranyl
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.987700e-07)
mat1.add_nuclide("U235", 2.383000e-05)
mat1.add_nuclide("U236", 3.941700e-08)
mat1.add_nuclide("U238", 3.670800e-04)
mat1.add_nuclide("O16", 3.692000e-02)
mat1.add_nuclide("H1", 5.972300e-02)
mat1.add_element("N", 2.354100e-03)
mat1.add_s_alpha_beta("c_H_in_H2O")

# UO2
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 1.165000e-05)
mat2.add_nuclide("U235", 1.155400e-03)
mat2.add_nuclide("U236", 9.240800e-06)
mat2.add_nuclide("U238", 2.174600e-02)
mat2.add_nuclide("O16", 4.591300e-02)

# Zr-4
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Sn", 4.352800e-04)
mat3.add_element("Fe", 1.483200e-04)
mat3.add_element("Cr", 8.344700e-05)
mat3.add_nuclide("O16", 3.180400e-04)
mat3.add_element("C", 4.269300e-05)
mat3.add_element("Si", 1.376400e-05)
mat3.add_element("Zr", 4.246900e-02)

# Zr-4
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Sn", 5.050600e-04)
mat4.add_element("Fe", 1.553900e-04)
mat4.add_element("Cr", 8.344700e-05)
mat4.add_nuclide("O16", 3.205000e-04)
mat4.add_element("Zr", 4.238300e-02)

# SS304L
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 9.939900e-05)
mat5.add_element("Si", 1.207300e-03)
mat5.add_element("Mn", 1.312600e-03)
mat5.add_element("P", 4.625400e-05)
mat5.add_element("S", 7.445500e-06)
mat5.add_element("Ni", 8.210100e-03)
mat5.add_element("Cr", 1.669700e-02)
mat5.add_element("Fe", 5.938700e-02)

# Air
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("N", 3.901400e-05)
mat6.add_nuclide("O16", 1.041000e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Zircaloy upper  grid plate
surf1 = openmc.ZCylinder(surface_id=1, r=29.5)
# Zircaloy middle grid plate
surf2 = openmc.ZCylinder(surface_id=2, r=29.5)
# Zircaloy lower  grid plate
surf3 = openmc.ZCylinder(surface_id=3, r=29.5)
# SS304L tank, inner
surf4 = openmc.ZCylinder(surface_id=4, r=29.505)
# SS304L tank, upper
surf5 = openmc.ZCylinder(surface_id=5, r=24.0)
# SS304L tank, outer
surf6 = openmc.ZCylinder(surface_id=6, r=29.825)
# Air reflector
surf7 = openmc.ZCylinder(surface_id=7, r=59.825, boundary_type="vacuum")
# Solution height
surf10 = openmc.ZPlane(surface_id=10, z0=52.07)
# UO2
surf11 = openmc.ZCylinder(surface_id=11, r=0.41015)
# Air
surf12 = openmc.ZCylinder(surface_id=12, r=0.4175)
# Zr-4 clad
surf13 = openmc.ZCylinder(surface_id=13, r=0.4746)
# Zr-4 ends
surf14 = openmc.ZCylinder(surface_id=14, r=0.2)
# Hole
surf15 = openmc.ZCylinder(surface_id=15, r=0.4956)
# Lattice
# Prism 20: 8-sided polygon
surf20_0 = openmc.Plane(a=0.7071067812, b=0.7071067812, c=0, d=25.9799870243)
surf20_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=22.0447500000)
surf20_2 = openmc.Plane(a=-0.7071067812, b=0.7071067812, c=0, d=25.9799870243)
surf20_3 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=22.0447500000)
surf20_4 = openmc.Plane(a=-0.7071067812, b=-0.7071067812, c=0, d=25.9799870243)
surf20_5 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=22.0447500000)
surf20_6 = openmc.Plane(a=0.7071067812, b=-0.7071067812, c=0, d=25.9799870243)
surf20_7 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=22.0447500000)
# Safety blade slit
surf21 = openmc.model.RectangularParallelepiped(-21.0, 21.0, -10.04675, -8.848749999999999, 4.0, 147.0)
# Safety blade slit
surf22 = openmc.model.RectangularParallelepiped(-21.0, 21.0, 8.848749999999999, 10.04675, 4.0, 147.0)
# Pin
surf31 = openmc.ZCylinder(surface_id=31, r=0.585)
# Hole
surf32 = openmc.ZCylinder(surface_id=32, r=0.591)
surf51 = openmc.ZCylinder(surface_id=51, x0=-24.02087, y0=-9.94977, r=1.53)
surf52 = openmc.ZCylinder(surface_id=52, x0=24.02087, y0=-9.94977, r=1.53)
surf53 = openmc.ZCylinder(surface_id=53, x0=-24.02087, y0=9.94977, r=1.53)
surf54 = openmc.ZCylinder(surface_id=54, x0=24.02087, y0=9.94977, r=1.53)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1054, z0=145.4)
surf1_zmax = openmc.ZPlane(surface_id=1055, z0=146.0)
surf2_zmin = openmc.ZPlane(surface_id=1056, z0=105.0)
surf2_zmax = openmc.ZPlane(surface_id=1057, z0=105.6)
surf3_zmin = openmc.ZPlane(surface_id=1058, z0=5.0)
surf3_zmax = openmc.ZPlane(surface_id=1059, z0=5.6)
surf4_zmin = openmc.ZPlane(surface_id=1060, z0=0.0)
surf4_zmax = openmc.ZPlane(surface_id=1061, z0=150.25)
surf5_zmin = openmc.ZPlane(surface_id=1062, z0=150.25)
surf5_zmax = openmc.ZPlane(surface_id=1063, z0=152.25)
surf6_zmin = openmc.ZPlane(surface_id=1064, z0=-2.01)
surf6_zmax = openmc.ZPlane(surface_id=1065, z0=159.17)
surf7_zmin = openmc.ZPlane(surface_id=1066, z0=-32.01, boundary_type="vacuum")
surf7_zmax = openmc.ZPlane(surface_id=1067, z0=174.17, boundary_type="vacuum")
surf11_zmin = openmc.ZPlane(surface_id=1068, z0=1.48)
surf11_zmax = openmc.ZPlane(surface_id=1069, z0=143.54)
surf12_zmin = openmc.ZPlane(surface_id=1070, z0=1.48)
surf12_zmax = openmc.ZPlane(surface_id=1071, z0=148.05)
surf13_zmin = openmc.ZPlane(surface_id=1072, z0=0.55)
surf13_zmax = openmc.ZPlane(surface_id=1073, z0=148.97)
surf14_zmin = openmc.ZPlane(surface_id=1074, z0=0.0)
surf14_zmax = openmc.ZPlane(surface_id=1075, z0=149.52)
surf15_zmin = openmc.ZPlane(surface_id=1076, z0=0.0)
surf15_zmax = openmc.ZPlane(surface_id=1077, z0=149.52)
surf31_zmin = openmc.ZPlane(surface_id=1078, z0=0.0)
surf31_zmax = openmc.ZPlane(surface_id=1079, z0=149.52)
surf32_zmin = openmc.ZPlane(surface_id=1080, z0=0.0)
surf32_zmax = openmc.ZPlane(surface_id=1081, z0=149.52)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat4)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax)
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = -surf51
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = -surf52
u1_cell5 = openmc.Cell(fill=mat4)
u1_cell5.region = -surf53
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = -surf54
u1_cell7 = openmc.Cell(fill=mat1)
u1_cell7.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf10 & +surf51 & +surf52 & +surf53 & +surf54
u1_cell8 = openmc.Cell(fill=mat6)
u1_cell8.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & +surf10 & +surf51 & +surf52 & +surf53 & +surf54
u1_cell9 = openmc.Cell(fill=mat6)
u1_cell9.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)
u1_cell10 = openmc.Cell(fill=mat5)
u1_cell10.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax) & +surf51 & +surf52 & +surf53 & +surf54
u1_cell11 = openmc.Cell(fill=mat6)
u1_cell11.region = (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11])

u2_cell0 = openmc.Cell(fill=mat2)
u2_cell0.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u2_cell1 = openmc.Cell(fill=mat6)
u2_cell1.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u2_cell3 = openmc.Cell(fill=mat3)
u2_cell3.region = (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell4 = openmc.Cell(fill=mat6)
u2_cell4.region = +surf10 & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell5 = openmc.Cell(fill=mat1)
u2_cell5.region = -surf10 & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5])

u3_cell0 = openmc.Cell(fill=mat6)
u3_cell0.region = +surf10 & (-surf15 & +surf15_zmin & -surf15_zmax)
u3_cell1 = openmc.Cell(fill=mat1)
u3_cell1.region = -surf10 & (-surf15 & +surf15_zmin & -surf15_zmax)
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1])

u4_cell0 = openmc.Cell(fill=mat4)
u4_cell0.region = (-surf31 & +surf31_zmin & -surf31_zmax) & (-surf32 & +surf32_zmin & -surf32_zmax)
u4_cell1 = openmc.Cell(fill=mat6)
u4_cell1.region = +surf10 & (+surf31 | -surf31_zmin | +surf31_zmax) & (-surf32 & +surf32_zmin & -surf32_zmax)
u4_cell2 = openmc.Cell(fill=mat1)
u4_cell2.region = -surf10 & (+surf31 | -surf31_zmin | +surf31_zmax) & (-surf32 & +surf32_zmin & -surf32_zmax)
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2])

# Lattice 5: 21x21 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-22.04475, -22.04475]
lattice5.pitch = [2.099500, 2.099500]
lattice5.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1],
    [universe1, universe1, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe1, universe1],
    [universe1, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe1],
    [universe1, universe3, universe4, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe4, universe3, universe1],
    [universe3, universe3, universe4, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe4, universe3, universe3],
    [universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3],
    [universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3],
    [universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3],
    [universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3],
    [universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3],
    [universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3],
    [universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3],
    [universe3, universe3, universe4, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe4, universe3, universe3],
    [universe1, universe3, universe4, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe4, universe3, universe1],
    [universe1, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe1],
    [universe1, universe1, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe1, universe1],
    [universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

u6_cell0 = openmc.Cell(fill=mat2)
u6_cell0.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u6_cell1 = openmc.Cell(fill=mat6)
u6_cell1.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u6_cell2 = openmc.Cell(fill=mat3)
u6_cell2.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u6_cell3 = openmc.Cell(fill=mat3)
u6_cell3.region = (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u6_cell4 = openmc.Cell(fill=mat6)
u6_cell4.region = +surf10 & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)
u6_cell5 = openmc.Cell(fill=mat1)
u6_cell5.region = -surf10 & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)
universe6 = openmc.Universe(universe_id=6, cells=[u6_cell0, u6_cell1, u6_cell2, u6_cell3, u6_cell4, u6_cell5])

u7_cell0 = openmc.Cell(fill=mat6)
u7_cell0.region = +surf10 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)
u7_cell1 = openmc.Cell(fill=mat1)
u7_cell1.region = -surf10 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)
universe7 = openmc.Universe(universe_id=7, cells=[u7_cell0, u7_cell1])

u8_cell0 = openmc.Cell(fill=mat4)
u8_cell0.region = (-surf31 & +surf31_zmin & -surf31_zmax) & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)
u8_cell1 = openmc.Cell(fill=mat6)
u8_cell1.region = +surf10 & (+surf31 | -surf31_zmin | +surf31_zmax) & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)
u8_cell2 = openmc.Cell(fill=mat1)
u8_cell2.region = -surf10 & (+surf31 | -surf31_zmin | +surf31_zmax) & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)
universe8 = openmc.Universe(universe_id=8, cells=[u8_cell0, u8_cell1, u8_cell2])

# Lattice 9: 21x21 array
lattice9 = openmc.RectLattice(lattice_id=9)
lattice9.lower_left = [-22.04475, -22.04475]
lattice9.pitch = [2.099500, 2.099500]
lattice9.universes = [
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe8, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe8, universe7, universe7],
    [universe7, universe7, universe8, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe8, universe7, universe7],
    [universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7],
    [universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7],
    [universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7],
    [universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7],
    [universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7],
    [universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7],
    [universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7],
    [universe7, universe7, universe8, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe8, universe7, universe7],
    [universe7, universe7, universe8, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe8, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
]
universe9 = openmc.Universe(universe_id=9)
universe9.add_cell(openmc.Cell(fill=lattice9))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Slit
cell1 = openmc.Cell(cell_id=1, fill=universe9)
cell1.region = -surf21 & -surf22

# Core
cell2 = openmc.Cell(cell_id=2, fill=universe5)
cell2.region = (-surf7 & +surf7_zmin & -surf7_zmax) & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7) & +surf21 & +surf22

# Alles
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.region = (-surf7 & +surf7_zmin & -surf7_zmax) & (+surf20_0 | +surf20_1 | +surf20_2 | +surf20_3 | +surf20_4 | +surf20_5 | +surf20_6 | +surf20_7)

# Air
cell16 = openmc.Cell(cell_id=16, fill=mat6)
cell16.region = (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)

# Alles
cell23 = openmc.Cell(cell_id=23, fill=universe1)
cell23.region = (+surf15 | -surf15_zmin | +surf15_zmax) & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)

# Alles
cell26 = openmc.Cell(cell_id=26, fill=universe1)
cell26.region = (+surf15 | -surf15_zmin | +surf15_zmax) & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)

# Alles
cell30 = openmc.Cell(cell_id=30, fill=universe1)
cell30.region = (+surf32 | -surf32_zmin | +surf32_zmax) & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)

# Soln
cell37 = openmc.Cell(cell_id=37, fill=mat1)
cell37.region = -surf10 & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)

# Soln
cell40 = openmc.Cell(cell_id=40, fill=mat1)
cell40.region = -surf10 & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)

# Soln
cell44 = openmc.Cell(cell_id=44, fill=mat1)
cell44.region = -surf10 & (+surf31 | -surf31_zmin | +surf31_zmax) & (-surf20_0 & -surf20_1 & -surf20_2 & -surf20_3 & -surf20_4 & -surf20_5 & -surf20_6 & -surf20_7)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell16, cell23, cell26, cell30, cell37, cell40, cell44])
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
source.space = openmc.stats.Point((0.0, 0.0, 26.035))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
