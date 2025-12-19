"""
MCT012-25: MOX/Polystyrene (H/SQRT(LxW)=0.50) with H/X=172 reflected by 15.24cm Lucite
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 2.573200e-04)
mat1.add_nuclide("Pu240", 2.294500e-05)
mat1.add_nuclide("Pu241", 1.719900e-06)
mat1.add_nuclide("Pu242", 1.048600e-07)
mat1.add_nuclide("U235", 1.007900e-06)
mat1.add_nuclide("U238", 6.599300e-04)
mat1.add_nuclide("Am241", 3.159000e-07)
mat1.add_nuclide("H1", 4.466000e-02)
mat1.add_element("C", 4.534500e-02)
mat1.add_nuclide("O16", 1.973100e-03)
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

# Core
surf1 = openmc.model.RectangularParallelepiped(-20.36, 20.36, -20.36, 20.36, -10.11, 10.11)
# Refl
surf2 = openmc.model.RectangularParallelepiped(-35.6, 35.6, -35.6, 35.6, -25.35, 25.35, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Refl
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
