"""
PMF022-1S: Bare spherical assembly of 18.792 kg delta-239Pu(98%): simplified model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.662300e-02)
mat1.add_nuclide("Pu240", 6.695100e-04)
mat1.add_element("Ga", 2.197900e-03)
mat1.add_element("Fe", 1.424700e-04)
mat1.add_element("C", 2.931100e-04)
mat1.add_element("Ni", 1.862400e-03)

materials = openmc.Materials([mat1])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# dPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = 

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
source.space = openmc.stats.Box((-3.0, -3.0, -3.0), (3.0, 3.0, 3.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
