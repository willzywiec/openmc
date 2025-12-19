"""
PU-SOL-THERM-005 (Case 6) 0.907 kg Pu(95.95) @ H/X = 633 in a water reflected 14" SS-347 sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 9.303500e-05)
mat1.add_nuclide("Pu240", 3.910600e-06)
mat1.add_element("N", 3.255600e-03)
mat1.add_nuclide("H1", 5.893200e-02)
mat1.add_nuclide("O16", 3.779900e-02)
mat1.add_element("Fe", 1.358700e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.038600e-02)
mat2.add_element("Cr", 1.667800e-02)
mat2.add_element("Ni", 9.850400e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.662200e-02)
mat3.add_nuclide("O16", 3.331100e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=17.7865)
surf2 = openmc.Sphere(surface_id=2, r=17.9135)
surf3 = openmc.Sphere(surface_id=3, r=47.9135, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# SS347
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# WATER
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3

root_universe = openmc.Universe(cells=[cell1, cell2, cell3])
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
