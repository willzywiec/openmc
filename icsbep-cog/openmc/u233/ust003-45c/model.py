"""
U233-SOL-THERM-003 (Exp't 45 in 6.5"-Diam. Vessel) 1889 g U-233 @ H/X = 46
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 233U(98.7)O2F2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 1.340600e-03)
mat1.add_nuclide("U234", 6.250700e-06)
mat1.add_nuclide("U238", 1.195800e-05)
mat1.add_nuclide("H1", 6.104300e-02)
mat1.add_nuclide("O16", 3.323900e-02)
mat1.add_element("F", 2.850200e-03)
mat1.add_element("Al", 3.230900e-05)
mat1.add_element("Cr", 4.458500e-07)
mat1.add_element("Fe", 3.505100e-06)
mat1.add_element("Mg", 1.445200e-07)
mat1.add_element("Mo", 1.331300e-07)
mat1.add_element("Na", 2.578200e-05)
mat1.add_element("Ni", 2.720300e-07)
mat1.add_element("Sn", 1.210500e-07)
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

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# UNCHRM
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# Al2S
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3

# Prffn
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf3 & -surf4

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
source.space = openmc.stats.Point((0.0, 0.0, 8.35))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
