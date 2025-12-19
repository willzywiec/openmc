"""
IEU-MET-FAST-016-1s: ZPR-3 Assembly 11 Loading 10: Simplified benchmark R/Z model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Core
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 4.534070e-03)
mat1.add_nuclide("U238", 3.424870e-02)
mat1.add_nuclide("U234", 4.359640e-05)
mat1.add_nuclide("U236", 2.090050e-05)
mat1.add_element("Cr", 1.430700e-03)
mat1.add_element("Ni", 6.128620e-04)
mat1.add_element("Fe", 5.743690e-03)
mat1.add_element("C", 3.809650e-05)
mat1.add_element("Mn", 7.096850e-05)
mat1.add_element("H", 1.111710e-05)
mat1.add_element("Si", 7.256660e-05)
mat1.add_element("Cl", 1.911130e-05)
mat1.add_element("F", 5.658820e-05)

# Axial Blanket
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 8.090670e-05)
mat2.add_nuclide("U238", 3.983610e-02)
mat2.add_element("Cr", 1.446260e-03)
mat2.add_element("Ni", 6.170310e-04)
mat2.add_element("Fe", 5.814740e-03)
mat2.add_element("C", 1.046300e-05)
mat2.add_element("Mn", 7.041510e-05)
mat2.add_element("H", 3.037080e-06)
mat2.add_element("Si", 7.387100e-05)
mat2.add_element("Cl", 5.248610e-06)
mat2.add_element("F", 1.554180e-05)

# Radial Blanket
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U235", 8.124590e-05)
mat3.add_nuclide("U238", 4.002150e-02)
mat3.add_element("Cr", 1.114100e-03)
mat3.add_element("Ni", 4.562910e-04)
mat3.add_element("Fe", 4.547240e-03)
mat3.add_element("C", 8.726930e-06)
mat3.add_element("Mn", 4.414750e-05)
mat3.add_element("H", 2.496110e-06)
mat3.add_element("Si", 6.083170e-05)
mat3.add_element("Cl", 4.325450e-06)
mat3.add_element("F", 1.280880e-05)

# Drawer Gap
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 3.511520e-03)
mat4.add_element("Ni", 1.633910e-03)
mat4.add_element("Fe", 1.947810e-02)
mat4.add_element("C", 2.687420e-04)
mat4.add_element("Mo", 5.560950e-08)
mat4.add_element("Mn", 2.374820e-04)
mat4.add_element("Cu", 3.355510e-07)
mat4.add_element("Si", 1.501110e-04)

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
surf1 = openmc.ZCylinder(surface_id=1, r=29.34289)
# Drawer Gap
surf2 = openmc.ZCylinder(surface_id=2, r=29.34289)
# Drawer Gap
surf3 = openmc.ZCylinder(surface_id=3, r=29.34289)
# Axial Blanket
surf4 = openmc.ZCylinder(surface_id=4, r=29.34289)
# Radial Blanket
surf5 = openmc.ZCylinder(surface_id=5, r=65.31094)
# Matrix
surf6 = openmc.ZCylinder(surface_id=6, r=96.82257, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1006, z0=-25.48128)
surf1_zmax = openmc.ZPlane(surface_id=1007, z0=25.48128)
surf2_zmin = openmc.ZPlane(surface_id=1008, z0=-38.80722)
surf2_zmax = openmc.ZPlane(surface_id=1009, z0=-38.18128)
surf3_zmin = openmc.ZPlane(surface_id=1010, z0=38.18128)
surf3_zmax = openmc.ZPlane(surface_id=1011, z0=38.80722)
surf4_zmin = openmc.ZPlane(surface_id=1012, z0=-56.58722)
surf4_zmax = openmc.ZPlane(surface_id=1013, z0=56.58722)
surf5_zmin = openmc.ZPlane(surface_id=1014, z0=-55.88)
surf5_zmax = openmc.ZPlane(surface_id=1015, z0=55.88)
surf6_zmin = openmc.ZPlane(surface_id=1016, z0=-85.09, boundary_type="vacuum")
surf6_zmax = openmc.ZPlane(surface_id=1017, z0=85.09, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax)

# Drwr
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = (-surf2 & +surf2_zmin & -surf2_zmax)

# Drwr
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = (-surf3 & +surf3_zmin & -surf3_zmax)

# AxBl
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

# RdBl
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# Mtrx
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)

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
