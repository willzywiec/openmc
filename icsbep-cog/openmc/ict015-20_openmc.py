"""
ICT015-20: 25.40 x 25.40 x 21.9202 cc U(30.14)O2/wax parallelepiped reflected by 20.32 cm thick PERSPEX - batch 8
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Batch 8
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 3.263600e-02)
mat1.add_element("C", 1.616600e-02)
mat1.add_nuclide("O16", 2.728800e-02)
mat1.add_element("Al", 3.364800e-05)
mat1.add_nuclide("U234", 5.090700e-05)
mat1.add_nuclide("U235", 4.020500e-03)
mat1.add_nuclide("U236", 9.297900e-06)
mat1.add_nuclide("U238", 9.141900e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

# Perspex
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 5.740800e-02)
mat2.add_element("C", 3.588000e-02)
mat2.add_nuclide("O16", 1.435200e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.model.RectangularParallelepiped(-12.7, 12.7, -12.7, 12.7, -10.9601, 10.9601)
surf2 = openmc.model.RectangularParallelepiped(-33.02, 33.02, -33.02, 33.02, -31.2801, 31.2801, boundary_type="vacuum")

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
