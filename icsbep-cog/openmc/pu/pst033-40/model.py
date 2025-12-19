"""
PU-SOL-THERM-033-40: 202.67 gPu(3.13)/L at H/X=116.4 with 7 (4x60) pyrex tubes at 4.31cm pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.490300e-10)
mat1.add_nuclide("U238", 2.087400e-08)
mat1.add_nuclide("Pu239", 4.938800e-04)
mat1.add_nuclide("Pu240", 1.593900e-05)
mat1.add_nuclide("Pu241", 6.075700e-07)
mat1.add_nuclide("Pu242", 6.050600e-08)
mat1.add_nuclide("Am241", 7.088400e-08)
mat1.add_nuclide("H1", 5.749200e-02)
mat1.add_nuclide("O16", 3.866400e-02)
mat1.add_element("N", 3.554800e-03)
mat1.add_element("Fe", 2.943800e-06)
mat1.add_element("Cr", 3.520900e-07)
mat1.add_element("Ni", 4.159100e-07)
mat1.add_element("Mn", 1.332900e-07)
mat1.add_element("Ca", 1.827200e-06)
mat1.add_element("Cu", 2.496800e-07)
mat1.add_element("Mg", 1.004300e-06)
mat1.add_element("Zn", 2.799700e-07)
mat1.add_element("Na", 1.327200e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.954600e-02)
mat2.add_element("Si", 1.646900e-03)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Mn", 8.659700e-04)
mat2.add_element("Si", 1.693900e-03)
mat2.add_element("S", 4.450400e-05)
mat2.add_element("P", 6.143900e-05)
mat2.add_element("C", 1.188300e-04)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.670600e-02)
mat3.add_nuclide("O16", 3.335300e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("N", 4.198500e-05)
mat4.add_nuclide("O16", 1.126300e-05)

# Polyethylene
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 8.310400e-02)
mat5.add_element("C", 4.155200e-02)
mat5.add_s_alpha_beta("c_H_in_CH2")

# Borated
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("B10", 1.039600e-03)
mat6.add_nuclide("B11", 4.184400e-03)
mat6.add_element("Al", 5.334600e-04)
mat6.add_element("Fe", 3.705600e-06)
mat6.add_element("Na", 1.482700e-03)
mat6.add_element("K", 3.061000e-04)
mat6.add_element("Si", 1.789200e-02)
mat6.add_nuclide("O16", 4.532300e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Critical solution height, Hc
surf1 = openmc.ZPlane(surface_id=1, z0=23.83)
# SST solution tank, inner
# surf2: Unsupported surface type "rev" with params ['3', '0.0', '0.0', '0.6', '17.98', '80.7', '17.98']
# SST solution  tank, outer
surf3 = openmc.ZCylinder(surface_id=3, r=18.28)
# SST reflector tank, inner
surf4 = openmc.ZCylinder(surface_id=4, r=54.6)
# SST refelctor tank, top
surf5 = openmc.ZPlane(surface_id=5, z0=63.2)
# SST reflector tank, outer, and BCD
surf6 = openmc.ZCylinder(surface_id=6, r=55.0, boundary_type="vacuum")
# Basket outer boundary
surf10 = openmc.ZCylinder(surface_id=10, r=17.8)
# SST bottom plate
surf11 = openmc.ZCylinder(surface_id=11, r=17.5)
# SST annular top plate, inner
surf12 = openmc.ZCylinder(surface_id=12, r=13.75)
# SST annular top plate, outer
surf13 = openmc.ZCylinder(surface_id=13, r=17.8)
# Tie rod, inner
surf14 = openmc.ZCylinder(surface_id=14, r=0.3)
# Tie rod, outer
surf15 = openmc.ZCylinder(surface_id=15, r=0.4)
# Tie rod #1
surf16 = openmc.ZCylinder(surface_id=16, x0=-16.9, y0=0.0, r=0.4)
# Tie rod #2
surf17 = openmc.ZCylinder(surface_id=17, x0=8.45, y0=-14.63583, r=0.4)
# Tie rod #3
surf18 = openmc.ZCylinder(surface_id=18, x0=8.45, y0=14.63583, r=0.4)
# Lower polyethylene grid plate, inner region
surf19 = openmc.ZCylinder(surface_id=19, r=17.5)
# Upper polyethylene grid plate, inner region
surf20 = openmc.ZCylinder(surface_id=20, r=17.5)
# Lower polyethylene grid plate, outer region
surf21 = openmc.ZCylinder(surface_id=21, r=17.5)
# Upper polyethylene grid plate, outer region
surf22 = openmc.ZCylinder(surface_id=22, r=17.5)
# 4x60 pyrex tube, inner
surf23 = openmc.ZCylinder(surface_id=23, r=1.7415)
# 4x60 pyrex tube, outer
surf24 = openmc.ZCylinder(surface_id=24, r=2.0085)
# Unit cell #1
# Prism 31: 6-sided polygon
surf31_0 = openmc.Plane(a=0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf31_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=2.1550000000)
surf31_2 = openmc.Plane(a=-0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf31_3 = openmc.Plane(a=-0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
surf31_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=2.1550000000)
surf31_5 = openmc.Plane(a=0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
# Unit cell #2
# Prism 32: 6-sided polygon
surf32_0 = openmc.Plane(a=0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf32_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=2.1550000000)
surf32_2 = openmc.Plane(a=-0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf32_3 = openmc.Plane(a=-0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
surf32_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=2.1550000000)
surf32_5 = openmc.Plane(a=0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
# Unit cell #3
# Prism 33: 6-sided polygon
surf33_0 = openmc.Plane(a=0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf33_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=2.1550000000)
surf33_2 = openmc.Plane(a=-0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf33_3 = openmc.Plane(a=-0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
surf33_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=2.1550000000)
surf33_5 = openmc.Plane(a=0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
# Unit cell #4
# Prism 34: 6-sided polygon
surf34_0 = openmc.Plane(a=0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf34_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=2.1550000000)
surf34_2 = openmc.Plane(a=-0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf34_3 = openmc.Plane(a=-0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
surf34_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=2.1550000000)
surf34_5 = openmc.Plane(a=0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
# Unit cell #5
# Prism 35: 6-sided polygon
surf35_0 = openmc.Plane(a=0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf35_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=2.1550000000)
surf35_2 = openmc.Plane(a=-0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf35_3 = openmc.Plane(a=-0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
surf35_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=2.1550000000)
surf35_5 = openmc.Plane(a=0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
# Unit cell #6
# Prism 36: 6-sided polygon
surf36_0 = openmc.Plane(a=0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf36_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=2.1550000000)
surf36_2 = openmc.Plane(a=-0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf36_3 = openmc.Plane(a=-0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
surf36_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=2.1550000000)
surf36_5 = openmc.Plane(a=0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
# Unit cell #7
# Prism 37: 6-sided polygon
surf37_0 = openmc.Plane(a=0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf37_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=2.1550000000)
surf37_2 = openmc.Plane(a=-0.8660253742, b=0.5000000512, c=0, d=2.1550002207)
surf37_3 = openmc.Plane(a=-0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)
surf37_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=2.1550000000)
surf37_5 = openmc.Plane(a=0.8660253742, b=-0.5000000512, c=0, d=2.1550002207)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1037, z0=-0.3)
surf3_zmax = openmc.ZPlane(surface_id=1038, z0=80.7)
surf4_zmin = openmc.ZPlane(surface_id=1039, z0=-25.9)
surf4_zmax = openmc.ZPlane(surface_id=1040, z0=62.8)
surf6_zmin = openmc.ZPlane(surface_id=1041, z0=-26.3, boundary_type="vacuum")
surf6_zmax = openmc.ZPlane(surface_id=1042, z0=85.7, boundary_type="vacuum")
surf10_zmin = openmc.ZPlane(surface_id=1043, z0=1.2)
surf10_zmax = openmc.ZPlane(surface_id=1044, z0=82.2)
surf11_zmin = openmc.ZPlane(surface_id=1045, z0=1.2)
surf11_zmax = openmc.ZPlane(surface_id=1046, z0=1.38)
surf13_zmin = openmc.ZPlane(surface_id=1047, z0=81.8)
surf13_zmax = openmc.ZPlane(surface_id=1048, z0=82.2)
surf15_zmin = openmc.ZPlane(surface_id=1049, z0=1.38)
surf15_zmax = openmc.ZPlane(surface_id=1050, z0=81.8)
surf19_zmin = openmc.ZPlane(surface_id=1051, z0=2.5)
surf19_zmax = openmc.ZPlane(surface_id=1052, z0=2.7)
surf20_zmin = openmc.ZPlane(surface_id=1053, z0=59.3)
surf20_zmax = openmc.ZPlane(surface_id=1054, z0=59.5)
surf21_zmin = openmc.ZPlane(surface_id=1055, z0=2.5)
surf21_zmax = openmc.ZPlane(surface_id=1056, z0=2.556)
surf22_zmin = openmc.ZPlane(surface_id=1057, z0=59.444)
surf22_zmax = openmc.ZPlane(surface_id=1058, z0=59.5)
surf24_zmin = openmc.ZPlane(surface_id=1059, z0=1.5)
surf24_zmax = openmc.ZPlane(surface_id=1060, z0=61.5)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = +surf1 & -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = -surf1 & +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = +surf1 & +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell5 = openmc.Cell(fill=mat2)
u1_cell5.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf1 & -surf14 & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell1 = openmc.Cell(fill=mat4)
u2_cell1.region = +surf1 & -surf14 & (-surf15 & +surf15_zmin & -surf15_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1])

u3_cell0 = openmc.Cell(fill=mat1)
u3_cell0.region = -surf1 & -surf23 & (-surf24 & +surf24_zmin & -surf24_zmax) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5)
u3_cell1 = openmc.Cell(fill=mat6)
u3_cell1.region = +surf23 & (-surf24 & +surf24_zmin & -surf24_zmax) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5)
u3_cell2 = openmc.Cell(fill=mat1)
u3_cell2.region = -surf1 & (+surf24 | -surf24_zmin | +surf24_zmax) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & (+surf19 | -surf19_zmin | +surf19_zmax) & (+surf20 | -surf20_zmin | +surf20_zmax)
u3_cell3 = openmc.Cell(fill=mat5)
u3_cell3.region = (+surf24 | -surf24_zmin | +surf24_zmax) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & (-surf19 & +surf19_zmin & -surf19_zmax)
u3_cell4 = openmc.Cell(fill=mat5)
u3_cell4.region = (+surf24 | -surf24_zmin | +surf24_zmax) & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & (-surf20 & +surf20_zmin & -surf20_zmax)
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4])

u4_cell0 = openmc.Cell(fill=mat2)
u4_cell0.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf11 & +surf11_zmin & -surf11_zmax) & +surf16 & +surf17 & +surf18
u4_cell1 = openmc.Cell(fill=mat5)
u4_cell1.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf21 & +surf21_zmin & -surf21_zmax) & +surf16 & +surf17 & +surf18 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5) & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5) & (+surf34_0 | +surf34_1 | +surf34_2 | +surf34_3 | +surf34_4 | +surf34_5) & (+surf35_0 | +surf35_1 | +surf35_2 | +surf35_3 | +surf35_4 | +surf35_5) & (+surf36_0 | +surf36_1 | +surf36_2 | +surf36_3 | +surf36_4 | +surf36_5) & (+surf37_0 | +surf37_1 | +surf37_2 | +surf37_3 | +surf37_4 | +surf37_5)
u4_cell2 = openmc.Cell(fill=mat5)
u4_cell2.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf22 & +surf22_zmin & -surf22_zmax) & +surf16 & +surf17 & +surf18 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5) & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5) & (+surf34_0 | +surf34_1 | +surf34_2 | +surf34_3 | +surf34_4 | +surf34_5) & (+surf35_0 | +surf35_1 | +surf35_2 | +surf35_3 | +surf35_4 | +surf35_5) & (+surf36_0 | +surf36_1 | +surf36_2 | +surf36_3 | +surf36_4 | +surf36_5) & (+surf37_0 | +surf37_1 | +surf37_2 | +surf37_3 | +surf37_4 | +surf37_5)
u4_cell3 = openmc.Cell(fill=mat2)
u4_cell3.region = (-surf10 & +surf10_zmin & -surf10_zmax) & +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax) & +surf16 & +surf17 & +surf18
u4_cell4 = openmc.Cell(fill=mat1)
u4_cell4.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & +surf16 & +surf17 & +surf18 & (+surf21 | -surf21_zmin | +surf21_zmax) & (+surf22 | -surf22_zmin | +surf22_zmax)
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# inside
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = (-surf10 & +surf10_zmin & -surf10_zmax)

# outside
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.region = (-surf6 & +surf6_zmin & -surf6_zmax) & (+surf10 | -surf10_zmin | +surf10_zmax)

# Air
cell15 = openmc.Cell(cell_id=15, fill=mat4)
cell15.region = +surf1 & -surf14 & (-surf15 & +surf15_zmin & -surf15_zmax)

# Air
cell23 = openmc.Cell(cell_id=23, fill=mat4)
cell23.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell15, cell23])
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
source.space = openmc.stats.Box((-3.155, -3.488, 10.915), (3.155, 3.488, 12.915))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
