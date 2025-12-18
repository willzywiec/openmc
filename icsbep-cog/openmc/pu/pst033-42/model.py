"""
PU-SOL-THERM-033-42: 99.05 gPu(3.13)/L at H/X=250.4 with 7 (4x60) pyrex tubes at 4.31cm pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 7.283400e-11)
mat1.add_nuclide("U238", 1.020100e-08)
mat1.add_nuclide("Pu239", 2.413700e-04)
mat1.add_nuclide("Pu240", 7.788900e-06)
mat1.add_nuclide("Pu241", 2.969400e-07)
mat1.add_nuclide("Pu242", 2.957100e-08)
mat1.add_nuclide("Am241", 3.464300e-08)
mat1.add_nuclide("H1", 6.052100e-02)
mat1.add_nuclide("O16", 3.706200e-02)
mat1.add_element("N", 2.519100e-03)
mat1.add_element("Fe", 1.466500e-06)
mat1.add_element("Cr", 1.720800e-07)
mat1.add_element("Ni", 2.032700e-07)
mat1.add_element("Mn", 6.514500e-08)
mat1.add_element("Ca", 8.929900e-07)
mat1.add_element("Cu", 1.220300e-07)
mat1.add_element("Mg", 4.908400e-07)
mat1.add_element("Zn", 1.368300e-07)
mat1.add_element("Na", 6.486300e-07)
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
surf1 = openmc.ZPlane(surface_id=1, z0=26.80)
# SST solution tank, inner
# surf2: Unsupported surface type "rev" with params ['3', '0.0', '0.0', '0.6', '17.98', '80.7', '17.98']
# SST solution  tank, outer
surf3 = openmc.ZCylinder(surface_id=3, x0=-0.3, y0=80.7, r=18.28)
# SST reflector tank, inner
surf4 = openmc.ZCylinder(surface_id=4, x0=-25.9, y0=62.8, r=54.6)
# SST refelctor tank, top
surf5 = openmc.ZPlane(surface_id=5, z0=63.2)
# SST reflector tank, outer, and BCD
surf6 = openmc.ZCylinder(surface_id=6, x0=-26.3, y0=85.7, r=55.0, boundary_type="vacuum")
# Basket outer boundary
surf10 = openmc.ZCylinder(surface_id=10, x0=1.2, y0=82.2, r=17.8)
# SST bottom plate
surf11 = openmc.ZCylinder(surface_id=11, x0=1.2, y0=1.38, r=17.5)
# SST annular top plate, inner
surf12 = openmc.ZCylinder(surface_id=12, r=13.75)
# SST annular top plate, outer
surf13 = openmc.ZCylinder(surface_id=13, x0=81.8, y0=82.2, r=17.8)
# Tie rod, inner
surf14 = openmc.ZCylinder(surface_id=14, r=0.3)
# Tie rod, outer
surf15 = openmc.ZCylinder(surface_id=15, x0=1.38, y0=81.8, r=0.4)
# Tie rod #1
# surf16: Error converting surface type "c": could not convert string to float: 'tr'
# Tie rod #2
# surf17: Error converting surface type "c": could not convert string to float: 'tr'
# Tie rod #3
# surf18: Error converting surface type "c": could not convert string to float: 'tr'
# Lower polyethylene grid plate, inner region
surf19 = openmc.ZCylinder(surface_id=19, x0=2.5, y0=2.7, r=17.5)
# Upper polyethylene grid plate, inner region
surf20 = openmc.ZCylinder(surface_id=20, x0=59.3, y0=59.5, r=17.5)
# Lower polyethylene grid plate, outer region
surf21 = openmc.ZCylinder(surface_id=21, x0=2.5, y0=2.556, r=17.5)
# Upper polyethylene grid plate, outer region
surf22 = openmc.ZCylinder(surface_id=22, x0=59.444, y0=59.5, r=17.5)
# 4x60 pyrex tube, inner
surf23 = openmc.ZCylinder(surface_id=23, r=1.7415)
# 4x60 pyrex tube, outer
surf24 = openmc.ZCylinder(surface_id=24, x0=1.5, y0=61.5, r=2.0085)
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

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf2 & -surf3
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = +surf1 & -surf2 & -surf3
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf2 & -surf3
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = -surf1 & +surf2 & +surf3 & -surf4
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = +surf1 & +surf2 & +surf3 & -surf4
u1_cell5 = openmc.Cell(fill=mat2)
u1_cell5.region = +surf2 & +surf3 & +surf4 & -surf5 & -surf6
u1_cell6 = openmc.Cell(fill=mat4)
u1_cell6.region = +surf2 & +surf3 & +surf4 & +surf5 & -surf6
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf1 & -surf14 & -surf15
u2_cell1 = openmc.Cell(fill=mat4)
u2_cell1.region = +surf1 & -surf14 & -surf15
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1])

u3_cell0 = openmc.Cell(fill=mat1)
u3_cell0.region = -surf1 & -surf23 & -surf24 & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5)
u3_cell1 = openmc.Cell(fill=mat6)
u3_cell1.region = +surf23 & -surf24 & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5)
u3_cell2 = openmc.Cell(fill=mat1)
u3_cell2.region = -surf1 & +surf24 & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & +surf19 & +surf20
u3_cell3 = openmc.Cell(fill=mat5)
u3_cell3.region = +surf24 & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf19
u3_cell4 = openmc.Cell(fill=mat5)
u3_cell4.region = +surf24 & (-surf31_0 & -surf31_1 & -surf31_2 & -surf31_3 & -surf31_4 & -surf31_5) & -surf20
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4])

u4_cell0 = openmc.Cell(fill=mat2)
u4_cell0.region = -surf10 & -surf11 & +surf16 & +surf17 & +surf18
u4_cell1 = openmc.Cell(fill=mat5)
u4_cell1.region = -surf10 & -surf21 & +surf16 & +surf17 & +surf18 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5) & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5) & (+surf34_0 | +surf34_1 | +surf34_2 | +surf34_3 | +surf34_4 | +surf34_5) & (+surf35_0 | +surf35_1 | +surf35_2 | +surf35_3 | +surf35_4 | +surf35_5) & (+surf36_0 | +surf36_1 | +surf36_2 | +surf36_3 | +surf36_4 | +surf36_5) & (+surf37_0 | +surf37_1 | +surf37_2 | +surf37_3 | +surf37_4 | +surf37_5)
u4_cell2 = openmc.Cell(fill=mat5)
u4_cell2.region = -surf10 & -surf22 & +surf16 & +surf17 & +surf18 & (+surf31_0 | +surf31_1 | +surf31_2 | +surf31_3 | +surf31_4 | +surf31_5) & (+surf32_0 | +surf32_1 | +surf32_2 | +surf32_3 | +surf32_4 | +surf32_5) & (+surf33_0 | +surf33_1 | +surf33_2 | +surf33_3 | +surf33_4 | +surf33_5) & (+surf34_0 | +surf34_1 | +surf34_2 | +surf34_3 | +surf34_4 | +surf34_5) & (+surf35_0 | +surf35_1 | +surf35_2 | +surf35_3 | +surf35_4 | +surf35_5) & (+surf36_0 | +surf36_1 | +surf36_2 | +surf36_3 | +surf36_4 | +surf36_5) & (+surf37_0 | +surf37_1 | +surf37_2 | +surf37_3 | +surf37_4 | +surf37_5)
u4_cell3 = openmc.Cell(fill=mat2)
u4_cell3.region = -surf10 & +surf12 & -surf13 & +surf16 & +surf17 & +surf18
u4_cell4 = openmc.Cell(fill=mat1)
u4_cell4.region = -surf10 & +surf11 & +surf16 & +surf17 & +surf18 & +surf21 & +surf22
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# inside
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = -surf10

# outside
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.region = -surf6 & +surf10

# Air
cell15 = openmc.Cell(cell_id=15, fill=mat4)
cell15.region = +surf1 & -surf14 & -surf15

# Air
cell23 = openmc.Cell(cell_id=23, fill=mat4)
cell23.region = +surf2 & +surf3 & +surf4 & +surf5 & -surf6

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
source.space = openmc.stats.Box((-3.155, -3.488, 12.4), (3.155, 3.488, 14.4))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
