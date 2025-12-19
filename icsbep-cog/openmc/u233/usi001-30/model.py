"""
FALSTAFF; Sol'n No. 3; Sphere No. 5; 3.10 cm CH2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U233", 1.465700e-03)
mat1.add_nuclide("U234", 1.595500e-05)
mat1.add_nuclide("U235", 5.868200e-07)
mat1.add_nuclide("U238", 4.668700e-06)
mat1.add_nuclide("H1", 5.914600e-02)
mat1.add_nuclide("O16", 3.247400e-02)
mat1.add_element("F", 3.121400e-03)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS-347 @ 8.0 g/cc
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("P", 8.000000e+00)
mat2.add_element("Fe", 7.100000e+01)
mat2.add_element("Cr", 1.800000e+01)
mat2.add_element("Ni", 1.100000e+01)

# Polyethylene
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 1.000000e+00)
mat3.add_nuclide("H1", 2.000000e+00)
mat3.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=10.1625)
surf2 = openmc.Sphere(surface_id=2, r=10.2107)
surf3 = openmc.Sphere(surface_id=3, r=13.3107, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# SS347
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# CH2
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3

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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
