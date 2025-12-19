"""
PU-SOL-THERM-023 (Case 23)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Inner Sol'n
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.231900e-09)
mat1.add_nuclide("Pu239", 1.604100e-05)
mat1.add_nuclide("Pu240", 7.077600e-07)
mat1.add_nuclide("Pu241", 4.692800e-08)
mat1.add_nuclide("Pu242", 2.655300e-09)
mat1.add_nuclide("Am241", 1.167300e-08)
mat1.add_element("N", 2.279500e-03)
mat1.add_nuclide("H1", 6.139400e-02)
mat1.add_nuclide("O16", 3.643100e-02)
mat1.add_element("Fe", 5.391600e-07)
mat1.add_element("Cr", 1.447700e-07)
mat1.add_element("Ni", 7.125600e-08)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Driver Sol'n
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu238", 2.158900e-08)
mat2.add_nuclide("Pu239", 2.811200e-04)
mat2.add_nuclide("Pu240", 1.240400e-05)
mat2.add_nuclide("Pu241", 8.338900e-07)
mat2.add_nuclide("Pu242", 4.653500e-08)
mat2.add_nuclide("Am241", 1.931200e-07)
mat2.add_element("N", 2.417900e-03)
mat2.add_nuclide("H1", 6.073600e-02)
mat2.add_nuclide("O16", 3.701100e-02)
mat2.add_element("Fe", 4.205500e-06)
mat2.add_element("Cr", 1.129200e-06)
mat2.add_element("Ni", 5.558000e-07)
mat2.add_s_alpha_beta("c_H_in_H2O")

# SST Type
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 5.868600e-02)
mat3.add_element("Cr", 1.646900e-02)
mat3.add_element("Ni", 8.106100e-03)
mat3.add_element("Mn", 1.731900e-03)
mat3.add_element("Si", 1.693900e-03)
mat3.add_element("C", 1.584400e-03)
mat3.add_element("P", 6.143900e-05)
mat3.add_element("S", 4.450400e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.670800e-02)
mat4.add_nuclide("O16", 3.335400e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLNI
cell1 = openmc.Cell(cell_id=1, fill=mat1)
# SST
cell2 = openmc.Cell(cell_id=2, fill=mat3)
# SOLND
cell3 = openmc.Cell(cell_id=3, fill=mat2)
# SST
cell4 = openmc.Cell(cell_id=4, fill=mat3)
# WATER
cell5 = openmc.Cell(cell_id=5, fill=mat4)
# SST
cell6 = openmc.Cell(cell_id=6, fill=mat3)
root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6])
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
source.space = openmc.stats.Point((0.0, 0.0, 14.3))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
