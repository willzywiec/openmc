"""
MCF004-1S: ZPR-3/56B Benchmark Model (Simplified)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu240", 1.770330e-04)
mat1.add_nuclide("Pu241", 2.297930e-05)
mat1.add_nuclide("U235", 1.360660e-05)
mat1.add_nuclide("U238", 6.201610e-03)
mat1.add_nuclide("Pu239", 1.333370e-03)
mat1.add_nuclide("Pu238", 5.655600e-07)
mat1.add_nuclide("Pu242", 2.366130e-06)
mat1.add_nuclide("Am241", 2.666480e-06)
mat1.add_nuclide("Cr50", 1.146130e-04)
mat1.add_nuclide("Cr52", 2.210220e-03)
mat1.add_nuclide("Cr53", 2.505920e-04)
mat1.add_nuclide("Cr54", 6.238440e-05)
mat1.add_nuclide("Ni58", 8.265130e-04)
mat1.add_nuclide("Ni60", 3.183200e-04)
mat1.add_nuclide("Ni61", 1.384000e-05)
mat1.add_nuclide("Ni62", 4.406940e-05)
mat1.add_nuclide("Ni64", 1.129050e-05)
mat1.add_nuclide("Fe54", 7.980960e-04)
mat1.add_nuclide("Fe56", 1.251720e-02)
mat1.add_nuclide("Fe57", 2.892250e-04)
mat1.add_nuclide("Fe58", 3.819950e-05)
mat1.add_element("Al", 5.069700e-06)
mat1.add_element("Na", 8.681240e-03)
mat1.add_nuclide("O16", 1.502310e-02)
mat1.add_element("C", 1.018410e-03)
mat1.add_nuclide("Mo100", 3.292470e-05)
mat1.add_nuclide("Mo92", 5.073750e-05)
mat1.add_nuclide("Mo94", 3.162550e-05)
mat1.add_nuclide("Mo95", 5.442990e-05)
mat1.add_nuclide("Mo96", 5.702840e-05)
mat1.add_nuclide("Mo97", 3.265120e-05)
mat1.add_nuclide("Mo98", 8.249960e-05)
mat1.add_element("Mn", 1.627980e-04)
mat1.add_nuclide("Cu63", 4.749410e-06)
mat1.add_nuclide("Cu65", 2.116870e-06)
mat1.add_element("H", 9.655530e-06)
mat1.add_nuclide("Si28", 1.207860e-04)
mat1.add_nuclide("Si29", 6.115900e-06)
mat1.add_nuclide("Si30", 4.059810e-06)
mat1.add_nuclide("Ca40", 1.471550e-06)
mat1.add_nuclide("Ca42", 9.821340e-09)
mat1.add_nuclide("Ca43", 2.049280e-09)
mat1.add_nuclide("Ca44", 3.166510e-08)
mat1.add_nuclide("Ca46", 6.071920e-11)
mat1.add_nuclide("Ca48", 2.838620e-09)
mat1.add_nuclide("Cl35", 2.198740e-06)
mat1.add_nuclide("Cl37", 7.031200e-07)

# Axial
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Cr50", 1.013350e-04)
mat2.add_nuclide("Cr52", 1.954170e-03)
mat2.add_nuclide("Cr53", 2.215620e-04)
mat2.add_nuclide("Cr54", 5.515710e-05)
mat2.add_nuclide("Ni58", 1.281460e-02)
mat2.add_nuclide("Ni60", 4.935360e-03)
mat2.add_nuclide("Ni61", 2.145820e-04)
mat2.add_nuclide("Ni62", 6.832690e-04)
mat2.add_nuclide("Ni64", 1.750530e-04)
mat2.add_nuclide("Fe54", 5.304190e-04)
mat2.add_nuclide("Fe56", 8.318950e-03)
mat2.add_nuclide("Fe57", 1.922200e-04)
mat2.add_nuclide("Fe58", 2.538750e-05)
mat2.add_element("Al", 3.644630e-06)
mat2.add_element("Na", 1.347900e-02)
mat2.add_nuclide("O16", 9.797520e-07)
mat2.add_element("C", 5.832360e-05)
mat2.add_nuclide("Mo100", 1.241070e-07)
mat2.add_nuclide("Mo92", 1.912510e-07)
mat2.add_nuclide("Mo94", 1.192100e-07)
mat2.add_nuclide("Mo95", 2.051690e-07)
mat2.add_nuclide("Mo96", 2.149640e-07)
mat2.add_nuclide("Mo97", 1.230760e-07)
mat2.add_nuclide("Mo98", 3.109760e-07)
mat2.add_element("Mn", 1.826470e-04)
mat2.add_nuclide("Cu63", 8.822770e-06)
mat2.add_nuclide("Cu65", 3.932410e-06)
mat2.add_nuclide("Si28", 1.312830e-04)
mat2.add_nuclide("Si29", 6.647440e-06)
mat2.add_nuclide("Si30", 4.412640e-06)
mat2.add_nuclide("Ca40", 2.998730e-06)
mat2.add_nuclide("Ca42", 2.001400e-08)
mat2.add_nuclide("Ca43", 4.176030e-09)
mat2.add_nuclide("Ca44", 6.452750e-08)
mat2.add_nuclide("Ca46", 1.237340e-10)
mat2.add_nuclide("Ca48", 5.784550e-09)
mat2.add_nuclide("Cl35", 3.350140e-07)
mat2.add_nuclide("Cl37", 1.071320e-07)
mat2.add_nuclide("Co59", 9.513260e-06)

# Radial
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Cr50", 8.461230e-05)
mat3.add_nuclide("Cr52", 1.631680e-03)
mat3.add_nuclide("Cr53", 1.849980e-04)
mat3.add_nuclide("Cr54", 4.605480e-05)
mat3.add_nuclide("Ni58", 3.226870e-02)
mat3.add_nuclide("Ni60", 1.242780e-02)
mat3.add_nuclide("Ni61", 5.403410e-04)
mat3.add_nuclide("Ni62", 1.720550e-03)
mat3.add_nuclide("Ni64", 4.408040e-04)
mat3.add_nuclide("Fe54", 4.463540e-04)
mat3.add_nuclide("Fe56", 7.000510e-03)
mat3.add_nuclide("Fe57", 1.617560e-04)
mat3.add_nuclide("Fe58", 2.136400e-05)
mat3.add_element("Al", 2.614760e-06)
mat3.add_element("Na", 6.606760e-03)
mat3.add_nuclide("O16", 4.757130e-07)
mat3.add_element("C", 3.971600e-05)
mat3.add_nuclide("Mo100", 8.873420e-08)
mat3.add_nuclide("Mo92", 1.367410e-07)
mat3.add_nuclide("Mo94", 8.523270e-08)
mat3.add_nuclide("Mo95", 1.466920e-07)
mat3.add_nuclide("Mo96", 1.536950e-07)
mat3.add_nuclide("Mo97", 8.799700e-08)
mat3.add_nuclide("Mo98", 2.223420e-07)
mat3.add_element("Mn", 1.880240e-04)
mat3.add_nuclide("Cu63", 6.007020e-06)
mat3.add_nuclide("Cu65", 2.677390e-06)
mat3.add_nuclide("Si28", 1.076220e-04)
mat3.add_nuclide("Si29", 5.449340e-06)
mat3.add_nuclide("Si30", 3.617330e-06)
mat3.add_nuclide("Ca40", 1.467050e-06)
mat3.add_nuclide("Ca42", 9.791300e-09)
mat3.add_nuclide("Ca43", 2.043010e-09)
mat3.add_nuclide("Ca44", 3.156830e-08)
mat3.add_nuclide("Ca46", 6.053360e-11)
mat3.add_nuclide("Ca48", 2.829950e-09)
mat3.add_nuclide("Cl35", 1.626650e-07)
mat3.add_nuclide("Cl37", 5.201750e-08)
mat3.add_nuclide("Co59", 6.772950e-06)

# Al
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("Cr50", 6.375250e-05)
mat4.add_nuclide("Cr52", 1.229420e-03)
mat4.add_nuclide("Cr53", 1.393900e-04)
mat4.add_nuclide("Cr54", 3.470070e-05)
mat4.add_nuclide("Ni58", 4.920300e-04)
mat4.add_nuclide("Ni60", 1.894980e-04)
mat4.add_nuclide("Ni61", 8.239040e-06)
mat4.add_nuclide("Ni62", 2.623490e-05)
mat4.add_nuclide("Ni64", 6.721330e-06)
mat4.add_nuclide("Fe54", 3.696760e-04)
mat4.add_nuclide("Fe56", 5.797910e-03)
mat4.add_nuclide("Fe57", 1.339680e-04)
mat4.add_nuclide("Fe58", 1.769390e-05)
mat4.add_element("Al", 2.496610e-03)
mat4.add_element("C", 1.941520e-05)
mat4.add_element("Mn", 7.212800e-05)
mat4.add_nuclide("Si28", 6.887430e-05)
mat4.add_nuclide("Si29", 3.487400e-06)
mat4.add_nuclide("Si30", 2.314980e-06)

# Matrix
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("Cr50", 4.821200e-05)
mat5.add_nuclide("Cr52", 9.297320e-04)
mat5.add_nuclide("Cr53", 1.054110e-04)
mat5.add_nuclide("Cr54", 2.624190e-05)
mat5.add_nuclide("Ni58", 3.087800e-04)
mat5.add_nuclide("Ni60", 1.189220e-04)
mat5.add_nuclide("Ni61", 5.170520e-06)
mat5.add_nuclide("Ni62", 1.646400e-05)
mat5.add_nuclide("Ni64", 4.218060e-06)
mat5.add_nuclide("Fe54", 2.649860e-04)
mat5.add_nuclide("Fe56", 4.155980e-03)
mat5.add_nuclide("Fe57", 9.602910e-05)
mat5.add_nuclide("Fe58", 1.268310e-05)
mat5.add_element("Mn", 4.349570e-05)
mat5.add_nuclide("Si28", 5.604820e-05)
mat5.add_nuclide("Si29", 2.837960e-06)
mat5.add_nuclide("Si30", 1.883870e-06)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# (31x5.54609cm)x(2x85.09)x(31x5.52577)
surf1 = openmc.model.RectangularParallelepiped(-85.96435, 85.96435, -85.09, 85.09, -85.6494, 85.6494, boundary_type="vacuum")
surf2 = openmc.YPlane(surface_id=2, y0=82.55)
surf3 = openmc.YPlane(surface_id=3, y0=74.37952)
surf4 = openmc.YPlane(surface_id=4, y0=74.37628)
surf5 = openmc.YPlane(surface_id=5, y0=45.80452)
surf6 = openmc.YPlane(surface_id=6, y0=-45.80452)
surf7 = openmc.YPlane(surface_id=7, y0=-74.37628)
surf8 = openmc.YPlane(surface_id=8, y0=-74.37952)
surf9 = openmc.YPlane(surface_id=9, y0=-82.55)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat5)
u1_cell0.region = -surf1 & +surf2
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = -surf1 & -surf2 & +surf3
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = -surf1 & -surf3 & +surf5
u1_cell3 = openmc.Cell(fill=mat1)
u1_cell3.region = -surf1 & -surf5 & +surf6
u1_cell4 = openmc.Cell(fill=mat2)
u1_cell4.region = -surf1 & -surf6 & +surf8
u1_cell5 = openmc.Cell(fill=mat4)
u1_cell5.region = -surf1 & -surf8 & +surf9
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = -surf1 & -surf9
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = -surf1 & +surf2
u2_cell1 = openmc.Cell(fill=mat4)
u2_cell1.region = -surf1 & -surf2 & +surf4
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = -surf1 & -surf4 & +surf7
u2_cell3 = openmc.Cell(fill=mat4)
u2_cell3.region = -surf1 & -surf7 & +surf9
u2_cell4 = openmc.Cell(fill=mat5)
u2_cell4.region = -surf1 & -surf9
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4])

u3_cell0 = openmc.Cell(fill=mat5)
u3_cell0.region = -surf1
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0])

universe4 = openmc.Universe(universe_id=4, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# ZPR
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = -surf1

# Mx
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = -surf1 & -surf9

# Mx
cell15 = openmc.Cell(cell_id=15, fill=mat5)
cell15.region = -surf1 & -surf9

# Mx
cell17 = openmc.Cell(cell_id=17, fill=mat5)
cell17.region = -surf1

root_universe = openmc.Universe(cells=[cell1, cell9, cell15, cell17])
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
