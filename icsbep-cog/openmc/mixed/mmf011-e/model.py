"""
MIX-MET-FAST-011; ZPPR-21 Phase E; Benchmark Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 4.903950e-07)
mat1.add_nuclide("Pu239", 8.772650e-04)
mat1.add_nuclide("Pu240", 1.160820e-04)
mat1.add_nuclide("Pu241", 6.195580e-06)
mat1.add_nuclide("Pu242", 1.915240e-06)
mat1.add_nuclide("Am241", 1.158640e-05)
mat1.add_nuclide("U234", 6.555590e-05)
mat1.add_nuclide("U235", 6.694490e-03)
mat1.add_nuclide("U236", 3.142660e-05)
mat1.add_nuclide("U238", 5.284040e-03)
mat1.add_element("Cr", 3.707460e-03)
mat1.add_element("Ni", 1.682220e-03)
mat1.add_element("Fe", 1.306170e-02)
mat1.add_element("Al", 3.418070e-06)
mat1.add_element("C", 3.539500e-05)
mat1.add_element("Mo", 2.384020e-04)
mat1.add_element("Mn", 2.984060e-04)
mat1.add_element("Cu", 2.591560e-05)
mat1.add_element("Si", 1.758010e-04)
mat1.add_element("N", 6.520700e-06)
mat1.add_element("Co", 2.051600e-06)
mat1.add_element("Zr", 4.344250e-03)

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
mat3.add_element("Cr", 1.406200e-03)
mat3.add_element("Ni", 5.704630e-04)
mat3.add_element("Fe", 5.061150e-03)
mat3.add_element("Al", 2.331910e-08)
mat3.add_element("C", 6.661160e-02)
mat3.add_element("Mo", 8.787350e-06)
mat3.add_element("Mn", 1.179960e-04)
mat3.add_element("Cu", 1.750830e-05)
mat3.add_element("Si", 7.603890e-05)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 3.533270e-03)
mat4.add_element("Ni", 1.537120e-03)
mat4.add_element("Fe", 1.259440e-02)
mat4.add_element("Al", 5.000170e-06)
mat4.add_element("C", 4.501220e-05)
mat4.add_element("Mo", 1.655860e-05)
mat4.add_element("Mn", 2.874510e-04)
mat4.add_element("Cu", 3.706970e-05)
mat4.add_element("Si", 1.991910e-04)
mat4.add_element("Co", 1.435790e-06)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 1.789520e-03)
mat5.add_element("Ni", 7.675690e-04)
mat5.add_element("Fe", 6.377710e-03)
mat5.add_element("Al", 1.499310e-06)
mat5.add_element("C", 2.434390e-05)
mat5.add_element("Mo", 9.615890e-06)
mat5.add_element("Mn", 1.492720e-04)
mat5.add_element("Cu", 2.043980e-05)
mat5.add_element("Si", 1.001390e-04)
mat5.add_element("Co", 4.438760e-07)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Cr", 1.564140e-03)
mat6.add_element("Ni", 6.561510e-04)
mat6.add_element("Fe", 5.599650e-03)
mat6.add_element("Al", 9.570910e-07)
mat6.add_element("C", 2.234220e-05)
mat6.add_element("Mo", 9.006890e-06)
mat6.add_element("Mn", 1.319850e-04)
mat6.add_element("Cu", 1.901490e-05)
mat6.add_element("Si", 8.769590e-05)
mat6.add_element("Co", 2.764290e-07)

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Cr", 1.582520e-03)
mat7.add_element("Ni", 6.554140e-04)
mat7.add_element("Fe", 1.533590e-02)
mat7.add_element("Al", 1.754040e-06)
mat7.add_element("C", 1.084270e-04)
mat7.add_element("Mo", 9.785650e-06)
mat7.add_element("Mn", 1.851200e-04)
mat7.add_element("Cu", 1.929120e-05)
mat7.add_element("H", 2.208430e-02)
mat7.add_element("Si", 8.542250e-05)
mat7.add_nuclide("Li6", 1.627650e-03)
mat7.add_nuclide("Li7", 2.048780e-02)

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
mat11.add_element("Cr", 1.198670e-03)
mat11.add_element("Ni", 4.847640e-04)
mat11.add_element("Fe", 4.315500e-03)
mat11.add_element("Al", 2.288650e-08)
mat11.add_element("C", 1.884350e-05)
mat11.add_element("Mo", 8.301870e-06)
mat11.add_element("Mn", 1.065950e-04)
mat11.add_element("Cu", 1.729490e-05)
mat11.add_element("Si", 6.880440e-05)
mat11.add_element("Co", 6.892520e-09)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.ZCylinder(surface_id=1, r=18.9592)
surf2 = openmc.ZCylinder(surface_id=2, r=31.75001)
surf3 = openmc.ZCylinder(surface_id=3, r=32.541)
surf4 = openmc.ZCylinder(surface_id=4, r=34.2855)
surf5 = openmc.ZCylinder(surface_id=5, r=40.51925)
surf6 = openmc.ZCylinder(surface_id=6, r=52.9867, boundary_type="vacuum")
# surf11: Unsupported surface type "analytic" with params ['1.', 'z', '0.00000', 'constant']
# surf12: Unsupported surface type "analytic" with params ['1.', 'z', '-20.68936', 'constant']
# surf13: Unsupported surface type "analytic" with params ['1.', 'z', '-30.84936', 'constant']
# surf14: Unsupported surface type "analytic" with params ['1.', 'z', '-48.62936', 'constant']
# surf15: Unsupported surface type "analytic" with params ['1.', 'z', '-59.28505', 'constant']
# surf16: Unsupported surface type "analytic" with params ['1.', 'z', '-126.40113', 'constant']

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
