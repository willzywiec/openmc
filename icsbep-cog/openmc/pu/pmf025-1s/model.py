"""
PMF025-1S: 1.550cm steel reflected spherical assembly of 13.847 kg delta-239Pu(98%): simplified model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.670400e-02)
mat1.add_nuclide("Pu240", 6.700900e-04)
mat1.add_element("Ga", 2.201300e-03)
mat1.add_element("Fe", 1.415900e-04)
mat1.add_element("C", 2.903800e-04)
mat1.add_element("Ni", 1.979400e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 7.955700e-02)
mat2.add_element("C", 1.128900e-03)
mat2.add_element("Si", 1.609300e-04)
mat2.add_element("Cr", 2.607800e-04)
mat2.add_element("Mn", 3.290900e-04)
mat2.add_element("Ni", 2.310400e-04)
mat2.add_element("Cu", 2.133800e-04)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# dPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
# Steel
cell2 = openmc.Cell(cell_id=2, fill=mat2)
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
