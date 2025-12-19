"""
MCT013-1: MOX/Polystyrene with H/X=226 with 15.24cm Lucite reflector
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 1.951600e-04)
mat1.add_nuclide("Pu240", 1.701600e-05)
mat1.add_nuclide("Pu241", 9.553300e-07)
mat1.add_nuclide("Pu242", 8.035800e-08)
mat1.add_nuclide("U235", 1.903400e-06)
mat1.add_nuclide("U238", 1.251000e-03)
mat1.add_nuclide("Am241", 7.344000e-07)
mat1.add_nuclide("H1", 4.483100e-02)
mat1.add_element("C", 4.410100e-02)
mat1.add_nuclide("O16", 3.017500e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 5.664200e-02)
mat2.add_element("C", 3.564800e-02)
mat2.add_nuclide("O16", 1.427300e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Height of lower fuel + absorber + upper fuel = 14.6714 + 0 + 9.3946 = 24.0660 cm
surf1 = openmc.model.RectangularParallelepiped(-20.36, 20.36, -20.38, 20.38, -12.033, 12.033)
# Lucite reflector, 15.24 cm thick
surf2 = openmc.model.RectangularParallelepiped(-35.6, 35.6, -35.62, 35.62, -19.653, 19.653, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Lucite
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
