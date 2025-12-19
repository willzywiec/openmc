"""
IEU-MET-FAST-004-1D: 15.222 kg graphite reflected spherical assembly of 211.874 kg U(36) [Detailed Model] Rev. 2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Layer 1
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.592600e-04)
mat1.add_nuclide("U235", 1.744300e-02)
mat1.add_nuclide("U238", 2.999600e-02)
mat1.add_element("C", 4.701800e-04)
mat1.add_element("Fe", 1.618000e-04)
mat1.add_element("W", 1.228700e-05)

# Layer 2
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 1.587800e-04)
mat2.add_nuclide("U235", 1.741500e-02)
mat2.add_nuclide("U238", 2.988700e-02)
mat2.add_element("C", 3.750200e-04)
mat2.add_element("Fe", 1.613100e-04)
mat2.add_element("W", 1.225000e-05)

# Layer 3
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U234", 1.580300e-04)
mat3.add_nuclide("U235", 1.741800e-02)
mat3.add_nuclide("U238", 2.965100e-02)
mat3.add_element("C", 5.598600e-04)
mat3.add_element("Fe", 1.605400e-04)
mat3.add_element("W", 1.219200e-05)

# Layer 4
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U234", 1.342300e-04)
mat4.add_nuclide("U235", 1.735600e-02)
mat4.add_nuclide("U238", 2.978600e-02)
mat4.add_element("C", 7.472700e-04)
mat4.add_element("Fe", 1.205400e-04)
mat4.add_element("W", 1.220500e-05)

# Layer 5
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U234", 1.628100e-04)
mat5.add_nuclide("U235", 1.741700e-02)
mat5.add_nuclide("U238", 2.966300e-02)
mat5.add_element("C", 5.598300e-04)
mat5.add_element("Fe", 1.003400e-04)
mat5.add_element("W", 6.095600e-06)

# Layer 6
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("U234", 1.760900e-04)
mat6.add_nuclide("U235", 1.732600e-02)
mat6.add_nuclide("U238", 2.943200e-02)
mat6.add_element("C", 9.273700e-04)
mat6.add_element("Fe", 9.972500e-05)
mat6.add_element("W", 1.211700e-05)

# Layer 7
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("U234", 1.515600e-04)
mat7.add_nuclide("U235", 1.726600e-02)
mat7.add_nuclide("U238", 2.930900e-02)
mat7.add_element("C", 6.460400e-04)
mat7.add_element("Fe", 9.924500e-05)
mat7.add_element("W", 6.029400e-06)

mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("C", 7.771600e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=2.788)
surf2 = openmc.Sphere(surface_id=2, r=6.000)
surf3 = openmc.Sphere(surface_id=3, r=7.550)
surf4 = openmc.Sphere(surface_id=4, r=9.150)
surf5 = openmc.Sphere(surface_id=5, r=11.00)
surf6 = openmc.Sphere(surface_id=6, r=12.25)
surf7 = openmc.Sphere(surface_id=7, r=13.25)
surf8 = openmc.Sphere(surface_id=8, r=14.0)
surf9 = openmc.Sphere(surface_id=9, r=17.2, boundary_type="vacuum")

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

# L7
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = +surf7 & -surf8

# C
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
