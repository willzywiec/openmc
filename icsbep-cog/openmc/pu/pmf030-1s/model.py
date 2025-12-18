"""
PMF030-1S: 8.0394 kg alpha-239Pu(88%); 4.49cm Graphite reflected; simplified model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# a-Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu241", 6.761100e-04)
mat1.add_element("Fe", 2.879700e-04)
mat1.add_element("C", 1.263000e-03)
mat1.add_element("H", 3.226800e-04)
mat1.add_element("N", 3.484000e-05)
mat1.add_nuclide("O16", 5.163300e-05)

# Graphite
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 7.721300e-02)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# aPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = 

# C
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = 

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
