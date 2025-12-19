"""
LCT007-9: 277 U(4.738)O2 fuel rods with 1.72 cm triangular pitch in water
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(4.738)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 7.108700e-06)
mat1.add_nuclide("U235", 1.110400e-03)
mat1.add_nuclide("U236", 3.179200e-05)
mat1.add_nuclide("U238", 2.200600e-02)
mat1.add_nuclide("O16", 4.631100e-02)
mat1.add_element("Al", 4.170100e-06)
mat1.add_element("Fe", 9.514000e-06)
mat1.add_element("Si", 2.247900e-05)
mat1.add_nuclide("B10", 6.903700e-08)
mat1.add_nuclide("B11", 2.778800e-07)

# AGS clad, plugs
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.959600e-02)
mat2.add_element("Mg", 3.144200e-04)
mat2.add_element("Si", 2.489400e-04)
mat2.add_element("Zn", 7.459700e-06)
mat2.add_element("Fe", 6.405200e-05)

# Air
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("N", 4.198500e-05)
mat3.add_nuclide("O16", 1.126300e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.670600e-02)
mat4.add_nuclide("O16", 3.335300e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Stainless steel
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 5.941400e-05)
mat5.add_element("Cr", 1.646900e-02)
mat5.add_element("Fe", 6.001400e-02)
mat5.add_element("Mn", 8.659700e-04)
mat5.add_element("Ni", 8.106100e-03)
mat5.add_element("Si", 8.469600e-04)
mat5.add_element("S", 2.225600e-05)
mat5.add_nuclide("P31", 3.071900e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Entire problem (BCD)
surf1 = openmc.model.RectangularParallelepiped(-60.0, 60.0, -60.0, 60.0, -21.799999999999997, 98.2, boundary_type="vacuum")
# Hexagonal
# Prism 2: 6-sided polygon
surf2_0 = openmc.Plane(a=0.8660254482, b=0.4999999231, c=0, d=14.8956377088)
surf2_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=14.8956400000)
surf2_2 = openmc.Plane(a=-0.8660254482, b=0.4999999231, c=0, d=14.8956377088)
surf2_3 = openmc.Plane(a=-0.8660254482, b=-0.4999999231, c=0, d=14.8956377088)
surf2_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=14.8956400000)
surf2_5 = openmc.Plane(a=0.8660254482, b=-0.4999999231, c=0, d=14.8956377088)
# Hexagonal
# Prism 3: 6-sided polygon
surf3_0 = openmc.Plane(a=0.8660254482, b=0.4999999231, c=0, d=15.6404195943)
surf3_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=15.6404220000)
surf3_2 = openmc.Plane(a=-0.8660254482, b=0.4999999231, c=0, d=15.6404195943)
surf3_3 = openmc.Plane(a=-0.8660254482, b=-0.4999999231, c=0, d=15.6404195943)
surf3_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=15.6404220000)
surf3_5 = openmc.Plane(a=0.8660254482, b=-0.4999999231, c=0, d=15.6404195943)
# Hc
surf10 = openmc.ZPlane(surface_id=10, z0=61.99)
# UO2
surf11 = openmc.ZCylinder(surface_id=11, r=0.3946)
# Gap
surf12 = openmc.ZCylinder(surface_id=12, r=0.41)
# AGS
# surf13: Unsupported surface type "rev" with params ['3', '-1.8', '0.0', '-1.0', '0.47', '98.2', '0.47']
# Hole in grid plates
surf14 = openmc.ZCylinder(surface_id=14, r=0.5)
# SS pedestal plate
surf15 = openmc.model.RectangularParallelepiped(-47.5, 47.5, -47.5, 47.5, -2.6, -1.8000000000000003)
# SS bottom grid plate
surf16 = openmc.ZCylinder(surface_id=16, r=999.9)
# SS upper grid plate
surf17 = openmc.ZCylinder(surface_id=17, r=999.9)
# Hole in grid plates
surf21 = openmc.ZCylinder(surface_id=21, x0=-0.86, y0=1.489564, r=0.5)
# Hole in grid plates
surf22 = openmc.ZCylinder(surface_id=22, x0=-0.86, y0=-1.489564, r=0.5)
# Hole in grid plates
surf23 = openmc.ZCylinder(surface_id=23, x0=0.86, y0=1.489564, r=0.5)
# Hole in grid plates
surf24 = openmc.ZCylinder(surface_id=24, x0=0.86, y0=-1.489564, r=0.5)
surf101 = openmc.ZCylinder(surface_id=101, x0=-8.6, y0=14.89564, r=0.5)
surf102 = openmc.ZCylinder(surface_id=102, x0=-6.88, y0=14.89564, r=0.5)
surf103 = openmc.ZCylinder(surface_id=103, x0=-5.16, y0=14.89564, r=0.5)
surf104 = openmc.ZCylinder(surface_id=104, x0=-3.44, y0=14.89564, r=0.5)
surf105 = openmc.ZCylinder(surface_id=105, x0=0.0, y0=14.89564, r=0.5)
surf106 = openmc.ZCylinder(surface_id=106, x0=3.44, y0=14.89564, r=0.5)
surf107 = openmc.ZCylinder(surface_id=107, x0=5.16, y0=14.89564, r=0.5)
surf108 = openmc.ZCylinder(surface_id=108, x0=6.88, y0=14.89564, r=0.5)
surf109 = openmc.ZCylinder(surface_id=109, x0=8.6, y0=14.89564, r=0.5)
surf110 = openmc.ZCylinder(surface_id=110, x0=-9.46, y0=13.406076, r=0.5)
surf111 = openmc.ZCylinder(surface_id=111, x0=-7.74, y0=13.406076, r=0.5)
surf112 = openmc.ZCylinder(surface_id=112, x0=7.74, y0=13.406076, r=0.5)
surf113 = openmc.ZCylinder(surface_id=113, x0=9.46, y0=13.406076, r=0.5)
surf114 = openmc.ZCylinder(surface_id=114, x0=-10.32, y0=11.916512, r=0.5)
surf115 = openmc.ZCylinder(surface_id=115, x0=10.32, y0=11.916512, r=0.5)
surf116 = openmc.ZCylinder(surface_id=116, x0=-11.18, y0=10.426948, r=0.5)
surf117 = openmc.ZCylinder(surface_id=117, x0=11.18, y0=10.426948, r=0.5)
surf118 = openmc.ZCylinder(surface_id=118, x0=-12.9, y0=7.44782, r=0.5)
surf119 = openmc.ZCylinder(surface_id=119, x0=12.9, y0=7.44782, r=0.5)
surf120 = openmc.ZCylinder(surface_id=120, x0=-14.62, y0=4.468692, r=0.5)
surf121 = openmc.ZCylinder(surface_id=121, x0=14.62, y0=4.468692, r=0.5)
surf122 = openmc.ZCylinder(surface_id=122, x0=-15.48, y0=2.979128, r=0.5)
surf123 = openmc.ZCylinder(surface_id=123, x0=15.48, y0=2.979128, r=0.5)
surf124 = openmc.ZCylinder(surface_id=124, x0=-16.34, y0=1.489564, r=0.5)
surf125 = openmc.ZCylinder(surface_id=125, x0=16.34, y0=1.489564, r=0.5)
surf126 = openmc.ZCylinder(surface_id=126, x0=-17.2, y0=0.0, r=0.5)
surf127 = openmc.ZCylinder(surface_id=127, x0=-15.48, y0=0.0, r=0.5)
surf128 = openmc.ZCylinder(surface_id=128, x0=15.48, y0=0.0, r=0.5)
surf129 = openmc.ZCylinder(surface_id=129, x0=17.2, y0=0.0, r=0.5)
surf130 = openmc.ZCylinder(surface_id=130, x0=-16.34, y0=-1.489564, r=0.5)
surf131 = openmc.ZCylinder(surface_id=131, x0=16.34, y0=-1.489564, r=0.5)
surf132 = openmc.ZCylinder(surface_id=132, x0=-15.48, y0=-2.979128, r=0.5)
surf133 = openmc.ZCylinder(surface_id=133, x0=15.48, y0=-2.979128, r=0.5)
surf134 = openmc.ZCylinder(surface_id=134, x0=-14.62, y0=-4.468692, r=0.5)
surf135 = openmc.ZCylinder(surface_id=135, x0=14.62, y0=-4.468692, r=0.5)
surf136 = openmc.ZCylinder(surface_id=136, x0=-12.9, y0=-7.44782, r=0.5)
surf137 = openmc.ZCylinder(surface_id=137, x0=12.9, y0=-7.44782, r=0.5)
surf138 = openmc.ZCylinder(surface_id=138, x0=-11.18, y0=-10.426948, r=0.5)
surf139 = openmc.ZCylinder(surface_id=139, x0=11.18, y0=-10.426948, r=0.5)
surf140 = openmc.ZCylinder(surface_id=140, x0=-10.32, y0=-11.916512, r=0.5)
surf141 = openmc.ZCylinder(surface_id=141, x0=10.32, y0=-11.916512, r=0.5)
surf142 = openmc.ZCylinder(surface_id=142, x0=-9.46, y0=-13.406076, r=0.5)
surf143 = openmc.ZCylinder(surface_id=143, x0=-7.74, y0=-13.406076, r=0.5)
surf144 = openmc.ZCylinder(surface_id=144, x0=7.74, y0=-13.406076, r=0.5)
surf145 = openmc.ZCylinder(surface_id=145, x0=9.46, y0=-13.406076, r=0.5)
surf146 = openmc.ZCylinder(surface_id=146, x0=-8.6, y0=-14.89564, r=0.5)
surf147 = openmc.ZCylinder(surface_id=147, x0=-6.88, y0=-14.89564, r=0.5)
surf148 = openmc.ZCylinder(surface_id=148, x0=-5.16, y0=-14.89564, r=0.5)
surf149 = openmc.ZCylinder(surface_id=149, x0=-3.44, y0=-14.89564, r=0.5)
surf150 = openmc.ZCylinder(surface_id=150, x0=0.0, y0=-14.89564, r=0.5)
surf151 = openmc.ZCylinder(surface_id=151, x0=3.44, y0=-14.89564, r=0.5)
surf152 = openmc.ZCylinder(surface_id=152, x0=5.16, y0=-14.89564, r=0.5)
surf153 = openmc.ZCylinder(surface_id=153, x0=6.88, y0=-14.89564, r=0.5)
surf154 = openmc.ZCylinder(surface_id=154, x0=8.6, y0=-14.89564, r=0.5)

# Z-plane surfaces for bounded cylinders
surf11_zmin = openmc.ZPlane(surface_id=1154, z0=0.0)
surf11_zmax = openmc.ZPlane(surface_id=1155, z0=89.7)
surf12_zmin = openmc.ZPlane(surface_id=1156, z0=0.0)
surf12_zmax = openmc.ZPlane(surface_id=1157, z0=96.9)
surf16_zmin = openmc.ZPlane(surface_id=1158, z0=-0.3)
surf16_zmax = openmc.ZPlane(surface_id=1159, z0=-0.05)
surf17_zmin = openmc.ZPlane(surface_id=1160, z0=96.45)
surf17_zmax = openmc.ZPlane(surface_id=1161, z0=96.7)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & (-surf11 & +surf11_zmin & -surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf1 & (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = -surf1 & (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & -surf13
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = -surf1 & -surf10 & +surf13
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = -surf1 & +surf10 & +surf13
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = -surf1 & -surf15
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = -surf1 & +surf14 & (-surf16 & +surf16_zmin & -surf16_zmax) & +surf21 & +surf22 & +surf23 & +surf24
u2_cell2 = openmc.Cell(fill=mat5)
u2_cell2.region = -surf1 & +surf14 & (-surf17 & +surf17_zmin & -surf17_zmax) & +surf21 & +surf22 & +surf23 & +surf24
u2_cell3 = openmc.Cell(fill=mat4)
u2_cell3.region = -surf1 & -surf10 & +surf14 & +surf15 & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax) & +surf21 & +surf22 & +surf23 & +surf24
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = -surf1 & +surf10 & +surf14 & +surf15 & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax) & +surf21 & +surf22 & +surf23 & +surf24
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

# Lattice 3: 21x11 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-18.06, -16.385204]
lattice3.pitch = [1.720000, 2.979128]
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
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

u4_cell0 = openmc.Cell(fill=mat3)
u4_cell0.region = -surf1 & +surf10
u4_cell1 = openmc.Cell(fill=mat4)
u4_cell1.region = -surf1 & -surf10 & +surf15
u4_cell2 = openmc.Cell(fill=mat5)
u4_cell2.region = -surf1 & -surf10 & -surf15
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf1 & (-surf3_0 & -surf3_1 & -surf3_2 & -surf3_3 & -surf3_4 & -surf3_5) & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110

# Hole
cell2 = openmc.Cell(cell_id=2, fill=universe4)
cell2.region = -surf1 & -surf101 & -surf1 & -surf102 & -surf1 & -surf103 & -surf1 & -surf104 & -surf1 & -surf105

# Hole
cell3 = openmc.Cell(cell_id=3, fill=universe4)
cell3.region = -surf1 & -surf106 & -surf1 & -surf107 & -surf1 & -surf108 & -surf1 & -surf109 & -surf1 & -surf110

# Hole
cell4 = openmc.Cell(cell_id=4, fill=universe4)
cell4.region = -surf1 & -surf111 & -surf1 & -surf112 & -surf1 & -surf113 & -surf1 & -surf114 & -surf1 & -surf115

# Hole
cell5 = openmc.Cell(cell_id=5, fill=universe4)
cell5.region = -surf1 & -surf116 & -surf1 & -surf117 & -surf1 & -surf118 & -surf1 & -surf119 & -surf1 & -surf120

# Hole
cell6 = openmc.Cell(cell_id=6, fill=universe4)
cell6.region = -surf1 & -surf121 & -surf1 & -surf122 & -surf1 & -surf123 & -surf1 & -surf124 & -surf1 & -surf125

# Hole
cell7 = openmc.Cell(cell_id=7, fill=universe4)
cell7.region = -surf1 & -surf126 & -surf1 & -surf127 & -surf1 & -surf128 & -surf1 & -surf129 & -surf1 & -surf130

# Hole
cell8 = openmc.Cell(cell_id=8, fill=universe4)
cell8.region = -surf1 & -surf131 & -surf1 & -surf132 & -surf1 & -surf133 & -surf1 & -surf134 & -surf1 & -surf135

# Hole
cell9 = openmc.Cell(cell_id=9, fill=universe4)
cell9.region = -surf1 & -surf136 & -surf1 & -surf137 & -surf1 & -surf138 & -surf1 & -surf139 & -surf1 & -surf140

# Hole
cell10 = openmc.Cell(cell_id=10, fill=universe4)
cell10.region = -surf1 & -surf141 & -surf1 & -surf142 & -surf1 & -surf143 & -surf1 & -surf144 & -surf1 & -surf145

# Hole
cell11 = openmc.Cell(cell_id=11, fill=universe4)
cell11.region = -surf1 & -surf146 & -surf1 & -surf147 & -surf1 & -surf148 & -surf1 & -surf149 & -surf1 & -surf150

# Hole
cell12 = openmc.Cell(cell_id=12, fill=universe4)
cell12.region = -surf1 & -surf151 & -surf1 & -surf152 & -surf1 & -surf153 & -surf1 & -surf154

# Refl
cell13 = openmc.Cell(cell_id=13, fill=universe4)
cell13.region = -surf1 & (+surf3_0 | +surf3_1 | +surf3_2 | +surf3_3 | +surf3_4 | +surf3_5)

# Air
cell19 = openmc.Cell(cell_id=19, fill=mat3)
cell19.region = -surf1 & +surf10 & +surf13

# Air
cell25 = openmc.Cell(cell_id=25, fill=mat3)
cell25.region = -surf1 & +surf10 & +surf14 & +surf15 & (+surf16 | -surf16_zmin | +surf16_zmax) & (+surf17 | -surf17_zmin | +surf17_zmax) & +surf21 & +surf22 & +surf23 & +surf24

# SS
cell29 = openmc.Cell(cell_id=29, fill=mat5)
cell29.region = -surf1 & -surf10 & -surf15

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell19, cell25, cell29])
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
source.space = openmc.stats.Point((0.0, 0.0, 30.995))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
