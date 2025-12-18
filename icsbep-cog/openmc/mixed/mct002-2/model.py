"""
MIX-COMP-THERM-002-2: PNL-31
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

# Borated water for PNL-31
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.668500e-02)
mat4.add_nuclide("O16", 3.340000e-02)
mat4.add_nuclide("B10", 7.583800e-06)
mat4.add_nuclide("B11", 3.071800e-05)
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
surf3 = openmc.model.RectangularParallelepiped(-0.73025, 0.73025, -0.73025, 0.73025, -499.95, 499.95)
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
surf91 = openmc.XPlane(surface_id=91, x0=0.0)
surf92 = openmc.YPlane(surface_id=92, y0=0.0)
surf93 = openmc.ZPlane(surface_id=93, z0=0.0)
surf94 = openmc.ZPlane(surface_id=94, z0=142.0140)
surf101 = openmc.XPlane(surface_id=101, x0=-0.889)
surf102 = openmc.XPlane(surface_id=102, x0=0.889)
surf103 = openmc.XPlane(surface_id=103, x0=2.667)
surf104 = openmc.XPlane(surface_id=104, x0=4.445)
surf105 = openmc.XPlane(surface_id=105, x0=6.223)
surf106 = openmc.XPlane(surface_id=106, x0=8.001)
surf107 = openmc.XPlane(surface_id=107, x0=9.779)
surf108 = openmc.XPlane(surface_id=108, x0=11.557)
surf109 = openmc.XPlane(surface_id=109, x0=13.335)
surf110 = openmc.XPlane(surface_id=110, x0=15.113)
surf111 = openmc.XPlane(surface_id=111, x0=16.891)
surf112 = openmc.XPlane(surface_id=112, x0=18.669)
surf113 = openmc.XPlane(surface_id=113, x0=20.447)
surf114 = openmc.XPlane(surface_id=114, x0=22.225)
surf115 = openmc.XPlane(surface_id=115, x0=24.003)
surf116 = openmc.XPlane(surface_id=116, x0=25.781)
surf117 = openmc.XPlane(surface_id=117, x0=27.559)
surf118 = openmc.XPlane(surface_id=118, x0=29.337)
surf119 = openmc.XPlane(surface_id=119, x0=31.115)
surf120 = openmc.XPlane(surface_id=120, x0=32.893)
surf121 = openmc.XPlane(surface_id=121, x0=34.671)
surf122 = openmc.XPlane(surface_id=122, x0=36.449)
surf123 = openmc.XPlane(surface_id=123, x0=38.227)
surf124 = openmc.XPlane(surface_id=124, x0=40.005)
surf125 = openmc.XPlane(surface_id=125, x0=41.783)
surf126 = openmc.XPlane(surface_id=126, x0=43.561)
surf127 = openmc.XPlane(surface_id=127, x0=45.339)
surf128 = openmc.XPlane(surface_id=128, x0=47.117)
surf129 = openmc.XPlane(surface_id=129, x0=48.895)
surf130 = openmc.XPlane(surface_id=130, x0=50.673)
surf131 = openmc.XPlane(surface_id=131, x0=52.451)
surf132 = openmc.XPlane(surface_id=132, x0=54.229)
surf133 = openmc.XPlane(surface_id=133, x0=56.007)
surf134 = openmc.XPlane(surface_id=134, x0=57.785)
surf135 = openmc.XPlane(surface_id=135, x0=59.563)
surf136 = openmc.XPlane(surface_id=136, x0=61.341)
surf137 = openmc.XPlane(surface_id=137, x0=63.119)
surf151 = openmc.YPlane(surface_id=151, y0=-63.119)
surf152 = openmc.YPlane(surface_id=152, y0=-61.341)
surf153 = openmc.YPlane(surface_id=153, y0=-59.563)
surf154 = openmc.YPlane(surface_id=154, y0=-57.785)
surf155 = openmc.YPlane(surface_id=155, y0=-56.007)
surf156 = openmc.YPlane(surface_id=156, y0=-54.229)
surf157 = openmc.YPlane(surface_id=157, y0=-52.451)
surf158 = openmc.YPlane(surface_id=158, y0=-50.673)
surf159 = openmc.YPlane(surface_id=159, y0=-48.895)
surf160 = openmc.YPlane(surface_id=160, y0=-47.117)
surf161 = openmc.YPlane(surface_id=161, y0=-45.339)
surf162 = openmc.YPlane(surface_id=162, y0=-43.561)
surf163 = openmc.YPlane(surface_id=163, y0=-41.783)
surf164 = openmc.YPlane(surface_id=164, y0=-40.005)
surf165 = openmc.YPlane(surface_id=165, y0=-38.227)
surf166 = openmc.YPlane(surface_id=166, y0=-36.449)
surf167 = openmc.YPlane(surface_id=167, y0=-34.671)
surf168 = openmc.YPlane(surface_id=168, y0=-32.893)
surf169 = openmc.YPlane(surface_id=169, y0=-31.115)
surf170 = openmc.YPlane(surface_id=170, y0=-29.337)
surf171 = openmc.YPlane(surface_id=171, y0=-27.559)
surf172 = openmc.YPlane(surface_id=172, y0=-25.781)
surf173 = openmc.YPlane(surface_id=173, y0=-24.003)
surf174 = openmc.YPlane(surface_id=174, y0=-22.225)
surf175 = openmc.YPlane(surface_id=175, y0=-20.447)
surf176 = openmc.YPlane(surface_id=176, y0=-18.669)
surf177 = openmc.YPlane(surface_id=177, y0=-16.891)
surf178 = openmc.YPlane(surface_id=178, y0=-15.113)
surf179 = openmc.YPlane(surface_id=179, y0=-13.335)
surf180 = openmc.YPlane(surface_id=180, y0=-11.557)
surf181 = openmc.YPlane(surface_id=181, y0=-9.779)
surf182 = openmc.YPlane(surface_id=182, y0=-8.001)
surf183 = openmc.YPlane(surface_id=183, y0=-6.223)
surf184 = openmc.YPlane(surface_id=184, y0=-4.445)
surf185 = openmc.YPlane(surface_id=185, y0=-2.667)
surf186 = openmc.YPlane(surface_id=186, y0=-0.889)
surf187 = openmc.YPlane(surface_id=187, y0=0.889)
surf191 = openmc.ZPlane(surface_id=191, z0=-999.0)
surf192 = openmc.ZPlane(surface_id=192, z0=999.0)

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

# PNL31
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf90 & +surf91 & -surf92 & +surf93 & -surf94

# unit2
cell15 = openmc.Cell(cell_id=15, fill=universe2)
cell15.translation = (62.23, -62.23, 0.0)
cell15.region = +surf136 & -surf137 & +surf151 & -surf152 & +surf191 & -surf192

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
source.space = openmc.stats.Point((0.1, -0.1, 79.526))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
