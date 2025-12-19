"""
ICT016-4: 22.86 x 22.86 x 31.2166 U(30.14)O2/wax parallelepiped with 20.32 cm Polythene on bottom & sides - bare on top - batch 80L
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Batch 80L
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 5.124700e-02)
mat1.add_element("C", 2.538600e-02)
mat1.add_nuclide("O16", 4.369300e-03)
mat1.add_element("Al", 5.994400e-05)
mat1.add_nuclide("U234", 8.002200e-06)
mat1.add_nuclide("U235", 6.319900e-04)
mat1.add_nuclide("U236", 1.461600e-06)
mat1.add_nuclide("U238", 1.437000e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

# Polythene
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 7.891100e-02)
mat2.add_nuclide("O16", 3.495500e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.model.RectangularParallelepiped(-11.43, 11.43, -11.43, 11.43, -15.6083, 15.6083)
surf2 = openmc.model.RectangularParallelepiped(-31.75, 31.75, -31.75, 31.75, -35.9283, 35.9283, boundary_type="vacuum")
surf3 = openmc.ZPlane(surface_id=3, z0=15.6083)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# UO2WAX
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# POLY
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2 & -surf3

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
