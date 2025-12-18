"""
IEU-MET-FAST-005-1S: Spherical assembly of 177.997 kg U(36) reflected by 241.360 kg steel [Simplified Model] Rev. 2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(36)
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.551100e-04)
mat1.add_nuclide("U235", 1.715400e-02)
mat1.add_nuclide("U238", 2.929700e-02)
mat1.add_element("W", 1.071100e-05)
mat1.add_element("Fe", 1.232400e-04)
mat1.add_element("C", 6.494500e-04)
mat1.add_element("Cu", 2.679100e-04)
mat1.add_element("Ni", 2.900800e-04)

# 1st steel layer
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 7.928500e-02)
mat2.add_element("C", 1.125100e-03)
mat2.add_element("Si", 1.603800e-04)
mat2.add_element("Cr", 2.598900e-04)
mat2.add_element("Mn", 3.279600e-04)
mat2.add_element("Ni", 2.302500e-04)
mat2.add_element("Cu", 2.126500e-04)

# 2nd steel layer
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 8.038800e-02)
mat3.add_element("C", 1.140700e-03)
mat3.add_element("Si", 1.626100e-04)
mat3.add_element("Cr", 2.635100e-04)
mat3.add_element("Mn", 3.325300e-04)
mat3.add_element("Ni", 2.334500e-04)
mat3.add_element("Cu", 2.156100e-04)

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.Sphere(surface_id=1, r=2.686)
surf2 = openmc.Sphere(surface_id=2, r=13.25)
surf3 = openmc.Sphere(surface_id=3, r=15.00)
surf4 = openmc.Sphere(surface_id=4, r=21.50, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U36
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# STL1
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

# STL2
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf3 & -surf4

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
source.space = openmc.stats.Box((-4.0, -4.0, -4.0), (4.0, 4.0, 4.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
