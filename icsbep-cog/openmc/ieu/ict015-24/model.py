"""
ICT015-24: 27.94 x 27.94 x 24.9428 cc U(30.14)O2/wax parallelepiped reflected by 20.32 cm thick PERSPEX - batch 16L
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Batch 16L
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 3.500300e-02)
mat1.add_element("C", 1.734200e-02)
mat1.add_nuclide("O16", 1.468700e-02)
mat1.add_element("Al", 5.166500e-05)
mat1.add_nuclide("U234", 2.730700e-05)
mat1.add_nuclide("U235", 2.156600e-03)
mat1.add_nuclide("U236", 4.987500e-06)
mat1.add_nuclide("U238", 4.903800e-03)
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

surf1 = openmc.model.RectangularParallelepiped(-13.97, 13.97, -13.97, 13.97, -12.4714, 12.4714)
surf2 = openmc.model.RectangularParallelepiped(-34.29, 34.29, -34.29, 34.29, -32.7914, 32.7914, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# UO2WAX
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# PERSPEX
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
