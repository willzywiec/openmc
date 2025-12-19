"""
MCT012-6: MOX/Polystyrene (H/SQRT(LxW)=0.80) with H/X=343 reflected by 15.24cm Lucite
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 9.532200e-07)
mat1.add_nuclide("Pu239", 1.091700e-04)
mat1.add_nuclide("Pu240", 3.686900e-05)
mat1.add_nuclide("Pu241", 8.942300e-06)
mat1.add_nuclide("Pu242", 4.687600e-06)
mat1.add_nuclide("U235", 2.896100e-06)
mat1.add_nuclide("U238", 1.967400e-03)
mat1.add_nuclide("Am241", 3.764900e-06)
mat1.add_nuclide("H1", 4.153800e-02)
mat1.add_element("C", 4.285700e-02)
mat1.add_nuclide("O16", 4.346700e-03)
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
surf1 = openmc.model.RectangularParallelepiped(-25.45, 25.45, -25.45, 25.45, -20.38, 20.38)
# Refl
surf2 = openmc.model.RectangularParallelepiped(-40.69, 40.69, -40.69, 40.69, -35.62, 35.62, boundary_type="vacuum")

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
