"""
LCT052-4: Pseudocylindrical array of 1285 U(4.738)O2 fuel rods with 1.35 cm triangular pitch in gadolinium nitrate solution
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(4.738)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 7.131800e-06)
mat1.add_nuclide("U235", 1.110400e-03)
mat1.add_nuclide("U236", 3.183800e-05)
mat1.add_nuclide("U238", 2.200600e-02)
mat1.add_nuclide("O16", 4.639100e-02)

# AGS clad, plugs
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.956900e-02)
mat2.add_element("Mg", 3.144200e-04)
mat2.add_element("Si", 2.489400e-04)
mat2.add_element("Fe", 6.405200e-05)
mat2.add_element("Zn", 7.459700e-06)

# Stainless steel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.869400e-02)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Mn", 1.731900e-03)
mat3.add_element("Si", 1.693900e-03)
mat3.add_element("C", 1.188300e-04)
mat3.add_element("P", 6.143800e-05)
mat3.add_element("S", 4.450400e-05)

# Gadolinium nitrate solution
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Gd", 2.297780e-06)
mat4.add_element("N", 1.171100e-05)
mat4.add_nuclide("H1", 6.666810e-02)
mat4.add_nuclide("O16", 3.336680e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Entire problem (BCD)
surf1 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -20.0, 100.0, boundary_type="vacuum")
# Support plate
surf2 = openmc.model.RectangularParallelepiped(-47.5, 47.5, -47.5, 47.5, -2.6, -1.8000000000000003)
# Lower grid plate
surf3 = openmc.model.RectangularParallelepiped(-30.0, 30.0, -30.0, 30.0, -0.3, -0.04999999999999999)
# Upper grid plate
surf4 = openmc.model.RectangularParallelepiped(-30.0, 30.0, -30.0, 30.0, 96.45, 96.7)
# Solution critica height
surf5 = openmc.ZPlane(surface_id=5, z0=88.1)
# UO2
surf11 = openmc.ZCylinder(surface_id=11, r=0.395)
# Gap
surf12 = openmc.ZCylinder(surface_id=12, r=0.41)
# AGS
surf13 = openmc.Revolution(surface_id=13, rz=[(-1.8, 0.0), (-1.0, 0.47), (98.2, 0.47)], axis="x")
# Hole
surf20 = openmc.ZCylinder(surface_id=20, r=0.5)
# Hole
surf21 = openmc.ZCylinder(surface_id=21, x0=-0.675, y0=1.169134, r=0.5)
# Hole
surf22 = openmc.ZCylinder(surface_id=22, x0=0.675, y0=1.169134, r=0.5)
# Hole
surf23 = openmc.ZCylinder(surface_id=23, x0=-1.35, y0=0.0, r=0.5)
# Hole
surf24 = openmc.ZCylinder(surface_id=24, x0=1.35, y0=0.0, r=0.5)
# Hole
surf25 = openmc.ZCylinder(surface_id=25, x0=-0.675, y0=-1.169134, r=0.5)
# Hole
surf26 = openmc.ZCylinder(surface_id=26, x0=0.675, y0=-1.169134, r=0.5)
surf31 = openmc.ZCylinder(surface_id=31, x0=-8.775, y0=24.551821, r=0.51)
surf32 = openmc.ZCylinder(surface_id=32, x0=-7.425, y0=24.551821, r=0.51)
surf33 = openmc.ZCylinder(surface_id=33, x0=7.425, y0=24.551821, r=0.51)
surf34 = openmc.ZCylinder(surface_id=34, x0=8.775, y0=24.551821, r=0.51)
surf35 = openmc.ZCylinder(surface_id=35, x0=-10.8, y0=23.382686, r=0.51)
surf36 = openmc.ZCylinder(surface_id=36, x0=10.8, y0=23.382686, r=0.51)
surf37 = openmc.ZCylinder(surface_id=37, x0=-12.825, y0=22.213551, r=0.51)
surf38 = openmc.ZCylinder(surface_id=38, x0=12.825, y0=22.213551, r=0.51)
surf39 = openmc.ZCylinder(surface_id=39, x0=-14.85, y0=21.044418, r=0.51)
surf40 = openmc.ZCylinder(surface_id=40, x0=14.85, y0=21.044418, r=0.51)
surf41 = openmc.ZCylinder(surface_id=41, x0=-16.875, y0=19.875283, r=0.51)
surf42 = openmc.ZCylinder(surface_id=42, x0=16.875, y0=19.875283, r=0.51)
surf43 = openmc.ZCylinder(surface_id=43, x0=-17.55, y0=18.706149, r=0.51)
surf44 = openmc.ZCylinder(surface_id=44, x0=17.55, y0=18.706149, r=0.51)
surf45 = openmc.ZCylinder(surface_id=45, x0=-24.975, y0=5.845671, r=0.51)
surf46 = openmc.ZCylinder(surface_id=46, x0=24.975, y0=5.845671, r=0.51)
surf47 = openmc.ZCylinder(surface_id=47, x0=-25.65, y0=4.676537, r=0.51)
surf48 = openmc.ZCylinder(surface_id=48, x0=25.65, y0=4.676537, r=0.51)
surf49 = openmc.ZCylinder(surface_id=49, x0=-25.65, y0=2.338268, r=0.51)
surf50 = openmc.ZCylinder(surface_id=50, x0=25.65, y0=2.338268, r=0.51)
surf51 = openmc.ZCylinder(surface_id=51, x0=-25.65, y0=0.0, r=0.51)
surf52 = openmc.ZCylinder(surface_id=52, x0=25.65, y0=0.0, r=0.51)
surf53 = openmc.ZCylinder(surface_id=53, x0=-25.65, y0=-2.338268, r=0.51)
surf54 = openmc.ZCylinder(surface_id=54, x0=25.65, y0=-2.338268, r=0.51)
surf55 = openmc.ZCylinder(surface_id=55, x0=-25.65, y0=-4.676537, r=0.51)
surf56 = openmc.ZCylinder(surface_id=56, x0=25.65, y0=-4.676537, r=0.51)
surf57 = openmc.ZCylinder(surface_id=57, x0=-24.975, y0=-5.845671, r=0.51)
surf58 = openmc.ZCylinder(surface_id=58, x0=24.975, y0=-5.845671, r=0.51)
surf59 = openmc.ZCylinder(surface_id=59, x0=-17.55, y0=-18.706149, r=0.51)
surf60 = openmc.ZCylinder(surface_id=60, x0=17.55, y0=-18.706149, r=0.51)
surf61 = openmc.ZCylinder(surface_id=61, x0=-16.875, y0=-19.875283, r=0.51)
surf62 = openmc.ZCylinder(surface_id=62, x0=16.875, y0=-19.875283, r=0.51)
surf63 = openmc.ZCylinder(surface_id=63, x0=-14.85, y0=-21.044418, r=0.51)
surf64 = openmc.ZCylinder(surface_id=64, x0=14.85, y0=-21.044418, r=0.51)
surf65 = openmc.ZCylinder(surface_id=65, x0=-12.825, y0=-22.213551, r=0.51)
surf66 = openmc.ZCylinder(surface_id=66, x0=12.825, y0=-22.213551, r=0.51)
surf67 = openmc.ZCylinder(surface_id=67, x0=-10.8, y0=-23.382686, r=0.51)
surf68 = openmc.ZCylinder(surface_id=68, x0=10.8, y0=-23.382686, r=0.51)
surf69 = openmc.ZCylinder(surface_id=69, x0=-8.775, y0=-24.551821, r=0.51)
surf70 = openmc.ZCylinder(surface_id=70, x0=-7.425, y0=-24.551821, r=0.51)
surf71 = openmc.ZCylinder(surface_id=71, x0=7.425, y0=-24.551821, r=0.51)
surf72 = openmc.ZCylinder(surface_id=72, x0=8.775, y0=-24.551821, r=0.51)
# Lattice
# Prism 99: 12-sided polygon
surf99_0 = openmc.Plane(a=0.5115854008, b=-0.8592324352, c=0, d=25.3965317853)
surf99_1 = openmc.Plane(a=0.8660241033, b=-0.5000022524, c=0, d=25.1363814176)
surf99_2 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=25.6500000000)
surf99_3 = openmc.Plane(a=0.8660241033, b=0.5000022524, c=0, d=25.1363814176)
surf99_4 = openmc.Plane(a=0.5115854008, b=0.8592324352, c=0, d=25.3965317853)
surf99_5 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=25.1364000000)
surf99_6 = openmc.Plane(a=-0.5115854008, b=0.8592324352, c=0, d=25.3965317853)
surf99_7 = openmc.Plane(a=-0.8660241033, b=0.5000022524, c=0, d=25.1363814176)
surf99_8 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=25.6500000000)
surf99_9 = openmc.Plane(a=-0.8660241033, b=-0.5000022524, c=0, d=25.1363814176)
surf99_10 = openmc.Plane(a=-0.5115854008, b=-0.8592324352, c=0, d=25.3965317853)
surf99_11 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=25.1364000000)

# Z-plane surfaces for bounded cylinders
surf11_zmin = openmc.ZPlane(surface_id=1099, z0=0.0)
surf11_zmax = openmc.ZPlane(surface_id=1100, z0=90.0)
surf12_zmin = openmc.ZPlane(surface_id=1101, z0=0.0)
surf12_zmax = openmc.ZPlane(surface_id=1102, z0=96.9)
surf20_zmin = openmc.ZPlane(surface_id=1103, z0=-1.8)
surf20_zmax = openmc.ZPlane(surface_id=1104, z0=98.2)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

universe2 = openmc.Universe(universe_id=2, cells=[])

# Lattice 3: 21x23 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-28.35, -26.8900889]
lattice3.pitch = [2.700000, 2.338269]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

u4_cell0 = openmc.Cell(fill=mat4)
u4_cell0.region = -surf1 & +surf2 & +surf3 & +surf4 & -surf5
u4_cell1 = openmc.Cell(fill=mat3)
u4_cell1.region = -surf2
u4_cell2 = openmc.Cell(fill=mat3)
u4_cell2.region = -surf3
u4_cell3 = openmc.Cell(fill=mat3)
u4_cell3.region = -surf4
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & +surf31 & +surf32 & +surf33 & +surf34 & +surf35 & +surf36 & +surf37 & +surf38 & +surf39 & +surf40 & +surf41 & +surf42 & +surf43 & +surf44 & +surf45 & +surf46 & +surf47 & +surf48 & +surf49 & +surf50

# Refl
cell2 = openmc.Cell(cell_id=2, fill=universe4)
cell2.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf31 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf52

# Refl
cell3 = openmc.Cell(cell_id=3, fill=universe4)
cell3.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf32 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf53

# Refl
cell4 = openmc.Cell(cell_id=4, fill=universe4)
cell4.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf33 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf54

# Refl
cell5 = openmc.Cell(cell_id=5, fill=universe4)
cell5.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf34 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf55

# Refl
cell6 = openmc.Cell(cell_id=6, fill=universe4)
cell6.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf35 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf56

# Refl
cell7 = openmc.Cell(cell_id=7, fill=universe4)
cell7.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf36 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf57

# Refl
cell8 = openmc.Cell(cell_id=8, fill=universe4)
cell8.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf37 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf58

# Refl
cell9 = openmc.Cell(cell_id=9, fill=universe4)
cell9.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf38 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf59

# Refl
cell10 = openmc.Cell(cell_id=10, fill=universe4)
cell10.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf39 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf60

# Refl
cell11 = openmc.Cell(cell_id=11, fill=universe4)
cell11.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf40 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf61

# Refl
cell12 = openmc.Cell(cell_id=12, fill=universe4)
cell12.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf41 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf62

# Refl
cell13 = openmc.Cell(cell_id=13, fill=universe4)
cell13.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf42 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf63

# Refl
cell14 = openmc.Cell(cell_id=14, fill=universe4)
cell14.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf43 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf64

# Refl
cell15 = openmc.Cell(cell_id=15, fill=universe4)
cell15.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf44 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf65

# Refl
cell16 = openmc.Cell(cell_id=16, fill=universe4)
cell16.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf45 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf66

# Refl
cell17 = openmc.Cell(cell_id=17, fill=universe4)
cell17.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf46 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf67

# Refl
cell18 = openmc.Cell(cell_id=18, fill=universe4)
cell18.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf47 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf68

# Refl
cell19 = openmc.Cell(cell_id=19, fill=universe4)
cell19.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf48 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf69

# Refl
cell20 = openmc.Cell(cell_id=20, fill=universe4)
cell20.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf49 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf70

# Refl
cell21 = openmc.Cell(cell_id=21, fill=universe4)
cell21.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf50 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf71

# Refl
cell22 = openmc.Cell(cell_id=22, fill=universe4)
cell22.region = -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf51 & +surf4 & -surf1 & (-surf99_0 & -surf99_1 & -surf99_2 & -surf99_3 & -surf99_4 & -surf99_5 & -surf99_6 & -surf99_7 & -surf99_8 & -surf99_9 & -surf99_10 & -surf99_11) & -surf72

# Refl
cell23 = openmc.Cell(cell_id=23, fill=universe4)
cell23.region = -surf1 & (+surf99_0 | +surf99_1 | +surf99_2 | +surf99_3 | +surf99_4 | +surf99_5 | +surf99_6 | +surf99_7 | +surf99_8 | +surf99_9 | +surf99_10 | +surf99_11)

# UO2
cell24 = openmc.Cell(cell_id=24, fill=mat1)
cell24.region = (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)

# Void
cell25 = openmc.Cell(cell_id=25)
cell25.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)

# AGS
cell26 = openmc.Cell(cell_id=26, fill=mat2)
cell26.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & -surf13 & (-surf20 & +surf20_zmin & -surf20_zmax)

# Soln
cell27 = openmc.Cell(cell_id=27, fill=mat4)
cell27.region = -surf5 & +surf13 & (-surf20 & +surf20_zmin & -surf20_zmax)

# Refl
cell28 = openmc.Cell(cell_id=28, fill=universe4)
cell28.region = -surf1 & (+surf20 | -surf20_zmin | +surf20_zmax) & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26

# Grid
cell33 = openmc.Cell(cell_id=33, fill=mat3)
cell33.region = -surf4

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell33])
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
source.space = openmc.stats.Point((0.0, 0.0, 44.05))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
