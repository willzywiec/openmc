"""
ICT015-25: 20.32 x 20.32 x 16.3576 cc U(30.14)O2/wax parallelepiped reflected by 20.32 cm thick PERSPEX - batch 40
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Batch 40
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 6.097900e-02)
mat1.add_element("C", 3.020500e-02)
mat1.add_nuclide("O16", 1.065700e-02)
mat1.add_element("Al", 6.483300e-05)
mat1.add_nuclide("U234", 1.974000e-05)
mat1.add_nuclide("U235", 1.559000e-03)
mat1.add_nuclide("U236", 3.605400e-06)
mat1.add_nuclide("U238", 3.544900e-03)
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

surf1 = openmc.model.RectangularParallelepiped(-10.16, 10.16, -10.16, 10.16, -8.1788, 8.1788)
surf2 = openmc.model.RectangularParallelepiped(-30.48, 30.48, -30.48, 30.48, -28.4988, 28.4988, boundary_type="vacuum")

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
