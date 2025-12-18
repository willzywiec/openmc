"""
IEU-COMP-FAST-001:  ZPR6-6A Loading 06 (Simplified Benchmark Model)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# IC1
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.127770e-05)
mat1.add_nuclide("U235", 1.150840e-03)
mat1.add_nuclide("U236", 5.406890e-06)
mat1.add_nuclide("U238", 5.796120e-03)
mat1.add_element("C", 4.979450e-05)
mat1.add_element("Cl", 3.926030e-06)
mat1.add_element("Co", 8.326310e-07)
mat1.add_element("Cr", 2.823090e-03)
mat1.add_element("Cu", 2.669860e-05)
mat1.add_element("F", 1.074110e-05)
mat1.add_element("Fe", 1.336690e-02)
mat1.add_element("H", 2.078790e-06)
mat1.add_element("Mn", 2.344990e-04)
mat1.add_element("Mo", 1.423660e-05)
mat1.add_element("Na", 9.277520e-03)
mat1.add_element("Ni", 1.225580e-03)
mat1.add_nuclide("O16", 1.375260e-02)
mat1.add_element("Si", 1.569980e-04)
mat1.add_element("Al", 2.875110e-06)

# IAB1
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 8.274350e-05)
mat2.add_nuclide("U238", 3.723320e-02)
mat2.add_element("C", 3.671300e-05)
mat2.add_element("Cl", 3.039520e-06)
mat2.add_element("Cr", 1.458380e-03)
mat2.add_element("Cu", 1.841700e-05)
mat2.add_element("F", 9.009340e-06)
mat2.add_element("Fe", 5.355980e-03)
mat2.add_element("H", 1.785000e-06)
mat2.add_element("Mn", 1.278530e-04)
mat2.add_element("Mo", 9.332610e-06)
mat2.add_element("Ni", 5.975000e-04)
mat2.add_element("Si", 8.682580e-05)

# IAB2
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U235", 8.652640e-05)
mat3.add_nuclide("U238", 3.874790e-02)
mat3.add_element("C", 1.874150e-05)
mat3.add_element("Cr", 1.189090e-03)
mat3.add_element("Cu", 1.723190e-05)
mat3.add_element("Fe", 4.279140e-03)
mat3.add_element("Mn", 1.059050e-04)
mat3.add_element("Mo", 8.256530e-06)
mat3.add_element("Ni", 4.801750e-04)
mat3.add_element("Si", 6.831050e-05)

# OC1
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U234", 1.116110e-05)
mat4.add_nuclide("U235", 1.143900e-03)
mat4.add_nuclide("U236", 5.350520e-06)
mat4.add_nuclide("U238", 5.795030e-03)
mat4.add_element("C", 4.734060e-05)
mat4.add_element("Cl", 3.685900e-06)
mat4.add_element("Co", 2.582950e-07)
mat4.add_element("Cr", 2.825460e-03)
mat4.add_element("Cu", 2.686000e-05)
mat4.add_element("F", 1.003110e-05)
mat4.add_element("Fe", 1.380580e-02)
mat4.add_element("H", 1.928540e-06)
mat4.add_element("Mn", 2.336630e-04)
mat4.add_element("Mo", 1.500690e-05)
mat4.add_element("Na", 9.163240e-03)
mat4.add_element("Ni", 1.220870e-03)
mat4.add_nuclide("O16", 1.430940e-02)
mat4.add_element("Si", 1.508390e-04)
mat4.add_element("Al", 2.459580e-06)

# OAB1
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U235", 8.256080e-05)
mat5.add_nuclide("U238", 3.716710e-02)
mat5.add_element("C", 3.732300e-05)
mat5.add_element("Cl", 3.337530e-06)
mat5.add_element("Cr", 1.467560e-03)
mat5.add_element("Cu", 1.849340e-05)
mat5.add_element("F", 9.891770e-06)
mat5.add_element("Fe", 5.386910e-03)
mat5.add_element("H", 1.955510e-06)
mat5.add_element("Mn", 1.285170e-04)
mat5.add_element("Mo", 9.390690e-06)
mat5.add_element("Ni", 6.014010e-04)
mat5.add_element("Si", 8.698210e-05)

# OAB2
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("U235", 8.577020e-05)
mat6.add_nuclide("U238", 3.841840e-02)
mat6.add_element("C", 1.928610e-05)
mat6.add_element("Cl", 1.622150e-07)
mat6.add_element("Cr", 1.208650e-03)
mat6.add_element("Cu", 1.736930e-05)
mat6.add_element("F", 4.808170e-07)
mat6.add_element("Fe", 4.341880e-03)
mat6.add_element("H", 9.526330e-08)
mat6.add_element("Mn", 1.072360e-04)
mat6.add_element("Mo", 8.405840e-06)
mat6.add_element("Ni", 4.877120e-04)
mat6.add_element("Si", 6.888110e-05)

# RR1/RR2
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("U235", 8.665550e-05)
mat7.add_nuclide("U238", 3.880760e-02)
mat7.add_element("C", 1.857210e-05)
mat7.add_element("Cr", 1.178210e-03)
mat7.add_element("Cu", 1.707480e-05)
mat7.add_element("Fe", 4.239980e-03)
mat7.add_element("Mn", 1.049360e-04)
mat7.add_element("Mo", 8.181360e-06)
mat7.add_element("Ni", 4.757800e-04)
mat7.add_element("Si", 6.768480e-05)

# MAT
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("C", 1.864340e-05)
mat8.add_element("Cr", 1.183150e-03)
mat8.add_element("Cu", 1.713500e-05)
mat8.add_element("Fe", 4.257670e-03)
mat8.add_element("Mn", 1.053520e-04)
mat8.add_element("Mo", 8.218680e-06)
mat8.add_element("Ni", 4.778140e-04)
mat8.add_element("Si", 6.793000e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# IC1
cell1 = openmc.Cell(cell_id=1, fill=mat1)
# IAB1
cell2 = openmc.Cell(cell_id=2, fill=mat2)
# IAB2
cell3 = openmc.Cell(cell_id=3, fill=mat3)
# OC1
cell4 = openmc.Cell(cell_id=4, fill=mat4)
# OAB1
cell5 = openmc.Cell(cell_id=5, fill=mat5)
# OAB2
cell6 = openmc.Cell(cell_id=6, fill=mat6)
# RR1
cell7 = openmc.Cell(cell_id=7, fill=mat7)
# RR2
cell8 = openmc.Cell(cell_id=8, fill=mat7)
# MAT
cell9 = openmc.Cell(cell_id=9, fill=mat8)
root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9])
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
