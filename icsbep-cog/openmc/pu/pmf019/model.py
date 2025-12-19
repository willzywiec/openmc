"""
PU-MET-FAST-019: Sphere of Pu Reflected by Beryllium at VNIITF
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

# Be ---- Table 1
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Be", 1.208100e-01)
mat2.add_nuclide("O16", 8.206400e-05)
mat2.add_element("C", 1.002000e-04)
mat2.add_element("Fe", 5.093900e-05)

# Cu ---- section 3.3
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cu", 8.236500e-02)

# Steel - Section 3.3
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 8.117400e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Pu/IR
surf1 = openmc.Sphere(surface_id=1, r=1.4)
# Pu/OR
surf2 = openmc.Sphere(surface_id=2, r=5.35)
# Be/OR/LHS
surf3 = openmc.Sphere(surface_id=3, r=11.0)
# Cu/OR
surf4 = openmc.Sphere(surface_id=4, r=11.15)
# Be/TOP/LHS
# surf5: Unsupported surface type "analytic" with params ['1.', 'x', '0.15', 'constant']
# Cu/SIDE
surf6 = openmc.XCylinder(surface_id=6, r=9.7)
# Steel
surf7 = openmc.XCylinder(surface_id=7, r=2.5)
# Be/IR
surf11 = openmc.Sphere(surface_id=11, x0=5.35, y0=tr, z0=1.05, r=0.)
# Be/OR
surf12 = openmc.Sphere(surface_id=12, x0=11.00, y0=tr, z0=1.05, r=0.)
# Be/Bottom
# surf13: Unsupported surface type "analytic" with params ['1.', 'x', '-1.20', 'constant']
# Be/Hole
surf14 = openmc.XCylinder(surface_id=14, r=1.1)
# STL/IR
surf21 = openmc.XCylinder(surface_id=21, r=5.5)
# STL/OR
surf22 = openmc.XCylinder(surface_id=22, r=14.0)

# Z-plane surfaces for bounded cylinders
surf6_zmin = openmc.ZPlane(surface_id=1022, z0=-12.0)
surf6_zmax = openmc.ZPlane(surface_id=1023, z0=-3.0)
surf7_zmin = openmc.ZPlane(surface_id=1024, z0=-14.15)
surf7_zmax = openmc.ZPlane(surface_id=1025, z0=-7.0)
surf21_zmin = openmc.ZPlane(surface_id=1026, z0=1.0)
surf21_zmax = openmc.ZPlane(surface_id=1027, z0=1.2)
surf22_zmin = openmc.ZPlane(surface_id=1028, z0=1.0)
surf22_zmax = openmc.ZPlane(surface_id=1029, z0=1.2)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Pu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# Be
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3 & -surf5

# Be
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf11 & -surf12 & +surf13 & +surf14

# Cu
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf3 & -surf4 & (-surf6 & +surf6_zmin & -surf6_zmax)

# STL
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf4 & (-surf7 & +surf7_zmin & -surf7_zmax)

# STL
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = (+surf21 | -surf21_zmin | +surf21_zmax) & (-surf22 & +surf22_zmin & -surf22_zmax)

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
