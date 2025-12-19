"""
MCT012-21: MOX/Polystyrene (H/SQRT(LxW)=1.04) with H/X=226, bare
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 1.951600e-04)
mat1.add_nuclide("Pu240", 1.701600e-05)
mat1.add_nuclide("Pu241", 1.210400e-06)
mat1.add_nuclide("Pu242", 8.035800e-08)
mat1.add_nuclide("U235", 1.903400e-06)
mat1.add_nuclide("U238", 1.251000e-03)
mat1.add_nuclide("Am241", 4.841500e-07)
mat1.add_nuclide("H1", 4.483100e-02)
mat1.add_element("C", 4.410100e-02)
mat1.add_nuclide("O16", 3.017500e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Core
surf1 = openmc.model.RectangularParallelepiped(-20.36, 20.36, -22.93, 22.93, -22.55, 22.55, boundary_type="vacuum")

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
