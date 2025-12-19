"""
PMF042-2D: Pu hemisphere reflected by one 0.3228 cm steel shell and infinite oil; detailed model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 4.908500e-06)
mat1.add_nuclide("Pu239", 4.574100e-02)
mat1.add_nuclide("Pu240", 2.871800e-03)
mat1.add_nuclide("Pu241", 2.375200e-04)
mat1.add_nuclide("Pu242", 9.654400e-06)

# Grease, oil & air
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 3.988400e-02)
mat2.add_nuclide("Li6", 1.459700e-05)
mat2.add_nuclide("Li6", 1.543500e-04)
mat2.add_element("C", 2.056200e-02)
mat2.add_element("N", 1.068400e-05)
mat2.add_nuclide("O16", 2.100500e-03)
mat2.add_element("Si", 1.813200e-03)
mat2.add_element("Ar", 6.390000e-08)
mat2.add_s_alpha_beta("c_H_in_H2O")

# Steel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 6.708000e-04)
mat3.add_element("P", 3.118300e-05)
mat3.add_element("S", 3.694600e-05)
mat3.add_element("Mn", 6.470100e-04)
mat3.add_element("Fe", 8.404500e-02)

# Oil & air between steel shells
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 3.398100e-02)
mat4.add_element("C", 1.939000e-02)
mat4.add_element("N", 1.602600e-05)
mat4.add_nuclide("O16", 4.401700e-06)
mat4.add_element("Ar", 9.585000e-08)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Oil
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.796200e-02)
mat5.add_element("C", 3.878100e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

# Air
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 4.104900e-07)
mat6.add_element("N", 3.205300e-05)
mat6.add_nuclide("O16", 8.803400e-06)
mat6.add_element("Ar", 1.917000e-07)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Hemi
surf1 = openmc.XPlane(surface_id=1, x0=-2.37375)
# Hc
surf2 = openmc.ZPlane(surface_id=2, z0=-1.09)
# BCD
surf3 = openmc.ZCylinder(surface_id=3, r=25.0, boundary_type="vacuum")
# Pu1
surf11 = openmc.Sphere(surface_id=11, x0=2.0000, y0=tr, z0=-2.37375, r=0)
# Pu2
surf12 = openmc.Sphere(surface_id=12, x0=2.0100, y0=tr, z0=-2.37375, r=0)
# Pu2
surf13 = openmc.Sphere(surface_id=13, x0=2.1542, y0=tr, z0=-2.37375, r=0)
# Pu3
surf14 = openmc.Sphere(surface_id=14, x0=2.1764, y0=tr, z0=-2.37375, r=0)
# Pu3
surf15 = openmc.Sphere(surface_id=15, x0=2.3206, y0=tr, z0=-2.37375, r=0)
# Pu4
surf16 = openmc.Sphere(surface_id=16, x0=2.3428, y0=tr, z0=-2.37375, r=0)
# Pu4
surf17 = openmc.Sphere(surface_id=17, x0=2.4870, y0=tr, z0=-2.37375, r=0)
# Pu5
surf18 = openmc.Sphere(surface_id=18, x0=2.5092, y0=tr, z0=-2.37375, r=0)
# Pu5
surf19 = openmc.Sphere(surface_id=19, x0=2.6534, y0=tr, z0=-2.37375, r=0)
# Pu6
surf20 = openmc.Sphere(surface_id=20, x0=2.6756, y0=tr, z0=-2.37375, r=0)
# Pu6
surf21 = openmc.Sphere(surface_id=21, x0=2.8198, y0=tr, z0=-2.37375, r=0)
# Pu7
surf22 = openmc.Sphere(surface_id=22, x0=2.8420, y0=tr, z0=-2.37375, r=0)
# Pu7
surf23 = openmc.Sphere(surface_id=23, x0=2.9862, y0=tr, z0=-2.37375, r=0)
# Pu8
surf24 = openmc.Sphere(surface_id=24, x0=3.0084, y0=tr, z0=-2.37375, r=0)
# Pu8
surf25 = openmc.Sphere(surface_id=25, x0=3.1526, y0=tr, z0=-2.37375, r=0)
# Pu9
surf26 = openmc.Sphere(surface_id=26, x0=3.1748, y0=tr, z0=-2.37375, r=0)
# Pu9
surf27 = openmc.Sphere(surface_id=27, x0=3.3190, y0=tr, z0=-2.37375, r=0)
# Pu10
surf28 = openmc.Sphere(surface_id=28, x0=3.3412, y0=tr, z0=-2.37375, r=0)
# Pu10
surf29 = openmc.Sphere(surface_id=29, x0=3.4854, y0=tr, z0=-2.37375, r=0)
# Pu11
surf30 = openmc.Sphere(surface_id=30, x0=3.5076, y0=tr, z0=-2.37375, r=0)
# Pu11
surf31 = openmc.Sphere(surface_id=31, x0=3.6518, y0=tr, z0=-2.37375, r=0)
# Pu12
surf32 = openmc.Sphere(surface_id=32, x0=3.6740, y0=tr, z0=-2.37375, r=0)
# Pu12
surf33 = openmc.Sphere(surface_id=33, x0=3.8182, y0=tr, z0=-2.37375, r=0)
# Pu13
surf34 = openmc.Sphere(surface_id=34, x0=3.8404, y0=tr, z0=-2.37375, r=0)
# Pu13
surf35 = openmc.Sphere(surface_id=35, x0=3.9846, y0=tr, z0=-2.37375, r=0)
# Pu14
surf36 = openmc.Sphere(surface_id=36, x0=4.0068, y0=tr, z0=-2.37375, r=0)
# Pu14
surf37 = openmc.Sphere(surface_id=37, x0=4.1510, y0=tr, z0=-2.37375, r=0)
# Pu15
surf38 = openmc.Sphere(surface_id=38, x0=4.1732, y0=tr, z0=-2.37375, r=0)
# Pu15
surf39 = openmc.Sphere(surface_id=39, x0=4.3174, y0=tr, z0=-2.37375, r=0)
# Pu16
surf40 = openmc.Sphere(surface_id=40, x0=4.3396, y0=tr, z0=-2.37375, r=0)
# Pu16
surf41 = openmc.Sphere(surface_id=41, x0=4.4838, y0=tr, z0=-2.37375, r=0)
# Pu17
surf42 = openmc.Sphere(surface_id=42, x0=4.5060, y0=tr, z0=-2.37375, r=0)
# Pu17
surf43 = openmc.Sphere(surface_id=43, x0=4.6502, y0=tr, z0=-2.37375, r=0)
# Pu18
surf44 = openmc.Sphere(surface_id=44, x0=4.6724, y0=tr, z0=-2.37375, r=0)
# Pu18
surf45 = openmc.Sphere(surface_id=45, x0=4.8166, y0=tr, z0=-2.37375, r=0)
# Pu19
surf46 = openmc.Sphere(surface_id=46, x0=4.8388, y0=tr, z0=-2.37375, r=0)
# Pu19
surf47 = openmc.Sphere(surface_id=47, x0=4.9830, y0=tr, z0=-2.37375, r=0)
# Pu20
surf48 = openmc.Sphere(surface_id=48, x0=5.0052, y0=tr, z0=-2.37375, r=0)
# Pu20
surf49 = openmc.Sphere(surface_id=49, x0=5.1494, y0=tr, z0=-2.37375, r=0)
# Pu21
surf50 = openmc.Sphere(surface_id=50, x0=5.1716, y0=tr, z0=-2.37375, r=0)
# Pu21
surf51 = openmc.Sphere(surface_id=51, x0=5.3158, y0=tr, z0=-2.37375, r=0)
# Pu22
surf52 = openmc.Sphere(surface_id=52, x0=5.3380, y0=tr, z0=-2.37375, r=0)
# Pu22
surf53 = openmc.Sphere(surface_id=53, x0=5.4822, y0=tr, z0=-2.37375, r=0)
# Pu23
surf54 = openmc.Sphere(surface_id=54, x0=5.5044, y0=tr, z0=-2.37375, r=0)
# Pu23
surf55 = openmc.Sphere(surface_id=55, x0=5.6486, y0=tr, z0=-2.37375, r=0)
# Pu24
surf56 = openmc.Sphere(surface_id=56, x0=5.6708, y0=tr, z0=-2.37375, r=0)
# Pu24
surf57 = openmc.Sphere(surface_id=57, x0=5.8150, y0=tr, z0=-2.37375, r=0)
# Pu25
surf58 = openmc.Sphere(surface_id=58, x0=5.8372, y0=tr, z0=-2.37375, r=0)
# Pu25
surf59 = openmc.Sphere(surface_id=59, x0=5.9814, y0=tr, z0=-2.37375, r=0)
# Pu26
surf60 = openmc.Sphere(surface_id=60, x0=6.0036, y0=tr, z0=-2.37375, r=0)
# Pu26
surf61 = openmc.Sphere(surface_id=61, x0=6.1478, y0=tr, z0=-2.37375, r=0)
# Pu27
surf62 = openmc.Sphere(surface_id=62, x0=6.1700, y0=tr, z0=-2.37375, r=0)
# Pu27
surf63 = openmc.Sphere(surface_id=63, x0=6.3142, y0=tr, z0=-2.37375, r=0)
# S1
surf64 = openmc.Sphere(surface_id=64, x0=6.3386, y0=tr, z0=-2.37375, r=0)
# S1
surf65 = openmc.Sphere(surface_id=65, x0=6.6614, y0=tr, z0=-2.37375, r=0)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1065, z0=-31.333, boundary_type="vacuum")
surf3_zmax = openmc.ZPlane(surface_id=1066, z0=18.667, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = +surf1 & -surf11
u1_cell1 = openmc.Cell(fill=mat1)
u1_cell1.region = +surf1 & +surf12 & -surf13
u1_cell2 = openmc.Cell(fill=mat1)
u1_cell2.region = +surf1 & +surf14 & -surf15
u1_cell3 = openmc.Cell(fill=mat1)
u1_cell3.region = +surf1 & +surf16 & -surf17
u1_cell4 = openmc.Cell(fill=mat1)
u1_cell4.region = +surf1 & +surf18 & -surf19
u1_cell5 = openmc.Cell(fill=mat1)
u1_cell5.region = +surf1 & +surf20 & -surf21
u1_cell6 = openmc.Cell(fill=mat1)
u1_cell6.region = +surf1 & +surf22 & -surf23
u1_cell7 = openmc.Cell(fill=mat1)
u1_cell7.region = +surf1 & +surf24 & -surf25
u1_cell8 = openmc.Cell(fill=mat1)
u1_cell8.region = +surf1 & +surf26 & -surf27
u1_cell9 = openmc.Cell(fill=mat1)
u1_cell9.region = +surf1 & +surf28 & -surf29
u1_cell10 = openmc.Cell(fill=mat1)
u1_cell10.region = +surf1 & +surf30 & -surf31
u1_cell11 = openmc.Cell(fill=mat1)
u1_cell11.region = +surf1 & +surf32 & -surf33
u1_cell12 = openmc.Cell(fill=mat1)
u1_cell12.region = +surf1 & +surf34 & -surf35
u1_cell13 = openmc.Cell(fill=mat1)
u1_cell13.region = +surf1 & +surf36 & -surf37
u1_cell14 = openmc.Cell(fill=mat1)
u1_cell14.region = +surf1 & +surf38 & -surf39
u1_cell15 = openmc.Cell(fill=mat1)
u1_cell15.region = +surf1 & +surf40 & -surf41
u1_cell16 = openmc.Cell(fill=mat1)
u1_cell16.region = +surf1 & +surf42 & -surf43
u1_cell17 = openmc.Cell(fill=mat1)
u1_cell17.region = +surf1 & +surf44 & -surf45
u1_cell18 = openmc.Cell(fill=mat1)
u1_cell18.region = +surf1 & +surf46 & -surf47
u1_cell19 = openmc.Cell(fill=mat1)
u1_cell19.region = +surf1 & +surf48 & -surf49
u1_cell20 = openmc.Cell(fill=mat1)
u1_cell20.region = +surf1 & +surf50 & -surf51
u1_cell21 = openmc.Cell(fill=mat1)
u1_cell21.region = +surf1 & +surf52 & -surf53
u1_cell22 = openmc.Cell(fill=mat1)
u1_cell22.region = +surf1 & +surf54 & -surf55
u1_cell23 = openmc.Cell(fill=mat1)
u1_cell23.region = +surf1 & +surf56 & -surf57
u1_cell24 = openmc.Cell(fill=mat1)
u1_cell24.region = +surf1 & +surf58 & -surf59
u1_cell25 = openmc.Cell(fill=mat1)
u1_cell25.region = +surf1 & +surf60 & -surf61
u1_cell26 = openmc.Cell(fill=mat1)
u1_cell26.region = +surf1 & +surf62 & -surf63
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11, u1_cell12, u1_cell13, u1_cell14, u1_cell15, u1_cell16, u1_cell17, u1_cell18, u1_cell19, u1_cell20, u1_cell21, u1_cell22, u1_cell23, u1_cell24, u1_cell25, u1_cell26])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# hemis
cell1 = openmc.Cell(cell_id=1, fill=universe1)
cell1.region = +surf1 & -surf64

# Steel
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = +surf1 & +surf64 & -surf65

# Oil
cell3 = openmc.Cell(cell_id=3, fill=mat5)
cell3.region = +surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf65

# Oil
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = -surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)

# Air
cell5 = openmc.Cell(cell_id=5, fill=mat6)
cell5.region = -surf1 & +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)

# Air
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf1 & +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & +surf65

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6])
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
source.space = openmc.stats.Point((0.0, 0.0, -6.333))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
