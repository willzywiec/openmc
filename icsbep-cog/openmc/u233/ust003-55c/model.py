"""
U233-SOL-THERM-003 (Exp't 55 in 6.5"-Diam. Vessel) 2162 g U-233 @ H/X = 39
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 233U(98.7)O2F2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 1.552500e-03)
mat1.add_nuclide("U234", 7.238400e-06)
mat1.add_nuclide("U238", 1.384700e-05)
mat1.add_nuclide("H1", 6.051300e-02)
mat1.add_nuclide("O16", 3.340400e-02)
mat1.add_element("F", 3.336400e-03)
mat1.add_element("Al", 4.874200e-05)
mat1.add_element("Cr", 7.117300e-07)
mat1.add_element("Fe", 5.975600e-06)
mat1.add_element("Mg", 2.691500e-07)
mat1.add_element("Mo", 2.479400e-07)
mat1.add_element("Na", 2.621900e-05)
mat1.add_element("Ni", 5.066100e-07)
mat1.add_element("Sn", 2.254300e-07)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Unichrome
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 5.284300e-02)
mat2.add_element("C", 3.319500e-02)
mat2.add_nuclide("O16", 3.952100e-03)
mat2.add_element("Cl", 5.507900e-03)
mat2.add_s_alpha_beta("c_H_in_CH2")

# Al-2S
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.988100e-02)
mat3.add_element("Si", 5.810800e-04)

# Paraffin
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 7.991100e-02)
mat4.add_nuclide("O16", 3.841900e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

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

# UNCHRM
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = 

# Al2S
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = 

# Prffn
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5])
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
source.space = openmc.stats.Point((0.0, 0.0, 8.35))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
