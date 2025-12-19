"""
PU-MET-FAST-044: Case 2 THOR Pu sphere with Fe + Poly Reflector
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_element("Ga", 1.288000e-03)
mat1.add_nuclide("Pu239", 3.702800e-02)
mat1.add_nuclide("Pu240", 1.993100e-03)
mat1.add_nuclide("Pu241", 1.359400e-04)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Ni", 1.296200e-01)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 8.583400e-02)

mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 4.121600e-02)
mat4.add_nuclide("H1", 8.243100e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
# clad
cell2 = openmc.Cell(cell_id=2, fill=mat2)
# refl
cell3 = openmc.Cell(cell_id=3, fill=mat3)
# poly
cell4 = openmc.Cell(cell_id=4, fill=mat4)
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
