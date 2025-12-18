"""
LMT004-4: 46 U(4.948) Metal Rods in Water; Pitch=4.72cm; Hf=30cm; Hw=36.85cm
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# LEU
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.846500e-05)
mat1.add_nuclide("U235", 2.394100e-03)
mat1.add_nuclide("U238", 4.539100e-02)

# H2O
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.665800e-02)
mat2.add_nuclide("O16", 3.332900e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# U (fuel)
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0, y0=30.0, r=1.2475)
# surf2: Error converting surface type "c": could not convert string to float: 'tr'
# surf3: Error converting surface type "c": could not convert string to float: 'tr'
# surf4: Error converting surface type "c": could not convert string to float: 'tr'
# surf5: Error converting surface type "c": could not convert string to float: 'tr'
# surf6: Error converting surface type "c": could not convert string to float: 'tr'
# surf7: Error converting surface type "c": could not convert string to float: 'tr'
surf10 = openmc.YPlane(surface_id=10, y0=-14.3067)
surf11 = openmc.YPlane(surface_id=11, y0=-10.2191)
surf12 = openmc.YPlane(surface_id=12, y0=-6.1315)
surf13 = openmc.YPlane(surface_id=13, y0=-2.0438)
surf14 = openmc.YPlane(surface_id=14, y0=2.0438)
surf15 = openmc.YPlane(surface_id=15, y0=6.1315)
surf16 = openmc.YPlane(surface_id=16, y0=10.2191)
surf17 = openmc.YPlane(surface_id=17, y0=14.3067)
# Water/boundary
surf90 = openmc.ZCylinder(surface_id=90, x0=-16.51, y0=36.85, r=58.3, boundary_type="vacuum")
# Arbitrary
surf99 = openmc.model.RectangularParallelepiped(-499.5, 499.5, -499.5, 499.5, -499.5, 499.5)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1
u1_cell1 = openmc.Cell(fill=mat1)
u1_cell2 = openmc.Cell(fill=mat1)
u1_cell3 = openmc.Cell(fill=mat1)
u1_cell4 = openmc.Cell(fill=mat1)
u1_cell5 = openmc.Cell(fill=mat1)
u1_cell6 = openmc.Cell(fill=mat1)
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = -surf99 & +surf1
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# LINE
cell1 = openmc.Cell(cell_id=1, fill=universe1)
cell1.translation = (0.0, 16.35056, 0.0)
cell1.region = -surf90 & +surf17

# LINE
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.translation = (-11.8, 12.26292, 0.0)
cell2.region = -surf90 & +surf16 & -surf17

# LINE
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (-14.16, 8.17528, 0.0)
cell3.region = -surf90 & +surf15 & -surf16

# LINE
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.translation = (-11.8, 4.08764, 0.0)
cell4.region = -surf90 & +surf14 & -surf15

# LINE
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.translation = (-14.16, 0.0, 0.0)
cell5.region = -surf90 & +surf13 & -surf14

# LINE
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.translation = (-11.8, -4.08764, 0.0)
cell6.region = -surf90 & +surf12 & -surf13

# LINE
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.translation = (-14.16, -8.17528, 0.0)
cell7.region = -surf90 & +surf11 & -surf12

# LINE
cell8 = openmc.Cell(cell_id=8, fill=universe1)
cell8.translation = (-7.08, -12.26292, 0.0)
cell8.region = -surf90 & +surf10 & -surf11

# LINE
cell9 = openmc.Cell(cell_id=9, fill=universe1)
cell9.translation = (-4.72, -16.35056, 0.0)
cell9.region = -surf90 & -surf10

# H2O
cell18 = openmc.Cell(cell_id=18, fill=mat2)
cell18.region = -surf99 & +surf1

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell18])
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
source.space = openmc.stats.Point((0.0, 0.0, 15.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
