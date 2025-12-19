"""
PU-COMP-INTER-001; HECTOR/HISS/HPG
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 1.077000e-04)
mat1.add_nuclide("B10", 1.015100e-04)
mat1.add_nuclide("B11", 4.085900e-04)
mat1.add_element("C", 7.090000e-02)
mat1.add_nuclide("O16", 2.707000e-03)
mat1.add_element("Ca", 8.280000e-04)
mat1.add_nuclide("Pu239", 2.735000e-04)
mat1.add_nuclide("Pu240", 1.549000e-05)
mat1.add_nuclide("Pu241", 1.072000e-06)
mat1.add_nuclide("Pu242", 5.800000e-08)
mat1.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.model.RectangularParallelepiped(-500.0, 500.0, -500.0, 500.0, -500.0, 500.0, boundary_type="reflecting")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# INFMEDIUM
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
