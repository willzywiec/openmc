"""
ICT015-1: 30.48 x 30.48 x 28.6004 bare U(30.14)O2/wax parallelepiped - batch 16
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Batch 16
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 4.677300e-02)
mat1.add_element("C", 2.317000e-02)
mat1.add_nuclide("O16", 1.962600e-02)
mat1.add_element("Al", 5.773800e-05)
mat1.add_nuclide("U234", 3.652200e-05)
mat1.add_nuclide("U235", 2.884400e-03)
mat1.add_nuclide("U236", 6.670700e-06)
mat1.add_nuclide("U238", 6.558700e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.model.RectangularParallelepiped(-15.24, 15.24, -15.24, 15.24, -14.3002, 14.3002, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# UO2WAX
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
