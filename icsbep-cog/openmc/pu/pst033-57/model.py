"""
PU-SOL-THERM-033-57: 355.6 gPu(3.13)/L at H/X=60.5 with 31 (4x14.78) pyrex tubes at 5.83cm pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 2.614800e-10)
mat1.add_nuclide("U238", 3.662500e-08)
mat1.add_nuclide("Pu239", 8.665500e-04)
mat1.add_nuclide("Pu240", 2.796300e-05)
mat1.add_nuclide("Pu241", 1.066000e-06)
mat1.add_nuclide("Pu242", 1.061600e-07)
mat1.add_nuclide("Am241", 1.243700e-07)
mat1.add_nuclide("H1", 5.246700e-02)
mat1.add_nuclide("O16", 4.074400e-02)
mat1.add_element("N", 5.080500e-03)
mat1.add_element("Fe", 5.305300e-06)
mat1.add_element("Cr", 6.177800e-07)
mat1.add_element("Ni", 7.297500e-07)
mat1.add_element("Mn", 2.338800e-07)
mat1.add_element("Ca", 3.205900e-06)
mat1.add_element("Cu", 4.380900e-07)
mat1.add_element("Mg", 1.762100e-06)
mat1.add_element("Zn", 4.912300e-07)
mat1.add_element("Na", 2.328700e-06)
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
surf1 = openmc.ZPlane(surface_id=1, z0=29.60)
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
# Lower polyethylene grid plate, entire grid
surf19 = openmc.ZCylinder(surface_id=19, r=17.5)
# Upper polyethylene grid plate, entire grid
surf20 = openmc.ZCylinder(surface_id=20, r=17.5)
# 4x14.78 pyrex tube, inner
surf23 = openmc.ZCylinder(surface_id=23, r=1.7442)
# 4x14.78 pyrex tube, outer
surf24 = openmc.ZCylinder(surface_id=24, r=2.0058)
# Pyrex tube #1
surf101 = openmc.ZCylinder(surface_id=101, x0=-2.915, y0=15.146784, r=2.0058)
# Pyrex tube #2
surf102 = openmc.ZCylinder(surface_id=102, x0=2.915, y0=15.146784, r=2.0058)
# Pyrex tube #3
surf103 = openmc.ZCylinder(surface_id=103, x0=-11.66, y0=10.097856, r=2.0058)
# Pyrex tube #4
surf104 = openmc.ZCylinder(surface_id=104, x0=-5.83, y0=10.097856, r=2.0058)
# Pyrex tube #5
surf105 = openmc.ZCylinder(surface_id=105, x0=0.0, y0=10.097856, r=2.0058)
# Pyrex tube #6
surf106 = openmc.ZCylinder(surface_id=106, x0=5.83, y0=10.097856, r=2.0058)
# Pyrex tube #7
surf107 = openmc.ZCylinder(surface_id=107, x0=11.66, y0=10.097856, r=2.0058)
# Pyrex tube #8
surf108 = openmc.ZCylinder(surface_id=108, x0=-14.575, y0=5.048928, r=2.0058)
# Pyrex tube #9
surf109 = openmc.ZCylinder(surface_id=109, x0=-8.745, y0=5.048928, r=2.0058)
# Pyrex tube #10
surf110 = openmc.ZCylinder(surface_id=110, x0=-2.915, y0=5.048928, r=2.0058)
# Pyrex tube #11
surf111 = openmc.ZCylinder(surface_id=111, x0=2.915, y0=5.048928, r=2.0058)
# Pyrex tube #12
surf112 = openmc.ZCylinder(surface_id=112, x0=8.745, y0=5.048928, r=2.0058)
# Pyrex tube #13
surf113 = openmc.ZCylinder(surface_id=113, x0=14.575, y0=5.048928, r=2.0058)
# Pyrex tube #14
surf114 = openmc.ZCylinder(surface_id=114, x0=-11.66, y0=0.0, r=2.0058)
# Pyrex tube #15
surf115 = openmc.ZCylinder(surface_id=115, x0=-5.83, y0=0.0, r=2.0058)
# Pyrex tube #16
surf116 = openmc.ZCylinder(surface_id=116, x0=0.0, y0=0.0, r=2.0058)
# Pyrex tube #17
surf117 = openmc.ZCylinder(surface_id=117, x0=5.83, y0=0.0, r=2.0058)
# Pyrex tube #18
surf118 = openmc.ZCylinder(surface_id=118, x0=11.66, y0=0.0, r=2.0058)
# Pyrex tube #19
surf119 = openmc.ZCylinder(surface_id=119, x0=-14.575, y0=-5.048928, r=2.0058)
# Pyrex tube #20
surf120 = openmc.ZCylinder(surface_id=120, x0=-8.745, y0=-5.048928, r=2.0058)
# Pyrex tube #21
surf121 = openmc.ZCylinder(surface_id=121, x0=-2.915, y0=-5.048928, r=2.0058)
# Pyrex tube #22
surf122 = openmc.ZCylinder(surface_id=122, x0=2.915, y0=-5.048928, r=2.0058)
# Pyrex tube #23
surf123 = openmc.ZCylinder(surface_id=123, x0=8.745, y0=-5.048928, r=2.0058)
# Pyrex tube #24
surf124 = openmc.ZCylinder(surface_id=124, x0=14.575, y0=-5.048928, r=2.0058)
# Pyrex tube #25
surf125 = openmc.ZCylinder(surface_id=125, x0=-11.66, y0=-10.097856, r=2.0058)
# Pyrex tube
surf126 = openmc.ZCylinder(surface_id=126, x0=-5.83, y0=-10.097856, r=2.0058)
# Pyrex tube #27
surf127 = openmc.ZCylinder(surface_id=127, x0=0.0, y0=-10.097856, r=2.0058)
# Pyrex tube #28
surf128 = openmc.ZCylinder(surface_id=128, x0=5.83, y0=-10.097856, r=2.0058)
# Pyrex tube #29
surf129 = openmc.ZCylinder(surface_id=129, x0=11.66, y0=-10.097856, r=2.0058)
# Pyrex tube #30
surf130 = openmc.ZCylinder(surface_id=130, x0=-2.915, y0=-15.146784, r=2.0058)
# Pyrex tube #31
surf131 = openmc.ZCylinder(surface_id=131, x0=2.915, y0=-15.146784, r=2.0058)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1131, z0=-0.3)
surf3_zmax = openmc.ZPlane(surface_id=1132, z0=80.7)
surf4_zmin = openmc.ZPlane(surface_id=1133, z0=-25.9)
surf4_zmax = openmc.ZPlane(surface_id=1134, z0=62.8)
surf6_zmin = openmc.ZPlane(surface_id=1135, z0=-26.3, boundary_type="vacuum")
surf6_zmax = openmc.ZPlane(surface_id=1136, z0=85.7, boundary_type="vacuum")
surf10_zmin = openmc.ZPlane(surface_id=1137, z0=1.2)
surf10_zmax = openmc.ZPlane(surface_id=1138, z0=82.2)
surf11_zmin = openmc.ZPlane(surface_id=1139, z0=1.2)
surf11_zmax = openmc.ZPlane(surface_id=1140, z0=1.38)
surf13_zmin = openmc.ZPlane(surface_id=1141, z0=81.8)
surf13_zmax = openmc.ZPlane(surface_id=1142, z0=82.2)
surf15_zmin = openmc.ZPlane(surface_id=1143, z0=1.38)
surf15_zmax = openmc.ZPlane(surface_id=1144, z0=81.8)
surf19_zmin = openmc.ZPlane(surface_id=1145, z0=2.5)
surf19_zmax = openmc.ZPlane(surface_id=1146, z0=2.637)
surf20_zmin = openmc.ZPlane(surface_id=1147, z0=14.08)
surf20_zmax = openmc.ZPlane(surface_id=1148, z0=14.28)
surf24_zmin = openmc.ZPlane(surface_id=1149, z0=1.5)
surf24_zmax = openmc.ZPlane(surface_id=1150, z0=16.28)

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
u3_cell0.region = -surf1 & -surf23 & (-surf6 & +surf6_zmin & -surf6_zmax)
u3_cell1 = openmc.Cell(fill=mat4)
u3_cell1.region = +surf1 & -surf23 & (-surf6 & +surf6_zmin & -surf6_zmax)
u3_cell2 = openmc.Cell(fill=mat6)
u3_cell2.region = +surf23 & (-surf6 & +surf6_zmin & -surf6_zmax)
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2])

u4_cell0 = openmc.Cell(fill=mat2)
u4_cell0.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf11 & +surf11_zmin & -surf11_zmax) & +surf16 & +surf17 & +surf18
u4_cell1 = openmc.Cell(fill=mat5)
u4_cell1.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf19 & +surf19_zmin & -surf19_zmax) & +surf16 & +surf17 & +surf18 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110 & +surf111 & +surf112 & +surf113 & +surf114 & +surf115 & +surf116 & +surf117 & +surf118 & +surf119 & +surf120
u4_cell2 = openmc.Cell(fill=mat5)
u4_cell2.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf20 & +surf20_zmin & -surf20_zmax) & +surf16 & +surf17 & +surf18 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110 & +surf111 & +surf112 & +surf113 & +surf114 & +surf115 & +surf116 & +surf117 & +surf118 & +surf119 & +surf120
u4_cell3 = openmc.Cell(fill=mat2)
u4_cell3.region = (-surf10 & +surf10_zmin & -surf10_zmax) & +surf12 & (-surf13 & +surf13_zmin & -surf13_zmax) & +surf16 & +surf17 & +surf18
u4_cell4 = openmc.Cell(fill=mat1)
u4_cell4.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & +surf16 & +surf17 & +surf18 & (+surf19 | -surf19_zmin | +surf19_zmax) & (+surf20 | -surf20_zmin | +surf20_zmax) & -surf1 & +surf101 & +surf102 & +surf103 & +surf104 & +surf105 & +surf106 & +surf107 & +surf108 & +surf109 & +surf110 & +surf111 & +surf112 & +surf113 & +surf114 & +surf115 & +surf116 & +surf117 & +surf118 & +surf119 & +surf120
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

# Pyrex
cell11 = openmc.Cell(cell_id=11, fill=mat6)
cell11.region = +surf23 & (-surf6 & +surf6_zmin & -surf6_zmax)

# Air
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = +surf1 & -surf14 & (-surf15 & +surf15_zmin & -surf15_zmax)

# Air
cell22 = openmc.Cell(cell_id=22, fill=mat4)
cell22.region = +surf2 & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & +surf5 & (-surf6 & +surf6_zmin & -surf6_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell11, cell14, cell22])
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
source.space = openmc.stats.Point((0.0, 0.0, 14.8))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
