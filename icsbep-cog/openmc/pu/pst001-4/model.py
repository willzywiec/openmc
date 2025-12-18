"""
PU-SOL-THERM-001 (Case 4) 1.696 kg Pu(95.3) @ H/X = 190 in a water reflected l1.5" SS304L sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 2.003600e-08)
mat1.add_nuclide("Pu239", 3.159400e-04)
mat1.add_nuclide("Pu240", 1.545800e-05)
mat1.add_nuclide("Pu241", 1.005800e-06)
mat1.add_nuclide("Pu242", 2.955600e-08)
mat1.add_element("N", 2.714600e-03)
mat1.add_nuclide("H1", 6.016400e-02)
mat1.add_nuclide("O16", 3.753300e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.935500e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Ni", 7.720300e-03)
mat2.add_element("Mn", 1.736300e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.665500e-02)
mat3.add_nuclide("O16", 3.332700e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOLN
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = 

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = 

# WATER
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = 

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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
