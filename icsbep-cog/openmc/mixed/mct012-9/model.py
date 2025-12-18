"""
MCT012-9: MOX/Polystyrene (H/SQRT(LxW)=0.37) with H/X=705 reflected by 15.24cm Lucite
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 6.515400e-05)
mat1.add_nuclide("Pu240", 5.796800e-06)
mat1.add_nuclide("Pu241", 4.173000e-07)
mat1.add_nuclide("Pu242", 3.463100e-08)
mat1.add_nuclide("U235", 1.283900e-06)
mat1.add_nuclide("U238", 8.367900e-04)
mat1.add_nuclide("Am241", 1.738800e-07)
mat1.add_nuclide("H1", 4.715800e-02)
mat1.add_element("C", 4.536500e-02)
mat1.add_nuclide("O16", 1.828000e-03)
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

# Core
surf1 = openmc.model.RectangularParallelepiped(-30.54, 30.54, -30.48, 30.48, -11.33, 11.33)
# Refl
surf2 = openmc.model.RectangularParallelepiped(-45.78, 45.78, -45.72, 45.72, -26.57, 26.57, boundary_type="vacuum")

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
