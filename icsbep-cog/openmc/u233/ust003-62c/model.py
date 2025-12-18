"""
U233-SOL-THERM-003 (Exp't 62 in 9"-Diam. Vessel) 608 g U-233 @ H/X = 392
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 233U(98.7)O2F2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 1.673700e-04)
mat1.add_nuclide("U234", 7.803600e-07)
mat1.add_nuclide("U238", 1.492900e-06)
mat1.add_nuclide("H1", 6.560900e-02)
mat1.add_nuclide("O16", 3.314400e-02)
mat1.add_element("F", 4.989900e-04)
mat1.add_element("Al", 4.275200e-05)
mat1.add_element("Cr", 6.474300e-07)
mat1.add_element("Fe", 5.648600e-06)
mat1.add_element("Mg", 2.663500e-07)
mat1.add_element("Mo", 2.453700e-07)
mat1.add_element("Na", 1.548700e-05)
mat1.add_element("Ni", 5.013600e-07)
mat1.add_element("Sn", 2.230900e-07)
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
mat3.add_nuclide("O16", 3.841900e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Al2S
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# Prffn
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3

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
source.space = openmc.stats.Point((0.0, 0.0, 11.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
