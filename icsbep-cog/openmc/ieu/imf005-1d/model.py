"""
IEU-MET-FAST-005-1D: Spherical assembly of 177.675 kg U(36) reflected by 241.360 kg steel [Detailed Model] Rev. 2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 1st U(36) layer
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.581300e-04)
mat1.add_nuclide("U235", 1.732000e-02)
mat1.add_nuclide("U238", 2.978300e-02)
mat1.add_element("W", 1.220000e-05)
mat1.add_element("Fe", 1.606500e-04)
mat1.add_element("C", 4.668500e-04)
mat1.add_element("Cu", 1.631500e-04)
mat1.add_element("Ni", 1.766500e-04)

# 2nd U(36) layer
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 1.567700e-04)
mat2.add_nuclide("U235", 1.719400e-02)
mat2.add_nuclide("U238", 2.950800e-02)
mat2.add_element("W", 1.209500e-05)
mat2.add_element("Fe", 1.592600e-04)
mat2.add_element("C", 3.702600e-04)
mat2.add_element("Cu", 2.744000e-04)
mat2.add_element("Ni", 2.971000e-04)

# 3rd U(36) layer
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U234", 1.558100e-04)
mat3.add_nuclide("U235", 1.717400e-02)
mat3.add_nuclide("U238", 2.923500e-02)
mat3.add_element("W", 1.202100e-05)
mat3.add_element("Fe", 1.582900e-04)
mat3.add_element("C", 5.520100e-04)
mat3.add_element("Cu", 2.089300e-04)
mat3.add_element("Ni", 2.262100e-04)

# 4th U(36) layer
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U234", 1.325600e-04)
mat4.add_nuclide("U235", 1.714100e-02)
mat4.add_nuclide("U238", 2.941700e-02)
mat4.add_element("W", 1.205400e-05)
mat4.add_element("Fe", 1.190400e-04)
mat4.add_element("C", 7.380200e-04)
mat4.add_element("Cu", 1.942300e-04)
mat4.add_element("Ni", 2.103000e-04)

# 5th U(36) layer
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U234", 1.600400e-04)
mat5.add_nuclide("U235", 1.712100e-02)
mat5.add_nuclide("U238", 2.915900e-02)
mat5.add_element("W", 5.992000e-06)
mat5.add_element("Fe", 9.863000e-05)
mat5.add_element("C", 5.503100e-04)
mat5.add_element("Cu", 3.367300e-04)
mat5.add_element("Ni", 3.645900e-04)

# 6th U(36) layer
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("U234", 1.723500e-04)
mat6.add_nuclide("U235", 1.695800e-02)
mat6.add_nuclide("U238", 2.880600e-02)
mat6.add_element("W", 1.186000e-05)
mat6.add_element("Fe", 9.760700e-05)
mat6.add_element("C", 9.076700e-04)
mat6.add_element("Cu", 3.593400e-04)
mat6.add_element("Ni", 3.890700e-04)

# 1st steel layer
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Fe", 7.928500e-02)
mat7.add_element("C", 1.125100e-03)
mat7.add_element("Si", 1.603800e-04)
mat7.add_element("Cr", 2.598900e-04)
mat7.add_element("Mn", 3.279600e-04)
mat7.add_element("Ni", 2.302500e-04)
mat7.add_element("Cu", 2.126500e-04)

# 2nd steel layer
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Fe", 8.038800e-02)
mat8.add_element("C", 1.140700e-03)
mat8.add_element("Si", 1.626100e-04)
mat8.add_element("Cr", 2.635100e-04)
mat8.add_element("Mn", 3.325300e-04)
mat8.add_element("Ni", 2.334500e-04)
mat8.add_element("Cu", 2.156100e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=2.686)
surf2 = openmc.Sphere(surface_id=2, r=6.000)
surf3 = openmc.Sphere(surface_id=3, r=7.550)
surf4 = openmc.Sphere(surface_id=4, r=9.150)
surf5 = openmc.Sphere(surface_id=5, r=11.00)
surf6 = openmc.Sphere(surface_id=6, r=12.25)
surf7 = openmc.Sphere(surface_id=7, r=13.25)
surf8 = openmc.Sphere(surface_id=8, r=15.00)
surf9 = openmc.Sphere(surface_id=9, r=21.50, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# L1
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# L2
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

# L3
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf3 & -surf4

# L4
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf4 & -surf5

# L5
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf5 & -surf6

# L6
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf6 & -surf7

# STL1
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = +surf7 & -surf8

# STL2
cell8 = openmc.Cell(cell_id=8, fill=mat8)
cell8.region = +surf8 & -surf9

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8])
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
