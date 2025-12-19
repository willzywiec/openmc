"""
PU-MET-FAST-020:  Sphere of Pu Reflected by Depleted Uranium at VNIITF
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Materials:
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

# D38 ----- Table 10
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 2.378700e-04)
mat2.add_nuclide("U238", 4.673800e-02)

# Duralum - Table ll
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.807700e-02)
mat3.add_element("Mg", 1.033200e-03)
mat3.add_element("Mn", 1.828400e-04)
mat3.add_element("Cu", 1.132900e-03)

# Steel - Section 3.3
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 8.117400e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Pu/IR
surf1 = openmc.Sphere(surface_id=1, r=1.4)
# Pu/OR
surf2 = openmc.Sphere(surface_id=2, r=5.35)
# D38/1/OR
surf3 = openmc.Sphere(surface_id=3, r=9.15)
# D38/2/OR
surf4 = openmc.Sphere(surface_id=4, r=13.00)
# Duralumin/OR
surf5 = openmc.Sphere(surface_id=5, r=13.20)
# Midplane
# surf6: Unsupported surface type "analytic" with params ['1.', 'x', '0.00', 'constant']
# D38/HOLE
surf7 = openmc.XCylinder(surface_id=7, r=1.75)
# Duralumin/SIDE
surf8 = openmc.XCylinder(surface_id=8, r=11.0)
# Duralumin/RAM
surf9 = openmc.XCylinder(surface_id=9, r=2.5)
# Pu/BOTTOM
# surf10: Unsupported surface type "analytic" with params ['1.', 'x', '-0.61', 'constant']
# Pu/IR
surf11 = openmc.Sphere(surface_id=11, x0=1.4, y0=tr, z0=0.61, r=0.)
# Pu/OR
surf12 = openmc.Sphere(surface_id=12, x0=5.35, y0=tr, z0=0.61, r=0.)
# D38/1/OR
surf13 = openmc.Sphere(surface_id=13, x0=9.15, y0=tr, z0=0.61, r=0.)
# D38/2/OR
surf14 = openmc.Sphere(surface_id=14, x0=13.00, y0=tr, z0=0.61, r=0.)
# D38/LARGE/HOLE
surf15 = openmc.XCylinder(surface_id=15, r=1.75)
# D38/SMALL/HOLE
surf16 = openmc.XCylinder(surface_id=16, r=0.5)
# STL/Diaphragm
surf17 = openmc.XCylinder(surface_id=17, r=15.0)

# Z-plane surfaces for bounded cylinders
surf8_zmin = openmc.ZPlane(z0=-14.0)
surf8_zmax = openmc.ZPlane(z0=-3.0)
surf9_zmin = openmc.ZPlane(z0=-16.0)
surf9_zmax = openmc.ZPlane(z0=-7.0)
surf17_zmin = openmc.ZPlane(z0=0.41)
surf17_zmax = openmc.ZPlane(z0=0.61)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Pu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2 & -surf6

# Pu
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf10 & +surf11 & -surf12

# D38
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & -surf3 & -surf6 & +surf7

# D38
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf3 & -surf4 & -surf6

# D38
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf10 & +surf12 & -surf13 & +surf15

# D38
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf10 & +surf13 & -surf14 & +surf16

# Al
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf4 & -surf5 & -surf6 & (-surf8 & +surf8_zmin & -surf8_zmax)

# A1
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = +surf5 & (-surf9 & +surf9_zmin & -surf9_zmax)

# STL
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = -surf10 & (-surf17 & +surf17_zmin & -surf17_zmax)

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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
