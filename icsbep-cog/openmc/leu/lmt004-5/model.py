"""
LMT004-5: 32 U(4.948) Metal Rods in Water; Pitch=5.22cm; Hf=60cm; Hw=59.45cm
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
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0, y0=60.0, r=1.2475)
# surf2: Error converting surface type "c": could not convert string to float: 'tr'
# surf3: Error converting surface type "c": could not convert string to float: 'tr'
# surf4: Error converting surface type "c": could not convert string to float: 'tr'
# surf5: Error converting surface type "c": could not convert string to float: 'tr'
# surf6: Error converting surface type "c": could not convert string to float: 'tr'
surf11 = openmc.YPlane(surface_id=11, y0=-11.30163)
surf12 = openmc.YPlane(surface_id=12, y0=-6.78098)
surf13 = openmc.YPlane(surface_id=13, y0=-2.26033)
surf14 = openmc.YPlane(surface_id=14, y0=2.26033)
surf15 = openmc.YPlane(surface_id=15, y0=6.78098)
surf16 = openmc.YPlane(surface_id=16, y0=11.30163)
# Radial reflector/boundary
surf90 = openmc.ZCylinder(surface_id=90, x0=-16.51, y0=60.0, r=58.3, boundary_type="vacuum")
# Water height
surf91 = openmc.ZPlane(surface_id=91, z0=59.45)
# Arbitrary
surf99 = openmc.model.RectangularParallelepiped(-499.5, 499.5, -499.5, 499.5, -499.5, 499.5)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1
u1_cell1 = openmc.Cell(fill=mat1)
u1_cell1.region = -surf2
u1_cell2 = openmc.Cell(fill=mat1)
u1_cell2.region = -surf3
u1_cell3 = openmc.Cell(fill=mat1)
u1_cell3.region = -surf4
u1_cell4 = openmc.Cell(fill=mat1)
u1_cell4.region = -surf5
u1_cell5 = openmc.Cell(fill=mat1)
u1_cell5.region = -surf6
u1_cell6 = openmc.Cell()
u1_cell6.region = +surf91 & -surf99 & +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & +surf6
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = -surf91 & -surf99 & +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & +surf6
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7])

u2_cell0 = openmc.Cell()
u2_cell0.region = +surf91 & -surf99
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = -surf91 & -surf99
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# LINE
cell1 = openmc.Cell(cell_id=1, fill=universe1)
cell1.translation = (-2.61, 13.561958, 0.0)
cell1.region = -surf90 & +surf16 & -surf21

# LINE
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.translation = (-10.44, 9.041305, 0.0)
cell2.region = -surf90 & +surf15 & -surf16 & -surf22

# LINE
cell3 = openmc.Cell(cell_id=3, fill=universe1)
cell3.translation = (-13.05, 4.520653, 0.0)
cell3.region = -surf90 & +surf14 & -surf15

# LINE
cell4 = openmc.Cell(cell_id=4, fill=universe1)
cell4.translation = (-10.44, 0.0, 0.0)
cell4.region = -surf90 & +surf13 & -surf14 & -surf22

# LINE
cell5 = openmc.Cell(cell_id=5, fill=universe1)
cell5.translation = (-13.05, -4.520653, 0.0)
cell5.region = -surf90 & +surf12 & -surf13

# LINE
cell6 = openmc.Cell(cell_id=6, fill=universe1)
cell6.translation = (-10.44, -9.041305, 0.0)
cell6.region = -surf90 & +surf11 & -surf12 & -surf22

# LINE
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.translation = (-7.83, -13.561958, 0.0)
cell7.region = -surf90 & -surf11 & -surf21

# H2O
cell16 = openmc.Cell(cell_id=16, fill=mat2)
cell16.region = -surf91 & -surf99 & +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & +surf6

# H2O
cell19 = openmc.Cell(cell_id=19, fill=mat2)
cell19.region = -surf91 & -surf99

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell16, cell19])
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
source.space = openmc.stats.Point((0.0, 0.0, 29.725))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
