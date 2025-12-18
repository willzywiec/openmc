"""
LCT034-17: Four 18x18 arrays of U(4.738)O2 rods, 1.60 cm pitch, 0.33cm steel and Cd, 0.0cm water gap, Hc=33.89cm
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
mat1.add_nuclide("B10", 5.753100e-08)
mat1.add_nuclide("B11", 2.315700e-07)

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
mat3.add_element("P", 6.143800e-05)
mat3.add_element("S", 4.450400e-05)
mat3.add_element("C", 1.188300e-04)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.670700e-02)
mat4.add_nuclide("O16", 3.335400e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Cadmium
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cd", 4.634000e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# UO2
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0, y0=90.0, r=0.395)
# Gap
surf2 = openmc.ZCylinder(surface_id=2, x0=0.0, y0=96.9, r=0.41)
# AGS
surf3 = openmc.ZCylinder(surface_id=3, x0=-1.27, y0=98.2, r=0.47)
# Hole
surf4 = openmc.ZCylinder(surface_id=4, x0=-1.27, y0=98.2, r=0.5)
# Critical water height
surf5 = openmc.ZPlane(surface_id=5, z0=33.89)
# Lower grid plate
surf6 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -0.30000000000000004, -0.1)
# Upper grid plate
surf7 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, 96.60000000000001, 96.8)
# Basket, inner
surf8 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -1.8000000000000043, 103.4)
# Basket, outer
surf9 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -2.200000000000003, 103.8)
# Basket
surf10 = openmc.model.RectangularParallelepiped(-29.130000000000003, -0.33000000000000007, 0.33000000000000007, 29.130000000000003, -2.200000000000003, 103.8)
# Basket
surf12 = openmc.model.RectangularParallelepiped(0.33000000000000007, 29.130000000000003, 0.33000000000000007, 29.130000000000003, -2.200000000000003, 103.8)
# Basket
surf14 = openmc.model.RectangularParallelepiped(-29.130000000000003, -0.33000000000000007, -29.130000000000003, -0.33000000000000007, -2.200000000000003, 103.8)
# Basket
surf16 = openmc.model.RectangularParallelepiped(0.33000000000000007, 29.130000000000003, -29.130000000000003, -0.33000000000000007, -2.200000000000003, 103.8)
# Pedestal support plate
surf18 = openmc.model.RectangularParallelepiped(-47.5, 47.5, -47.5, 47.5, -3.0, -2.2)
# Tank & BCD
surf19 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -22.200000000000003, 103.8, boundary_type="vacuum")
surf20_cyl = openmc.ZCylinder(surface_id=20, x0=tr, y0=-28.1975, r=0.7975)
surf20_zmin = openmc.ZPlane(z0=28.1975)
surf20_zmax = openmc.ZPlane(z0=0.0)
surf20 = (surf20_cyl, surf20_zmin, surf20_zmax)
# surf21: Error converting surface type "c": could not convert string to float: 'tr'
# surf22: Error converting surface type "c": could not convert string to float: 'tr'
# surf23: Error converting surface type "c": could not convert string to float: 'tr'
surf25_cyl = openmc.ZCylinder(surface_id=25, x0=tr, y0=28.1975, r=0.7975)
surf25_zmin = openmc.ZPlane(z0=28.1975)
surf25_zmax = openmc.ZPlane(z0=0.0)
surf25 = (surf25_cyl, surf25_zmin, surf25_zmax)
# surf26: Error converting surface type "c": could not convert string to float: 'tr'
# surf27: Error converting surface type "c": could not convert string to float: 'tr'
# surf28: Error converting surface type "c": could not convert string to float: 'tr'
# Steel,   28.8  x 0.2  x 106
surf101 = openmc.model.RectangularParallelepiped(-29.130000000000003, -0.33000000000000007, 0.13000000000000078, 29.33, -2.200000000000003, 103.8)
# Cadmium, 28.8  x 0.05 x 106
surf102 = openmc.model.RectangularParallelepiped(-29.130000000000003, -0.33000000000000007, 0.08000000000000007, 29.380000000000003, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.08 x 106
surf103 = openmc.model.RectangularParallelepiped(-29.130000000000003, -0.33000000000000007, 0.0, 29.46, -2.200000000000003, 103.8)
# Steel,    0.2  x 28.8 x 106
surf111 = openmc.model.RectangularParallelepiped(-29.33, -0.13000000000000078, 0.33000000000000007, 29.130000000000003, -2.200000000000003, 103.8)
# Cadmium,  0.05 x 28.8 x 106
surf112 = openmc.model.RectangularParallelepiped(-29.380000000000003, -0.08000000000000007, 0.33000000000000007, 29.130000000000003, -2.200000000000003, 103.8)
# Steel,    0.08 x 28.8 x 106
surf113 = openmc.model.RectangularParallelepiped(-29.46, 0.0, 0.33000000000000007, 29.130000000000003, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.2  x 106
surf121 = openmc.model.RectangularParallelepiped(0.33000000000000007, 29.130000000000003, 0.13000000000000078, 29.33, -2.200000000000003, 103.8)
# Cadmium, 28.8  x 0.05 x 106
surf122 = openmc.model.RectangularParallelepiped(0.33000000000000007, 29.130000000000003, 0.08000000000000007, 29.380000000000003, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.08 x 106
surf123 = openmc.model.RectangularParallelepiped(0.33000000000000007, 29.130000000000003, 0.0, 29.46, -2.200000000000003, 103.8)
# Steel,    0.2  x 28.8 x 106
surf131 = openmc.model.RectangularParallelepiped(0.13000000000000078, 29.33, 0.33000000000000007, 29.130000000000003, -2.200000000000003, 103.8)
# Cadmium,  0.05 x 28.8 x 106
surf132 = openmc.model.RectangularParallelepiped(0.08000000000000007, 29.380000000000003, 0.33000000000000007, 29.130000000000003, -2.200000000000003, 103.8)
# Steel,    0.08 x 28.8 x 106
surf133 = openmc.model.RectangularParallelepiped(0.0, 29.46, 0.33000000000000007, 29.130000000000003, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.2  x 106
surf141 = openmc.model.RectangularParallelepiped(-29.130000000000003, -0.33000000000000007, -29.33, -0.13000000000000078, -2.200000000000003, 103.8)
# Cadmium, 28.8  x 0.05 x 106
surf142 = openmc.model.RectangularParallelepiped(-29.130000000000003, -0.33000000000000007, -29.380000000000003, -0.08000000000000007, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.08 x 106
surf143 = openmc.model.RectangularParallelepiped(-29.130000000000003, -0.33000000000000007, -29.46, 0.0, -2.200000000000003, 103.8)
# Steel,    0.2  x 28.8 x 106
surf151 = openmc.model.RectangularParallelepiped(-29.33, -0.13000000000000078, -29.130000000000003, -0.33000000000000007, -2.200000000000003, 103.8)
# Cadmium,  0.05 x 28.8 x 106
surf152 = openmc.model.RectangularParallelepiped(-29.380000000000003, -0.08000000000000007, -29.130000000000003, -0.33000000000000007, -2.200000000000003, 103.8)
# Steel,    0.08 x 28.8 x 106
surf153 = openmc.model.RectangularParallelepiped(-29.46, 0.0, -29.130000000000003, -0.33000000000000007, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.2  x 106
surf161 = openmc.model.RectangularParallelepiped(0.33000000000000007, 29.130000000000003, -29.33, -0.13000000000000078, -2.200000000000003, 103.8)
# Cadmium, 28.8  x 0.05 x 106
surf162 = openmc.model.RectangularParallelepiped(0.33000000000000007, 29.130000000000003, -29.380000000000003, -0.08000000000000007, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.08 x 106
surf163 = openmc.model.RectangularParallelepiped(0.33000000000000007, 29.130000000000003, -29.46, 0.0, -2.200000000000003, 103.8)
# Steel,    0.2  x 28.8 x 106
surf171 = openmc.model.RectangularParallelepiped(0.13000000000000078, 29.33, -29.130000000000003, -0.33000000000000007, -2.200000000000003, 103.8)
# Cadmium,  0.05 x 28.8 x 106
surf172 = openmc.model.RectangularParallelepiped(0.08000000000000007, 29.380000000000003, -29.130000000000003, -0.33000000000000007, -2.200000000000003, 103.8)
# Steel,    0.08 x 28.8 x 106
surf173 = openmc.model.RectangularParallelepiped(0.0, 29.46, -29.130000000000003, -0.33000000000000007, -2.200000000000003, 103.8)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf2
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf1 & +surf2 & -surf3
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = +surf3 & -surf4 & -surf5
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = +surf4 & -surf6
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = +surf4 & -surf7
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = +surf8 & -surf9
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = +surf4 & -surf5 & +surf6 & +surf7 & -surf8 & -surf9
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

# Lattice 2: 18x18 array
lattice2 = openmc.RectLattice(lattice_id=2)
lattice2.lower_left = [-14.4, -14.4]
lattice2.pitch = [1.600000, 1.600000]
lattice2.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe2 = openmc.Universe(universe_id=2)
universe2.add_cell(openmc.Cell(fill=lattice2))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Assy
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.translation = (-14.73, 14.73, 0.0)
cell1.region = +surf18 & -surf10 & +surf21 & +surf22 & +surf23

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = +surf18 & -surf10 & +surf20 & -surf21 & -surf10 & -surf22 & -surf10 & -surf23

# Abstl
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf18 & +surf10 & -surf101 & -surf102 & -surf103

# Abcad
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = +surf18 & +surf10 & +surf101 & -surf102 & -surf103

# Abstl
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf18 & +surf10 & +surf101 & +surf102 & -surf103

# Abstl
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf18 & +surf10 & -surf111 & -surf112 & -surf113 & +surf103

# Abcad
cell7 = openmc.Cell(cell_id=7, fill=mat5)
cell7.region = +surf18 & +surf10 & +surf111 & -surf112 & -surf113 & +surf103

# Abstl
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = +surf18 & +surf10 & +surf111 & +surf112 & -surf113 & +surf103

# Assy
cell9 = openmc.Cell(cell_id=9, fill=universe2)
cell9.translation = (14.73, 14.73, 0.0)
cell9.region = +surf18 & -surf12 & +surf26 & +surf27 & +surf28

# SST
cell10 = openmc.Cell(cell_id=10, fill=mat3)
cell10.region = +surf18 & -surf12 & +surf25 & -surf26 & -surf12 & -surf27 & -surf12 & -surf28

# Abstl
cell11 = openmc.Cell(cell_id=11, fill=mat3)
cell11.region = +surf18 & +surf12 & -surf121 & -surf122 & -surf123 & +surf103 & +surf113

# Abcad
cell12 = openmc.Cell(cell_id=12, fill=mat5)
cell12.region = +surf18 & +surf12 & +surf121 & -surf122 & -surf123 & +surf103 & +surf113

# Abstl
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = +surf18 & +surf12 & +surf121 & +surf122 & -surf123 & +surf103 & +surf113

# Abstl
cell14 = openmc.Cell(cell_id=14, fill=mat3)
cell14.region = +surf18 & +surf12 & -surf131 & -surf132 & -surf133 & +surf123 & +surf103 & +surf113

# Abcad
cell15 = openmc.Cell(cell_id=15, fill=mat5)
cell15.region = +surf18 & +surf12 & +surf131 & -surf132 & -surf133 & +surf123 & +surf103 & +surf113

# Abstl
cell16 = openmc.Cell(cell_id=16, fill=mat3)
cell16.region = +surf18 & +surf12 & +surf131 & +surf132 & -surf133 & +surf123 & +surf103 & +surf113

# Assy
cell17 = openmc.Cell(cell_id=17, fill=universe2)
cell17.translation = (-14.73, -14.73, 0.0)
cell17.region = +surf18 & -surf14 & +surf31 & +surf32 & +surf33

# SST
cell18 = openmc.Cell(cell_id=18, fill=mat3)
cell18.region = +surf18 & -surf14 & +surf30 & -surf31 & -surf14 & -surf32 & -surf14 & -surf33

# Abstl
cell19 = openmc.Cell(cell_id=19, fill=mat3)
cell19.region = +surf18 & +surf14 & -surf141 & -surf142 & -surf143 & +surf103 & +surf113 & +surf123 & +surf133

# Abcad
cell20 = openmc.Cell(cell_id=20, fill=mat5)
cell20.region = +surf18 & +surf14 & +surf141 & -surf142 & -surf143 & +surf103 & +surf113 & +surf123 & +surf133

# Abstl
cell21 = openmc.Cell(cell_id=21, fill=mat3)
cell21.region = +surf18 & +surf14 & +surf141 & +surf142 & -surf143 & +surf103 & +surf113 & +surf123 & +surf133

# Abstl
cell22 = openmc.Cell(cell_id=22, fill=mat3)
cell22.region = +surf18 & +surf14 & -surf151 & -surf152 & -surf153 & +surf143 & +surf103 & +surf113 & +surf123 & +surf133

# Abcad
cell23 = openmc.Cell(cell_id=23, fill=mat5)
cell23.region = +surf18 & +surf14 & +surf151 & -surf152 & -surf153 & +surf143 & +surf103 & +surf113 & +surf123 & +surf133

# Abstl
cell24 = openmc.Cell(cell_id=24, fill=mat3)
cell24.region = +surf18 & +surf14 & +surf151 & +surf152 & -surf153 & +surf143 & +surf103 & +surf113 & +surf123 & +surf133

# Assy
cell25 = openmc.Cell(cell_id=25, fill=universe2)
cell25.translation = (14.73, -14.73, 0.0)
cell25.region = +surf18 & -surf16 & +surf36 & +surf37 & +surf38

# SST
cell26 = openmc.Cell(cell_id=26, fill=mat3)
cell26.region = +surf18 & -surf16 & +surf35 & -surf36 & -surf16 & -surf37 & -surf16 & -surf38

# Abstl
cell27 = openmc.Cell(cell_id=27, fill=mat3)
cell27.region = +surf18 & +surf16 & -surf161 & -surf162 & -surf163 & +surf103 & +surf113 & +surf123 & +surf133 & +surf143 & +surf153

# Abcad
cell28 = openmc.Cell(cell_id=28, fill=mat5)
cell28.region = +surf18 & +surf16 & +surf161 & -surf162 & -surf163 & +surf103 & +surf113 & +surf123 & +surf133 & +surf143 & +surf153

# Abstl
cell29 = openmc.Cell(cell_id=29, fill=mat3)
cell29.region = +surf18 & +surf16 & +surf161 & +surf162 & -surf163 & +surf103 & +surf113 & +surf123 & +surf133 & +surf143 & +surf153

# Abstl
cell30 = openmc.Cell(cell_id=30, fill=mat3)
cell30.region = +surf18 & +surf16 & -surf171 & -surf172 & -surf173 & +surf163 & +surf103 & +surf113 & +surf123 & +surf133 & +surf143 & +surf153

# Abcad
cell31 = openmc.Cell(cell_id=31, fill=mat5)
cell31.region = +surf18 & +surf16 & +surf171 & -surf172 & -surf173 & +surf163 & +surf103 & +surf113 & +surf123 & +surf133 & +surf143 & +surf153

# Abstl
cell32 = openmc.Cell(cell_id=32, fill=mat3)
cell32.region = +surf18 & +surf16 & +surf171 & +surf172 & -surf173 & +surf163 & +surf103 & +surf113 & +surf123 & +surf133 & +surf143 & +surf153

# SST
cell33 = openmc.Cell(cell_id=33, fill=mat3)
cell33.region = -surf18

# Water
cell34 = openmc.Cell(cell_id=34, fill=mat4)
cell34.region = -surf19 & -surf5 & +surf10 & +surf103 & +surf113 & +surf12 & +surf123 & +surf133 & +surf14 & +surf143 & +surf153 & +surf16 & +surf163 & +surf173 & +surf18

# Water
cell42 = openmc.Cell(cell_id=42, fill=mat4)
cell42.region = +surf4 & -surf5 & +surf6 & +surf7 & -surf8 & -surf9

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell42])
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
source.space = openmc.stats.Box((-29.33, -29.33, 15.945), (29.33, 29.33, 17.945))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
