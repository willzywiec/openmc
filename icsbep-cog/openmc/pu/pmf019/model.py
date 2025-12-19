"""
PU-MET-FAST-019: Sphere of Pu Reflected by Beryllium at VNIITF
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Materials:
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.393000e-02)
mat1.add_nuclide("Pu240", 3.504300e-03)
mat1.add_nuclide("Pu241", 3.918900e-04)
mat1.add_element("Ga", 2.210500e-03)
mat1.add_element("C", 3.024600e-04)
mat1.add_element("Fe", 3.252500e-04)
mat1.add_element("W", 7.410000e-05)
mat1.add_element("Ni", 1.418700e-03)

# Be ---- Table 1
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Be", 1.208100e-01)
mat2.add_nuclide("O16", 8.206400e-05)
mat2.add_element("C", 1.002000e-04)
mat2.add_element("Fe", 5.093900e-05)

# Cu ---- section 3.3
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cu", 8.236500e-02)

# Steel - Section 3.3
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 8.117400e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Pu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
# Be
cell2 = openmc.Cell(cell_id=2, fill=mat2)
# Be
cell3 = openmc.Cell(cell_id=3, fill=mat2)
# Cu
cell4 = openmc.Cell(cell_id=4, fill=mat3)
# STL
cell5 = openmc.Cell(cell_id=5, fill=mat4)
# STL
cell6 = openmc.Cell(cell_id=6, fill=mat4)
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
