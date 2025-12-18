"""
LCT049-8S: Simplified model of R2-2R(5,5) with H/U=2.5 and d=8.92cm
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
mat1.add_nuclide("O16", 2.464500e-02)
mat1.add_nuclide("H1", 1.841300e-02)
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

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

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

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf2
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf1 & -surf2
u1_cell2 = openmc.Cell(fill=mat5)
u1_cell2.region = +surf2 & -surf3 & -surf4
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = +surf2 & +surf3 & -surf4
u1_cell4 = openmc.Cell(fill=mat2)
u1_cell4.region = +surf3 & +surf4 & -surf5
u1_cell5 = openmc.Cell(fill=mat5)
u1_cell5.region = +surf2 & +surf4 & +surf5 & -surf6
u1_cell6 = openmc.Cell(fill=mat2)
u1_cell6.region = +surf6 & -surf7
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

u2_cell0 = openmc.Cell(fill=mat4)
u2_cell0.region = -surf8
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = -surf6 & +surf8
u2_cell2 = openmc.Cell(fill=mat2)
u2_cell2.region = +surf6 & -surf7 & +surf8
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

u3_cell0 = openmc.Cell(fill=mat5)
u3_cell0.region = -surf9
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0])

universe4 = openmc.Universe(universe_id=4, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# lttc
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = 

# Air
cell13 = openmc.Cell(cell_id=13, fill=mat5)
cell13.region = -surf9

root_universe = openmc.Universe(cells=[cell1, cell13])
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
source.space = openmc.stats.Box((-15.72, -1.0, -1.0), (15.72, 1.0, 1.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
