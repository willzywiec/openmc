"""
ICT015-30: 20.32 x 20.32 x 30.7340 cc U(30.14)O2/wax parallelepiped with 0.0381 cm Cadmium plus 20.32 cm thick BEECHWOOD - batch 80
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

# Cadmium
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cd", 4.634000e-02)

# Beechwood
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 2.652600e-02)
mat3.add_element("C", 1.596400e-02)
mat3.add_element("N", 2.266700e-05)
mat3.add_nuclide("O16", 1.235000e-02)
mat3.add_element("Na", 2.725600e-06)
mat3.add_element("Mg", 1.718800e-06)
mat3.add_element("K", 1.282100e-05)
mat3.add_element("Ca", 8.338600e-06)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.model.RectangularParallelepiped(-10.16, 10.16, -10.16, 10.16, -15.367, 15.367)
# 0.0381 cm thick Cadmium
surf2 = openmc.model.RectangularParallelepiped(-10.1981, 10.1981, -10.1981, 10.1981, -15.4051, 15.4051)
# 20.32   cm thick Beechwood
surf3 = openmc.model.RectangularParallelepiped(-30.5181, 30.5181, -30.5181, 30.5181, -35.7251, 35.7251, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# UO2WAX
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# CADMIUM
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# BEECH
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
