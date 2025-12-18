"""
IEU-MET-FAST-022-2: FR0 5-S; simplified homogeous cylindrical benchmark; C/X=5.5; H/X=1.2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U20
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.966300e-05)
mat1.add_nuclide("U235", 4.957500e-03)
mat1.add_nuclide("U238", 1.947000e-02)
mat1.add_element("C", 2.817900e-05)
mat1.add_element("F", 5.635800e-05)
mat1.add_element("C", 2.447400e-02)
mat1.add_element("C", 2.991900e-03)
mat1.add_element("H", 5.984000e-03)
mat1.add_element("Fe", 3.907000e-03)
mat1.add_element("Cr", 1.063900e-03)
mat1.add_element("Ni", 4.974500e-04)
mat1.add_element("Mn", 5.593900e-05)
mat1.add_element("Si", 5.471100e-05)

# CU
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cu", 7.450500e-02)
mat2.add_element("Ag", 7.036700e-05)
mat2.add_nuclide("O16", 1.186000e-04)
mat2.add_element("Fe", 3.907000e-03)
mat2.add_element("Cr", 1.063900e-03)
mat2.add_element("Ni", 4.974500e-04)
mat2.add_element("Mn", 5.593900e-05)
mat2.add_element("Si", 5.471100e-05)

# IV
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 3.907000e-03)
mat3.add_element("Cr", 1.063900e-03)
mat3.add_element("Ni", 4.974500e-04)
mat3.add_element("Mn", 5.593900e-05)
mat3.add_element("Si", 5.471100e-05)

# IEB
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 5.677700e-02)
mat4.add_element("Cr", 1.546000e-02)
mat4.add_element("Ni", 7.228900e-03)
mat4.add_element("Mn", 8.129000e-04)
mat4.add_element("Si", 7.950600e-04)

# OEB
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 5.312800e-02)
mat5.add_element("Cr", 1.446700e-02)
mat5.add_element("Ni", 6.764300e-03)
mat5.add_element("Mn", 7.606600e-04)
mat5.add_element("Si", 7.439600e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# (U20)
surf1 = openmc.ZCylinder(surface_id=1, x0=-19.3545, y0=19.3545, r=18.0024)
# Copper (CU)
surf2 = openmc.ZCylinder(surface_id=2, x0=-59.00, y0=59.00, r=51.114)
# Void Region (VR)
surf3 = openmc.ZCylinder(surface_id=3, x0=-61.15, y0=61.15, r=51.114)
# Inside End Blocks (IEB)
surf4 = openmc.ZCylinder(surface_id=4, x0=-63.10, y0=63.10, r=51.114)
# Outside End Blocks (OEB)
surf5 = openmc.ZCylinder(surface_id=5, x0=-64.85, y0=64.85, r=51.114, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U20
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Cu
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2 & -surf3 & -surf4 & -surf5

# VR
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3 & -surf4 & -surf5

# IEB
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf2 & +surf3 & -surf4 & -surf5

# OEB
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf2 & +surf3 & +surf4 & -surf5

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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
