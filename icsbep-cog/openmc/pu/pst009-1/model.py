"""
PU-SOL-THERM-009 (Case 1) 6.579 kg Pu(97.5) @ H/X = 2646 in a bare 48" Al-1100 sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.013900e-09)
mat1.add_nuclide("Pu239", 2.458200e-05)
mat1.add_nuclide("Pu240", 6.336900e-07)
mat1.add_nuclide("Pu241", 1.877400e-08)
mat1.add_nuclide("Pu242", 3.490000e-09)
mat1.add_element("N", 7.749400e-04)
mat1.add_nuclide("H1", 6.509800e-02)
mat1.add_nuclide("O16", 3.454200e-02)
mat1.add_element("Al", 2.236700e-06)
mat1.add_element("B", 7.814100e-09)
mat1.add_element("Cd", 3.758200e-10)
mat1.add_element("Cl", 3.403200e-08)
mat1.add_element("Ca", 4.516800e-08)
mat1.add_element("Cr", 1.740800e-07)
mat1.add_element("Gd", 3.837600e-10)
mat1.add_element("Ga", 4.328200e-07)
mat1.add_element("Fe", 7.562900e-07)
mat1.add_element("F", 3.176500e-07)
mat1.add_element("Mg", 4.963900e-08)
mat1.add_element("Mn", 1.647600e-08)
mat1.add_element("Ni", 1.028200e-07)
mat1.add_element("P", 1.948500e-07)
mat1.add_element("K", 1.543700e-08)
mat1.add_element("S", 1.881700e-07)
mat1.add_element("Si", 1.074400e-07)
mat1.add_element("Na", 7.873400e-08)
mat1.add_nuclide("U235", 7.701700e-09)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.988100e-02)
mat2.add_element("Si", 3.777000e-04)
mat2.add_element("Cu", 5.136400e-05)
mat2.add_element("Zn", 2.495800e-05)
mat2.add_element("Mn", 1.485300e-05)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf3

# ALUM
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

root_universe = openmc.Universe(cells=[cell1, cell2])
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
