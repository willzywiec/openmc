"""
PU-COMP-MIXED-002 (Case 11) 18.417 kg Pu @ H/X = 15.4 with 2.20 wt-% Pu-240 and H/SQRT(A) = 0.259
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 2.756500e-03)
mat1.add_nuclide("Pu240", 6.171100e-05)
mat1.add_nuclide("Pu241", 2.999400e-06)
mat1.add_element("C", 4.260200e-02)
mat1.add_nuclide("H1", 4.260400e-02)
mat1.add_nuclide("O16", 5.642100e-03)
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

# Fuel with C(Pu) = 1.1200 g/oc
surf1 = openmc.model.RectangularParallelepiped(-20.675, 20.675, -19.23, 19.23, -5.17, 5.17)
# 6" (15.24 cm) Plexiglas Reflector
surf2 = openmc.model.RectangularParallelepiped(-35.915, 35.915, -34.47, 34.47, -20.41, 20.41, boundary_type="vacuum")

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
