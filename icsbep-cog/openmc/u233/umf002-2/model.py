"""
U233-MET-FAST-002: 7.601 kg 233U(98.2) + 1.9888 cm Oy
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U-233 per Table 2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_element("P", 1.864400e+01)
mat1.add_nuclide("U233", 9.820000e+01)
mat1.add_nuclide("U234", 1.100000e+00)
mat1.add_nuclide("U238", 7.000000e-01)

# U-235 per Table 3
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("P", 1.880000e+01)
mat2.add_nuclide("U235", 9.320000e+01)
mat2.add_nuclide("U238", 6.800000e+00)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Dimensions per
surf1 = openmc.Sphere(surface_id=1, r=4.5999)
# Section 3.2.2
surf2 = openmc.Sphere(surface_id=2, r=6.5877, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U233
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Oy
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
