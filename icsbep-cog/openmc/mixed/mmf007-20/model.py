"""
MixMF007-20: 4.664 kg alpha-Pu; 6.200 kg HEU; 2.09 cm Be
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# alpha-Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.553600e-02)
mat1.add_nuclide("Pu240", 2.771900e-03)
mat1.add_nuclide("Pu241", 1.731300e-04)

# HEU
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 4.440100e-02)
mat2.add_nuclide("U238", 3.213700e-03)

# Be
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Be", 1.229500e-01)

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# alpha-Pu
# surf1: Unsupported surface type "s" with params ['3.8673']
# HEU
# surf2: Unsupported surface type "s" with params ['5.1604']
# Be
# surf3: Unsupported surface type "s" with params ['7.2504']

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# aPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
# HEU
cell2 = openmc.Cell(cell_id=2, fill=mat2)
# Be
cell3 = openmc.Cell(cell_id=3, fill=mat3)
root_universe = openmc.Universe(cells=[cell1, cell2, cell3])
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
