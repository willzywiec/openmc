"""
IEU-MET-FAST-008-1: Spherical assembly of 178.961 kg U(36) reflected by 165.790 kg D38
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(36) layer no. 0
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_nuclide("U234", 1.231400e-04)
mat10.add_nuclide("U235", 1.651700e-02)
mat10.add_nuclide("U238", 2.832000e-02)
mat10.add_element("W", 5.805800e-06)
mat10.add_element("Fe", 2.484700e-04)
mat10.add_element("C", 5.332100e-04)
mat10.add_element("Cu", 1.177200e-03)
mat10.add_element("Ni", 1.274600e-03)

# U(36) layer no. 1
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_nuclide("U234", 1.581400e-04)
mat11.add_nuclide("U235", 1.732100e-02)
mat11.add_nuclide("U238", 2.978500e-02)
mat11.add_element("W", 1.220000e-05)
mat11.add_element("Fe", 1.606600e-04)
mat11.add_element("C", 4.668700e-04)
mat11.add_element("Cu", 1.631500e-04)
mat11.add_element("Ni", 1.766500e-04)

# U(36) layer no. 2
mat12 = openmc.Material(material_id=12)
mat12.set_density("sum")
mat12.add_nuclide("U234", 1.567700e-04)
mat12.add_nuclide("U235", 1.719400e-02)
mat12.add_nuclide("U238", 2.950800e-02)
mat12.add_element("W", 1.209500e-05)
mat12.add_element("Fe", 1.592600e-04)
mat12.add_element("C", 3.702600e-04)
mat12.add_element("Cu", 2.744000e-04)
mat12.add_element("Ni", 2.971000e-04)

# U(36) layer no. 3
mat13 = openmc.Material(material_id=13)
mat13.set_density("sum")
mat13.add_nuclide("U234", 1.558100e-04)
mat13.add_nuclide("U235", 1.717400e-02)
mat13.add_nuclide("U238", 2.923500e-02)
mat13.add_element("W", 1.202100e-05)
mat13.add_element("Fe", 1.582900e-04)
mat13.add_element("C", 5.520100e-04)
mat13.add_element("Cu", 2.089300e-04)
mat13.add_element("Ni", 2.262100e-04)

# U(36) layer no. 4
mat14 = openmc.Material(material_id=14)
mat14.set_density("sum")
mat14.add_nuclide("U234", 1.325600e-04)
mat14.add_nuclide("U235", 1.714100e-02)
mat14.add_nuclide("U238", 2.941700e-02)
mat14.add_element("W", 1.205400e-05)
mat14.add_element("Fe", 1.190400e-04)
mat14.add_element("C", 7.380200e-04)
mat14.add_element("Cu", 1.942300e-04)
mat14.add_element("Ni", 2.103000e-04)

# U(36) layer no. 5
mat15 = openmc.Material(material_id=15)
mat15.set_density("sum")
mat15.add_nuclide("U234", 1.600400e-04)
mat15.add_nuclide("U235", 1.712100e-02)
mat15.add_nuclide("U238", 2.915900e-02)
mat15.add_element("W", 5.992000e-06)
mat15.add_element("Fe", 9.863000e-05)
mat15.add_element("C", 5.503100e-04)
mat15.add_element("Cu", 3.367300e-04)
mat15.add_element("Ni", 3.645900e-04)

# U(36) layer no. 6
mat16 = openmc.Material(material_id=16)
mat16.set_density("sum")
mat16.add_nuclide("U234", 1.723500e-04)
mat16.add_nuclide("U235", 1.695800e-02)
mat16.add_nuclide("U238", 2.880600e-02)
mat16.add_element("W", 1.186000e-05)
mat16.add_element("Fe", 9.760700e-05)
mat16.add_element("C", 9.076700e-04)
mat16.add_element("Cu", 3.593400e-04)
mat16.add_element("Ni", 3.890700e-04)

# D-38  layer no. 1
mat21 = openmc.Material(material_id=21)
mat21.set_density("sum")
mat21.add_nuclide("U235", 2.029800e-04)
mat21.add_nuclide("U238", 4.512000e-02)
mat21.add_element("Fe", 3.688900e-04)
mat21.add_element("C", 2.798500e-03)

# D-38  layer no. 2
mat22 = openmc.Material(material_id=22)
mat22.set_density("sum")
mat22.add_nuclide("U235", 2.157700e-04)
mat22.add_nuclide("U238", 4.587000e-02)
mat22.add_element("Fe", 3.750900e-04)
mat22.add_element("C", 2.845600e-03)

# D-38  layer no. 3
mat23 = openmc.Material(material_id=23)
mat23.set_density("sum")
mat23.add_nuclide("U235", 2.069200e-04)
mat23.add_nuclide("U238", 4.599700e-02)
mat23.add_element("Fe", 3.760600e-04)
mat23.add_element("C", 2.852900e-03)

materials = openmc.Materials([mat10, mat11, mat12, mat13, mat14, mat15, mat16, mat21, mat22, mat23])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.Sphere(surface_id=1, r=1.40)
surf2 = openmc.Sphere(surface_id=2, r=2.00)
surf3 = openmc.Sphere(surface_id=3, r=6.00)
surf4 = openmc.Sphere(surface_id=4, r=7.55)
surf5 = openmc.Sphere(surface_id=5, r=9.15)
surf6 = openmc.Sphere(surface_id=6, r=11.00)
surf7 = openmc.Sphere(surface_id=7, r=12.25)
surf8 = openmc.Sphere(surface_id=8, r=13.25)
surf9 = openmc.Sphere(surface_id=9, r=14.00)
surf10 = openmc.Sphere(surface_id=10, r=15.00)
surf11 = openmc.Sphere(surface_id=11, r=16.50, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U36-0
cell1 = openmc.Cell(cell_id=1, fill=mat10)
cell1.region = +surf1 & -surf2

# U36-1
cell2 = openmc.Cell(cell_id=2, fill=mat11)
cell2.region = +surf2 & -surf3

# U36-2
cell3 = openmc.Cell(cell_id=3, fill=mat12)
cell3.region = +surf3 & -surf4

# U36-3
cell4 = openmc.Cell(cell_id=4, fill=mat13)
cell4.region = +surf4 & -surf5

# U36-4
cell5 = openmc.Cell(cell_id=5, fill=mat14)
cell5.region = +surf5 & -surf6

# U36-5
cell6 = openmc.Cell(cell_id=6, fill=mat15)
cell6.region = +surf6 & -surf7

# U36-6
cell7 = openmc.Cell(cell_id=7, fill=mat16)
cell7.region = +surf7 & -surf8

# D38-1
cell8 = openmc.Cell(cell_id=8, fill=mat21)
cell8.region = +surf8 & -surf9

# D38-1
cell9 = openmc.Cell(cell_id=9, fill=mat22)
cell9.region = +surf9 & -surf10

# D38-1
cell10 = openmc.Cell(cell_id=10, fill=mat23)
cell10.region = +surf10 & -surf11

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10])
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
