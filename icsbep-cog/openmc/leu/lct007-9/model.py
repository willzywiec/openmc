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
surf11 = openmc.ZCylinder(surface_id=11, x0=0.0, y0=89.7, r=0.3946)
# Gap
surf12 = openmc.ZCylinder(surface_id=12, x0=0.0, y0=96.9, r=0.41)
# AGS
# surf13: Unsupported surface type "rev" with params ['3', '-1.8', '0.0', '-1.0', '0.47', '98.2', '0.47']
# Hole in grid plates
surf14 = openmc.ZCylinder(surface_id=14, r=0.5)
# SS pedestal plate
surf15 = openmc.model.RectangularParallelepiped(-47.5, 47.5, -47.5, 47.5, -2.6, -1.8000000000000003)
# SS bottom grid plate
surf16 = openmc.ZCylinder(surface_id=16, x0=-0.3, y0=-0.05, r=999.9)
# SS upper grid plate
surf17 = openmc.ZCylinder(surface_id=17, x0=96.45, y0=96.7, r=999.9)
# Hole in grid plates
surf21_cyl = openmc.ZCylinder(surface_id=21, x0=tr, y0=-0.86, r=0.5)
surf21_zmin = openmc.ZPlane(z0=1.489564)
surf21_zmax = openmc.ZPlane(z0=0.0)
surf21 = (surf21_cyl, surf21_zmin, surf21_zmax)
# Hole in grid plates
surf22_cyl = openmc.ZCylinder(surface_id=22, x0=tr, y0=-0.86, r=0.5)
surf22_zmin = openmc.ZPlane(z0=-1.489564)
surf22_zmax = openmc.ZPlane(z0=0.0)
surf22 = (surf22_cyl, surf22_zmin, surf22_zmax)
# Hole in grid plates
surf23_cyl = openmc.ZCylinder(surface_id=23, x0=tr, y0=0.86, r=0.5)
surf23_zmin = openmc.ZPlane(z0=1.489564)
surf23_zmax = openmc.ZPlane(z0=0.0)
surf23 = (surf23_cyl, surf23_zmin, surf23_zmax)
# Hole in grid plates
surf24_cyl = openmc.ZCylinder(surface_id=24, x0=tr, y0=0.86, r=0.5)
surf24_zmin = openmc.ZPlane(z0=-1.489564)
surf24_zmax = openmc.ZPlane(z0=0.0)
surf24 = (surf24_cyl, surf24_zmin, surf24_zmax)
# surf101: Error converting surface type "c": could not convert string to float: 'tr'
# surf102: Error converting surface type "c": could not convert string to float: 'tr'
# surf103: Error converting surface type "c": could not convert string to float: 'tr'
# surf104: Error converting surface type "c": could not convert string to float: 'tr'
# surf105: Error converting surface type "c": could not convert string to float: 'tr'
# surf106: Error converting surface type "c": could not convert string to float: 'tr'
# surf107: Error converting surface type "c": could not convert string to float: 'tr'
# surf108: Error converting surface type "c": could not convert string to float: 'tr'
# surf109: Error converting surface type "c": could not convert string to float: 'tr'
# surf110: Error converting surface type "c": could not convert string to float: 'tr'
# surf111: Error converting surface type "c": could not convert string to float: 'tr'
# surf112: Error converting surface type "c": could not convert string to float: 'tr'
# surf113: Error converting surface type "c": could not convert string to float: 'tr'
# surf114: Error converting surface type "c": could not convert string to float: 'tr'
# surf115: Error converting surface type "c": could not convert string to float: 'tr'
# surf116: Error converting surface type "c": could not convert string to float: 'tr'
# surf117: Error converting surface type "c": could not convert string to float: 'tr'
# surf118: Error converting surface type "c": could not convert string to float: 'tr'
# surf119: Error converting surface type "c": could not convert string to float: 'tr'
# surf120: Error converting surface type "c": could not convert string to float: 'tr'
# surf121: Error converting surface type "c": could not convert string to float: 'tr'
# surf122: Error converting surface type "c": could not convert string to float: 'tr'
# surf123: Error converting surface type "c": could not convert string to float: 'tr'
# surf124: Error converting surface type "c": could not convert string to float: 'tr'
# surf125: Error converting surface type "c": could not convert string to float: 'tr'
# surf126: Error converting surface type "c": could not convert string to float: 'tr'
# surf127: Error converting surface type "c": could not convert string to float: 'tr'
# surf128: Error converting surface type "c": could not convert string to float: 'tr'
# surf129: Error converting surface type "c": could not convert string to float: 'tr'
# surf130: Error converting surface type "c": could not convert string to float: 'tr'
# surf131: Error converting surface type "c": could not convert string to float: 'tr'
# surf132: Error converting surface type "c": could not convert string to float: 'tr'
# surf133: Error converting surface type "c": could not convert string to float: 'tr'
# surf134: Error converting surface type "c": could not convert string to float: 'tr'
# surf135: Error converting surface type "c": could not convert string to float: 'tr'
# surf136: Error converting surface type "c": could not convert string to float: 'tr'
# surf137: Error converting surface type "c": could not convert string to float: 'tr'
# surf138: Error converting surface type "c": could not convert string to float: 'tr'
# surf139: Error converting surface type "c": could not convert string to float: 'tr'
# surf140: Error converting surface type "c": could not convert string to float: 'tr'
# surf141: Error converting surface type "c": could not convert string to float: 'tr'
# surf142: Error converting surface type "c": could not convert string to float: 'tr'
# surf143: Error converting surface type "c": could not convert string to float: 'tr'
# surf144: Error converting surface type "c": could not convert string to float: 'tr'
# surf145: Error converting surface type "c": could not convert string to float: 'tr'
# surf146: Error converting surface type "c": could not convert string to float: 'tr'
# surf147: Error converting surface type "c": could not convert string to float: 'tr'
# surf148: Error converting surface type "c": could not convert string to float: 'tr'
# surf149: Error converting surface type "c": could not convert string to float: 'tr'
# surf150: Error converting surface type "c": could not convert string to float: 'tr'
# surf151: Error converting surface type "c": could not convert string to float: 'tr'
# surf152: Error converting surface type "c": could not convert string to float: 'tr'
# surf153: Error converting surface type "c": could not convert string to float: 'tr'
# surf154: Error converting surface type "c": could not convert string to float: 'tr'

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf11 & -surf12
u1_cell1 = openmc.Cell(fill=mat3)
u1_cell1.region = -surf1 & +surf11 & -surf12
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = -surf1 & +surf11 & +surf12 & -surf13
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = -surf1 & -surf10 & +surf13
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = -surf1 & +surf10 & +surf13
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = -surf1 & -surf15
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = -surf1 & +surf14 & -surf16 & +surf21 & +surf22 & +surf23 & +surf24
u2_cell2 = openmc.Cell(fill=mat5)
u2_cell2.region = -surf1 & +surf14 & -surf17 & +surf21 & +surf22 & +surf23 & +surf24
u2_cell3 = openmc.Cell(fill=mat4)
u2_cell3.region = -surf1 & -surf10 & +surf14 & +surf15 & +surf16 & +surf17 & +surf21 & +surf22 & +surf23 & +surf24
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = -surf1 & +surf10 & +surf14 & +surf15 & +surf16 & +surf17 & +surf21 & +surf22 & +surf23 & +surf24
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
cell2.region = -surf1 & -surf101 & +surf4 & -surf1 & -surf102 & +surf4 & -surf1 & -surf103 & +surf4 & -surf1 & -surf104 & +surf4 & -surf1 & -surf105

