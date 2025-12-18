"""
ICT016-43: 17.78 x 17.78 x 22.3774 U(30.14)O2/wax parallelepiped with 20.32 cm Polythene on bottom & sides - 0.0381 cm Cd plus 20.32 cm Beechwood B on top - batch 80
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Batch 80
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 6.867200e-02)
mat1.add_element("C", 3.401500e-02)
mat1.add_nuclide("O16", 5.841800e-03)
mat1.add_element("Al", 6.888200e-05)
mat1.add_nuclide("U234", 1.073000e-05)
mat1.add_nuclide("U235", 8.474100e-04)
mat1.add_nuclide("U236", 1.959800e-06)
mat1.add_nuclide("U238", 1.926900e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

# Polythene
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 7.891100e-02)
mat2.add_nuclide("O16", 3.495500e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

# Cadmium
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cd", 4.634000e-02)

# Beechwood B
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 2.669100e-02)
mat4.add_element("C", 1.574800e-02)
mat4.add_element("N", 1.868200e-05)
mat4.add_nuclide("O16", 1.201100e-02)
mat4.add_element("K", 1.779500e-05)
mat4.add_element("Ca", 8.010600e-06)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.model.RectangularParallelepiped(-8.89, 8.89, -8.89, 8.89, -11.1887, 11.1887)
surf2 = openmc.model.RectangularParallelepiped(-29.21, 29.21, -29.21, 29.21, -49.99995, 49.99995, boundary_type="vacuum")
# Bottom of polythene
surf3 = openmc.ZPlane(surface_id=3, z0=-31.5087)
# Top of core
surf4 = openmc.ZPlane(surface_id=4, z0=11.1887)
# Top of cadmium
surf5 = openmc.ZPlane(surface_id=5, z0=11.2268)
# Top of top reflector
surf6 = openmc.ZPlane(surface_id=6, z0=31.5468)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# UO2WAX
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# POLY
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2 & +surf3 & -surf4

# CD
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf1 & -surf2 & +surf4 & -surf5

# TopRefl
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf1 & -surf2 & +surf5 & -surf6

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4])
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
