"""
PMF028-1S: 1.176cm void; 9.8375 kg delta-239Pu(89%); 19.65cm Steel reflector; simplified model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# d-Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu241", 3.913900e-04)
mat1.add_element("Ga", 2.239100e-03)
mat1.add_element("Fe", 4.553800e-04)
mat1.add_element("C", 9.165300e-04)
mat1.add_element("Ni", 1.426100e-03)

# Steel
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 7.949900e-02)
mat2.add_element("C", 1.128100e-03)
mat2.add_element("Si", 1.608100e-04)
mat2.add_element("Cr", 2.605900e-04)
mat2.add_element("Mn", 3.288500e-04)
mat2.add_element("Ni", 2.308700e-04)
mat2.add_element("Cu", 2.132300e-04)

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
source.space = openmc.stats.Box((-3.0, -3.0, -3.0), (3.0, 3.0, 3.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