# Hole
cell3 = openmc.Cell(cell_id=3, fill=universe4)
cell3.region = -surf1 & -surf106 & +surf4 & -surf1 & -surf107 & +surf4 & -surf1 & -surf108 & +surf4 & -surf1 & -surf109 & +surf4 & -surf1 & -surf110

# Hole
cell4 = openmc.Cell(cell_id=4, fill=universe4)
cell4.region = -surf1 & -surf111 & +surf4 & -surf1 & -surf112 & +surf4 & -surf1 & -surf113 & +surf4 & -surf1 & -surf114 & +surf4 & -surf1 & -surf115

# Hole
cell5 = openmc.Cell(cell_id=5, fill=universe4)
cell5.region = -surf1 & -surf116 & +surf4 & -surf1 & -surf117 & +surf4 & -surf1 & -surf118 & +surf4 & -surf1 & -surf119 & +surf4 & -surf1 & -surf120

# Hole
cell6 = openmc.Cell(cell_id=6, fill=universe4)
cell6.region = -surf1 & -surf121 & +surf4 & -surf1 & -surf122 & +surf4 & -surf1 & -surf123 & +surf4 & -surf1 & -surf124 & +surf4 & -surf1 & -surf125

# Hole
cell7 = openmc.Cell(cell_id=7, fill=universe4)
cell7.region = -surf1 & -surf126 & +surf4 & -surf1 & -surf127 & +surf4 & -surf1 & -surf128 & +surf4 & -surf1 & -surf129 & +surf4 & -surf1 & -surf130

# Hole
cell8 = openmc.Cell(cell_id=8, fill=universe4)
cell8.region = -surf1 & -surf131 & +surf4 & -surf1 & -surf132 & +surf4 & -surf1 & -surf133 & +surf4 & -surf1 & -surf134 & +surf4 & -surf1 & -surf135

# Hole
cell9 = openmc.Cell(cell_id=9, fill=universe4)
cell9.region = -surf1 & -surf136 & +surf4 & -surf1 & -surf137 & +surf4 & -surf1 & -surf138 & +surf4 & -surf1 & -surf139 & +surf4 & -surf1 & -surf140

# Hole
cell10 = openmc.Cell(cell_id=10, fill=universe4)
cell10.region = -surf1 & -surf141 & +surf4 & -surf1 & -surf142 & +surf4 & -surf1 & -surf143 & +surf4 & -surf1 & -surf144 & +surf4 & -surf1 & -surf145

# Hole
cell11 = openmc.Cell(cell_id=11, fill=universe4)
cell11.region = -surf1 & -surf146 & +surf4 & -surf1 & -surf147 & +surf4 & -surf1 & -surf148 & +surf4 & -surf1 & -surf149 & +surf4 & -surf1 & -surf150

# Hole
cell12 = openmc.Cell(cell_id=12, fill=universe4)
cell12.region = -surf1 & -surf151 & +surf4 & -surf1 & -surf152 & +surf4 & -surf1 & -surf153 & +surf4 & -surf1 & -surf154

# Refl
cell13 = openmc.Cell(cell_id=13, fill=universe4)
cell13.region = -surf1 & (+surf3_0 | +surf3_1 | +surf3_2 | +surf3_3 | +surf3_4 | +surf3_5)

# Air
cell19 = openmc.Cell(cell_id=19, fill=mat3)
cell19.region = -surf1 & +surf10 & +surf13

# Air
cell25 = openmc.Cell(cell_id=25, fill=mat3)
cell25.region = -surf1 & +surf10 & +surf14 & +surf15 & +surf16 & +surf17 & +surf21 & +surf22 & +surf23 & +surf24

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
