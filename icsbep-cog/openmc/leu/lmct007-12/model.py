"""
LMCT007-12: STACY run 624 with U(5)O2 rods immersed in 94.77cm of U(6) uranyl nitrate, unreflected
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Uranyl
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.291700e-07)
mat1.add_nuclide("U235", 1.543400e-05)
mat1.add_nuclide("U236", 2.561400e-08)
mat1.add_nuclide("U238", 2.386000e-04)
mat1.add_nuclide("O16", 3.559300e-02)
mat1.add_nuclide("H1", 6.245300e-02)
mat1.add_element("N", 1.441800e-03)
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

# Water
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.665800e-02)
mat6.add_nuclide("O16", 3.332900e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

# Air
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("N", 3.901400e-05)
mat7.add_nuclide("O16", 1.041000e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Zircaloy upper  grid plate
surf1 = openmc.ZCylinder(surface_id=1, r=30.0)
# Zircaloy middle grid plate
surf2 = openmc.ZCylinder(surface_id=2, r=30.0)
# Zircaloy lower  grid plate
surf3 = openmc.ZCylinder(surface_id=3, r=30.0)
# SS304L tank, inner
surf4 = openmc.ZCylinder(surface_id=4, r=29.505)
# SS304L tank, upper
surf5 = openmc.ZCylinder(surface_id=5, r=24.0)
# SS304L tank, outer
surf6 = openmc.ZCylinder(surface_id=6, r=29.825)
# Air reflector
surf7 = openmc.ZCylinder(surface_id=7, r=59.825, boundary_type="vacuum")
# Solution height
surf10 = openmc.ZPlane(surface_id=10, z0=94.77)
# UO2
surf11 = openmc.ZCylinder(surface_id=11, r=0.41015)
# Air
surf12 = openmc.ZCylinder(surface_id=12, r=0.4175)
# Zr-4 clad
surf13 = openmc.ZCylinder(surface_id=13, r=0.4746)
# Zr-4 ends
surf14 = openmc.ZCylinder(surface_id=14, r=0.2)
# Hole
surf15 = openmc.ZCylinder(surface_id=15, r=0.49555)
# Lattice plane boundary
surf20 = openmc.model.RectangularParallelepiped(-23.7405, 23.7405, -23.7405, 23.7405, -499.95, 499.95)
# Safety blade slit
surf21 = openmc.model.RectangularParallelepiped(-20.995, 20.995, -10.140829, -9.296828999999999, 4.0, 147.0)
# Safety blade slit
surf22 = openmc.model.RectangularParallelepiped(-20.995, 20.995, 9.296828999999999, 10.140829, 4.0, 147.0)
# Pin
surf31 = openmc.ZCylinder(surface_id=31, r=0.585)
# Hole
surf32 = openmc.ZCylinder(surface_id=32, r=0.591)
surf41 = openmc.ZCylinder(surface_id=41, x0=-15.903539, y0=-10.602359, r=0.591)
surf42 = openmc.ZCylinder(surface_id=42, x0=15.903539, y0=-10.602359, r=0.591)
surf43 = openmc.ZCylinder(surface_id=43, x0=-17.670598, y0=-8.835299, r=0.591)
surf44 = openmc.ZCylinder(surface_id=44, x0=17.670598, y0=-8.835299, r=0.591)
surf45 = openmc.ZCylinder(surface_id=45, x0=-17.670598, y0=8.835299, r=0.591)
surf46 = openmc.ZCylinder(surface_id=46, x0=17.670598, y0=8.835299, r=0.591)
surf47 = openmc.ZCylinder(surface_id=47, x0=-15.903539, y0=10.602359, r=0.591)
surf48 = openmc.ZCylinder(surface_id=48, x0=15.903539, y0=10.602359, r=0.591)
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
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = (-surf3 & +surf3_zmin & -surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell3 = openmc.Cell(fill=mat1)
u1_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf10
u1_cell4 = openmc.Cell(fill=mat7)
u1_cell4.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & +surf10
u1_cell5 = openmc.Cell(fill=mat7)
u1_cell5.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)
u1_cell7 = openmc.Cell(fill=mat7)
u1_cell7.region = (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7])

u2_cell0 = openmc.Cell(fill=mat2)
u2_cell0.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u2_cell1 = openmc.Cell(fill=mat7)
u2_cell1.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u2_cell3 = openmc.Cell(fill=mat3)
u2_cell3.region = (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell4 = openmc.Cell(fill=mat7)
u2_cell4.region = +surf10 & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell5 = openmc.Cell(fill=mat1)
u2_cell5.region = -surf10 & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5])

u3_cell0 = openmc.Cell(fill=mat7)
u3_cell0.region = +surf10 & (-surf15 & +surf15_zmin & -surf15_zmax)
u3_cell1 = openmc.Cell(fill=mat1)
u3_cell1.region = -surf10 & (-surf15 & +surf15_zmin & -surf15_zmax)
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1])

# Lattice 4: 19x19 array
lattice4 = openmc.RectLattice(lattice_id=4)
lattice4.lower_left = [-23.7405, -23.7405]
lattice4.pitch = [2.499000, 2.499000]
lattice4.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe1, universe1, universe1],
    [universe1, universe1, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe1, universe1],
    [universe1, universe1, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe1, universe1],
    [universe1, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe1],
    [universe1, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe1],
    [universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3],
    [universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3],
    [universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3],
    [universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3],
    [universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3],
    [universe1, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe1],
    [universe1, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe1],
    [universe1, universe1, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe1, universe1],
    [universe1, universe1, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe1, universe1],
    [universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe4 = openmc.Universe(universe_id=4)
universe4.add_cell(openmc.Cell(fill=lattice4))

u5_cell0 = openmc.Cell(fill=mat2)
u5_cell0.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u5_cell1 = openmc.Cell(fill=mat7)
u5_cell1.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u5_cell2 = openmc.Cell(fill=mat3)
u5_cell2.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u5_cell3 = openmc.Cell(fill=mat3)
u5_cell3.region = (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u5_cell4 = openmc.Cell(fill=mat7)
u5_cell4.region = +surf10 & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & -surf20
u5_cell5 = openmc.Cell(fill=mat1)
u5_cell5.region = -surf10 & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & -surf20
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0, u5_cell1, u5_cell2, u5_cell3, u5_cell4, u5_cell5])

u6_cell0 = openmc.Cell(fill=mat7)
u6_cell0.region = +surf10 & -surf20
u6_cell1 = openmc.Cell(fill=mat1)
u6_cell1.region = -surf10 & -surf20
universe6 = openmc.Universe(universe_id=6, cells=[u6_cell0, u6_cell1])

# Lattice 7: 19x19 array
lattice7 = openmc.RectLattice(lattice_id=7)
lattice7.lower_left = [-23.7405, -23.7405]
lattice7.pitch = [2.499000, 2.499000]
lattice7.universes = [
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe6, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe6, universe6, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe6, universe6, universe5, universe5, universe5],
    [universe5, universe5, universe6, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe6, universe5, universe5],
    [universe5, universe5, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe5, universe5],
    [universe5, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe5],
    [universe5, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe5],
    [universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6],
    [universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6],
    [universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6],
    [universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6],
    [universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6],
    [universe5, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe5],
    [universe5, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe5],
    [universe5, universe5, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe5, universe5],
    [universe5, universe5, universe6, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe6, universe5, universe5],
    [universe5, universe5, universe5, universe6, universe6, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe6, universe6, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe5, universe5, universe5, universe5, universe5],
    [universe5, universe5, universe5, universe5, universe5, universe5, universe5, universe6, universe6, universe6, universe6, universe6, universe5, universe5, universe5, universe5, universe5, universe5, universe5],
]
universe7 = openmc.Universe(universe_id=7)
universe7.add_cell(openmc.Cell(fill=lattice7))

u8_cell0 = openmc.Cell(fill=mat4)
u8_cell0.region = (-surf31 & +surf31_zmin & -surf31_zmax) & (-surf32 & +surf32_zmin & -surf32_zmax)
u8_cell1 = openmc.Cell(fill=mat7)
u8_cell1.region = +surf10 & (+surf31 | -surf31_zmin | +surf31_zmax) & (-surf32 & +surf32_zmin & -surf32_zmax)
u8_cell2 = openmc.Cell(fill=mat1)
u8_cell2.region = -surf10 & (+surf31 | -surf31_zmin | +surf31_zmax) & (-surf32 & +surf32_zmin & -surf32_zmax)
universe8 = openmc.Universe(universe_id=8, cells=[u8_cell0, u8_cell1, u8_cell2])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Pin
cell1 = openmc.Cell(cell_id=1, fill=universe8)
cell1.translation = (-15.903539, -10.602359, 0.0)
cell1.region = -surf41

# Pin
cell2 = openmc.Cell(cell_id=2, fill=universe8)
cell2.translation = (15.903539, -10.602359, 0.0)
cell2.region = -surf42

# Pin
cell3 = openmc.Cell(cell_id=3, fill=universe8)
cell3.translation = (-17.670598, -8.835299, 0.0)
cell3.region = -surf43

# Pin
cell4 = openmc.Cell(cell_id=4, fill=universe8)
cell4.translation = (17.670598, -8.835299, 0.0)
cell4.region = -surf44

# Pin
cell5 = openmc.Cell(cell_id=5, fill=universe8)
cell5.translation = (-17.670598, 8.835299, 0.0)
cell5.region = -surf45

# Pin
cell6 = openmc.Cell(cell_id=6, fill=universe8)
cell6.translation = (17.670598, 8.835299, 0.0)
cell6.region = -surf46

# Pin
cell7 = openmc.Cell(cell_id=7, fill=universe8)
cell7.translation = (-15.903539, 10.602359, 0.0)
cell7.region = -surf47

# Pin
cell8 = openmc.Cell(cell_id=8, fill=universe8)
cell8.translation = (15.903539, 10.602359, 0.0)
cell8.region = -surf48

# Slit
cell9 = openmc.Cell(cell_id=9, fill=universe7)
cell9.translation = (0.0, 0.0, 0.0)
cell9.region = -surf21 & +surf41 & +surf42 & +surf43 & +surf44

# Slit
cell10 = openmc.Cell(cell_id=10, fill=universe7)
cell10.translation = (0.0, 0.0, 0.0)
cell10.region = -surf22 & +surf45 & +surf46 & +surf47 & +surf48

# Core
cell11 = openmc.Cell(cell_id=11, fill=universe4)
cell11.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax) & -surf20 & +surf21 & +surf22 & +surf41 & +surf42 & +surf43 & +surf44 & +surf45 & +surf46 & +surf47 & +surf48 & +surf51 & +surf52 & +surf53 & +surf54

# Alles
cell12 = openmc.Cell(cell_id=12, fill=universe1)
cell12.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax) & +surf20 & +surf51 & +surf52 & +surf53 & +surf54

# Alles
cell13 = openmc.Cell(cell_id=13, fill=universe1)
cell13.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax) & +surf51 & +surf52 & +surf53 & +surf54

# Zr4
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = -surf51 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf52 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf53 & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf54

# Air
cell23 = openmc.Cell(cell_id=23, fill=mat7)
cell23.region = (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)

# Alles
cell30 = openmc.Cell(cell_id=30, fill=universe1)
cell30.region = (+surf15 | -surf15_zmin | +surf15_zmax) & -surf20

# Alles
cell33 = openmc.Cell(cell_id=33, fill=universe1)
cell33.region = (+surf15 | -surf15_zmin | +surf15_zmax) & -surf20

# Soln
cell40 = openmc.Cell(cell_id=40, fill=mat1)
cell40.region = -surf10 & (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & -surf20

# Soln
cell43 = openmc.Cell(cell_id=43, fill=mat1)
cell43.region = -surf10 & -surf20

# Soln
cell47 = openmc.Cell(cell_id=47, fill=mat1)
cell47.region = -surf10 & (+surf31 | -surf31_zmin | +surf31_zmax) & (-surf32 & +surf32_zmin & -surf32_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell23, cell30, cell33, cell40, cell43, cell47])
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
source.space = openmc.stats.Point((0.0, 0.0, 47.385))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
