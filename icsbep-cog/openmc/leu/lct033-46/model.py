"""
LCT033-46: U(2)F4-6, Unreflected
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(2)F4-6
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 6.228200e-05)
mat1.add_nuclide("U238", 3.012600e-03)
mat1.add_nuclide("U234", 6.254800e-07)
mat1.add_nuclide("H1", 6.058600e-02)
mat1.add_element("C", 2.912800e-02)
mat1.add_element("F", 1.230200e-02)
mat1.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.model.RectangularParallelepiped(-50.985, 50.985, -50.925, 50.925, -33.32, 33.32, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# UF4+
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
