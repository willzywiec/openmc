"""
U233-SOL-THERM-004 (Exp't 3 in 6"-Diam. Vessel) 1370 g U-233 @ H/X = 119
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# H/U-233 = 119
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 5.110600e-04)
mat1.add_nuclide("U234", 2.372600e-06)
mat1.add_nuclide("U238", 4.462400e-06)
mat1.add_nuclide("H1", 6.081500e-02)
mat1.add_nuclide("O16", 3.573100e-02)
mat1.add_element("N", 1.508000e-03)
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
# Soln
cell2 = openmc.Cell(cell_id=2, fill=mat1)
# Al2S
cell3 = openmc.Cell(cell_id=3, fill=mat2)
# Prffn
cell4 = openmc.Cell(cell_id=4, fill=mat3)
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
source.space = openmc.stats.Point((0.0, 0.0, 19.294))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
