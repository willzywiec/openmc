"""
MIX-COMP-INTER-005:  MOX Test Lattice with U(0.52)O2-10.89Pu(77.4)O2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# MOX per Table 17
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 8.369560e-07)
mat1.add_nuclide("U235", 1.083400e-04)
mat1.add_nuclide("U238", 2.046360e-02)
mat1.add_nuclide("Pu238", 2.953590e-05)
mat1.add_nuclide("Pu239", 1.709430e-03)
mat1.add_nuclide("Pu240", 4.673310e-04)
mat1.add_nuclide("Pu241", 2.240890e-04)
mat1.add_nuclide("Pu242", 6.695090e-05)
mat1.add_nuclide("Am241", 1.720050e-05)
mat1.add_nuclide("O16", 4.585150e-02)

# Air per Section 3.3
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("O16", 1.126300e-05)
mat2.add_element("N", 4.198500e-05)

# SST per Table 7
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("P", 7.794000e+00)
mat3.add_element("Fe", 6.859000e+01)
mat3.add_element("Cr", 1.812000e+01)
mat3.add_element("Ni", 1.061000e+01)
mat3.add_element("Mn", 1.430000e+00)
mat3.add_element("Mo", 2.400000e-01)
mat3.add_element("Cu", 2.000000e-01)
mat3.add_element("Co", 1.500000e-01)
mat3.add_element("Si", 5.100000e-01)
mat3.add_element("N", 8.700000e-02)
mat3.add_element("C", 2.600000e-02)
mat3.add_element("P", 2.500000e-02)
mat3.add_element("S", 9.000000e-03)

# H2O per Section 3.3
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("O16", 3.735898e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# MOX
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf6

# AIR
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2 & -surf6

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3 & -surf6

# AIR
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf3 & -surf4 & -surf6

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf4 & -surf5 & -surf6

# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf5 & -surf6

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6])
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
