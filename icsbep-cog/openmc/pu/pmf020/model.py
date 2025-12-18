"""
PU-MET-FAST-020:  Sphere of Pu Reflected by Depleted Uranium at VNIITF
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

# D38 ----- Table 10
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 2.378700e-04)
mat2.add_nuclide("U238", 4.673800e-02)

# Duralum - Table ll
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.807700e-02)
mat3.add_element("Mg", 1.033200e-03)
mat3.add_element("Mn", 1.828400e-04)
mat3.add_element("Cu", 1.132900e-03)

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
cell1.region = +surf1 & -surf2 & -surf6

# Pu
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf10 & +surf11 & -surf12

# D38
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & -surf3 & -surf6 & +surf7

# D38
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf3 & -surf4 & -surf6

# D38
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf10 & +surf12 & -surf13 & +surf15

# D38
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf10 & +surf13 & -surf14 & +surf16

# Al
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf4 & -surf5 & -surf6 & -surf8

# A1
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = +surf5 & -surf9

# STL
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = -surf10 & -surf17

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9])
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
