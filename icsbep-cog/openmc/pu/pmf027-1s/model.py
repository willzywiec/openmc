"""
PMF027-1S: 0.985cm void; 9.8815 kg delta-239Pu(89%); 5.58cm CH2 Reflector; simplified model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# d-Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu241", 3.913000e-04)
mat1.add_element("Ga", 2.239100e-03)
mat1.add_element("Ni", 1.429200e-03)
mat1.add_element("Fe", 4.551400e-04)
mat1.add_element("C", 9.159100e-04)

# CH2 inner
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 3.822200e-02)
mat2.add_nuclide("H1", 7.644300e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

# CH2 outer
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 3.864300e-02)
mat3.add_nuclide("H1", 7.728500e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# dPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
# CH2
cell2 = openmc.Cell(cell_id=2, fill=mat2)
# CH2
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
source.space = openmc.stats.Box((-3.0, -3.0, -3.0), (3.0, 3.0, 3.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
