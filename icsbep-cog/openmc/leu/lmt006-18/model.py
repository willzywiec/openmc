"""
LMT006-18: Case 18; Bugey 23; detailed; 46 type 1 and 6 type 2 tubes; 12.7cm pitch; Hw=63.51cm
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
surf5 = openmc.ZCylinder(surface_id=5, x0=0.0, y0=59.0, r=4.85)
# Type 1 steel disk
surf6 = openmc.ZCylinder(surface_id=6, x0=59.0, y0=59.5, r=4.85)
# Beam/inner
surf7 = openmc.model.RectangularParallelepiped(-1.8, 1.8, -499.95, 499.95, 60.7, 64.3)
# Beam/outer
surf8 = openmc.model.RectangularParallelepiped(-2.0, 2.0, -50.0, 50.0, 60.5, 64.5)
# Type 2 fuel tube/inner
surf40 = openmc.ZCylinder(surface_id=40, r=3.85)
# Type 2 fuel tube/outer
surf50 = openmc.ZCylinder(surface_id=50, x0=0.0, y0=50.0, r=4.75)
# Type 2 steel disk
surf60 = openmc.ZCylinder(surface_id=60, x0=50.0, y0=50.5, r=4.75)
# Basic fuel tube and disk
# surf101: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf102: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf103: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf104: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf105: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf106: Error converting surface type "c": could not convert string to float: 'tr'
# fuel tube and disk
# surf107: Error converting surface type "c": could not convert string to float: 'tr'
# Second row
# surf111: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf112: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf113: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf114: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf115: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf116: Error converting surface type "c": could not convert string to float: 'tr'
# Third row
# surf121: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf122: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf123: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf124: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf125: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf126: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf127: Error converting surface type "c": could not convert string to float: 'tr'
# Fourth row
# surf131: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf132: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf133: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf134: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf135: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf136: Error converting surface type "c": could not convert string to float: 'tr'
# Fifth row
# surf141: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf142: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf143: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf144: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf145: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf146: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf147: Error converting surface type "c": could not convert string to float: 'tr'
# Sixth row
# surf151: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf152: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf153: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf154: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf155: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf156: Error converting surface type "c": could not convert string to float: 'tr'
# Seventh row
# surf161: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf162: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf163: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf164: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf165: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf166: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf167: Error converting surface type "c": could not convert string to float: 'tr'
# Sixth row
# surf171: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf172: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf173: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf174: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf175: Error converting surface type "c": could not convert string to float: 'tr'
# ditto
# surf176: Error converting surface type "c": could not convert string to float: 'tr'
surf901 = openmc.ZPlane(surface_id=901, z0=-4.4)
surf902 = openmc.ZPlane(surface_id=902, z0=-0.4)
surf903 = openmc.ZPlane(surface_id=903, z0=0.0)
# Critical water height, Hw
surf904 = openmc.ZPlane(surface_id=904, z0=63.51)
# Above disk and below beam
surf905 = openmc.ZPlane(surface_id=905, z0=60.0)
# Boundary condition
surf999 = openmc.model.RectangularParallelepiped(-65.0, 65.0, -70.0, 70.0, -35.4, 104.6, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = +surf1 & -surf2
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0])

universe2 = openmc.Universe(universe_id=2, cells=[])

u3_cell0 = openmc.Cell(fill=mat2)
u3_cell0.region = -surf4 & -surf5 & -surf904
u3_cell1 = openmc.Cell(fill=mat1)
u3_cell1.region = +surf4 & -surf5
u3_cell2 = openmc.Cell(fill=mat3)
u3_cell2.region = +surf5 & -surf6
u3_cell3 = openmc.Cell(fill=mat2)
u3_cell3.region = +surf4 & +surf5 & +surf6 & -surf904
u3_cell4 = openmc.Cell(fill=mat5)
u3_cell4.region = +surf4 & +surf5 & +surf6 & +surf904
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4])

u4_cell0 = openmc.Cell(fill=mat5)
u4_cell0.region = -surf7 & +surf904
u4_cell1 = openmc.Cell(fill=mat2)
u4_cell1.region = -surf7 & -surf904
u4_cell2 = openmc.Cell(fill=mat3)
u4_cell2.region = +surf7 & -surf8
u4_cell3 = openmc.Cell(fill=mat2)
u4_cell3.region = +surf8 & -surf904
u4_cell4 = openmc.Cell(fill=mat5)
u4_cell4.region = +surf8 & +surf904
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3, u4_cell4])

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
u6_cell0.region = -surf40 & -surf50 & -surf904
u6_cell1 = openmc.Cell(fill=mat1)
u6_cell1.region = +surf40 & -surf50
u6_cell2 = openmc.Cell(fill=mat3)
u6_cell2.region = +surf50 & -surf60
u6_cell3 = openmc.Cell(fill=mat2)
u6_cell3.region = +surf40 & +surf50 & +surf60 & -surf904
u6_cell4 = openmc.Cell(fill=mat5)
u6_cell4.region = +surf40 & +surf50 & +surf60 & +surf904
universe6 = openmc.Universe(universe_id=6, cells=[u6_cell0, u6_cell1, u6_cell2, u6_cell3, u6_cell4])

universe7 = openmc.Universe(universe_id=7, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Beams
cell1 = openmc.Cell(cell_id=1, fill=universe5)
cell1.region = +surf905 & -surf999

# Tubes
cell2 = openmc.Cell(cell_id=2, fill=universe7)
cell2.region = +surf903 & -surf905 & -surf999

# Plate
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = -surf3 & +surf902 & -surf903 & -surf999

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf3 & +surf902 & -surf903 & -surf999

# Water
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf901 & -surf902 & -surf999

# Water
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf901 & -surf902 & -surf999

# Water
cell7 = openmc.Cell(cell_id=7, fill=mat2)
cell7.region = -surf901 & -surf999

# Air
cell14 = openmc.Cell(cell_id=14, fill=mat5)
cell14.region = +surf4 & +surf5 & +surf6 & +surf904

# Air
cell20 = openmc.Cell(cell_id=20, fill=mat5)
cell20.region = +surf8 & +surf904

# Water
cell25 = openmc.Cell(cell_id=25, fill=mat2)
cell25.region = -surf904 & -surf999

# Air
cell31 = openmc.Cell(cell_id=31, fill=mat5)
cell31.region = +surf40 & +surf50 & +surf60 & +surf904

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell14, cell20, cell25, cell31])
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
source.space = openmc.stats.Box((-3.7, -9.25, 28.5), (0.7, 5.45, 30.5))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
