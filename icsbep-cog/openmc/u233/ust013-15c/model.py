"""
U233-SOL-THERM-013: Case No. 15 (Experment No. 168)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 233U(97.5)O2(NO3)2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U232", 1.668800e-09)
mat1.add_nuclide("U233", 2.505000e-04)
mat1.add_nuclide("U234", 2.677400e-06)
mat1.add_nuclide("U235", 6.620400e-08)
mat1.add_nuclide("U236", 2.535500e-09)
mat1.add_nuclide("U238", 3.484500e-06)
mat1.add_element("Th", 3.220900e-06)
mat1.add_nuclide("H1", 6.448400e-02)
mat1.add_element("N", 5.939300e-04)
mat1.add_nuclide("O16", 3.450300e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Heresite
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 4.057500e-02)
mat2.add_element("C", 4.057500e-02)
mat2.add_nuclide("O16", 7.438700e-03)
mat2.add_element("Fe", 6.762400e-04)
mat2.add_s_alpha_beta("c_H_in_CH2")

# Al-1100
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.974600e-02)
mat3.add_element("Si", 2.753900e-04)
mat3.add_element("Mn", 1.482000e-05)
mat3.add_element("Fe", 1.385000e-04)
mat3.add_element("Cu", 3.203000e-05)
mat3.add_element("Zn", 2.490200e-05)

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Solution
surf1 = openmc.Sphere(surface_id=1, r=15.7983)
# Heresite
surf2 = openmc.Sphere(surface_id=2, r=15.8743)
# Al-1100
surf3 = openmc.Sphere(surface_id=3, r=16.0013, boundary_type="vacuum")
surf4 = openmc.ZPlane(surface_id=4, z0=26.759)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Air
cell1 = openmc.Cell(cell_id=1)
cell1.region = -surf1 & +surf4

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = -surf1 & -surf4

# Hrst
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf1 & -surf2

# Alum
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf2 & -surf3

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4])
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
