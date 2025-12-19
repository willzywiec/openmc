"""
MIX-COMP-THERM-002-3: PNL-32
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# PuO2-UO2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 3.883600e-08)
mat1.add_nuclide("Pu239", 3.946200e-04)
mat1.add_nuclide("Pu240", 3.320600e-05)
mat1.add_nuclide("Pu241", 1.608100e-06)
mat1.add_nuclide("Pu242", 1.188200e-07)
mat1.add_nuclide("Am241", 1.495400e-06)
mat1.add_nuclide("U234", 1.245800e-06)
mat1.add_nuclide("U235", 1.488600e-04)
mat1.add_nuclide("U236", 2.093600e-09)
mat1.add_nuclide("U238", 2.061100e-02)
mat1.add_nuclide("O16", 4.377900e-02)

# Natural UO2 @ 9.286 g/cc
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 1.240600e-06)
mat2.add_nuclide("U235", 1.482400e-04)
mat2.add_nuclide("U236", 2.084800e-09)
mat2.add_nuclide("U238", 2.052500e-02)
mat2.add_nuclide("O16", 4.194300e-02)

# Clad and plugs
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Sn", 4.832800e-04)
mat3.add_element("Fe", 9.564200e-05)
mat3.add_element("Cr", 7.609300e-05)
mat3.add_element("Ni", 3.033600e-05)
mat3.add_element("Zr", 4.262100e-02)

# Borated water for PNL-32
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.670600e-02)
mat4.add_nuclide("O16", 3.335300e-02)
mat4.add_nuclide("B10", 9.903400e-09)
mat4.add_nuclide("B11", 4.011400e-08)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Al-6061 eggcrate and
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Si", 3.460700e-04)
mat5.add_element("Fe", 1.015200e-04)
mat5.add_element("Cu", 6.373100e-05)
mat5.add_element("Mn", 2.211500e-05)
mat5.add_element("Mg", 6.665100e-04)
mat5.add_element("Cr", 6.231000e-05)
mat5.add_element("Zn", 3.096700e-05)
mat5.add_element("Ti", 2.537500e-05)
mat5.add_element("Al", 5.843300e-02)

# Lead shield
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Pb", 3.217400e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZCylinder(surface_id=1, r=0.64135)
surf2 = openmc.ZCylinder(surface_id=2, r=0.71755)
# Eggcrate inner
surf3 = openmc.model.RectangularParallelepiped(-0.74041, 0.74041, -0.74041, 0.74041, -499.95, 499.95)
surf4 = openmc.ZPlane(surface_id=4, z0=30.0)
surf5 = openmc.ZPlane(surface_id=5, z0=32.8575)
surf6 = openmc.ZPlane(surface_id=6, z0=33.1750)
surf7 = openmc.ZPlane(surface_id=7, z0=33.5560)
surf8 = openmc.ZPlane(surface_id=8, z0=34.0560)
surf9 = openmc.ZPlane(surface_id=9, z0=35.7150)
surf10 = openmc.ZPlane(surface_id=10, z0=122.3925)
surf11 = openmc.ZPlane(surface_id=11, z0=124.9325)
surf12 = openmc.ZPlane(surface_id=12, z0=124.9960)
surf13 = openmc.ZPlane(surface_id=13, z0=125.8215)
surf14 = openmc.ZPlane(surface_id=14, z0=126.7740)
# Arbitrary big box for unit cell bcd
surf15 = openmc.model.RectangularParallelepiped(-4.95, 4.95, -4.95, 4.95, -499.95, 499.95)
surf90 = openmc.ZCylinder(surface_id=90, r=60.0, boundary_type="vacuum")
surf101 = openmc.XPlane(surface_id=101, x0=-62.96049)
surf102 = openmc.XPlane(surface_id=102, x0=-60.75135)
surf103 = openmc.XPlane(surface_id=103, x0=-58.54221)
surf104 = openmc.XPlane(surface_id=104, x0=-56.33307)
surf105 = openmc.XPlane(surface_id=105, x0=-54.12393)
surf106 = openmc.XPlane(surface_id=106, x0=-51.91479)
surf107 = openmc.XPlane(surface_id=107, x0=-49.70565)
surf108 = openmc.XPlane(surface_id=108, x0=-47.49651)
surf109 = openmc.XPlane(surface_id=109, x0=-45.28737)
surf110 = openmc.XPlane(surface_id=110, x0=-43.07823)
surf111 = openmc.XPlane(surface_id=111, x0=-40.86909)
surf112 = openmc.XPlane(surface_id=112, x0=-38.65995)
surf113 = openmc.XPlane(surface_id=113, x0=-36.45081)
surf114 = openmc.XPlane(surface_id=114, x0=-34.24167)
surf115 = openmc.XPlane(surface_id=115, x0=-32.03253)
surf116 = openmc.XPlane(surface_id=116, x0=-29.82339)
surf117 = openmc.XPlane(surface_id=117, x0=-27.61425)
surf118 = openmc.XPlane(surface_id=118, x0=-25.40511)
surf119 = openmc.XPlane(surface_id=119, x0=-23.19597)
surf120 = openmc.XPlane(surface_id=120, x0=-20.98683)
surf121 = openmc.XPlane(surface_id=121, x0=-18.77769)
surf122 = openmc.XPlane(surface_id=122, x0=-16.56855)
surf123 = openmc.XPlane(surface_id=123, x0=-14.35941)
surf124 = openmc.XPlane(surface_id=124, x0=-12.15027)
surf125 = openmc.XPlane(surface_id=125, x0=-9.94113)
surf126 = openmc.XPlane(surface_id=126, x0=-7.73199)
surf127 = openmc.XPlane(surface_id=127, x0=-5.52285)
surf128 = openmc.XPlane(surface_id=128, x0=-3.31371)
surf129 = openmc.XPlane(surface_id=129, x0=-1.10457)
surf130 = openmc.XPlane(surface_id=130, x0=1.10457)
surf131 = openmc.XPlane(surface_id=131, x0=3.31371)
surf132 = openmc.XPlane(surface_id=132, x0=5.52285)
surf133 = openmc.XPlane(surface_id=133, x0=7.73199)
surf134 = openmc.XPlane(surface_id=134, x0=9.94113)
surf135 = openmc.XPlane(surface_id=135, x0=12.15027)
surf136 = openmc.XPlane(surface_id=136, x0=14.35941)
surf137 = openmc.XPlane(surface_id=137, x0=16.56855)
surf138 = openmc.XPlane(surface_id=138, x0=18.77769)
surf139 = openmc.XPlane(surface_id=139, x0=20.98683)
surf140 = openmc.XPlane(surface_id=140, x0=23.19597)
surf141 = openmc.XPlane(surface_id=141, x0=25.40511)
surf142 = openmc.XPlane(surface_id=142, x0=27.61425)
surf143 = openmc.XPlane(surface_id=143, x0=29.82339)
surf144 = openmc.XPlane(surface_id=144, x0=32.03253)
surf145 = openmc.XPlane(surface_id=145, x0=34.24167)
surf146 = openmc.XPlane(surface_id=146, x0=36.45081)
surf147 = openmc.XPlane(surface_id=147, x0=38.65995)
surf148 = openmc.XPlane(surface_id=148, x0=40.86909)
surf149 = openmc.XPlane(surface_id=149, x0=43.07823)
surf150 = openmc.XPlane(surface_id=150, x0=45.28737)
surf151 = openmc.XPlane(surface_id=151, x0=47.49651)
surf152 = openmc.XPlane(surface_id=152, x0=49.70565)
surf153 = openmc.XPlane(surface_id=153, x0=51.91479)
surf154 = openmc.XPlane(surface_id=154, x0=54.12393)
surf155 = openmc.XPlane(surface_id=155, x0=56.33307)
surf156 = openmc.XPlane(surface_id=156, x0=58.54221)
surf157 = openmc.XPlane(surface_id=157, x0=60.75135)
surf158 = openmc.XPlane(surface_id=158, x0=62.96049)
surf201 = openmc.YPlane(surface_id=201, y0=-62.96049)
surf202 = openmc.YPlane(surface_id=202, y0=-60.75135)
surf203 = openmc.YPlane(surface_id=203, y0=-58.54221)
surf204 = openmc.YPlane(surface_id=204, y0=-56.33307)
surf205 = openmc.YPlane(surface_id=205, y0=-54.12393)
surf206 = openmc.YPlane(surface_id=206, y0=-51.91479)
surf207 = openmc.YPlane(surface_id=207, y0=-49.70565)
surf208 = openmc.YPlane(surface_id=208, y0=-47.49651)
surf209 = openmc.YPlane(surface_id=209, y0=-45.28737)
surf210 = openmc.YPlane(surface_id=210, y0=-43.07823)
surf211 = openmc.YPlane(surface_id=211, y0=-40.86909)
surf212 = openmc.YPlane(surface_id=212, y0=-38.65995)
surf213 = openmc.YPlane(surface_id=213, y0=-36.45081)
surf214 = openmc.YPlane(surface_id=214, y0=-34.24167)
surf215 = openmc.YPlane(surface_id=215, y0=-32.03253)
surf216 = openmc.YPlane(surface_id=216, y0=-29.82339)
surf217 = openmc.YPlane(surface_id=217, y0=-27.61425)
surf218 = openmc.YPlane(surface_id=218, y0=-25.40511)
surf219 = openmc.YPlane(surface_id=219, y0=-23.19597)
surf220 = openmc.YPlane(surface_id=220, y0=-20.98683)
surf221 = openmc.YPlane(surface_id=221, y0=-18.77769)
surf222 = openmc.YPlane(surface_id=222, y0=-16.56855)
surf223 = openmc.YPlane(surface_id=223, y0=-14.35941)
surf224 = openmc.YPlane(surface_id=224, y0=-12.15027)
surf225 = openmc.YPlane(surface_id=225, y0=-9.94113)
surf226 = openmc.YPlane(surface_id=226, y0=-7.73199)
surf227 = openmc.YPlane(surface_id=227, y0=-5.52285)
surf228 = openmc.YPlane(surface_id=228, y0=-3.31371)
surf229 = openmc.YPlane(surface_id=229, y0=-1.10457)
surf230 = openmc.YPlane(surface_id=230, y0=1.10457)
surf231 = openmc.YPlane(surface_id=231, y0=3.31371)
surf232 = openmc.YPlane(surface_id=232, y0=5.52285)
surf233 = openmc.YPlane(surface_id=233, y0=7.73199)
surf234 = openmc.YPlane(surface_id=234, y0=9.94113)
surf235 = openmc.YPlane(surface_id=235, y0=12.15027)
surf236 = openmc.YPlane(surface_id=236, y0=14.35941)
surf237 = openmc.YPlane(surface_id=237, y0=16.56855)
surf238 = openmc.YPlane(surface_id=238, y0=18.77769)
surf239 = openmc.YPlane(surface_id=239, y0=20.98683)
surf240 = openmc.YPlane(surface_id=240, y0=23.19597)
surf241 = openmc.YPlane(surface_id=241, y0=25.40511)
surf242 = openmc.YPlane(surface_id=242, y0=27.61425)
surf243 = openmc.YPlane(surface_id=243, y0=29.82339)
surf244 = openmc.YPlane(surface_id=244, y0=32.03253)
surf245 = openmc.YPlane(surface_id=245, y0=34.24167)
surf246 = openmc.YPlane(surface_id=246, y0=36.45081)
surf247 = openmc.YPlane(surface_id=247, y0=38.65995)
surf248 = openmc.YPlane(surface_id=248, y0=40.86909)
surf249 = openmc.YPlane(surface_id=249, y0=43.07823)
surf250 = openmc.YPlane(surface_id=250, y0=45.28737)
surf251 = openmc.YPlane(surface_id=251, y0=47.49651)
surf252 = openmc.YPlane(surface_id=252, y0=49.70565)
surf253 = openmc.YPlane(surface_id=253, y0=51.91479)
surf254 = openmc.YPlane(surface_id=254, y0=54.12393)
surf255 = openmc.YPlane(surface_id=255, y0=56.33307)
surf256 = openmc.YPlane(surface_id=256, y0=58.54221)
surf257 = openmc.YPlane(surface_id=257, y0=60.75135)
surf258 = openmc.YPlane(surface_id=258, y0=62.96049)
surf301 = openmc.ZPlane(surface_id=301, z0=-999.0)
surf302 = openmc.ZPlane(surface_id=302, z0=999.0)

# Z-plane surfaces for bounded cylinders
surf90_zmin = openmc.ZPlane(surface_id=1302, z0=0.0, boundary_type="vacuum")
surf90_zmax = openmc.ZPlane(surface_id=1303, z0=132.489, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & +surf8 & -surf12
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = -surf1 & +surf7 & -surf8
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = -surf2 & +surf5 & -surf7
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = +surf1 & -surf2 & +surf7 & -surf12
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = -surf2 & +surf12 & -surf13
u1_cell5 = openmc.Cell(fill=mat5)
u1_cell5.region = +surf4 & -surf5 & -surf15
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = +surf3 & +surf6 & -surf9 & -surf15
u1_cell7 = openmc.Cell(fill=mat5)
u1_cell7.region = +surf3 & +surf10 & -surf11 & -surf15
u1_cell8 = openmc.Cell(fill=mat6)
u1_cell8.region = +surf13 & -surf14 & -surf15
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = +surf4 & -surf5 & -surf15
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = +surf3 & +surf6 & -surf9 & -surf15
u2_cell2 = openmc.Cell(fill=mat5)
u2_cell2.region = +surf3 & +surf10 & -surf11 & -surf15
u2_cell3 = openmc.Cell(fill=mat6)
u2_cell3.region = +surf13 & -surf14 & -surf15
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3])

universe3 = openmc.Universe(universe_id=3, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# PNL32
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = (-surf90 & +surf90_zmin & -surf90_zmax)

# unit2
cell15 = openmc.Cell(cell_id=15, fill=universe2)
cell15.translation = (61.85592, -61.85592, 0.0)
cell15.region = +surf157 & -surf158 & +surf201 & -surf202 & +surf301 & -surf302

root_universe = openmc.Universe(cells=[cell1, cell15])
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
source.space = openmc.stats.Point((0.0, 0.0, 79.526))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
