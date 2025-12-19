"""
PU-MET-FAST-033; ZPPR-21 Phase A; Benchmark Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 4.975490e-07)
mat1.add_nuclide("Pu239", 5.151080e-03)
mat1.add_nuclide("Pu240", 3.196150e-04)
mat1.add_nuclide("Pu241", 1.079260e-05)
mat1.add_nuclide("Pu242", 2.098010e-06)
mat1.add_nuclide("Am241", 2.581700e-05)
mat1.add_nuclide("U235", 1.087130e-05)
mat1.add_nuclide("U238", 4.963670e-03)
mat1.add_element("Cr", 3.414780e-03)
mat1.add_element("Ni", 1.486970e-03)
mat1.add_element("Fe", 1.199400e-02)
mat1.add_element("Al", 4.459090e-04)
mat1.add_element("C", 3.987080e-05)
mat1.add_element("Mo", 2.457080e-04)
mat1.add_element("Mn", 2.873700e-04)
mat1.add_element("Cu", 3.424790e-05)
mat1.add_element("Si", 1.753770e-04)
mat1.add_element("Co", 7.055550e-07)
mat1.add_element("Zr", 4.403710e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cr", 1.497460e-03)
mat2.add_element("Ni", 6.168230e-04)
mat2.add_element("Fe", 5.364410e-03)
mat2.add_element("C", 6.576680e-02)
mat2.add_element("Mo", 9.559240e-06)
mat2.add_element("Mn", 1.274410e-04)
mat2.add_element("Cu", 1.885940e-05)
mat2.add_element("Si", 8.156160e-05)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cr", 1.243560e-03)
mat3.add_element("Ni", 5.045120e-04)
mat3.add_element("Fe", 4.475730e-03)
mat3.add_element("Al", 2.134020e-08)
mat3.add_element("C", 6.750420e-02)
mat3.add_element("Mo", 7.769980e-06)
mat3.add_element("Mn", 1.043390e-04)
mat3.add_element("Cu", 1.547940e-05)
mat3.add_element("Si", 6.723940e-05)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 4.125430e-03)
mat4.add_element("Ni", 1.791640e-03)
mat4.add_element("Fe", 1.470890e-02)
mat4.add_element("Al", 5.650470e-06)
mat4.add_element("C", 5.288190e-05)
mat4.add_element("Mo", 1.949970e-05)
mat4.add_element("Mn", 3.358630e-04)
mat4.add_element("Cu", 4.349740e-05)
mat4.add_element("Si", 2.322650e-04)
mat4.add_element("Co", 1.618360e-06)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 1.798720e-03)
mat5.add_element("Ni", 7.720590e-04)
mat5.add_element("Fe", 6.409870e-03)
mat5.add_element("Al", 1.534750e-06)
mat5.add_element("C", 2.441720e-05)
mat5.add_element("Mo", 9.642800e-06)
mat5.add_element("Mn", 1.499500e-04)
mat5.add_element("Cu", 2.048610e-05)
mat5.add_element("Si", 1.006410e-04)
mat5.add_element("Co", 4.543680e-07)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Cr", 1.704030e-03)
mat6.add_element("Ni", 7.212330e-04)
mat6.add_element("Fe", 6.092830e-03)
mat6.add_element("Al", 1.292070e-06)
mat6.add_element("C", 2.374140e-05)
mat6.add_element("Mo", 9.328990e-06)
mat6.add_element("Mn", 1.418760e-04)
mat6.add_element("Cu", 1.976180e-05)
mat6.add_element("Si", 9.497590e-05)
mat6.add_element("Co", 3.731800e-07)

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Cr", 1.587960e-03)
mat7.add_element("Ni", 6.576680e-04)
mat7.add_element("Fe", 1.531570e-02)
mat7.add_element("Na", 1.746850e-06)
mat7.add_element("C", 1.081670e-04)
mat7.add_element("Mo", 9.819560e-06)
mat7.add_element("Mn", 1.853660e-04)
mat7.add_element("Cu", 1.935830e-05)
mat7.add_element("H", 2.199370e-02)
mat7.add_element("Si", 8.571920e-05)
mat7.add_nuclide("Li6", 1.620970e-03)
mat7.add_nuclide("Li7", 2.040370e-02)

mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Cr", 1.763910e-03)
mat8.add_element("Ni", 7.490950e-04)
mat8.add_element("Fe", 6.303950e-03)
mat8.add_element("Al", 1.435640e-06)
mat8.add_element("C", 2.433840e-05)
mat8.add_element("Mo", 9.466590e-06)
mat8.add_element("Mn", 1.461100e-04)
mat8.add_element("Cu", 2.008140e-05)
mat8.add_element("Si", 9.809210e-05)
mat8.add_element("Co", 4.146440e-07)

mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Cr", 1.600020e-03)
mat9.add_element("Ni", 6.632510e-04)
mat9.add_element("Fe", 6.049560e-03)
mat9.add_nuclide("O16", 6.243370e-03)
mat9.add_element("C", 2.296600e-02)
mat9.add_element("Mo", 9.830100e-06)
mat9.add_element("Mn", 1.346130e-04)
mat9.add_nuclide("B10", 4.114700e-04)
mat9.add_nuclide("B11", 1.669300e-03)
mat9.add_element("Cu", 1.943070e-05)
mat9.add_nuclide("H1", 5.178760e-02)
mat9.add_element("Si", 8.633390e-05)
mat9.add_s_alpha_beta("c_H_in_CH2")

mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_element("Cr", 1.170050e-03)
mat10.add_element("Ni", 4.724840e-04)
mat10.add_element("Fe", 1.268710e-02)
mat10.add_element("Na", 2.041500e-06)
mat10.add_element("C", 8.201320e-05)
mat10.add_element("Mo", 8.124990e-06)
mat10.add_element("Mn", 1.511060e-04)
mat10.add_element("Cu", 1.695700e-05)
mat10.add_element("H", 2.570750e-02)
mat10.add_element("Si", 6.721550e-05)
mat10.add_nuclide("Li6", 1.894690e-03)
mat10.add_nuclide("Li7", 2.384830e-02)

mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_element("Cr", 1.198680e-03)
mat11.add_element("Ni", 4.847710e-04)
mat11.add_element("Fe", 4.315560e-03)
mat11.add_element("Al", 2.288580e-08)
mat11.add_element("C", 1.884370e-05)
mat11.add_element("Mo", 8.301990e-06)
mat11.add_element("Mn", 1.065960e-04)
mat11.add_element("Cu", 1.729490e-05)
mat11.add_element("Si", 6.880490e-05)
mat11.add_element("Co", 6.892320e-09)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZCylinder(surface_id=1, r=18.9592)
surf2 = openmc.ZCylinder(surface_id=2, r=27.01335)
surf3 = openmc.ZCylinder(surface_id=3, r=28.0518)
surf4 = openmc.ZCylinder(surface_id=4, r=34.2855)
surf5 = openmc.ZCylinder(surface_id=5, r=40.51925)
surf6 = openmc.ZCylinder(surface_id=6, r=52.9867, boundary_type="vacuum")
# surf11: Unsupported surface type "analytic" with params ['1.', 'z', '0.00000', 'constant']
# surf12: Unsupported surface type "analytic" with params ['1.', 'z', '-20.40997', 'constant']
# surf13: Unsupported surface type "analytic" with params ['1.', 'z', '-30.56997', 'constant']
# surf14: Unsupported surface type "analytic" with params ['1.', 'z', '-48.34997', 'constant']
# surf15: Unsupported surface type "analytic" with params ['1.', 'z', '-59.04956', 'constant']
# surf16: Unsupported surface type "analytic" with params ['1.', 'z', '-126.20483', 'constant']

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# RGN1
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & +surf11 & -surf12

# RGN2
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = -surf1 & +surf12 & -surf13

# RGN3
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf1 & -surf2 & +surf11 & -surf13

# RGN4
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf2 & -surf3 & +surf11 & -surf13

# RGN5
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = -surf3 & +surf13 & -surf14

# RGN6
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf3 & -surf4 & +surf11 & -surf14

# RGN7
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = -surf4 & +surf14 & -surf15

# RGN8
cell8 = openmc.Cell(cell_id=8, fill=mat8)
cell8.region = +surf4 & -surf5 & +surf11 & -surf14

# RGN9
cell9 = openmc.Cell(cell_id=9, fill=mat9)
cell9.region = +surf4 & -surf5 & +surf14 & -surf15

# RGN10
cell10 = openmc.Cell(cell_id=10, fill=mat10)
cell10.region = +surf5 & -surf6 & +surf11 & -surf15

# RGN11
cell11 = openmc.Cell(cell_id=11, fill=mat11)
cell11.region = -surf6 & +surf15 & -surf16

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11])
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0001))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
