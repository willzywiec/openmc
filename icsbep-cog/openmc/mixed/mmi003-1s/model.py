"""
MMI003-1: ZPR-3/54 Loading 11 Benchmark Model (Simplified)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Core
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu240", 1.065990e-04)
mat1.add_nuclide("Pu241", 8.393400e-06)
mat1.add_nuclide("U235", 6.026480e-06)
mat1.add_nuclide("U238", 2.601670e-03)
mat1.add_nuclide("Pu239", 1.654830e-03)
mat1.add_nuclide("Pu242", 3.422530e-07)
mat1.add_nuclide("Am241", 2.893030e-06)
mat1.add_element("Cr", 1.846890e-03)
mat1.add_element("Ni", 7.934540e-04)
mat1.add_element("Fe", 7.302290e-03)
mat1.add_element("Al", 1.104070e-04)
mat1.add_element("C", 5.558130e-02)
mat1.add_element("Mo", 2.094710e-04)
mat1.add_element("Mn", 9.881540e-05)
mat1.add_element("Cu", 2.791600e-06)
mat1.add_element("Si", 9.267160e-05)

# Axial
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cr", 1.473700e-03)
mat2.add_element("Ni", 6.201400e-04)
mat2.add_element("Fe", 7.558100e-02)
mat2.add_element("C", 5.590450e-04)
mat2.add_element("Mo", 3.726110e-09)
mat2.add_element("Mn", 5.690580e-04)
mat2.add_element("Cu", 2.765100e-07)
mat2.add_element("H", 1.430850e-06)
mat2.add_element("Si", 7.532890e-05)
mat2.add_element("Cl", 2.481360e-06)
mat2.add_element("F", 7.348040e-06)

# Radial
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cr", 1.141490e-03)
mat3.add_element("Ni", 4.583650e-04)
mat3.add_element("Fe", 7.471320e-02)
mat3.add_element("C", 5.598480e-04)
mat3.add_element("Mo", 9.554140e-09)
mat3.add_element("Mn", 5.546950e-04)
mat3.add_element("Cu", 2.966260e-08)
mat3.add_element("H", 9.589460e-08)
mat3.add_element("Si", 6.123920e-05)
mat3.add_element("Cl", 1.662990e-07)
mat3.add_element("F", 4.924600e-07)

# Drawer gap
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 3.460030e-03)
mat4.add_element("Ni", 1.601020e-03)
mat4.add_element("Fe", 1.925760e-02)
mat4.add_element("C", 2.642090e-04)
mat4.add_element("Mn", 2.347200e-04)
mat4.add_element("Si", 1.510070e-04)

# Matrix
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 1.109600e-03)
mat5.add_element("Ni", 4.535540e-04)
mat5.add_element("Fe", 4.529680e-03)
mat5.add_element("Mn", 4.349570e-05)
mat5.add_element("Si", 6.077000e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Core
surf1 = openmc.ZCylinder(surface_id=1, r=32.0805)
# Axial blanket
surf2 = openmc.ZCylinder(surface_id=2, r=32.0805)
# Drawer gap
surf3 = openmc.ZCylinder(surface_id=3, r=32.0805)
# Axial blanket
surf4 = openmc.ZCylinder(surface_id=4, r=32.0805)
# Radial blanket
surf5 = openmc.ZCylinder(surface_id=5, r=64.691)
# Matrix
surf6 = openmc.ZCylinder(surface_id=6, r=96.8226)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=-30.5634)
surf1_zmax = openmc.ZPlane(z0=30.5634)
surf2_zmin = openmc.ZPlane(z0=-53.4234)
surf2_zmax = openmc.ZPlane(z0=53.4234)
surf3_zmin = openmc.ZPlane(z0=-54.0584)
surf3_zmax = openmc.ZPlane(z0=54.0584)
surf4_zmin = openmc.ZPlane(z0=-61.6784)
surf4_zmax = openmc.ZPlane(z0=61.6784)
surf5_zmin = openmc.ZPlane(z0=-60.96)
surf5_zmax = openmc.ZPlane(z0=60.96)
surf6_zmin = openmc.ZPlane(z0=-85.09, boundary_type="vacuum")
surf6_zmax = openmc.ZPlane(z0=85.09, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# Ax
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# Gap
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# Ax
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# Rd
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# Mx
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)

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
