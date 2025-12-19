"""
LMT001-1: RB Reactor: Natural Uranium Rods in Heavy Water
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Natural
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 2.589100e-06)
mat1.add_nuclide("U235", 3.389400e-04)
mat1.add_nuclide("U238", 4.673400e-02)
mat1.add_nuclide("B10", 4.313100e-08)
mat1.add_nuclide("B11", 1.736100e-07)
mat1.add_element("C", 5.020400e-04)
mat1.add_element("N", 4.125700e-05)
mat1.add_element("Si", 2.177000e-05)
mat1.add_element("Mn", 1.991700e-06)
mat1.add_element("Fe", 1.580000e-05)
mat1.add_element("Ni", 2.007000e-06)
mat1.add_element("Cu", 1.996100e-06)

# SAV-1
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.991600e-02)
mat2.add_nuclide("B10", 2.117600e-08)
mat2.add_nuclide("B11", 8.523500e-08)
mat2.add_element("Mg", 3.786600e-04)
mat2.add_element("Si", 4.973800e-04)
mat2.add_element("Ti", 2.745900e-06)
mat2.add_element("Mn", 6.581100e-07)
mat2.add_element("Fe", 5.885500e-05)
mat2.add_element("Ni", 4.200300e-07)
mat2.add_element("Cu", 1.189700e-06)
mat2.add_element("Cd", 2.924000e-09)
mat2.add_element("Zn", 1.256600e-06)

# Heavy Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 1.196100e-04)
mat3.add_nuclide("H2", 6.633100e-02)
mat3.add_nuclide("O16", 3.322600e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")
mat3.add_s_alpha_beta("c_D_in_D2O")

# Air
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 8.015400e-09)
mat4.add_element("N", 3.912200e-05)
mat4.add_nuclide("O16", 1.051000e-05)
mat4.add_element("Ar", 2.350600e-07)

# Yu_Al
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 5.507800e-02)
mat5.add_nuclide("B10", 4.814800e-06)
mat5.add_nuclide("B11", 1.938000e-05)
mat5.add_element("Mg", 4.304800e-05)
mat5.add_element("Si", 3.193100e-05)
mat5.add_element("Ti", 9.365200e-06)
mat5.add_element("Cr", 1.149800e-05)
mat5.add_element("Mn", 2.720700e-05)
mat5.add_element("Fe", 5.352800e-05)
mat5.add_element("Ni", 5.093500e-06)
mat5.add_element("Cu", 4.704300e-06)
mat5.add_element("Cd", 1.329700e-06)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# U (fuel)
surf1 = openmc.ZCylinder(surface_id=1, r=1.25)
# SAV-1 (clad)
surf2 = openmc.ZCylinder(surface_id=2, r=1.35)
# Yu-Al (upper grid plate)
surf3 = openmc.ZCylinder(surface_id=3, r=999.9)
# Yu-Al (tank/inner)
surf4 = openmc.ZCylinder(surface_id=4, r=100.0)
# Yu-Al (tank/outer)
surf5 = openmc.ZCylinder(surface_id=5, r=101.0, boundary_type="vacuum")
# D2O (Hc)
surf6 = openmc.ZPlane(surface_id=6, z0=177.6)
surf101 = openmc.XPlane(surface_id=101, x0=-108.)
surf102 = openmc.XPlane(surface_id=102, x0=-96.)
surf103 = openmc.XPlane(surface_id=103, x0=-84.)
surf104 = openmc.XPlane(surface_id=104, x0=-72.)
surf105 = openmc.XPlane(surface_id=105, x0=-60.)
surf106 = openmc.XPlane(surface_id=106, x0=-48.)
surf107 = openmc.XPlane(surface_id=107, x0=-36.)
surf108 = openmc.XPlane(surface_id=108, x0=-24.)
surf109 = openmc.XPlane(surface_id=109, x0=-12.)
surf110 = openmc.XPlane(surface_id=110, x0=0.)
surf111 = openmc.XPlane(surface_id=111, x0=12.)
surf112 = openmc.XPlane(surface_id=112, x0=24.)
surf113 = openmc.XPlane(surface_id=113, x0=36.)
surf114 = openmc.XPlane(surface_id=114, x0=48.)
surf115 = openmc.XPlane(surface_id=115, x0=60.)
surf116 = openmc.XPlane(surface_id=116, x0=72.)
surf117 = openmc.XPlane(surface_id=117, x0=84.)
surf118 = openmc.XPlane(surface_id=118, x0=96.)
surf119 = openmc.XPlane(surface_id=119, x0=108.)
surf201 = openmc.YPlane(surface_id=201, y0=-108.)
surf202 = openmc.YPlane(surface_id=202, y0=-96.)
surf203 = openmc.YPlane(surface_id=203, y0=-84.)
surf204 = openmc.YPlane(surface_id=204, y0=-72.)
surf205 = openmc.YPlane(surface_id=205, y0=-60.)
surf206 = openmc.YPlane(surface_id=206, y0=-48.)
surf207 = openmc.YPlane(surface_id=207, y0=-36.)
surf208 = openmc.YPlane(surface_id=208, y0=-24.)
surf209 = openmc.YPlane(surface_id=209, y0=-12.)
surf210 = openmc.YPlane(surface_id=210, y0=0.)
surf211 = openmc.YPlane(surface_id=211, y0=12.)
surf212 = openmc.YPlane(surface_id=212, y0=24.)
surf213 = openmc.YPlane(surface_id=213, y0=36.)
surf214 = openmc.YPlane(surface_id=214, y0=48.)
surf215 = openmc.YPlane(surface_id=215, y0=60.)
surf216 = openmc.YPlane(surface_id=216, y0=72.)
surf217 = openmc.YPlane(surface_id=217, y0=84.)
surf218 = openmc.YPlane(surface_id=218, y0=96.)
surf219 = openmc.YPlane(surface_id=219, y0=108.)
surf301 = openmc.ZPlane(surface_id=301, z0=-999.0)
surf302 = openmc.ZPlane(surface_id=302, z0=999.0)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1302, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1303, z0=210.0)
surf2_zmin = openmc.ZPlane(surface_id=1304, z0=0.0)
surf2_zmax = openmc.ZPlane(surface_id=1305, z0=220.0)
surf3_zmin = openmc.ZPlane(surface_id=1306, z0=210.0)
surf3_zmax = openmc.ZPlane(surface_id=1307, z0=211.0)
surf4_zmin = openmc.ZPlane(surface_id=1308, z0=0.0)
surf4_zmax = openmc.ZPlane(surface_id=1309, z0=229.0)
surf5_zmin = openmc.ZPlane(surface_id=1310, z0=-4.0, boundary_type="vacuum")
surf5_zmax = openmc.ZPlane(surface_id=1311, z0=231.5, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell2 = openmc.Cell(fill=mat5)
u1_cell2.region = (-surf3 & +surf3_zmin & -surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & -surf6
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = (-surf3 & +surf3_zmin & -surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = (-surf4 & +surf4_zmin & -surf4_zmax) & -surf6
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1])

universe3 = openmc.Universe(universe_id=3, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# iTank
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = (-surf4 & +surf4_zmin & -surf4_zmax)

# oTank
cell2 = openmc.Cell(cell_id=2, fill=mat5)
cell2.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# unit2
cell9 = openmc.Cell(cell_id=9, fill=universe2)
cell9.translation = (102.0, -102.0, 0.0)
cell9.region = +surf118 & -surf119 & +surf201 & -surf202 & +surf301 & -surf302

root_universe = openmc.Universe(cells=[cell1, cell2, cell9])
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
source.space = openmc.stats.Box((-7.0, -7.0, 87.8), (7.0, 7.0, 89.8))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
