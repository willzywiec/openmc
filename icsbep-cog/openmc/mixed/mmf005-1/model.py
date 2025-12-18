"""
MIX-MET-FAST-005: Pu sphere surrounded by HEU reflected by Al
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.393000e-02)
mat1.add_nuclide("Pu240", 3.504300e-03)
mat1.add_nuclide("Pu241", 3.918900e-04)
mat1.add_element("Ga", 2.210500e-03)
mat1.add_element("C", 3.024600e-04)
mat1.add_element("Fe", 3.252500e-04)
mat1.add_element("W", 7.410000e-05)
mat1.add_element("Ni", 1.418700e-03)

# HEU
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 5.232100e-04)
mat2.add_nuclide("U235", 4.099300e-02)
mat2.add_nuclide("U236", 9.235600e-05)
mat2.add_nuclide("U238", 4.085400e-03)
mat2.add_element("C", 3.859000e-04)
mat2.add_element("Fe", 1.441800e-04)
mat2.add_element("W", 1.230700e-05)
mat2.add_element("Cu", 7.616400e-04)
mat2.add_element("Ni", 3.534300e-04)

# Al
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.882900e-02)

# Fe
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 8.117400e-02)

# Cu
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cu", 8.236500e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Steel (Fe) diaphragm, inner
surf1 = openmc.ZCylinder(surface_id=1, r=4.8)
# Steel (Fe) diaphragm, outer
surf2 = openmc.ZCylinder(surface_id=2, x0=-0.2, y0=0.0, r=13.9)
# interface
surf3 = openmc.ZPlane(surface_id=3, z0=0.0)
# Pu, inner
# surf4: Unsupported surface type "s" with params ['4.66']
# Pu, outer; HEU, inner
# surf5: Unsupported surface type "s" with params ['5.35']
# HEU, outer; Al, inner
# surf6: Unsupported surface type "s" with params ['6.75']
# Al, outer
# surf7: Unsupported surface type "s" with params ['10.00']
# Hole in upper HEU
surf8 = openmc.XCylinder(surface_id=8, r=0.6)
# top
surf10 = openmc.ZPlane(surface_id=10, z0=-0.4)
# Cavity
# surf11: Unsupported surface type "s" with params ['1.40', 'tr', '0', '0', '-0.4']
# Pu, 1st shell
# surf12: Unsupported surface type "s" with params ['4.66', 'tr', '0', '0', '-0.4']
# Pu, 2nd shell
# surf13: Unsupported surface type "s" with params ['5.35', 'tr', '0', '0', '-0.4']
# HEU
# surf14: Unsupported surface type "s" with params ['6.75', 'tr', '0', '0', '-0.4']
# Al
# surf15: Unsupported surface type "s" with params ['10.00', 'tr', '0', '0', '-0.4']
# Cu
# surf16: Unsupported surface type "s" with params ['10.15', 'tr', '0', '0', '-0.4']
# Steel (Fe)
surf17 = openmc.ZCylinder(surface_id=17, x0=-14.55, y0=-1.0, r=2.5)
# Hole in lower HEU
surf20_cyl = openmc.XCylinder(surface_id=20, x0=tr, y0=0, r=0.6)
surf20_zmin = openmc.ZPlane(z0=0.0)
surf20_zmax = openmc.ZPlane(z0=-0.4)
surf20 = (surf20_cyl, surf20_zmin, surf20_zmax)
# Extent of Cu
surf21 = openmc.ZCylinder(surface_id=21, r=8.7)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Steel
cell1 = openmc.Cell(cell_id=1, fill=mat4)
cell1.region = +surf1 & -surf2 & -surf3

# Pu
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf3 & +surf4 & -surf5

# HEU
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf3 & +surf5 & -surf6 & +surf8

# Al
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf3 & +surf6 & -surf7

# Pu
cell5 = openmc.Cell(cell_id=5, fill=mat1)
cell5.region = +surf11 & -surf12

# Pu
cell6 = openmc.Cell(cell_id=6, fill=mat1)
cell6.region = -surf10 & +surf12 & -surf13

# HEU
cell7 = openmc.Cell(cell_id=7, fill=mat2)
cell7.region = -surf10 & +surf13 & -surf14 & +surf20

# Al
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = -surf10 & +surf14 & -surf15

# Cu
cell9 = openmc.Cell(cell_id=9, fill=mat5)
cell9.region = -surf10 & +surf15 & -surf16 & -surf21

# Steel
cell10 = openmc.Cell(cell_id=10, fill=mat4)
cell10.region = -surf10 & +surf16 & -surf17

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10])
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
