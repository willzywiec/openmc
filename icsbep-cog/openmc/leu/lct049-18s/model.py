"""
LCT049-18S: Simplified model of R1-2R(3,3)M with 2x2 Modules of H/U=2, H/U=3, Air, and Absorber Boxes and d=5.63c
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(5)O2+H2O
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 3.409700e-06)
mat1.add_nuclide("U235", 3.686500e-04)
mat1.add_nuclide("U236", 2.802400e-06)
mat1.add_nuclide("U238", 6.942200e-03)
mat1.add_nuclide("O16", 2.644100e-02)
mat1.add_nuclide("H1", 2.200000e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# AG3
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.808600e-02)
mat2.add_element("Mg", 1.971900e-03)
mat2.add_element("Cu", 1.026100e-05)
mat2.add_element("Fe", 1.050800e-04)
mat2.add_element("Cr", 6.270400e-06)
mat2.add_element("Mn", 1.008900e-04)
mat2.add_element("Si", 6.965200e-05)
mat2.add_element("Ti", 6.809400e-06)
mat2.add_element("Zn", 4.986000e-06)

# Rubber
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 5.406500e-02)
mat3.add_nuclide("O16", 9.481500e-04)
mat3.add_element("N", 2.933200e-04)
mat3.add_nuclide("H1", 8.866000e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

# Polythene
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 4.121500e-02)
mat4.add_nuclide("H1", 8.243100e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

# Air
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("N", 4.198500e-05)
mat5.add_nuclide("O16", 1.126300e-05)

# U(5)O2+H2O
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("U234", 3.409700e-06)
mat6.add_nuclide("U235", 3.686500e-04)
mat6.add_nuclide("U236", 2.802400e-06)
mat6.add_nuclide("U238", 6.942200e-03)
mat6.add_nuclide("O16", 2.280100e-02)
mat6.add_nuclide("H1", 1.472500e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

# Borated
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Fe", 5.722100e-02)
mat7.add_element("Cr", 1.720200e-02)
mat7.add_element("Ni", 1.070700e-02)
mat7.add_element("Mn", 5.987600e-04)
mat7.add_element("B", 4.922000e-03)
mat7.add_element("C", 1.449900e-04)
mat7.add_element("Si", 1.050600e-03)
mat7.add_element("S", 9.078100e-06)
mat7.add_element("P", 4.685300e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# UO2
surf1 = openmc.model.RectangularParallelepiped(-9.8, 9.8, -9.8, 9.8, -9.31, 9.6)
# AG3 box
surf2 = openmc.model.RectangularParallelepiped(-9.95, 9.95, -9.95, 9.95, -9.56, 9.6)
# Air
surf3 = openmc.model.RectangularParallelepiped(-8.77, 8.77, -8.77, 8.77, 9.6, 9.700000000000001)
# Rubber
surf4 = openmc.model.RectangularParallelepiped(-9.95, 9.95, -9.95, 9.95, 9.6, 9.700000000000001)
# AG3 lid
surf5 = openmc.model.RectangularParallelepiped(-9.95, 9.95, -9.95, 9.95, 9.7, 10.0)
# Air
surf6 = openmc.model.RectangularParallelepiped(-10.15, 10.15, -10.15, 10.15, -10.0, 10.0)
# AG3 tube
surf7 = openmc.model.RectangularParallelepiped(-10.25, 10.25, -10.25, 10.25, -10.0, 10.0)
# Polythene
surf8 = openmc.model.RectangularParallelepiped(-10.05, 10.05, -10.05, 10.05, -10.0, 10.0)
# Dummy
surf9 = openmc.model.RectangularParallelepiped(-4999.5, 4999.5, -4999.5, 4999.5, -4999.5, 4999.5)
# AG3
# Prism 100: 8-sided polygon
surf100_0 = openmc.Plane(a=0.7071067812, b=-0.7071067812, c=0, d=9.2630988335)
surf100_1 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=8.5000000000)
surf100_2 = openmc.Plane(a=0.7071067812, b=0.7071067812, c=0, d=9.2630988335)
surf100_3 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=8.5000000000)
surf100_4 = openmc.Plane(a=-0.7071067812, b=0.7071067812, c=0, d=9.2630988335)
surf100_5 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=8.5000000000)
surf100_6 = openmc.Plane(a=-0.7071067812, b=-0.7071067812, c=0, d=9.2630988335)
surf100_7 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=8.5000000000)
# Borated SST
surf101 = openmc.model.RectangularParallelepiped(-9.65, 9.65, -0.075, 0.075, -9.5, 9.7)
# Borated SST
surf102 = openmc.model.RectangularParallelepiped(-0.075, 0.075, -9.65, 9.65, -9.5, 9.7)
# Polythene
surf103 = openmc.model.RectangularParallelepiped(-9.65, 9.65, -1.0, 1.0, -9.5, 9.7)
# Polythene
surf104 = openmc.model.RectangularParallelepiped(-1.0, 1.0, -9.65, 9.65, -9.5, 9.7)
# AG3 box, inner
surf105 = openmc.model.RectangularParallelepiped(-9.65, 9.65, -9.65, 9.65, -9.5, 9.7)
# AG3 box, outer
surf106 = openmc.model.RectangularParallelepiped(-9.95, 9.95, -9.95, 9.95, -9.8, 10.0)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat4)
u1_cell0.region = -surf8
u1_cell1 = openmc.Cell(fill=mat5)
u1_cell1.region = -surf6 & +surf8
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf6 & -surf7 & +surf8
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

u2_cell0 = openmc.Cell(fill=mat6)
u2_cell0.region = -surf1 & -surf2
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = +surf1 & -surf2
u2_cell2 = openmc.Cell(fill=mat5)
u2_cell2.region = +surf2 & -surf3 & -surf4
u2_cell3 = openmc.Cell(fill=mat3)
u2_cell3.region = +surf2 & +surf3 & -surf4
u2_cell4 = openmc.Cell(fill=mat2)
u2_cell4.region = +surf3 & +surf4 & -surf5
u2_cell5 = openmc.Cell(fill=mat5)
u2_cell5.region = +surf2 & +surf4 & +surf5 & -surf6
u2_cell6 = openmc.Cell(fill=mat2)
u2_cell6.region = +surf6 & -surf7
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6])

u3_cell0 = openmc.Cell(fill=mat1)
u3_cell0.region = -surf1 & -surf2
u3_cell1 = openmc.Cell(fill=mat2)
u3_cell1.region = +surf1 & -surf2
u3_cell2 = openmc.Cell(fill=mat5)
u3_cell2.region = +surf2 & -surf3 & -surf4
u3_cell3 = openmc.Cell(fill=mat3)
u3_cell3.region = +surf2 & +surf3 & -surf4
u3_cell4 = openmc.Cell(fill=mat2)
u3_cell4.region = +surf3 & +surf4 & -surf5
u3_cell5 = openmc.Cell(fill=mat5)
u3_cell5.region = +surf2 & +surf4 & +surf5 & -surf6
u3_cell6 = openmc.Cell(fill=mat2)
u3_cell6.region = +surf6 & -surf7
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0, u3_cell1, u3_cell2, u3_cell3, u3_cell4, u3_cell5, u3_cell6])

u4_cell0 = openmc.Cell(fill=mat2)
u4_cell0.region = +surf1 & -surf2
u4_cell1 = openmc.Cell(fill=mat3)
u4_cell1.region = +surf2 & +surf3 & -surf4
u4_cell2 = openmc.Cell(fill=mat2)
u4_cell2.region = +surf3 & +surf4 & -surf5
u4_cell3 = openmc.Cell(fill=mat2)
u4_cell3.region = +surf6 & -surf7
universe4 = openmc.Universe(universe_id=4, cells=[u4_cell0, u4_cell1, u4_cell2, u4_cell3])

u5_cell0 = openmc.Cell(fill=mat7)
u5_cell0.region = -surf101 & -surf105
u5_cell1 = openmc.Cell(fill=mat7)
u5_cell1.region = +surf101 & -surf102 & -surf105
u5_cell2 = openmc.Cell(fill=mat4)
u5_cell2.region = +surf101 & +surf102 & -surf103 & -surf105
u5_cell3 = openmc.Cell(fill=mat4)
u5_cell3.region = +surf101 & +surf102 & +surf103 & -surf104 & -surf105
u5_cell4 = openmc.Cell(fill=mat2)
u5_cell4.region = +surf105 & -surf106
u5_cell5 = openmc.Cell(fill=mat2)
u5_cell5.region = (-surf100_0 & -surf100_1 & -surf100_2 & -surf100_3 & -surf100_4 & -surf100_5 & -surf100_6 & -surf100_7) & +surf106
u5_cell6 = openmc.Cell(fill=mat2)
u5_cell6.region = +surf6 & -surf7
universe5 = openmc.Universe(universe_id=5, cells=[u5_cell0, u5_cell1, u5_cell2, u5_cell3, u5_cell4, u5_cell5, u5_cell6])

u6_cell0 = openmc.Cell(fill=mat5)
u6_cell0.region = -surf9
universe6 = openmc.Universe(universe_id=6, cells=[u6_cell0])

universe7 = openmc.Universe(universe_id=7, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# lttc
cell1 = openmc.Cell(cell_id=1, fill=universe7)
cell1.region = 

# Air
cell31 = openmc.Cell(cell_id=31, fill=mat5)
cell31.region = -surf9

root_universe = openmc.Universe(cells=[cell1, cell31])
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
source.space = openmc.stats.Box((-55.115, -11.26, -11.0), (55.115, 11.26, 11.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
