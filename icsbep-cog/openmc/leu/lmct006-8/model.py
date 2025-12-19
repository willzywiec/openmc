"""
LMCT006-8: STACY run 553 with U(5)O2 rods immersed in 60.54cm of U(6) uranyl nitrate and Gd solution, unreflected
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Uranyl nitrate
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.258500e-07)
mat1.add_nuclide("U235", 5.088400e-05)
mat1.add_nuclide("U236", 8.444600e-08)
mat1.add_nuclide("U238", 7.866100e-04)
mat1.add_nuclide("O16", 3.809300e-02)
mat1.add_nuclide("H1", 5.678100e-02)
mat1.add_element("N", 2.875100e-03)
mat1.add_element("Gd", 2.194400e-07)
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

# Zircaloy upper  grid plate
surf1 = openmc.ZCylinder(surface_id=1, x0=145.4, y0=146.0, r=30.0)
# Zircaloy middle grid plate
surf2 = openmc.ZCylinder(surface_id=2, x0=105.0, y0=105.6, r=30.0)
# Zircaloy lower  grid plate
surf3 = openmc.ZCylinder(surface_id=3, x0=5.0, y0=5.6, r=30.0)
# SS304L tank, inner
surf4 = openmc.ZCylinder(surface_id=4, x0=0.0, y0=150.25, r=29.505)
# SS304L tank, upper
surf5 = openmc.ZCylinder(surface_id=5, x0=150.25, y0=152.25, r=24.0)
# SS304L tank, outer
surf6 = openmc.ZCylinder(surface_id=6, x0=-2.01, y0=159.17, r=29.825)
# Air reflector
surf7 = openmc.ZCylinder(surface_id=7, x0=-32.01, y0=174.17, r=59.825, boundary_type="vacuum")
# Solution height
surf10 = openmc.ZPlane(surface_id=10, z0=60.54)
# UO2
surf11 = openmc.ZCylinder(surface_id=11, x0=1.48, y0=143.54, r=0.41015)
# Air
surf12 = openmc.ZCylinder(surface_id=12, x0=1.48, y0=148.05, r=0.4175)
# Zr-4 clad
surf13 = openmc.ZCylinder(surface_id=13, x0=0.55, y0=148.97, r=0.4746)
# Zr-4 ends
surf14 = openmc.ZCylinder(surface_id=14, x0=0.0, y0=149.52, r=0.2)
# Hole
surf15 = openmc.ZCylinder(surface_id=15, x0=0.0, y0=149.52, r=0.49555)
# Lattice x-y boundary
surf20 = openmc.model.RectangularParallelepiped(-23.25, 23.25, -23.25, 23.25, -499.95, 499.95)
# Safety blade slit
surf21 = openmc.model.RectangularParallelepiped(-20.995, 20.995, -10.048, -9.452, 4.0, 147.0)
# Safety blade slit
surf22 = openmc.model.RectangularParallelepiped(-20.995, 20.995, 9.452, 10.048, 4.0, 147.0)
# Pin
surf31 = openmc.ZCylinder(surface_id=31, x0=0.0, y0=149.52, r=0.585)
# Hole
surf32 = openmc.ZCylinder(surface_id=32, x0=0.0, y0=149.52, r=0.591)
surf41 = openmc.ZCylinder(surface_id=41, x0=-18.0, y0=10.5, r=0.585)
surf42 = openmc.ZCylinder(surface_id=42, x0=-18.0, y0=9.0, r=0.585)
surf43 = openmc.ZCylinder(surface_id=43, x0=-18.0, y0=-10.5, r=0.585)
surf44 = openmc.ZCylinder(surface_id=44, x0=-18.0, y0=-9.0, r=0.585)
surf45 = openmc.ZCylinder(surface_id=45, x0=18.0, y0=10.5, r=0.585)
surf46 = openmc.ZCylinder(surface_id=46, x0=18.0, y0=9.0, r=0.585)
surf47 = openmc.ZCylinder(surface_id=47, x0=18.0, y0=-10.5, r=0.585)
surf48 = openmc.ZCylinder(surface_id=48, x0=18.0, y0=-9.0, r=0.585)
surf51 = openmc.ZCylinder(surface_id=51, x0=-24.02087, y0=-9.94977, r=1.53)
surf52 = openmc.ZCylinder(surface_id=52, x0=24.02087, y0=-9.94977, r=1.53)
surf53 = openmc.ZCylinder(surface_id=53, x0=-24.02087, y0=9.94977, r=1.53)
surf54 = openmc.ZCylinder(surface_id=54, x0=24.02087, y0=9.94977, r=1.53)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat4)
u1_cell0.region = -surf1 & -surf4
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = -surf2 & -surf4
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = -surf3 & -surf4
u1_cell3 = openmc.Cell(fill=mat1)
u1_cell3.region = +surf1 & +surf2 & +surf3 & -surf4 & -surf10
u1_cell4 = openmc.Cell(fill=mat7)
u1_cell4.region = +surf1 & +surf2 & +surf3 & -surf4 & +surf10
u1_cell5 = openmc.Cell(fill=mat7)
u1_cell5.region = +surf4 & -surf5
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = +surf4 & +surf5 & -surf6
u1_cell7 = openmc.Cell(fill=mat7)
u1_cell7.region = +surf6 & -surf7
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7])

u2_cell0 = openmc.Cell(fill=mat2)
u2_cell0.region = -surf11 & -surf12 & -surf13
u2_cell1 = openmc.Cell(fill=mat7)
u2_cell1.region = +surf11 & -surf12 & -surf13
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf11 & +surf12 & -surf13
u2_cell3 = openmc.Cell(fill=mat3)
u2_cell3.region = +surf13 & -surf14 & -surf15
u2_cell4 = openmc.Cell(fill=mat7)
u2_cell4.region = +surf10 & +surf13 & +surf14 & -surf15
u2_cell5 = openmc.Cell(fill=mat1)
u2_cell5.region = -surf10 & +surf13 & +surf14 & -surf15
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5])

u3_cell0 = openmc.Cell(fill=mat7)
u3_cell0.region = +surf10 & -surf15
u3_cell1 = openmc.Cell(fill=mat1)
u3_cell1.region = -surf10 & -surf15
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1])

u4_cell0 = openmc.Cell(fill=mat4)
u4_cell0.region = -surf31 & -surf32
u4_cell1 = openmc.Cell(fill=mat7)
u4_cell1.region = +surf10 & +surf31 & -surf32
u4_cell2 = openmc.Cell(fill=mat1)
u4_cell2.region = -surf10 & +surf31 & -surf32
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2])

# Lattice 5: 31x31 array
lattice5 = openmc.RectLattice(lattice_id=5)
lattice5.lower_left = [-23.25, -23.25]
lattice5.pitch = [1.500000, 1.500000]
lattice5.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1],
    [universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1],
    [universe1, universe1, universe3, universe4, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe4, universe3, universe1, universe1],
    [universe1, universe3, universe3, universe4, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe4, universe3, universe3, universe1],
    [universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe3, universe1],
    [universe1, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe1],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3],
    [universe3, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe3],
    [universe1, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe1],
    [universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe3, universe1],
    [universe1, universe3, universe3, universe4, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe4, universe3, universe3, universe1],
    [universe1, universe1, universe3, universe4, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe4, universe3, universe1, universe1],
    [universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1],
    [universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe2, universe2, universe2, universe2, universe2, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe3, universe3, universe3, universe3, universe3, universe3, universe3, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe5 = openmc.Universe(universe_id=5)
universe5.add_cell(openmc.Cell(fill=lattice5))

u6_cell0 = openmc.Cell(fill=mat2)
u6_cell0.region = -surf11 & -surf12 & -surf13
u6_cell1 = openmc.Cell(fill=mat7)
u6_cell1.region = +surf11 & -surf12 & -surf13
u6_cell2 = openmc.Cell(fill=mat3)
u6_cell2.region = +surf11 & +surf12 & -surf13
u6_cell3 = openmc.Cell(fill=mat3)
u6_cell3.region = +surf13 & -surf14 & -surf15
u6_cell4 = openmc.Cell(fill=mat7)
u6_cell4.region = +surf10 & +surf13 & +surf14 & -surf20
u6_cell5 = openmc.Cell(fill=mat1)
u6_cell5.region = -surf10 & +surf13 & +surf14 & -surf20
universe6 = openmc.Universe(universe_id=6, cells=[u6_cell0, u6_cell1, u6_cell2, u6_cell3, u6_cell4, u6_cell5])

u7_cell0 = openmc.Cell(fill=mat7)
u7_cell0.region = +surf10 & -surf20
u7_cell1 = openmc.Cell(fill=mat1)
u7_cell1.region = -surf10 & -surf20
universe7 = openmc.Universe(universe_id=7, cells=[u7_cell0, u7_cell1])

u8_cell0 = openmc.Cell(fill=mat4)
u8_cell0.region = -surf31 & -surf32
u8_cell1 = openmc.Cell(fill=mat7)
u8_cell1.region = +surf10 & +surf31 & -surf20
u8_cell2 = openmc.Cell(fill=mat1)
u8_cell2.region = -surf10 & +surf31 & -surf20
universe8 = openmc.Universe(universe_id=8, cells=[u8_cell0, u8_cell1, u8_cell2])

# Lattice 9: 31x31 array
lattice9 = openmc.RectLattice(lattice_id=9)
lattice9.lower_left = [-23.25, -23.25]
lattice9.pitch = [1.500000, 1.500000]
lattice9.universes = [
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe8, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe8, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe8, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe8, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe8, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe8, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe8, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe8, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe6, universe6, universe6, universe6, universe6, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
    [universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7, universe7],
]
universe9 = openmc.Universe(universe_id=9)
universe9.add_cell(openmc.Cell(fill=lattice9))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Slit
cell1 = openmc.Cell(cell_id=1, fill=universe9)
cell1.region = -surf21

# Slit
cell2 = openmc.Cell(cell_id=2, fill=universe9)
cell2.region = -surf22

# Core
cell3 = openmc.Cell(cell_id=3, fill=universe5)
cell3.region = -surf4 & -surf7 & -surf20 & +surf21 & +surf22 & +surf51 & +surf52 & +surf53 & +surf54

# Alles
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.region = -surf4 & -surf7 & +surf20 & +surf51 & +surf52 & +surf53 & +surf54

# Alles
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.region = +surf4 & -surf7 & +surf51 & +surf52 & +surf53 & +surf54

# Zr4
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = -surf51 & +surf4 & -surf52 & -surf53 & -surf54

# Air
cell15 = openmc.Cell(cell_id=15, fill=mat7)
cell15.region = +surf6 & -surf7

# Alles
cell22 = openmc.Cell(cell_id=22, fill=universe1)
cell22.region = +surf15 & -surf20

# Alles
cell25 = openmc.Cell(cell_id=25, fill=universe1)
cell25.region = +surf15 & -surf20

# Alles
cell29 = openmc.Cell(cell_id=29, fill=universe1)
cell29.region = +surf32 & -surf20

# Soln
cell36 = openmc.Cell(cell_id=36, fill=mat1)
cell36.region = -surf10 & +surf13 & +surf14 & -surf20

# Soln
cell39 = openmc.Cell(cell_id=39, fill=mat1)
cell39.region = -surf10 & -surf20

# Soln
cell43 = openmc.Cell(cell_id=43, fill=mat1)
cell43.region = -surf10 & +surf31 & -surf20

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell15, cell22, cell25, cell29, cell36, cell39, cell43])
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
source.space = openmc.stats.Point((0.0, 0.0, 30.27))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
