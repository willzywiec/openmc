"""
IEU-MET-FAST-002: U(16) [average of HEU and Nat-U] cylinder reflected by Nat-U
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(16)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 8.443000e-05)
mat1.add_nuclide("U235", 7.777700e-03)
mat1.add_nuclide("U238", 3.967100e-02)

# Nat-U
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 2.643300e-06)
mat2.add_nuclide("U235", 3.460300e-04)
mat2.add_nuclide("U238", 4.771100e-02)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# U(16)
surf1 = openmc.ZCylinder(surface_id=1, x0=-15.9755, y0=15.9755, r=19.05)
# Nat-U
surf2 = openmc.ZCylinder(surface_id=2, x0=-23.5955, y0=23.4939, r=26.6446, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U16
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Nat-U
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

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
