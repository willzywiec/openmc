"""
ICT015-28: 20.32 x 20.32 x 18.9992 cc U(30.14)O2/wax parallelepiped reflected by 20.32 cm thick BEECHWOOD - batch 80
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

# Beechwood
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 2.652600e-02)
mat2.add_element("C", 1.596400e-02)
mat2.add_element("N", 2.266700e-05)
mat2.add_nuclide("O16", 1.235000e-02)
mat2.add_element("Na", 2.725600e-06)
mat2.add_element("Mg", 1.718800e-06)
mat2.add_element("K", 1.282100e-05)
mat2.add_element("Ca", 8.338600e-06)
mat2.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.model.RectangularParallelepiped(-10.16, 10.16, -10.16, 10.16, -9.4996, 9.4996)
surf2 = openmc.model.RectangularParallelepiped(-30.48, 30.48, -30.48, 30.48, -29.8196, 29.8196, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# UO2WAX
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# BEECH
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
