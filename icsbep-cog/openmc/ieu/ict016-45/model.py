"""
ICT016-45: 45.8470 x 17.7800 x 17.7800 U(30.14)O2/wax parallelepiped with 20.32 cm Polythene on bottom & sides extending up to core midplane on long side & to core bottom on short side - batch 80
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Batch 80
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 6.867200e-02)
mat1.add_element("C", 3.401500e-02)
mat1.add_nuclide("O16", 5.841800e-03)
mat1.add_element("Al", 6.888200e-05)
mat1.add_nuclide("U234", 1.073000e-05)
mat1.add_nuclide("U235", 8.474100e-04)
mat1.add_nuclide("U236", 1.959800e-06)
mat1.add_nuclide("U238", 1.926900e-03)
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

surf1 = openmc.model.RectangularParallelepiped(-22.9235, 22.9235, -8.89, 8.89, -8.89, 8.89)
surf2 = openmc.model.RectangularParallelepiped(-43.2435, 43.2435, -29.21, 29.21, -29.21, 29.21, boundary_type="vacuum")
surf3 = openmc.XPlane(surface_id=3, x0=-22.9235)
surf4 = openmc.XPlane(surface_id=4, x0=22.9235)
# Core bottom
surf5 = openmc.ZPlane(surface_id=5, z0=-8.8900)
# Core midplane
surf6 = openmc.ZPlane(surface_id=6, z0=0.0000)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# UO2WAX
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# POLY
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2 & -surf3 & -surf5

# POLY
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf1 & -surf2 & +surf3 & -surf4 & -surf6

# POLY
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf1 & -surf2 & +surf4 & -surf5

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
