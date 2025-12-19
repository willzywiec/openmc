"""
PU-COMP-MIXED-002 (Case 1) 38.020 kg Pu @ H/X = 0.047 with 18.35 wt-% Pu-240 and H/SQRT(A) = 0.391
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 3.380700e-05)
mat1.add_nuclide("Pu239", 1.091900e-02)
mat1.add_nuclide("Pu240", 2.652900e-03)
mat1.add_nuclide("Pu241", 7.265700e-04)
mat1.add_nuclide("Pu242", 1.631200e-04)
mat1.add_nuclide("H1", 5.506600e-04)
mat1.add_nuclide("O16", 3.088800e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

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

# Fuel with C(Pu) = 5.7615 g/cc
surf1 = openmc.model.RectangularParallelepiped(-12.825, 12.825, -12.825, 12.825, -5.015, 5.015)
# 6" (15.24 cm) Plexiglas Reflector
surf2 = openmc.model.RectangularParallelepiped(-28.065, 28.065, -28.065, 28.065, -20.255, 20.255, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# FUEL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# PLEX
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
