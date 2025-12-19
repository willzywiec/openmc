"""
PU-SOL-THERM-009 (Case 2) 8.647 kg Pu(97.5) @ H/X = 2777 in a bare 48" Al-1100 sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 9.652600e-10)
mat1.add_nuclide("Pu239", 2.340200e-05)
mat1.add_nuclide("Pu240", 6.032700e-07)
mat1.add_nuclide("Pu241", 1.787300e-08)
mat1.add_nuclide("Pu242", 3.322400e-09)
mat1.add_element("N", 7.695100e-04)
mat1.add_nuclide("H1", 6.503100e-02)
mat1.add_nuclide("O16", 3.449300e-02)
mat1.add_element("Al", 2.129300e-06)
mat1.add_element("B", 7.438900e-09)
mat1.add_element("Cd", 3.577800e-10)
mat1.add_element("Cl", 3.239900e-08)
mat1.add_element("Ca", 4.300000e-08)
mat1.add_element("Cr", 1.657200e-07)
mat1.add_element("Gd", 3.653400e-10)
mat1.add_element("Ga", 4.120400e-07)
mat1.add_element("Fe", 7.199900e-07)
mat1.add_element("F", 3.024000e-07)
mat1.add_element("Mg", 4.725600e-08)
mat1.add_element("Mn", 1.568500e-08)
mat1.add_element("Ni", 9.788100e-08)
mat1.add_element("P", 1.854900e-07)
mat1.add_element("K", 1.469600e-08)
mat1.add_element("S", 1.791400e-07)
mat1.add_element("Si", 1.022800e-07)
mat1.add_element("Na", 7.495400e-08)
mat1.add_nuclide("U235", 7.332000e-09)
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

surf1 = openmc.Sphere(surface_id=1, r=60.964)
surf2 = openmc.Sphere(surface_id=2, r=61.734, boundary_type="vacuum")
surf3 = openmc.ZPlane(surface_id=3, z0=45.3705)

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
