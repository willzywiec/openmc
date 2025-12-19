"""
LCT034-22: Four 18x18 arrays of U(4.738)O2 rods, 1.60 cm pitch, 0.33cm steel and Cd, 2.5cm water gap, Hc=54.64cm
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

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# UO2
surf1 = openmc.ZCylinder(surface_id=1, r=0.395)
# Gap
surf2 = openmc.ZCylinder(surface_id=2, r=0.41)
# AGS
surf3 = openmc.ZCylinder(surface_id=3, r=0.47)
# Hole
surf4 = openmc.ZCylinder(surface_id=4, r=0.5)
# Critical water height
surf5 = openmc.ZPlane(surface_id=5, z0=54.64)
# Lower grid plate
surf6 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -0.30000000000000004, -0.1)
# Upper grid plate
surf7 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, 96.60000000000001, 96.8)
# Basket, inner
surf8 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -1.8000000000000043, 103.4)
# Basket, outer
surf9 = openmc.model.RectangularParallelepiped(-14.4, 14.4, -14.4, 14.4, -2.200000000000003, 103.8)
# Basket
surf10 = openmc.model.RectangularParallelepiped(-30.380000000000003, -1.58, 1.58, 30.380000000000003, -2.200000000000003, 103.8)
# Basket
surf12 = openmc.model.RectangularParallelepiped(1.58, 30.380000000000003, 1.58, 30.380000000000003, -2.200000000000003, 103.8)
# Basket
surf14 = openmc.model.RectangularParallelepiped(-30.380000000000003, -1.58, -30.380000000000003, -1.58, -2.200000000000003, 103.8)
# Basket
surf16 = openmc.model.RectangularParallelepiped(1.58, 30.380000000000003, -30.380000000000003, -1.58, -2.200000000000003, 103.8)
# Pedestal support plate
surf18 = openmc.model.RectangularParallelepiped(-47.5, 47.5, -47.5, 47.5, -3.0, -2.2)
# Tank & BCD
surf19 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -22.200000000000003, 103.8, boundary_type="vacuum")
surf20 = openmc.ZCylinder(surface_id=20, x0=-29.4475, y0=29.4475, r=0.7975)
surf21 = openmc.ZCylinder(surface_id=21, x0=-29.4475, y0=29.4475, r=0.9325)
surf22 = openmc.ZCylinder(surface_id=22, x0=-2.38, y0=29.58, r=0.5)
surf23 = openmc.ZCylinder(surface_id=23, x0=-29.58, y0=2.38, r=0.5)
surf25 = openmc.ZCylinder(surface_id=25, x0=29.4475, y0=29.4475, r=0.7975)
surf26 = openmc.ZCylinder(surface_id=26, x0=29.4475, y0=29.4475, r=0.9325)
surf27 = openmc.ZCylinder(surface_id=27, x0=2.38, y0=29.58, r=0.5)
surf28 = openmc.ZCylinder(surface_id=28, x0=29.58, y0=2.38, r=0.5)
# Steel,   28.8  x 0.2  x 106
surf101 = openmc.model.RectangularParallelepiped(-30.380000000000003, -1.58, 1.3800000000000008, 30.58, -2.200000000000003, 103.8)
# Cadmium, 28.8  x 0.05 x 106
surf102 = openmc.model.RectangularParallelepiped(-30.380000000000003, -1.58, 1.33, 30.630000000000003, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.08 x 106
surf103 = openmc.model.RectangularParallelepiped(-30.380000000000003, -1.58, 1.25, 30.71, -2.200000000000003, 103.8)
# Steel,    0.2  x 28.8 x 106
surf111 = openmc.model.RectangularParallelepiped(-30.58, -1.3800000000000008, 1.58, 30.380000000000003, -2.200000000000003, 103.8)
# Cadmium,  0.05 x 28.8 x 106
surf112 = openmc.model.RectangularParallelepiped(-30.630000000000003, -1.33, 1.58, 30.380000000000003, -2.200000000000003, 103.8)
# Steel,    0.08 x 28.8 x 106
surf113 = openmc.model.RectangularParallelepiped(-30.71, -1.25, 1.58, 30.380000000000003, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.2  x 106
surf121 = openmc.model.RectangularParallelepiped(1.58, 30.380000000000003, 1.3800000000000008, 30.58, -2.200000000000003, 103.8)
# Cadmium, 28.8  x 0.05 x 106
surf122 = openmc.model.RectangularParallelepiped(1.58, 30.380000000000003, 1.33, 30.630000000000003, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.08 x 106
surf123 = openmc.model.RectangularParallelepiped(1.58, 30.380000000000003, 1.25, 30.71, -2.200000000000003, 103.8)
# Steel,    0.2  x 28.8 x 106
surf131 = openmc.model.RectangularParallelepiped(1.3800000000000008, 30.58, 1.58, 30.380000000000003, -2.200000000000003, 103.8)
# Cadmium,  0.05 x 28.8 x 106
surf132 = openmc.model.RectangularParallelepiped(1.33, 30.630000000000003, 1.58, 30.380000000000003, -2.200000000000003, 103.8)
# Steel,    0.08 x 28.8 x 106
surf133 = openmc.model.RectangularParallelepiped(1.25, 30.71, 1.58, 30.380000000000003, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.2  x 106
surf141 = openmc.model.RectangularParallelepiped(-30.380000000000003, -1.58, -30.58, -1.3800000000000008, -2.200000000000003, 103.8)
# Cadmium, 28.8  x 0.05 x 106
surf142 = openmc.model.RectangularParallelepiped(-30.380000000000003, -1.58, -30.630000000000003, -1.33, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.08 x 106
surf143 = openmc.model.RectangularParallelepiped(-30.380000000000003, -1.58, -30.71, -1.25, -2.200000000000003, 103.8)
# Steel,    0.2  x 28.8 x 106
surf151 = openmc.model.RectangularParallelepiped(-30.58, -1.3800000000000008, -30.380000000000003, -1.58, -2.200000000000003, 103.8)
# Cadmium,  0.05 x 28.8 x 106
surf152 = openmc.model.RectangularParallelepiped(-30.630000000000003, -1.33, -30.380000000000003, -1.58, -2.200000000000003, 103.8)
# Steel,    0.08 x 28.8 x 106
surf153 = openmc.model.RectangularParallelepiped(-30.71, -1.25, -30.380000000000003, -1.58, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.2  x 106
surf161 = openmc.model.RectangularParallelepiped(1.58, 30.380000000000003, -30.58, -1.3800000000000008, -2.200000000000003, 103.8)
# Cadmium, 28.8  x 0.05 x 106
surf162 = openmc.model.RectangularParallelepiped(1.58, 30.380000000000003, -30.630000000000003, -1.33, -2.200000000000003, 103.8)
# Steel,   28.8  x 0.08 x 106
surf163 = openmc.model.RectangularParallelepiped(1.58, 30.380000000000003, -30.71, -1.25, -2.200000000000003, 103.8)
# Steel,    0.2  x 28.8 x 106
surf171 = openmc.model.RectangularParallelepiped(1.3800000000000008, 30.58, -30.380000000000003, -1.58, -2.200000000000003, 103.8)
# Cadmium,  0.05 x 28.8 x 106
surf172 = openmc.model.RectangularParallelepiped(1.33, 30.630000000000003, -30.380000000000003, -1.58, -2.200000000000003, 103.8)
# Steel,    0.08 x 28.8 x 106
surf173 = openmc.model.RectangularParallelepiped(1.25, 30.71, -30.380000000000003, -1.58, -2.200000000000003, 103.8)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1173, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1174, z0=90.0)
surf2_zmin = openmc.ZPlane(surface_id=1175, z0=0.0)
surf2_zmax = openmc.ZPlane(surface_id=1176, z0=96.9)
surf3_zmin = openmc.ZPlane(surface_id=1177, z0=-1.27)
surf3_zmax = openmc.ZPlane(surface_id=1178, z0=98.2)
surf4_zmin = openmc.ZPlane(surface_id=1179, z0=-1.27)
surf4_zmax = openmc.ZPlane(surface_id=1180, z0=98.2)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf5
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf6
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf7
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = +surf8 & -surf9
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & +surf6 & +surf7 & -surf8 & -surf9
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
cell1.translation = (-15.98, 15.98, 0.0)
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
cell9.translation = (15.98, 15.98, 0.0)
cell9.region = +surf18 & -surf12 & +surf26 & +surf27 & +surf28

# SST
cell10 = openmc.Cell(cell_id=10, fill=mat3)
cell10.region = +surf18 & -surf12 & +surf25 & -surf26 & -surf12 & -surf27 & -surf12 & -surf28

# Abstl
cell11 = openmc.Cell(cell_id=11, fill=mat3)
cell11.region = +surf18 & +surf12 & -surf121 & -surf122 & -surf123

# Abcad
cell12 = openmc.Cell(cell_id=12, fill=mat5)
cell12.region = +surf18 & +surf12 & +surf121 & -surf122 & -surf123

# Abstl
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = +surf18 & +surf12 & +surf121 & +surf122 & -surf123

# Abstl
cell14 = openmc.Cell(cell_id=14, fill=mat3)
cell14.region = +surf18 & +surf12 & -surf131 & -surf132 & -surf133 & +surf123

# Abcad
cell15 = openmc.Cell(cell_id=15, fill=mat5)
cell15.region = +surf18 & +surf12 & +surf131 & -surf132 & -surf133 & +surf123

# Abstl
cell16 = openmc.Cell(cell_id=16, fill=mat3)
cell16.region = +surf18 & +surf12 & +surf131 & +surf132 & -surf133 & +surf123

# Assy
cell17 = openmc.Cell(cell_id=17, fill=universe2)
cell17.translation = (-15.98, -15.98, 0.0)
cell17.region = +surf18 & -surf14

# SST
cell18 = openmc.Cell(cell_id=18, fill=mat3)
cell18.region = +surf18 & -surf14 & -surf14 & -surf14

# Abstl
cell19 = openmc.Cell(cell_id=19, fill=mat3)
cell19.region = +surf18 & +surf14 & -surf141 & -surf142 & -surf143

# Abcad
cell20 = openmc.Cell(cell_id=20, fill=mat5)
cell20.region = +surf18 & +surf14 & +surf141 & -surf142 & -surf143

# Abstl
cell21 = openmc.Cell(cell_id=21, fill=mat3)
cell21.region = +surf18 & +surf14 & +surf141 & +surf142 & -surf143

# Abstl
cell22 = openmc.Cell(cell_id=22, fill=mat3)
cell22.region = +surf18 & +surf14 & -surf151 & -surf152 & -surf153 & +surf143

# Abcad
cell23 = openmc.Cell(cell_id=23, fill=mat5)
cell23.region = +surf18 & +surf14 & +surf151 & -surf152 & -surf153 & +surf143

# Abstl
cell24 = openmc.Cell(cell_id=24, fill=mat3)
cell24.region = +surf18 & +surf14 & +surf151 & +surf152 & -surf153 & +surf143

# Assy
cell25 = openmc.Cell(cell_id=25, fill=universe2)
cell25.translation = (15.98, -15.98, 0.0)
cell25.region = +surf18 & -surf16

# SST
cell26 = openmc.Cell(cell_id=26, fill=mat3)
cell26.region = +surf18 & -surf16 & -surf16 & -surf16

# Abstl
cell27 = openmc.Cell(cell_id=27, fill=mat3)
cell27.region = +surf18 & +surf16 & -surf161 & -surf162 & -surf163

# Abcad
cell28 = openmc.Cell(cell_id=28, fill=mat5)
cell28.region = +surf18 & +surf16 & +surf161 & -surf162 & -surf163

# Abstl
cell29 = openmc.Cell(cell_id=29, fill=mat3)
cell29.region = +surf18 & +surf16 & +surf161 & +surf162 & -surf163

# Abstl
cell30 = openmc.Cell(cell_id=30, fill=mat3)
cell30.region = +surf18 & +surf16 & -surf171 & -surf172 & -surf173 & +surf163

# Abcad
cell31 = openmc.Cell(cell_id=31, fill=mat5)
cell31.region = +surf18 & +surf16 & +surf171 & -surf172 & -surf173 & +surf163

# Abstl
cell32 = openmc.Cell(cell_id=32, fill=mat3)
cell32.region = +surf18 & +surf16 & +surf171 & +surf172 & -surf173 & +surf163

# SST
cell33 = openmc.Cell(cell_id=33, fill=mat3)
cell33.region = -surf18

# Water
cell34 = openmc.Cell(cell_id=34, fill=mat4)
cell34.region = -surf19 & -surf5 & +surf10 & +surf103 & +surf113 & +surf12 & +surf123 & +surf133 & +surf14 & +surf143 & +surf153 & +surf16 & +surf163 & +surf173 & +surf18

# Water
cell42 = openmc.Cell(cell_id=42, fill=mat4)
cell42.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & +surf6 & +surf7 & -surf8 & -surf9

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
source.space = openmc.stats.Box((-30.58, -30.58, 26.32), (30.58, 30.58, 28.32))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
