"""
U233-SOL-THERM-004 (Exp't 28 in 7.5"-Diam. Vessel) 1559 g U-233 @ H/X = 66
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# H/U-233 = 66.414
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 8.667300e-04)
mat1.add_nuclide("U234", 4.023800e-06)
mat1.add_nuclide("U238", 7.568000e-06)
mat1.add_nuclide("H1", 5.756300e-02)
mat1.add_nuclide("O16", 3.724400e-02)
mat1.add_element("N", 2.330900e-03)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Al-2S
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.988100e-02)
mat2.add_element("Si", 5.810800e-04)

# Paraffin
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 7.991100e-02)
mat3.add_element("C", 3.841900e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Void
cell1 = openmc.Cell(cell_id=1)
cell1.region = 

# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = 

# Al2S
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = 

# Prffn
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4])
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
source.space = openmc.stats.Point((0.0, 0.0, 8.1))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
