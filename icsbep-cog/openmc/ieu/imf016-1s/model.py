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

# Core
surf1 = openmc.ZCylinder(surface_id=1, x0=-25.48128, y0=25.48128, r=29.34289)
# Drawer Gap
surf2 = openmc.ZCylinder(surface_id=2, x0=-38.80722, y0=-38.18128, r=29.34289)
# Drawer Gap
surf3 = openmc.ZCylinder(surface_id=3, x0=38.18128, y0=38.80722, r=29.34289)
# Axial Blanket
surf4 = openmc.ZCylinder(surface_id=4, x0=-56.58722, y0=56.58722, r=29.34289)
# Radial Blanket
surf5 = openmc.ZCylinder(surface_id=5, x0=-55.88000, y0=55.88000, r=65.31094)
# Matrix
surf6 = openmc.ZCylinder(surface_id=6, x0=-85.09000, y0=85.09000, r=96.82257, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Drwr
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = -surf2

# Drwr
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = -surf3

# AxBl
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf1 & +surf2 & +surf3 & -surf4

# RdBl
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf1 & +surf2 & +surf3 & +surf4 & -surf5

# Mtrx
cell6 = openmc.Cell(cell_id=6, fill=mat5)
cell6.region = +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & -surf6

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
