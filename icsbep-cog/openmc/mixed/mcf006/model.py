"""
MIX-COMP-FAST-006; ZPPR-2 Loading 90 31; Benchmark Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Inner Core
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu240", 1.116510e-04)
mat1.add_nuclide("Pu241", 1.546620e-05)
mat1.add_nuclide("U235", 1.208490e-05)
mat1.add_nuclide("U238", 5.555910e-03)
mat1.add_nuclide("Pu239", 8.432040e-04)
mat1.add_nuclide("Pu238", 5.435680e-07)
mat1.add_nuclide("Pu242", 1.829640e-06)
mat1.add_nuclide("Am241", 1.840760e-06)
mat1.add_element("Cr", 2.290600e-03)
mat1.add_element("Ni", 1.049930e-03)
mat1.add_element("Fe", 1.117550e-02)
mat1.add_element("Al", 3.928930e-06)
mat1.add_element("Na", 8.785780e-03)
mat1.add_nuclide("O16", 1.311390e-02)
mat1.add_element("C", 3.171400e-05)
mat1.add_element("Mo", 2.284170e-04)
mat1.add_element("Mn", 1.889130e-04)
mat1.add_element("Cu", 1.844340e-05)
mat1.add_element("H", 1.322540e-06)
mat1.add_element("Si", 1.100680e-04)
mat1.add_element("Ca", 2.017610e-06)
mat1.add_element("Cl", 2.511930e-06)
mat1.add_element("Co", 7.887860e-07)
mat1.add_element("F", 6.603140e-06)

# Outer Core
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("Pu240", 1.686760e-04)
mat2.add_nuclide("Pu241", 2.326410e-05)
mat2.add_nuclide("U235", 1.144110e-05)
mat2.add_nuclide("U238", 5.198410e-03)
mat2.add_nuclide("Pu239", 1.273970e-03)
mat2.add_nuclide("Pu238", 8.240480e-07)
mat2.add_nuclide("Pu242", 2.753470e-06)
mat2.add_nuclide("Am241", 2.762590e-06)
mat2.add_element("Cr", 2.495170e-03)
mat2.add_element("Ni", 1.155260e-03)
mat2.add_element("Fe", 1.370460e-02)
mat2.add_element("Al", 4.937310e-06)
mat2.add_element("Na", 8.576530e-03)
mat2.add_nuclide("O16", 1.153920e-02)
mat2.add_element("C", 2.957190e-05)
mat2.add_element("Mo", 3.382980e-04)
mat2.add_element("Mn", 2.059590e-04)
mat2.add_element("Cu", 1.968720e-05)
mat2.add_element("H", 6.612740e-07)
mat2.add_element("Si", 1.210660e-04)
mat2.add_element("Ca", 1.969540e-06)
mat2.add_element("Cl", 1.391520e-06)
mat2.add_element("Co", 9.333870e-07)
mat2.add_element("F", 3.301590e-05)

# Inner Core Axial
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U235", 1.531170e-05)
mat3.add_nuclide("U238", 7.058490e-03)
mat3.add_element("Cr", 2.443820e-03)
mat3.add_element("Ni", 1.113190e-03)
mat3.add_element("Fe", 9.397450e-03)
mat3.add_element("Al", 2.726000e-06)
mat3.add_element("Na", 8.768690e-03)
mat3.add_nuclide("O16", 1.386960e-02)
mat3.add_element("C", 4.432260e-05)
mat3.add_element("Mo", 1.320220e-05)
mat3.add_element("Mn", 2.083660e-04)
mat3.add_element("Cu", 1.709450e-05)
mat3.add_element("H", 3.055130e-06)
mat3.add_element("Si", 1.209680e-04)
mat3.add_element("Ca", 2.014520e-06)
mat3.add_element("Cl", 5.500220e-06)
mat3.add_element("Co", 7.955770e-07)
mat3.add_element("F", 1.545420e-05)

# Outer Core Axial
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("U235", 1.531150e-05)
mat4.add_nuclide("U238", 7.058470e-03)
mat4.add_element("Cr", 2.412120e-03)
mat4.add_element("Ni", 1.099470e-03)
mat4.add_element("Fe", 9.325830e-03)
mat4.add_element("Al", 2.739360e-06)
mat4.add_element("Na", 8.811670e-03)
mat4.add_nuclide("O16", 1.392260e-02)
mat4.add_element("C", 4.382800e-05)
mat4.add_element("Mo", 1.316130e-05)
mat4.add_element("Mn", 2.061840e-04)
mat4.add_element("Cu", 1.704960e-05)
mat4.add_element("H", 3.055310e-06)
mat4.add_element("Si", 1.190870e-04)
mat4.add_element("Ca", 2.024410e-06)
mat4.add_element("Cl", 5.501840e-06)
mat4.add_element("Co", 7.994760e-07)
mat4.add_element("F", 1.545490e-05)

# Inner Radial
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("U235", 2.416800e-05)
mat5.add_nuclide("U238", 1.108130e-02)
mat5.add_element("Cr", 1.969800e-03)
mat5.add_element("Ni", 8.907400e-04)
mat5.add_element("Fe", 6.855010e-03)
mat5.add_element("Al", 2.281610e-06)
mat5.add_element("Na", 6.407030e-03)
mat5.add_nuclide("O16", 2.018180e-02)
mat5.add_element("C", 1.027440e-03)
mat5.add_element("Mo", 1.349610e-05)
mat5.add_element("Mn", 1.625410e-04)
mat5.add_element("Cu", 1.677440e-05)
mat5.add_element("H", 1.317300e-05)
mat5.add_element("Si", 9.077510e-05)
mat5.add_element("Ca", 1.016360e-06)
mat5.add_element("Cl", 9.877830e-06)
mat5.add_element("Co", 4.105040e-07)
mat5.add_element("F", 2.106660e-05)

# Outer Radial
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("U235", 2.416800e-05)
mat6.add_nuclide("U238", 1.108130e-02)
mat6.add_element("Cr", 2.157440e-03)
mat6.add_element("Ni", 9.869100e-04)
mat6.add_element("Fe", 7.506650e-03)
mat6.add_element("Al", 3.147470e-06)
mat6.add_element("Na", 5.994350e-03)
mat6.add_nuclide("O16", 2.018240e-02)
mat6.add_element("C", 1.028640e-03)
mat6.add_element("Mo", 1.360560e-05)
mat6.add_element("Mn", 1.765320e-04)
mat6.add_element("Cu", 1.780490e-05)
mat6.add_element("H", 1.317300e-05)
mat6.add_element("Si", 1.024240e-04)
mat6.add_element("Ca", 9.211230e-07)
mat6.add_element("Cl", 9.864380e-06)
mat6.add_element("Co", 6.894880e-07)
mat6.add_element("F", 2.106660e-05)

# Axial Reflector
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Cr", 5.336290e-03)
mat7.add_element("Ni", 2.285080e-03)
mat7.add_element("Fe", 3.549030e-02)
mat7.add_element("Al", 2.604350e-06)
mat7.add_element("Na", 8.935240e-03)
mat7.add_nuclide("O16", 6.477150e-07)
mat7.add_element("C", 1.976330e-04)
mat7.add_element("Mo", 5.399170e-05)
mat7.add_element("Mn", 5.460980e-04)
mat7.add_element("Cu", 4.599170e-05)
mat7.add_element("Si", 1.851510e-04)
mat7.add_element("Ca", 2.050020e-06)
mat7.add_element("Cl", 2.923030e-07)
mat7.add_element("Co", 7.844210e-07)

# Axial Reflector
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Cr", 1.557310e-03)
mat8.add_element("Ni", 6.705060e-04)
mat8.add_element("Fe", 7.238800e-02)
mat8.add_element("C", 5.588250e-04)
mat8.add_element("Mo", 1.284970e-05)
mat8.add_element("Mn", 6.211760e-04)
mat8.add_element("Cu", 1.414640e-05)

# Radial Reflector
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Cr", 1.192340e-03)
mat9.add_element("Ni", 5.077000e-04)
mat9.add_element("Fe", 7.150350e-02)
mat9.add_element("C", 5.570120e-04)
mat9.add_element("Mo", 1.163430e-05)
mat9.add_element("Mn", 5.966980e-04)
mat9.add_element("Cu", 1.248140e-05)
mat9.add_element("Si", 4.968520e-05)

# Drawer Gap
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_element("Cr", 4.786170e-03)
mat10.add_element("Ni", 1.620840e-03)
mat10.add_element("Fe", 2.324360e-02)
mat10.add_element("Al", 1.089370e-06)
mat10.add_element("C", 3.174580e-04)
mat10.add_element("Mo", 2.441810e-05)
mat10.add_element("Mn", 2.999550e-04)
mat10.add_element("Cu", 3.210590e-05)
mat10.add_element("Si", 1.831230e-04)

# Matrix
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_element("Cr", 1.172880e-03)
mat11.add_element("Ni", 5.087800e-04)
mat11.add_element("Fe", 4.073960e-03)
mat11.add_element("C", 1.898620e-05)
mat11.add_element("Mo", 1.165900e-05)
mat11.add_element("Mn", 1.055780e-04)
mat11.add_element("Cu", 1.250790e-05)
mat11.add_element("Si", 4.979100e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11])

# ==============================================================================
# Geometry
# ==============================================================================

# Inner Core
surf1 = openmc.ZCylinder(surface_id=1, r=64.6533)
# Outer Core
surf2 = openmc.ZCylinder(surface_id=2, r=91.4336)
# Axial Blanket
surf3 = openmc.ZCylinder(surface_id=3, r=94.4336)
# IRB
surf4 = openmc.ZCylinder(surface_id=4, r=110.3359)
# ORB
surf5 = openmc.ZCylinder(surface_id=5, r=129.4246)
# Axial Reflector
surf6 = openmc.ZCylinder(surface_id=6, r=129.4246)
# Radial Reflector
surf7 = openmc.ZCylinder(surface_id=7, r=141.152)
# Matrix
surf8 = openmc.ZCylinder(surface_id=8, r=172.1826)
# Upper Drawer Gap
surf11 = openmc.ZCylinder(surface_id=11, r=129.4246)
# Lower Drawer Gap
surf12 = openmc.ZCylinder(surface_id=12, r=129.4246)

# Z-plane surfaces for bounded cylinders
surf2_zmin = openmc.ZPlane(z0=-45.8117)
surf2_zmax = openmc.ZPlane(z0=45.8117)
surf3_zmin = openmc.ZPlane(z0=-87.0922)
surf3_zmax = openmc.ZPlane(z0=87.0922)
surf4_zmin = openmc.ZPlane(z0=-87.0922)
surf4_zmax = openmc.ZPlane(z0=87.0922)
surf5_zmin = openmc.ZPlane(z0=-87.0922)
surf5_zmax = openmc.ZPlane(z0=87.0922)
surf6_zmin = openmc.ZPlane(z0=-99.7922)
surf6_zmax = openmc.ZPlane(z0=107.4122)
surf7_zmin = openmc.ZPlane(z0=-96.52)
surf7_zmax = openmc.ZPlane(z0=96.52)
surf8_zmin = openmc.ZPlane(z0=-121.92, boundary_type="vacuum")
surf8_zmax = openmc.ZPlane(z0=121.92, boundary_type="vacuum")
surf11_zmin = openmc.ZPlane(z0=58.5117)
surf11_zmax = openmc.ZPlane(z0=59.1522)
surf12_zmin = openmc.ZPlane(z0=-59.1522)
surf12_zmax = openmc.ZPlane(z0=-58.5117)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# In-Core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & (-surf2 & +surf2_zmin & -surf2_zmax)

# Ou-Core
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & (-surf2 & +surf2_zmin & -surf2_zmax)

# IC-AB
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = -surf1 & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax)

# OC-AB
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf1 & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax)

# IRB
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax)

# ORB
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax)

# Ax-Refl
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)

# Rd-Refl
cell8 = openmc.Cell(cell_id=8, fill=mat9)
cell8.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)

# GAP
cell9 = openmc.Cell(cell_id=9, fill=mat10)
cell9.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf11 & +surf11_zmin & -surf11_zmax)

# GAP
cell10 = openmc.Cell(cell_id=10, fill=mat10)
cell10.region = (-surf5 & +surf5_zmin & -surf5_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)

# Matrix
cell11 = openmc.Cell(cell_id=11, fill=mat11)
cell11.region = (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11])
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
