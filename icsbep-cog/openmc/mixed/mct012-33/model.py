"""
MCT012-33: MOX/Polystyrene (H/SQRT(LxW)=0.67) with H/X=172, bare
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 2.573200e-04)
mat1.add_nuclide("Pu240", 2.294500e-05)
mat1.add_nuclide("Pu241", 1.719900e-06)
mat1.add_nuclide("Pu242", 1.048600e-07)
mat1.add_nuclide("U235", 1.007900e-06)
mat1.add_nuclide("U238", 6.599300e-04)
mat1.add_nuclide("Am241", 3.159000e-07)
mat1.add_nuclide("H1", 4.466000e-02)
mat1.add_element("C", 4.534500e-02)
mat1.add_nuclide("O16", 1.973100e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Core
surf1 = openmc.model.RectangularParallelepiped(-22.905, 22.905, -25.45, 25.45, -16.245, 16.245, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
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
