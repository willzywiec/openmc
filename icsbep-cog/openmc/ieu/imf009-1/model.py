"""
IEU-MET-FAST-009-1: Spherical assembly of 140.344 kg U(36) reflected by 14.560 kg polyethylene
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 1st U(36) layer
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.592200e-04)
mat1.add_nuclide("U235", 1.744000e-02)
mat1.add_nuclide("U238", 2.999000e-02)
mat1.add_element("C", 4.700900e-04)
mat1.add_element("Fe", 1.617600e-04)
mat1.add_element("W", 1.228400e-05)

# 2nd U(36) layer
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 1.587800e-04)
mat2.add_nuclide("U235", 1.741500e-02)
mat2.add_nuclide("U238", 2.988700e-02)
mat2.add_element("C", 3.750200e-04)
mat2.add_element("Fe", 1.613100e-04)
mat2.add_element("W", 1.225000e-05)

# 3rd U(36) layer
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U234", 1.580300e-04)
mat3.add_nuclide("U235", 1.741800e-02)
mat3.add_nuclide("U238", 2.965100e-02)
mat3.add_element("C", 5.598600e-04)
mat3.add_element("Fe", 1.605400e-04)
mat3.add_element("W", 1.219200e-05)

# 4th U(36) layer
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U234", 1.342300e-04)
mat4.add_nuclide("U235", 1.735600e-02)
mat4.add_nuclide("U238", 2.978600e-02)
mat4.add_element("C", 7.472700e-04)
mat4.add_element("Fe", 1.205400e-04)
mat4.add_element("W", 1.220500e-05)

# 5th U(36) layer
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U234", 1.628100e-04)
mat5.add_nuclide("U235", 1.741700e-02)
mat5.add_nuclide("U238", 2.966300e-02)
mat5.add_element("C", 5.598300e-04)
mat5.add_element("Fe", 1.003400e-04)
mat5.add_element("W", 6.095600e-06)

# 1st  CH2  layer
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 7.554200e-02)
mat6.add_element("C", 3.777100e-02)
mat6.add_s_alpha_beta("c_H_in_CH2")

# 2nd  CH2  layer
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("H1", 7.417000e-02)
mat7.add_element("C", 3.708500e-02)
mat7.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=3.445)
surf2 = openmc.Sphere(surface_id=2, r=6.000)
surf3 = openmc.Sphere(surface_id=3, r=7.550)
surf4 = openmc.Sphere(surface_id=4, r=9.150)
surf5 = openmc.Sphere(surface_id=5, r=11.00)
surf6 = openmc.Sphere(surface_id=6, r=12.25)
surf7 = openmc.Sphere(surface_id=7, r=15.15)
surf8 = openmc.Sphere(surface_id=8, r=18.00, boundary_type="vacuum")

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

# CH2-1
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf6 & -surf7

# CH2-2
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = +surf7 & -surf8

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
source.space = openmc.stats.Box((-5.0, -5.0, -5.0), (5.0, 5.0, 5.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
