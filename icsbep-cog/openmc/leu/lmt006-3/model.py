"""
LMT006-3: Case 3; Bugey 26; 46 type 1 and 6 type 2 tubes; 10.2cm pitch; Hw=52.91cm
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(1.6) Metal
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 7.017800e-06)
mat1.add_nuclide("U235", 7.554400e-04)
mat1.add_nuclide("U238", 4.586600e-02)
mat1.add_element("Fe", 5.961400e-05)
mat1.add_element("Al", 2.879100e-04)
mat1.add_element("C", 9.239500e-04)

# Water
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.669200e-02)
mat2.add_nuclide("O16", 3.334600e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

# Steel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 8.508600e-02)
mat3.add_element("C", 5.554500e-04)

# 85% SST and
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 1.000400e-02)
mat4.add_nuclide("O16", 5.001900e-03)
mat4.add_element("Fe", 4.989000e-02)
mat4.add_element("Cr", 1.399900e-02)
mat4.add_element("Ni", 6.890200e-03)
mat4.add_element("Mn", 1.472100e-03)
mat4.add_element("Si", 1.439800e-03)
mat4.add_element("P", 5.222300e-05)
mat4.add_element("S", 3.782800e-05)
mat4.add_element("C", 1.010000e-04)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Air
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("O16", 1.126300e-05)
mat5.add_element("N", 4.198500e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# U-shaped plates/inner
surf1 = openmc.model.RectangularParallelepiped(-4.5, 4.5, -50.0, 50.0, -8.2, -0.6000000000000005)
# U-shaped plates/outer
surf2 = openmc.model.RectangularParallelepiped(-4.7, 4.7, -50.0, 50.0, -8.4, -0.40000000000000036)
# Additional plate w/water in (smeared) holes
surf3 = openmc.model.RectangularParallelepiped(-59.7, 59.7, -50.0, 50.0, -49.95, 49.95)
# Type 1 fuel tube/inner
surf4 = openmc.ZCylinder(surface_id=4, r=3.75)
# Type 1 fuel tube/outer
surf5 = openmc.ZCylinder(surface_id=5, r=4.85)
# Type 1 steel disk
surf6 = openmc.ZCylinder(surface_id=6, r=4.85)
# Beam/inner
surf7 = openmc.model.RectangularParallelepiped(-1.8, 1.8, -499.95, 499.95, 60.7, 64.3)
# Beam/outer
surf8 = openmc.model.RectangularParallelepiped(-2.0, 2.0, -50.0, 50.0, 60.5, 64.5)
# Type 2 fuel tube/inner
surf40 = openmc.ZCylinder(surface_id=40, r=3.85)
# Type 2 fuel tube/outer
surf50 = openmc.ZCylinder(surface_id=50, r=4.75)
# Type 2 steel disk
surf60 = openmc.ZCylinder(surface_id=60, r=4.75)
# Basic fuel tube and disk
surf101 = openmc.ZCylinder(surface_id=101, x0=-40.0, y0=-40.0, r=4.85)
# fuel tube and disk
surf102 = openmc.ZCylinder(surface_id=102, x0=-40.0, y0=-29.8, r=4.85)
# fuel tube and disk
surf103 = openmc.ZCylinder(surface_id=103, x0=-40.0, y0=-19.6, r=4.85)
# fuel tube and disk
surf104 = openmc.ZCylinder(surface_id=104, x0=-40.0, y0=-9.4, r=4.85)
# fuel tube and disk
surf105 = openmc.ZCylinder(surface_id=105, x0=-40.0, y0=0.8, r=4.85)
# fuel tube and disk
surf106 = openmc.ZCylinder(surface_id=106, x0=-40.0, y0=11.0, r=4.85)
# fuel tube and disk
surf107 = openmc.ZCylinder(surface_id=107, x0=-40.0, y0=21.2, r=4.85)
# Second row
surf111 = openmc.ZCylinder(surface_id=111, x0=-31.16654, y0=-34.9, r=4.85)
# ditto
surf112 = openmc.ZCylinder(surface_id=112, x0=-31.16654, y0=-24.7, r=4.85)
# ditto
surf113 = openmc.ZCylinder(surface_id=113, x0=-31.16654, y0=-14.5, r=4.85)
# ditto
surf114 = openmc.ZCylinder(surface_id=114, x0=-31.16654, y0=-4.3, r=4.85)
# ditto
surf115 = openmc.ZCylinder(surface_id=115, x0=-31.16654, y0=5.9, r=4.85)
# ditto
surf116 = openmc.ZCylinder(surface_id=116, x0=-31.16654, y0=16.1, r=4.85)
# Third row
surf121 = openmc.ZCylinder(surface_id=121, x0=-22.33308, y0=-40.0, r=4.85)
# ditto
surf122 = openmc.ZCylinder(surface_id=122, x0=-22.33308, y0=-29.8, r=4.85)
# ditto
surf123 = openmc.ZCylinder(surface_id=123, x0=-22.33308, y0=-19.6, r=4.85)
# ditto
surf124 = openmc.ZCylinder(surface_id=124, x0=-22.33308, y0=-9.4, r=4.85)
# ditto
surf125 = openmc.ZCylinder(surface_id=125, x0=-22.33308, y0=0.8, r=4.85)
# ditto
surf126 = openmc.ZCylinder(surface_id=126, x0=-22.33308, y0=11.0, r=4.85)
# ditto
surf127 = openmc.ZCylinder(surface_id=127, x0=-22.33308, y0=21.2, r=4.85)
# Fourth row
surf131 = openmc.ZCylinder(surface_id=131, x0=-13.49962, y0=-34.9, r=4.85)
# ditto
surf132 = openmc.ZCylinder(surface_id=132, x0=-13.49962, y0=-24.7, r=4.85)
# ditto
surf133 = openmc.ZCylinder(surface_id=133, x0=-13.49962, y0=-14.5, r=4.85)
# ditto
surf134 = openmc.ZCylinder(surface_id=134, x0=-13.49962, y0=-4.3, r=4.85)
# ditto
surf135 = openmc.ZCylinder(surface_id=135, x0=-13.49962, y0=5.9, r=4.85)
# ditto
surf136 = openmc.ZCylinder(surface_id=136, x0=-13.49962, y0=16.1, r=4.85)
# Fifth row
surf141 = openmc.ZCylinder(surface_id=141, x0=-4.66616, y0=-40.0, r=4.85)
# ditto
surf142 = openmc.ZCylinder(surface_id=142, x0=-4.66616, y0=-29.8, r=4.85)
# ditto
surf143 = openmc.ZCylinder(surface_id=143, x0=-4.66616, y0=-19.6, r=4.85)
# ditto
surf144 = openmc.ZCylinder(surface_id=144, x0=-4.66616, y0=-9.4, r=4.85)
# ditto
surf145 = openmc.ZCylinder(surface_id=145, x0=-4.66616, y0=0.8, r=4.85)
# ditto
surf146 = openmc.ZCylinder(surface_id=146, x0=-4.66616, y0=11.0, r=4.85)
# ditto
surf147 = openmc.ZCylinder(surface_id=147, x0=-4.66616, y0=21.2, r=4.85)
# Sixth row
surf151 = openmc.ZCylinder(surface_id=151, x0=4.1673, y0=-34.9, r=4.85)
# ditto
surf152 = openmc.ZCylinder(surface_id=152, x0=4.1673, y0=-24.7, r=4.85)
# ditto
surf153 = openmc.ZCylinder(surface_id=153, x0=4.1673, y0=-14.5, r=4.85)
# ditto
surf154 = openmc.ZCylinder(surface_id=154, x0=4.1673, y0=-4.3, r=4.85)
# ditto
surf155 = openmc.ZCylinder(surface_id=155, x0=4.1673, y0=5.9, r=4.85)
# ditto
surf156 = openmc.ZCylinder(surface_id=156, x0=4.1673, y0=16.1, r=4.85)
# Seventh row
surf161 = openmc.ZCylinder(surface_id=161, x0=13.00075, y0=-40.0, r=4.85)
# ditto
surf162 = openmc.ZCylinder(surface_id=162, x0=13.00075, y0=-29.8, r=4.85)
# ditto
surf163 = openmc.ZCylinder(surface_id=163, x0=13.00075, y0=-19.6, r=4.85)
# ditto
surf164 = openmc.ZCylinder(surface_id=164, x0=13.00075, y0=-9.4, r=4.85)
# ditto
surf165 = openmc.ZCylinder(surface_id=165, x0=13.00075, y0=0.8, r=4.85)
# ditto
surf166 = openmc.ZCylinder(surface_id=166, x0=13.00075, y0=11.0, r=4.85)
# ditto
surf167 = openmc.ZCylinder(surface_id=167, x0=13.00075, y0=21.2, r=4.85)
# Sixth row
surf171 = openmc.ZCylinder(surface_id=171, x0=21.83421, y0=-34.9, r=4.85)
# ditto
surf172 = openmc.ZCylinder(surface_id=172, x0=21.83421, y0=-24.7, r=4.85)
# ditto
surf173 = openmc.ZCylinder(surface_id=173, x0=21.83421, y0=-14.5, r=4.85)
# ditto
surf174 = openmc.ZCylinder(surface_id=174, x0=21.83421, y0=-4.3, r=4.85)
# ditto
surf175 = openmc.ZCylinder(surface_id=175, x0=21.83421, y0=5.9, r=4.85)
# ditto
surf176 = openmc.ZCylinder(surface_id=176, x0=21.83421, y0=16.1, r=4.85)
surf901 = openmc.ZPlane(surface_id=901, z0=-4.4)
surf902 = openmc.ZPlane(surface_id=902, z0=-0.4)
surf903 = openmc.ZPlane(surface_id=903, z0=0.0)
# Critical water height, Hw
surf904 = openmc.ZPlane(surface_id=904, z0=52.91)
# Above disk and below beam
surf905 = openmc.ZPlane(surface_id=905, z0=60.0)
# Boundary condition
surf999 = openmc.model.RectangularParallelepiped(-65.0, 65.0, -70.0, 70.0, -35.4, 104.6, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf5_zmin = openmc.ZPlane(z0=0.0)
surf5_zmax = openmc.ZPlane(z0=59.0)
surf6_zmin = openmc.ZPlane(z0=59.0)
surf6_zmax = openmc.ZPlane(z0=59.5)
surf50_zmin = openmc.ZPlane(z0=0.0)
surf50_zmax = openmc.ZPlane(z0=50.0)
surf60_zmin = openmc.ZPlane(z0=50.0)
surf60_zmax = openmc.ZPlane(z0=50.5)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = +surf1 & -surf2
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0])

universe2 = openmc.Universe(universe_id=2, cells=[])

u3_cell0 = openmc.Cell(fill=mat2)
u3_cell0.region = -surf4 & (-surf5 & +surf5_zmin & -surf5_zmax) & -surf904
u3_cell1 = openmc.Cell(fill=mat5)
u3_cell1.region = -surf4 & (-surf5 & +surf5_zmin & -surf5_zmax) & +surf904
u3_cell2 = openmc.Cell(fill=mat1)
u3_cell2.region = +surf4 & (-surf5 & +surf5_zmin & -surf5_zmax)
u3_cell3 = openmc.Cell(fill=mat3)
u3_cell3.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)
u3_cell4 = openmc.Cell(fill=mat2)
u3_cell4.region = +surf4 & (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & -surf904
u3_cell5 = openmc.Cell(fill=mat5)
u3_cell5.region = +surf4 & (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & +surf904
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4, u3_cell5])

u4_cell0 = openmc.Cell(fill=mat3)
u4_cell0.region = +surf7 & -surf8
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0])

u5_cell0 = openmc.Cell(fill=mat5)
u5_cell0.region = +surf904 & -surf999
u5_cell1 = openmc.Cell(fill=mat5)
u5_cell1.region = +surf904 & -surf999
u5_cell2 = openmc.Cell(fill=mat2)
u5_cell2.region = -surf904 & -surf999
u5_cell3 = openmc.Cell(fill=mat2)
u5_cell3.region = -surf904 & -surf999
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0, u5_cell1, u5_cell2, u5_cell3])

u6_cell0 = openmc.Cell(fill=mat2)
u6_cell0.region = -surf40 & (-surf50 & +surf50_zmin & -surf50_zmax) & -surf904
u6_cell1 = openmc.Cell(fill=mat1)
u6_cell1.region = +surf40 & (-surf50 & +surf50_zmin & -surf50_zmax)
u6_cell2 = openmc.Cell(fill=mat3)
u6_cell2.region = (+surf50 | -surf50_zmin | +surf50_zmax) & (-surf60 & +surf60_zmin & -surf60_zmax)
u6_cell3 = openmc.Cell(fill=mat2)
u6_cell3.region = +surf40 & (+surf50 | -surf50_zmin | +surf50_zmax) & (+surf60 | -surf60_zmin | +surf60_zmax) & -surf904
u6_cell4 = openmc.Cell(fill=mat5)
u6_cell4.region = +surf40 & (+surf50 | -surf50_zmin | +surf50_zmax) & (+surf60 | -surf60_zmin | +surf60_zmax) & +surf904
universe6 = openmc.Universe(universe_id=6, cells=[u6_cell0, u6_cell1, u6_cell2, u6_cell3, u6_cell4])

universe7 = openmc.Universe(universe_id=7, cells=[])

universe8 = openmc.Universe(universe_id=8, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Beams
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = +surf905 & -surf999

# Tubes
cell2 = openmc.Cell(cell_id=2, fill=universe8)
cell2.region = +surf904 & -surf905 & -surf999

# Tubes
cell3 = openmc.Cell(cell_id=3, fill=universe7)
cell3.region = +surf903 & -surf904 & -surf999

# Plate
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = -surf3 & +surf902 & -surf903 & -surf999

# Water
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf3 & +surf902 & -surf903 & -surf999

# Water
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf901 & -surf902 & -surf999

# Water
cell7 = openmc.Cell(cell_id=7, fill=mat2)
cell7.region = +surf901 & -surf902 & -surf999

# Water
cell8 = openmc.Cell(cell_id=8, fill=mat2)
cell8.region = -surf901 & -surf999

# Air
cell16 = openmc.Cell(cell_id=16, fill=mat5)
cell16.region = +surf4 & (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & +surf904

# Water
cell22 = openmc.Cell(cell_id=22, fill=mat2)
cell22.region = -surf904 & -surf999

# Air
cell28 = openmc.Cell(cell_id=28, fill=mat5)
cell28.region = +surf40 & (+surf50 | -surf50_zmin | +surf50_zmax) & (+surf60 | -surf60_zmin | +surf60_zmax) & +surf904

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell16, cell22, cell28])
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
source.space = openmc.stats.Box((-18.5, -19.5, 25.455), (-8.5, -9.5, 27.455))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
