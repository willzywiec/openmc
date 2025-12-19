"""
IEU-MET-FAST-015-1: ZPR-3/6F spherical (simplified) benchmark
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Core
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 6.675530e-03)
mat1.add_nuclide("U238", 7.523390e-03)
mat1.add_nuclide("U234", 6.504990e-05)
mat1.add_nuclide("U236", 3.118530e-05)
mat1.add_element("Cr", 1.803930e-03)
mat1.add_element("Ni", 7.889890e-04)
mat1.add_element("Fe", 7.672310e-03)
mat1.add_element("Al", 2.060540e-02)
mat1.add_element("C", 3.317660e-05)
mat1.add_element("Mo", 5.773800e-06)
mat1.add_element("Mn", 9.458630e-05)
mat1.add_element("Cu", 6.986250e-06)
mat1.add_element("H", 6.428960e-06)
mat1.add_element("Si", 9.327040e-05)
mat1.add_element("Cl", 1.108580e-05)
mat1.add_element("F", 3.282650e-05)

# Reflector
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 8.085390e-05)
mat2.add_nuclide("U238", 3.981740e-02)
mat2.add_element("Cr", 1.118630e-03)
mat2.add_element("Ni", 4.587390e-04)
mat2.add_element("Fe", 4.574850e-03)
mat2.add_element("Al", 6.851730e-04)
mat2.add_element("C", 1.032910e-05)
mat2.add_element("Mo", 6.459450e-10)
mat2.add_element("Mn", 4.467230e-05)
mat2.add_element("Cu", 1.642540e-09)
mat2.add_element("H", 2.795620e-06)
mat2.add_element("Si", 6.091510e-05)
mat2.add_element("Cl", 4.835470e-06)
mat2.add_element("F", 1.431860e-05)

# Matrix
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cr", 1.109600e-03)
mat3.add_element("Ni", 4.535540e-04)
mat3.add_element("Fe", 4.529680e-03)
mat3.add_element("Mn", 4.349570e-05)
mat3.add_element("Si", 6.077000e-05)

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=22.9235)
surf2 = openmc.Sphere(surface_id=2, r=64.0363)
surf3 = openmc.Sphere(surface_id=3, r=106.1633, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# U47
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Refl
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# Mtrx
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & -surf3

root_universe = openmc.Universe(cells=[cell1, cell2, cell3])
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
