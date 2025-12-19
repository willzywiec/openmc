"""
PU-MET-INTER-004 (ZPR-3/59) Benchmark (R-Z) Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Core
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu240", 9.953650e-05)
mat1.add_nuclide("Pu241", 5.725620e-06)
mat1.add_nuclide("Pu239", 2.100810e-03)
mat1.add_nuclide("Pu238", 3.731870e-09)
mat1.add_nuclide("Pu242", 1.791010e-07)
mat1.add_nuclide("Am241", 3.293120e-06)
mat1.add_element("Cr", 1.914260e-03)
mat1.add_element("Ni", 8.561740e-04)
mat1.add_element("Fe", 7.449970e-03)
mat1.add_element("Al", 2.204210e-04)
mat1.add_nuclide("O16", 8.960440e-05)
mat1.add_element("C", 5.773090e-02)
mat1.add_element("Mo", 4.346890e-06)
mat1.add_element("Mn", 1.132240e-04)
mat1.add_element("Cu", 5.709330e-06)
mat1.add_element("Ti", 4.478130e-05)
mat1.add_element("Si", 9.559590e-05)
mat1.add_element("F", 1.431320e-04)

# Axial reflector
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cr", 1.466840e-03)
mat2.add_element("Ni", 6.207860e-04)
mat2.add_element("Fe", 5.893110e-03)
mat2.add_element("Mn", 7.209370e-05)
mat2.add_element("Pb", 2.751430e-02)
mat2.add_element("Si", 7.465980e-05)

# Radial reflector - half 1
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cr", 1.112120e-03)
mat3.add_element("Ni", 4.551970e-04)
mat3.add_element("Fe", 4.537860e-03)
mat3.add_element("Mn", 4.391920e-05)
mat3.add_element("Pb", 2.763450e-02)
mat3.add_element("Si", 6.078180e-05)

# Radial reflector - half 2
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 1.104310e-03)
mat4.add_element("Ni", 4.516680e-04)
mat4.add_element("Fe", 4.507180e-03)
mat4.add_element("Mn", 4.343310e-05)
mat4.add_element("Pb", 2.763930e-02)
mat4.add_element("Si", 6.042440e-05)
mat4.add_element("F", 1.216900e-05)

# Drawer gap
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 3.175370e-03)
mat5.add_element("Ni", 1.461920e-03)
mat5.add_element("Fe", 1.882650e-02)
mat5.add_element("C", 2.940490e-04)
mat5.add_element("Mn", 2.114940e-04)
mat5.add_element("Si", 1.401040e-04)

# Empty matrix
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Cr", 1.109600e-03)
mat6.add_element("Ni", 4.535540e-04)
mat6.add_element("Fe", 4.529680e-03)
mat6.add_element("Mn", 4.349570e-05)
mat6.add_element("Si", 6.077000e-05)
mat6.add_element("Mo", 8.236970e-06)
mat6.add_element("Si", 6.817470e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.ZPlane(surface_id=1, z0=-53.4248)
surf2 = openmc.ZPlane(surface_id=2, z0=-50.8106)
surf3 = openmc.ZPlane(surface_id=3, z0=-22.9448)
surf4 = openmc.ZPlane(surface_id=4, z0=0.0)
surf5 = openmc.ZPlane(surface_id=5, z0=28.0249)
surf6 = openmc.ZPlane(surface_id=6, z0=38.1849)
surf7 = openmc.ZPlane(surface_id=7, z0=38.8199)
surf8 = openmc.ZPlane(surface_id=8, z0=59.1392)
surf9 = openmc.ZPlane(surface_id=9, z0=60.8772)
surf10 = openmc.ZCylinder(surface_id=10, r=23.7864)
surf11 = openmc.ZCylinder(surface_id=11, r=23.8887)
surf12 = openmc.ZCylinder(surface_id=12, r=58.3482)
surf13 = openmc.ZCylinder(surface_id=13, r=96.8226, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf13_zmin = openmc.ZPlane(surface_id=1013, z0=-85.09, boundary_type="vacuum")
surf13_zmax = openmc.ZPlane(surface_id=1014, z0=85.09, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CoreH1
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf3 & -surf4 & -surf11

# CoreH2
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = +surf4 & -surf5 & -surf10

# AxRef1
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf1 & -surf3 & -surf11

# AxRef2
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf5 & -surf6 & -surf10

# DwgGap
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf6 & -surf7 & -surf10

# AxRef3
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = +surf7 & -surf8 & -surf10

# RdReH2
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf2 & -surf4 & +surf11 & -surf12

# RdReH1
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = +surf4 & -surf9 & +surf10 & -surf12

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8])
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
