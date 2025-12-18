"""
U233-MET-FAST-004: 10.012 kg 233U(98.2) + 2.4384 cm W-Alloy
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U-233   per Table 2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_element("P", 1.862100e+01)
mat1.add_nuclide("U233", 9.820000e+01)
mat1.add_nuclide("U234", 1.100000e+00)
mat1.add_nuclide("U238", 7.000000e-01)

# W-Alloy per Table 3
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("P", 1.721000e+01)
mat2.add_element("W", 9.130000e+01)
mat2.add_element("Ni", 5.500000e+00)
mat2.add_element("Cu", 2.500000e+00)
mat2.add_element("Zr", 7.000000e-01)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Dimensions per
surf1 = openmc.Sphere(surface_id=1, r=5.0444)
# Section 3.2.1
surf2 = openmc.Sphere(surface_id=2, r=7.4828, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U233
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# W
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
