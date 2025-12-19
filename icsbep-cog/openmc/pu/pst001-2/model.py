"""
PU-SOL-THERM-001 (Case 2) 1.236 kg Pu(95.3) @ H/X = 271 in a water reflected 1l.5" SS304L sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.457100e-08)
mat1.add_nuclide("Pu239", 2.297700e-04)
mat1.add_nuclide("Pu240", 1.124200e-05)
mat1.add_nuclide("Pu241", 7.314800e-07)
mat1.add_nuclide("Pu242", 2.149500e-08)
mat1.add_element("N", 1.972600e-03)
mat1.add_nuclide("H1", 6.239200e-02)
mat1.add_nuclide("O16", 3.661100e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.665500e-02)
mat3.add_nuclide("O16", 3.332700e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# = Hc per Table 5
surf1 = openmc.ZPlane(surface_id=1, z0=13.3995)
surf2 = openmc.Sphere(surface_id=2, r=14.5603)
surf3 = openmc.Sphere(surface_id=3, r=14.6848)
surf4 = openmc.Sphere(surface_id=4, r=44.6848, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

# WATER
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf3 & -surf4

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
