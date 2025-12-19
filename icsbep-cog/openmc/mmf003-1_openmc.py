"""
MIX-MET-FAST-003-1: Sphere of plutonium surronded by HEU (VNIITF)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# d-Pu-Ga
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.392800e-02)
mat1.add_nuclide("Pu240", 3.503200e-03)
mat1.add_nuclide("Pu241", 3.915800e-04)
mat1.add_element("Ga", 2.210400e-03)
mat1.add_element("C", 3.024400e-04)
mat1.add_element("Fe", 3.252300e-04)
mat1.add_element("W", 7.409400e-05)
mat1.add_element("Ni", 1.426600e-03)

# HEU
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 4.108100e-02)
mat2.add_nuclide("U238", 4.100200e-03)
mat2.add_nuclide("U234", 5.225300e-04)
mat2.add_nuclide("U236", 8.898100e-05)
mat2.add_element("C", 3.865000e-04)
mat2.add_element("Fe", 1.502700e-04)
mat2.add_element("W", 1.232900e-05)
mat2.add_element("Cu", 7.362600e-04)
mat2.add_element("Ni", 3.416500e-04)

# Duralumin
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Al", 5.807700e-02)
mat3.add_element("Mg", 1.033200e-03)
mat3.add_element("Mn", 1.828400e-04)
mat3.add_element("Cu", 1.132900e-03)

# Iron
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 8.117400e-02)

# Copper
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cu", 8.236500e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=1.00)
surf2 = openmc.Sphere(surface_id=2, r=5.35)
surf3 = openmc.Sphere(surface_id=3, r=7.55)
surf4 = openmc.Sphere(surface_id=4, r=7.70)
surf5 = openmc.ZPlane(surface_id=5, z0=0.0)
surf6 = openmc.XCylinder(surface_id=6, r=0.6)
surf7 = openmc.ZCylinder(surface_id=7, r=2.5)
surf8 = openmc.ZCylinder(surface_id=8, r=6.5)
surf9 = openmc.ZCylinder(surface_id=9, r=5.5)
surf10 = openmc.ZCylinder(surface_id=10, r=14.0)
surf11 = openmc.XCylinder(surface_id=11, x0=0.0, y0=0.0, r=0.6)
surf12 = openmc.ZCylinder(surface_id=12, r=1.1)
surf13 = openmc.Sphere(surface_id=13, x0=5.35, y0=tr, z0=0, r=0)
surf14 = openmc.Sphere(surface_id=14, x0=7.55, y0=tr, z0=0, r=0)
surf15 = openmc.ZPlane(surface_id=15, z0=1.225)
surf99 = openmc.ZCylinder(surface_id=99, r=15.0, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf7_zmin = openmc.ZPlane(surface_id=1099, z0=-14.7)
surf7_zmax = openmc.ZPlane(surface_id=1100, z0=-6.0)
surf10_zmin = openmc.ZPlane(surface_id=1101, z0=1.025)
surf10_zmax = openmc.ZPlane(surface_id=1102, z0=1.225)
surf99_zmin = openmc.ZPlane(surface_id=1103, z0=-15.0, boundary_type="vacuum")
surf99_zmax = openmc.ZPlane(surface_id=1104, z0=10.0, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# dPuGa
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# HEU
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3 & -surf5 & +surf6

# Cu
cell3 = openmc.Cell(cell_id=3, fill=mat5)
cell3.region = +surf3 & -surf4 & -surf5 & -surf8

# Iron
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf4 & (-surf7 & +surf7_zmin & -surf7_zmax)

# Dural
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf9 & (-surf10 & +surf10_zmin & -surf10_zmax)

# HEU
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf11 & +surf12 & +surf13 & -surf14 & +surf15

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6])
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
