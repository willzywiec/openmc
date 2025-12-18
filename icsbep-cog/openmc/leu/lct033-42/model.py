"""
LCT033-42: U(2)F4-5, Unreflected
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(2)F4-5
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 8.667500e-05)
mat1.add_nuclide("U238", 4.192600e-03)
mat1.add_nuclide("U234", 8.704600e-07)
mat1.add_nuclide("H1", 5.315500e-02)
mat1.add_element("C", 2.555500e-02)
mat1.add_element("F", 1.712000e-02)
mat1.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.model.RectangularParallelepiped(-30.65, 30.65, -33.27, 33.27, -33.26, 33.26, boundary_type="vacuum")

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
