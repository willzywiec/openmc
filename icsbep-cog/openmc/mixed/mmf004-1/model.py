"""
MIX-MET-FAST-004-1: Pu sphere surrounded by HEU reflected by Be metal
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.430400e-02)
mat1.add_nuclide("Pu240", 3.495000e-03)
mat1.add_nuclide("Pu241", 3.907600e-04)
mat1.add_element("Ga", 2.128900e-03)
mat1.add_element("C", 3.053600e-04)
mat1.add_element("Fe", 3.283700e-04)
mat1.add_element("W", 7.481100e-05)
mat1.add_element("Ni", 8.677400e-04)

# HEU
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 5.228600e-04)
mat2.add_nuclide("U235", 4.103000e-02)
mat2.add_nuclide("U236", 8.798900e-05)
mat2.add_nuclide("U238", 4.100900e-03)
mat2.add_element("C", 3.957100e-04)
mat2.add_element("Fe", 1.350700e-04)
mat2.add_element("W", 1.243600e-05)
mat2.add_element("Cu", 7.215000e-04)
mat2.add_element("Ni", 3.348000e-04)

# Be
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Be", 1.199400e-01)
mat3.add_nuclide("O16", 8.147000e-05)
mat3.add_element("C", 9.948000e-05)
mat3.add_element("Fe", 5.057000e-05)

# Duralumin
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Al", 5.807700e-02)
mat4.add_element("Mg", 1.033200e-03)
mat4.add_element("Mn", 1.828400e-04)
mat4.add_element("Cu", 1.132900e-03)

# Fe
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 8.117400e-02)

# Cu
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Cu", 8.236500e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Duralumin diaphragm, inner
surf1 = openmc.ZCylinder(surface_id=1, r=7.0)
# Duralumin diaphragm, outer
surf2 = openmc.ZCylinder(surface_id=2, r=14.0)
# interface
surf3 = openmc.ZPlane(surface_id=3, z0=0.0)
# HEU, inner
# surf4: Unsupported surface type "s" with params ['6.75']
# HEU, outer; Be, inner
# surf5: Unsupported surface type "s" with params ['8.35']
# Be, outer
# surf6: Unsupported surface type "s" with params ['9.15']
# Hole in HEU
surf7 = openmc.XCylinder(surface_id=7, r=0.6)
# Hole in Be
surf8 = openmc.XCylinder(surface_id=8, r=0.15)
# Hole in Be
surf9 = openmc.ZCylinder(surface_id=9, r=1.1)
# top
surf10 = openmc.ZPlane(surface_id=10, z0=-0.4)
# Cavity
# surf11: Unsupported surface type "s" with params ['1.40', 'tr', '0', '0', '-0.4']
# Pu
# surf12: Unsupported surface type "s" with params ['3.15', 'tr', '0', '0', '-0.4']
# HEU, full shell
# surf13: Unsupported surface type "s" with params ['6.75', 'tr', '0', '0', '-0.4']
# HEU, half shell
# surf14: Unsupported surface type "s" with params ['8.35', 'tr', '0', '0', '-0.4']
# Be
# surf15: Unsupported surface type "s" with params ['9.15', 'tr', '0', '0', '-0.4']
# Cu
# surf16: Unsupported surface type "s" with params ['9.30', 'tr', '0', '0', '-0.4']
# Steel (Fe)
surf17 = openmc.ZCylinder(surface_id=17, r=2.5)
# Hole in HEU
surf20 = openmc.XCylinder(surface_id=20, x0=0.0, y0=0.0, r=0.6)
# Hole in Be
surf21 = openmc.XCylinder(surface_id=21, x0=0.0, y0=0.0, r=0.15)
# Extent of Cu
surf22 = openmc.ZCylinder(surface_id=22, r=8.0)

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(surface_id=1022, z0=-0.2)
surf2_zmax = openmc.ZPlane(surface_id=1023, z0=0.0)
surf17_zmin = openmc.ZPlane(surface_id=1024, z0=-14.7)
surf17_zmax = openmc.ZPlane(surface_id=1025, z0=-1.0)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Dural
cell1 = openmc.Cell(cell_id=1, fill=mat4)
cell1.region = +surf1 & (-surf2 & +surf2_zmin & -surf2_zmax) & -surf3

# HEU
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf3 & +surf4 & -surf5 & +surf7

# Be
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf3 & +surf5 & -surf6 & +surf8 & +surf9

# Pu
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = +surf11 & -surf12

# HEU
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf12 & -surf13

# HEU
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = -surf10 & +surf13 & -surf14 & +surf20

# Be
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = -surf10 & +surf14 & -surf15 & +surf21

# Cu
cell8 = openmc.Cell(cell_id=8, fill=mat6)
cell8.region = -surf10 & +surf15 & -surf16 & -surf22

# Steel
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = -surf10 & +surf16 & (-surf17 & +surf17_zmin & -surf17_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9])
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
source.space = openmc.stats.Box((-3.0, -3.0, -3.0), (3.0, 3.0, 3.4))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
