"""
IEU-MET-FAST-021-1s: Rev. 1: FR0 4-S; simplified homogeous cylindrical benchmark
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# ID=1
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 8.513500e-05)
mat1.add_nuclide("U235", 8.498300e-03)
mat1.add_nuclide("U238", 3.337600e-02)
mat1.add_element("C", 4.354500e-05)
mat1.add_element("F", 8.709000e-05)
mat1.add_element("Fe", 3.967100e-03)
mat1.add_element("Cr", 1.080200e-03)
mat1.add_element("Ni", 5.051000e-04)
mat1.add_element("Mn", 5.680000e-05)
mat1.add_element("Si", 5.555300e-05)

# ID=2
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 2.323600e-06)
mat2.add_nuclide("U235", 3.040600e-04)
mat2.add_nuclide("U238", 4.192400e-02)
mat2.add_element("Fe", 3.967100e-03)
mat2.add_element("Cr", 1.080200e-03)
mat2.add_element("Ni", 5.051000e-04)
mat2.add_element("Mn", 5.680000e-05)
mat2.add_element("Si", 5.555300e-05)

# ID=3 (Nat-U)
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U234", 2.379700e-06)
mat3.add_nuclide("U235", 3.114000e-04)
mat3.add_nuclide("U238", 4.293700e-02)

# ID=4 (Al)
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 1.071300e-02)
mat4.add_element("Fe", 3.967100e-03)
mat4.add_element("Cr", 1.080200e-03)
mat4.add_element("Ni", 5.051000e-04)
mat4.add_element("Mn", 5.680000e-05)
mat4.add_element("Si", 5.555300e-05)

# ID=5 (SST)
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 3.967100e-03)
mat5.add_element("Cr", 1.080200e-03)
mat5.add_element("Ni", 5.051000e-04)
mat5.add_element("Mn", 5.680000e-05)
mat5.add_element("Si", 5.555300e-05)

# ID=6 (IEB)
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 5.655400e-02)
mat6.add_element("Cr", 1.540000e-02)
mat6.add_element("Ni", 7.200600e-03)
mat6.add_element("Mn", 8.097200e-04)
mat6.add_element("Si", 7.919400e-04)

# ID=7 (OEB)
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Fe", 4.761000e-02)
mat7.add_element("Cr", 1.296400e-02)
mat7.add_element("Ni", 6.061800e-03)
mat7.add_element("Mn", 6.816600e-04)
mat7.add_element("Si", 6.667000e-04)

# ID=8 (FE)
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Fe", 8.410900e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================

# ID1
surf1 = openmc.ZCylinder(surface_id=1, x0=-17.204, y0=17.204, r=16.745)
# ID2
surf2 = openmc.ZCylinder(surface_id=2, x0=-30.104, y0=30.104, r=19.635)
# ID3
surf3 = openmc.ZCylinder(surface_id=3, x0=-30.104, y0=30.104, r=27.077)
# ID4
surf4 = openmc.ZCylinder(surface_id=4, x0=-57.650, y0=-30.104, r=27.077)
# ID5
surf5 = openmc.ZCylinder(surface_id=5, x0=30.104, y0=58.050, r=27.077)
# ID6
surf6 = openmc.ZCylinder(surface_id=6, x0=-59.950, y0=60.050, r=27.077)
# ID7
surf7 = openmc.ZCylinder(surface_id=7, x0=-61.750, y0=61.750, r=27.077)
# ID8; top
surf8 = openmc.ZCylinder(surface_id=8, x0=61.750, y0=64.550, r=27.077)
# ID8; inner
surf9 = openmc.ZCylinder(surface_id=9, x0=-61.5535, y0=64.7465, r=68.4)
# ID8; outer
surf10 = openmc.ZCylinder(surface_id=10, x0=-77.5535, y0=64.7465, r=70.0, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# ID1
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# ID2
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2 & -surf3

# ID3
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf1 & +surf2 & -surf3

# ID4
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf1 & +surf2 & +surf3 & -surf4

# ID5
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf1 & +surf2 & +surf3 & -surf5

# ID6
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & -surf6

# ID7
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & +surf6 & -surf7

# ID8
cell8 = openmc.Cell(cell_id=8, fill=mat8)
cell8.region = +surf7 & -surf8 & -surf9 & -surf10

# ID8
cell9 = openmc.Cell(cell_id=9, fill=mat8)
cell9.region = +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & +surf6 & +surf7 & +surf8 & +surf9 & -surf10

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
