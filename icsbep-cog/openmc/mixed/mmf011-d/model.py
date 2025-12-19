"""
MIX-MET-FAST-011; ZPPR-21 Phase D; Benchmark Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 4.905110e-07)
mat1.add_nuclide("Pu239", 1.928320e-03)
mat1.add_nuclide("Pu240", 1.658860e-04)
mat1.add_nuclide("Pu241", 7.304620e-06)
mat1.add_nuclide("Pu242", 1.953850e-06)
mat1.add_nuclide("Am241", 1.506030e-05)
mat1.add_nuclide("U234", 4.370370e-05)
mat1.add_nuclide("U235", 4.466540e-03)
mat1.add_nuclide("U236", 2.095100e-05)
mat1.add_nuclide("U238", 5.154900e-03)
mat1.add_element("Cr", 3.810240e-03)
mat1.add_element("Ni", 1.730390e-03)
mat1.add_element("Fe", 1.340850e-02)
mat1.add_element("Al", 1.125350e-04)
mat1.add_element("C", 3.701080e-05)
mat1.add_element("Mo", 2.391590e-04)
mat1.add_element("Mn", 3.087170e-04)
mat1.add_element("Cu", 2.819270e-05)
mat1.add_element("Si", 1.784100e-04)
mat1.add_element("N", 4.347240e-06)
mat1.add_element("Co", 1.599760e-06)
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
mat3.add_element("Cr", 1.314370e-03)
mat3.add_element("Ni", 5.332120e-04)
mat3.add_element("Fe", 4.730630e-03)
mat3.add_element("Al", 2.168080e-08)
mat3.add_element("C", 6.732540e-02)
mat3.add_element("Mo", 8.212890e-06)
mat3.add_element("Mn", 1.102860e-04)
mat3.add_element("Cu", 1.636300e-05)
mat3.add_element("Si", 7.107030e-05)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 3.908560e-03)
mat4.add_element("Ni", 1.682790e-03)
mat4.add_element("Fe", 1.395290e-02)
mat4.add_element("Al", 4.692190e-06)
mat4.add_element("C", 5.138770e-05)
mat4.add_element("Mo", 1.925320e-05)
mat4.add_element("Mn", 3.195040e-04)
mat4.add_element("Cu", 4.217730e-05)
mat4.add_element("Si", 2.189620e-04)
mat4.add_element("Co", 1.344580e-06)

mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 1.784590e-03)
mat5.add_element("Ni", 7.651460e-04)
mat5.add_element("Fe", 6.360520e-03)
mat5.add_element("Al", 1.478360e-06)
mat5.add_element("C", 2.430990e-05)
mat5.add_element("Mo", 9.602210e-06)
mat5.add_element("Mn", 1.489070e-04)
mat5.add_element("Cu", 2.041540e-05)
mat5.add_element("Si", 9.986620e-05)
mat5.add_element("Co", 4.376730e-07)

mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Cr", 1.596020e-03)
mat6.add_element("Ni", 6.614290e-04)
mat6.add_element("Fe", 1.571580e-02)
mat6.add_element("Na", 1.814320e-06)
mat6.add_element("C", 1.115090e-04)
mat6.add_element("Mo", 9.838080e-06)
mat6.add_element("Mn", 1.878400e-04)
mat6.add_element("Cu", 1.936190e-05)
mat6.add_element("H", 2.284320e-02)
mat6.add_element("Si", 8.600960e-05)
mat6.add_nuclide("Li6", 1.683590e-03)
mat6.add_nuclide("Li7", 2.119180e-02)

mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Cr", 1.600010e-03)
mat7.add_element("Ni", 6.632510e-04)
mat7.add_element("Fe", 6.049560e-03)
mat7.add_nuclide("O16", 6.243370e-03)
mat7.add_element("C", 2.296600e-02)
mat7.add_element("Mo", 9.830100e-06)
mat7.add_element("Mn", 1.346130e-04)
mat7.add_nuclide("B10", 4.114700e-04)
mat7.add_nuclide("B11", 1.669300e-03)
mat7.add_element("Cu", 1.943070e-05)
mat7.add_nuclide("H1", 5.178760e-02)
mat7.add_element("Si", 8.633390e-05)
mat7.add_s_alpha_beta("c_H_in_CH2")

mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Cr", 1.689060e-03)
mat8.add_element("Ni", 7.142680e-04)
mat8.add_element("Fe", 6.040050e-03)
mat8.add_element("Al", 1.256180e-06)
mat8.add_element("C", 2.359210e-05)
mat8.add_element("Mo", 9.294600e-06)
mat8.add_element("Mn", 1.408170e-04)
mat8.add_element("Cu", 1.968190e-05)
mat8.add_element("Si", 9.419680e-05)
mat8.add_element("Co", 3.628140e-07)

mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Cr", 1.548650e-03)
mat9.add_element("Ni", 6.403670e-04)
mat9.add_element("Fe", 5.828260e-03)
mat9.add_nuclide("O16", 5.462950e-03)
mat9.add_element("C", 2.009760e-02)
mat9.add_element("Mo", 9.633410e-06)
mat9.add_element("Mn", 1.310240e-04)
mat9.add_nuclide("B10", 3.600360e-04)
mat9.add_nuclide("B11", 1.460640e-03)
mat9.add_element("Cu", 1.915580e-05)
mat9.add_nuclide("H1", 4.531420e-02)
mat9.add_element("Si", 8.408100e-05)
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
surf2 = openmc.ZCylinder(surface_id=2, r=33.7141)
surf3 = openmc.ZCylinder(surface_id=3, r=35.02901)
surf4 = openmc.ZCylinder(surface_id=4, r=36.482)
surf5 = openmc.ZCylinder(surface_id=5, r=40.51925)
surf6 = openmc.ZCylinder(surface_id=6, r=52.9867, boundary_type="vacuum")
# surf11: Unsupported surface type "analytic" with params ['1.', 'z', '0.00000', 'constant']
# surf12: Unsupported surface type "analytic" with params ['1.', 'z', '-20.68936', 'constant']
# surf13: Unsupported surface type "analytic" with params ['1.', 'z', '-30.84936', 'constant']
# surf14: Unsupported surface type "analytic" with params ['1.', 'z', '-48.62936', 'constant']
# surf15: Unsupported surface type "analytic" with params ['1.', 'z', '-59.28319', 'constant']
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
cell3.region = +surf1 & -surf3 & +surf11 & -surf13

# RGN4
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf3 & -surf4 & +surf11 & -surf13

# RGN5
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = -surf4 & +surf13 & -surf14

# RGN6
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = -surf2 & +surf14 & -surf15

# RGN7
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = +surf2 & -surf4 & +surf14 & -surf15

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
