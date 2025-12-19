"""
MIX-COMP-FAST-005; ZPR-9 Assembly 31; Benchmark Model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Core
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu240", 1.759520e-04)
mat1.add_nuclide("Pu241", 1.781980e-05)
mat1.add_nuclide("U235", 2.131110e-05)
mat1.add_nuclide("U238", 9.788670e-03)
mat1.add_nuclide("Pu239", 1.328150e-03)
mat1.add_nuclide("Pu238", 7.132340e-07)
mat1.add_nuclide("Pu242", 2.662450e-06)
mat1.add_nuclide("Am241", 8.543200e-06)
mat1.add_element("Cr", 2.895130e-03)
mat1.add_element("Ni", 1.304220e-03)
mat1.add_element("Fe", 1.025120e-02)
mat1.add_element("Al", 5.135640e-06)
mat1.add_element("Na", 8.911850e-03)
mat1.add_nuclide("O16", 4.942650e-06)
mat1.add_element("C", 1.080100e-02)
mat1.add_element("Mo", 3.539150e-04)
mat1.add_element("Mn", 2.455190e-04)
mat1.add_element("Cu", 3.457310e-05)
mat1.add_element("H", 1.119980e-05)
mat1.add_element("Si", 1.714200e-04)
mat1.add_element("Ca", 2.046320e-06)
mat1.add_element("Cl", 4.900520e-06)
mat1.add_element("Co", 4.616450e-06)
mat1.add_element("F", 1.365530e-05)

# Axial Blanket
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 2.575030e-05)
mat2.add_nuclide("U238", 1.206690e-02)
mat2.add_element("Cr", 2.394220e-03)
mat2.add_element("Ni", 1.050400e-03)
mat2.add_element("Fe", 8.528950e-03)
mat2.add_element("Al", 2.816910e-06)
mat2.add_element("Na", 9.148040e-03)
mat2.add_nuclide("O16", 5.683340e-06)
mat2.add_element("C", 1.261020e-02)
mat2.add_element("Mo", 1.483560e-05)
mat2.add_element("Mn", 2.038810e-04)
mat2.add_element("Cu", 3.174280e-05)
mat2.add_element("H", 1.562250e-05)
mat2.add_element("Si", 1.457600e-04)
mat2.add_element("Ca", 2.100330e-06)
mat2.add_element("Cl", 9.807180e-06)
mat2.add_element("Co", 4.393050e-06)
mat2.add_element("F", 2.818530e-05)

# Radial Blanket
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U235", 2.585190e-05)
mat3.add_nuclide("U238", 1.208350e-02)
mat3.add_element("Cr", 2.385450e-03)
mat3.add_element("Ni", 1.039990e-03)
mat3.add_element("Fe", 8.473940e-03)
mat3.add_element("Al", 2.299400e-06)
mat3.add_element("Na", 9.129690e-03)
mat3.add_nuclide("O16", 5.778090e-06)
mat3.add_element("C", 1.284510e-02)
mat3.add_element("Mo", 1.593690e-05)
mat3.add_element("Mn", 2.020870e-04)
mat3.add_element("Cu", 3.214910e-05)
mat3.add_element("H", 1.559920e-05)
mat3.add_element("Si", 1.377360e-04)
mat3.add_element("Ca", 2.096010e-06)
mat3.add_element("Cl", 9.641820e-06)
mat3.add_element("Co", 3.737070e-06)
mat3.add_element("F", 2.767800e-05)

# Radial Reflector
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 1.568550e-02)
mat4.add_element("Ni", 6.766190e-03)
mat4.add_element("Fe", 5.539620e-02)
mat4.add_element("C", 2.384910e-04)
mat4.add_element("Mo", 6.186190e-05)
mat4.add_element("Mn", 1.355970e-03)
mat4.add_element("Cu", 5.499150e-05)
mat4.add_element("Si", 8.419170e-04)
mat4.add_element("Co", 3.805980e-06)

# Axial Reflector
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 1.529410e-02)
mat5.add_element("Ni", 6.723540e-03)
mat5.add_element("Fe", 5.392730e-02)
mat5.add_element("C", 2.533740e-04)
mat5.add_element("Mo", 1.558920e-05)
mat5.add_element("Mn", 1.468920e-03)
mat5.add_element("Cu", 3.049990e-05)
mat5.add_element("Si", 1.010990e-03)
mat5.add_element("Co", 4.080250e-06)

# Matrix
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Cr", 1.179570e-03)
mat6.add_element("Ni", 4.763300e-04)
mat6.add_element("Fe", 4.244880e-03)
mat6.add_element("C", 1.859330e-05)
mat6.add_element("Mo", 8.190760e-06)
mat6.add_element("Mn", 1.050570e-04)
mat6.add_element("Cu", 1.709440e-05)
mat6.add_element("Si", 6.776300e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.ZCylinder(surface_id=1, r=59.0562)
surf2 = openmc.ZCylinder(surface_id=2, r=59.0562)
surf3 = openmc.ZCylinder(surface_id=3, r=89.3018)
surf4 = openmc.ZCylinder(surface_id=4, r=89.3018)
surf5 = openmc.ZCylinder(surface_id=5, r=105.4629)
surf6 = openmc.ZCylinder(surface_id=6, r=140.2589, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1006, z0=-45.7993)
surf1_zmax = openmc.ZPlane(surface_id=1007, z0=45.7993)
surf2_zmin = openmc.ZPlane(surface_id=1008, z0=-76.297)
surf2_zmax = openmc.ZPlane(surface_id=1009, z0=76.297)
surf3_zmin = openmc.ZPlane(surface_id=1010, z0=-76.297)
surf3_zmax = openmc.ZPlane(surface_id=1011, z0=76.297)
surf4_zmin = openmc.ZPlane(surface_id=1012, z0=-92.0801)
surf4_zmax = openmc.ZPlane(surface_id=1013, z0=92.0801)
surf5_zmin = openmc.ZPlane(surface_id=1014, z0=-92.0801)
surf5_zmax = openmc.ZPlane(surface_id=1015, z0=92.0801)
surf6_zmin = openmc.ZPlane(surface_id=1016, z0=-121.92, boundary_type="vacuum")
surf6_zmax = openmc.ZPlane(surface_id=1017, z0=121.92, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# AxBlnkt
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# RdBlnkt
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)

# AxRflct
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# RdRflct
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)

# Matrix
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)

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
