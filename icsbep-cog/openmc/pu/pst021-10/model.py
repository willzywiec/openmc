"""
PU-SOL-THERM-021 (Case 10) 0.712 kg Pu(95.4) @ H/X = 1156 sphere in water
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 3.582100e-09)
mat1.add_nuclide("Pu239", 5.649900e-05)
mat1.add_nuclide("Pu240", 2.764200e-06)
mat1.add_nuclide("Pu241", 1.668500e-07)
mat1.add_nuclide("Pu242", 5.284200e-09)
mat1.add_element("N", 5.328200e-04)
mat1.add_nuclide("H1", 6.548200e-02)
mat1.add_nuclide("O16", 3.419200e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.665500e-02)
mat2.add_nuclide("O16", 3.332700e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.Sphere(surface_id=1, r=19.3163)
surf2 = openmc.Sphere(surface_id=2, r=49.3163, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# H2O
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
