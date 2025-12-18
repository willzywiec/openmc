"""
ICT015-18: 27.94 x 27.94 x 14.9987 cc U(30.14)O2/wax parallelepiped reflected by 20.32 cm thick CH2 - batch 80C
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Batch 80C
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 5.048500e-02)
mat1.add_element("C", 5.274000e-02)
mat1.add_nuclide("O16", 4.333200e-03)
mat1.add_element("Al", 8.412900e-05)
mat1.add_nuclide("U234", 7.868600e-06)
mat1.add_nuclide("U235", 6.214400e-04)
mat1.add_nuclide("U236", 1.437200e-06)
mat1.add_nuclide("U238", 1.413000e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

# Polythene
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 7.891100e-02)
mat2.add_element("C", 3.945500e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.model.RectangularParallelepiped(-13.97, 13.97, -13.97, 13.97, -7.49935, 7.49935)
surf2 = openmc.model.RectangularParallelepiped(-34.29, 34.29, -34.29, 34.29, -27.81935, 27.81935, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# UO2WAX
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# POLY
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

root_universe = openmc.Universe(cells=[cell1, cell2])
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
