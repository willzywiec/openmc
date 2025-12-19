"""
MIX-MET-INTER-004; ZPR-3 Assembly 53; Benchmark Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Core
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu240", 1.066050e-04)
mat1.add_nuclide("Pu241", 8.371890e-06)
mat1.add_nuclide("U235", 6.027190e-06)
mat1.add_nuclide("U238", 2.601960e-03)
mat1.add_nuclide("Pu239", 1.654900e-03)
mat1.add_nuclide("Pu238", 3.423790e-07)
mat1.add_nuclide("Pu242", 3.423790e-07)
mat1.add_nuclide("Am241", 2.915890e-06)
mat1.add_element("Cr", 1.840750e-03)
mat1.add_element("Ni", 7.904570e-04)
mat1.add_element("Fe", 7.278910e-03)
mat1.add_element("Al", 1.104080e-04)
mat1.add_element("C", 5.560780e-02)
mat1.add_element("Mo", 2.094950e-04)
mat1.add_element("Mn", 9.831530e-05)
mat1.add_element("Cu", 2.791630e-06)
mat1.add_element("Si", 9.243620e-05)

# Axial Blanket
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 8.284760e-05)
mat2.add_nuclide("U238", 3.963500e-02)
mat2.add_element("Cr", 1.449240e-03)
mat2.add_element("Ni", 6.184870e-04)
mat2.add_element("Fe", 5.826110e-03)
mat2.add_element("C", 1.371510e-05)
mat2.add_element("Mn", 7.065760e-05)
mat2.add_element("H", 3.978710e-06)
mat2.add_element("Si", 7.398580e-05)
mat2.add_element("Cl", 6.879730e-06)
mat2.add_element("F", 2.037170e-05)

# Radial Blanket
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U235", 8.345230e-05)
mat3.add_nuclide("U238", 3.992530e-02)
mat3.add_element("Cr", 1.107160e-03)
mat3.add_element("Ni", 4.527730e-04)
mat3.add_element("Fe", 4.519010e-03)
mat3.add_element("C", 8.402600e-06)
mat3.add_element("Mn", 4.351320e-05)
mat3.add_element("H", 2.430870e-06)
mat3.add_element("Si", 6.059280e-05)
mat3.add_element("Cl", 4.214760e-06)
mat3.add_element("F", 1.248110e-05)

# Drawer Gap
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 3.457180e-03)
mat4.add_element("Ni", 1.599620e-03)
mat4.add_element("Fe", 1.921120e-02)
mat4.add_element("C", 2.625850e-04)
mat4.add_element("Mn", 2.344870e-04)
mat4.add_element("Si", 1.508980e-04)

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

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Core
surf1 = openmc.ZCylinder(surface_id=1, r=34.3564)
# Axial Blanket
surf2 = openmc.ZCylinder(surface_id=2, r=34.3564)
# Drawer Gap
surf3 = openmc.ZCylinder(surface_id=3, r=34.3564)
# Drawer Gap
surf4 = openmc.ZCylinder(surface_id=4, r=34.3564)
# Radial Blanket
surf5 = openmc.ZCylinder(surface_id=5, r=68.4995)
# Matrix
surf6 = openmc.ZCylinder(surface_id=6, r=96.8226, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1006, z0=-30.5631)
surf1_zmax = openmc.ZPlane(surface_id=1007, z0=30.5631)
surf2_zmin = openmc.ZPlane(surface_id=1008, z0=-61.6781)
surf2_zmax = openmc.ZPlane(surface_id=1009, z0=61.6781)
surf3_zmin = openmc.ZPlane(surface_id=1010, z0=53.4231)
surf3_zmax = openmc.ZPlane(surface_id=1011, z0=54.0581)
surf4_zmin = openmc.ZPlane(surface_id=1012, z0=-54.0581)
surf4_zmax = openmc.ZPlane(surface_id=1013, z0=-53.4231)
surf5_zmin = openmc.ZPlane(surface_id=1014, z0=-60.96)
surf5_zmax = openmc.ZPlane(surface_id=1015, z0=60.96)
surf6_zmin = openmc.ZPlane(surface_id=1016, z0=-85.09, boundary_type="vacuum")
surf6_zmax = openmc.ZPlane(surface_id=1017, z0=85.09, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

# AxBlnkt
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax)

# Gap
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# Gap
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# RdBlnkt
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# Matrix
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)

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
