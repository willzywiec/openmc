"""
PMF038-1S: Simplified model of the BeRP ball reflected by 8.5cm of beryllium
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Alpha
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 9.870900e-06)
mat1.add_nuclide("Pu239", 4.606800e-02)
mat1.add_nuclide("Pu240", 2.912100e-03)
mat1.add_nuclide("Pu241", 9.779300e-05)
mat1.add_nuclide("Pu242", 1.359000e-05)
mat1.add_nuclide("Am241", 5.535000e-05)

# SS-304 Cladding
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cr", 1.703800e-02)
mat2.add_element("Fe", 5.858700e-02)
mat2.add_element("Ni", 7.348700e-03)

# Beryllium, Inner Hemispheres
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Be", 1.239700e-01)

# Beryllium, Outer Hemispheres
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Be", 1.246500e-01)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Pu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# SS304
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

# SS304
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf3 & -surf4

# Be
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf5 & +surf6 & -surf7

# Be
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = -surf8 & +surf9 & -surf10

# Be
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf11 & +surf12 & -surf13 & -surf14

# Be
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf11 & +surf12 & -surf13 & +surf14 & +surf15

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7])
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
