"""
PU-MET-FAST-002: DIRTY JEZEBEL (19.460 kg Pu(20.1 at-% Pu-240)-1.01Ga @ 15.73 g/cc)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_element("Ga", 1.372200e-03)
mat1.add_nuclide("Pu239", 2.993400e-02)
mat1.add_nuclide("Pu240", 7.875400e-03)
mat1.add_nuclide("Pu241", 1.214600e-03)
mat1.add_nuclide("Pu242", 1.567200e-04)

materials = openmc.Materials([mat1])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# per Section 3.2
surf1 = openmc.Sphere(surface_id=1, r=6.6595, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# alloy
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
