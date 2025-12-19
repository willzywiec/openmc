"""
PU-SOL-THERM-021 (Case 8) 5.357 kg Pu(95.4) @ H/X = 131 bare sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 2.615300e-08)
mat1.add_nuclide("Pu239", 4.124900e-04)
mat1.add_nuclide("Pu240", 2.018100e-05)
mat1.add_nuclide("Pu241", 1.218100e-06)
mat1.add_nuclide("Pu242", 3.857900e-08)
mat1.add_element("N", 4.722800e-03)
mat1.add_nuclide("H1", 5.416000e-02)
mat1.add_nuclide("O16", 3.975500e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.Sphere(surface_id=1, r=19.5064, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

root_universe = openmc.Universe(cells=[cell1])
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
