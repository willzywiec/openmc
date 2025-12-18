"""
PU-SOL-THERM-011 (Case 18-2) 1.140 kg Pu(95.80) @ H/X = 1151 in a bare 18" SS347 + 0.020" Cd sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 5.615900e-05)
mat1.add_nuclide("Pu240", 2.451800e-06)
mat1.add_element("N", 9.495700e-04)
mat1.add_nuclide("H1", 6.465900e-02)
mat1.add_nuclide("O16", 3.482000e-02)
mat1.add_element("Fe", 1.358700e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 6.038600e-02)
mat2.add_element("Cr", 1.667800e-02)
mat2.add_element("Ni", 9.850400e-03)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cd", 4.634000e-02)

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

# SS347
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = 

# CD
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
