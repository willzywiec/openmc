"""
LCT028-5: 283 U(4.31)O2 rods with 2.286 cm triangular pitch in water with 0.4293 gCd/l
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(4.31)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 5.179000e-06)
mat1.add_nuclide("U235", 1.009300e-03)
mat1.add_nuclide("U236", 5.135000e-06)
mat1.add_nuclide("U238", 2.213800e-02)
mat1.add_nuclide("O16", 4.631500e-02)

# SS304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 1.188300e-04)
mat2.add_element("Mn", 8.659700e-04)
mat2.add_element("Si", 1.693900e-03)
mat2.add_element("Cr", 1.738400e-02)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Fe", 5.875400e-02)

# Al-6061
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Si", 3.489000e-04)
mat3.add_element("Fe", 1.023500e-04)
mat3.add_element("Cu", 7.196300e-05)
mat3.add_element("Mn", 2.229600e-05)
mat3.add_element("Mg", 6.719600e-04)
mat3.add_element("Cr", 6.282000e-05)
mat3.add_element("Zn", 3.122000e-05)
mat3.add_element("Ti", 2.558300e-05)
mat3.add_element("Al", 5.889300e-02)

# Lexan
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 3.978600e-02)
mat4.add_element("C", 4.547000e-02)
mat4.add_nuclide("O16", 8.525700e-03)
mat4.add_s_alpha_beta("c_H_in_CH2")

# Water with Cd (Case 5)
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.669800e-02)
mat5.add_element("N", 7.008600e-06)
mat5.add_nuclide("O16", 3.337500e-02)
mat5.add_element("Cd", 2.299900e-06)
mat5.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Lexan  lattice plate
surf1 = openmc.ZCylinder(surface_id=1, r=30.0)
# SS304L lattice plate
surf2 = openmc.ZCylinder(surface_id=2, r=30.0)
# Al6061 lattice plate
surf3 = openmc.ZCylinder(surface_id=3, r=30.0)
# Water and boundary condition
surf4 = openmc.ZCylinder(surface_id=4, r=50.8)
# Al6061 tie rod
surf5 = openmc.ZCylinder(surface_id=5, x0=0.0, y0=28.0, r=1.27)
# Al6061 tie rod
surf6 = openmc.ZCylinder(surface_id=6, x0=-24.2487, y0=-14.0, r=1.27)
# Al6061 tie rod
surf7 = openmc.ZCylinder(surface_id=7, x0=24.2487, y0=-14.0, r=1.27)
# U(4.31)O2 fuel
surf11 = openmc.ZCylinder(surface_id=11, r=0.63245)
# Void
surf12 = openmc.ZCylinder(surface_id=12, r=0.6387)
# SS304L clad
surf13 = openmc.ZCylinder(surface_id=13, r=0.72)
# SS304L cap
surf14 = openmc.ZCylinder(surface_id=14, r=0.397)
# Prism 21: 6-sided polygon
surf21_0 = openmc.Plane(a=0.8660246601, b=0.5000012881, c=0, d=21.7770561026)
surf21_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=21.7770000000)
surf21_2 = openmc.Plane(a=-0.8660246601, b=0.5000012881, c=0, d=21.7770561026)
surf21_3 = openmc.Plane(a=-0.8660246601, b=-0.5000012881, c=0, d=21.7770561026)
surf21_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=21.7770000000)
surf21_5 = openmc.Plane(a=0.8660246601, b=-0.5000012881, c=0, d=21.7770561026)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=83.165)
surf1_zmax = openmc.ZPlane(z0=83.8)
surf2_zmin = openmc.ZPlane(z0=-2.225)
surf2_zmax = openmc.ZPlane(z0=-0.635)
surf3_zmin = openmc.ZPlane(z0=-2.86)
surf3_zmax = openmc.ZPlane(z0=-2.225)
surf4_zmin = openmc.ZPlane(z0=-33.34, boundary_type="vacuum")
surf4_zmax = openmc.ZPlane(z0=146.66, boundary_type="vacuum")
surf11_zmin = openmc.ZPlane(z0=0.0)
surf11_zmax = openmc.ZPlane(z0=82.72)
surf12_zmin = openmc.ZPlane(z0=0.0)
surf12_zmax = openmc.ZPlane(z0=85.831)
surf13_zmin = openmc.ZPlane(z0=-0.635)
surf13_zmax = openmc.ZPlane(z0=86.141)
surf14_zmin = openmc.ZPlane(z0=86.141)
surf14_zmax = openmc.ZPlane(z0=90.461)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat4)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & -surf5
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & -surf6
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & -surf7
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = (-surf11 & +surf11_zmin & -surf11_zmax)
u2_cell1 = openmc.Cell()
u2_cell1.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u2_cell2 = openmc.Cell(fill=mat2)
u2_cell2.region = (+surf11 | -surf11_zmin | +surf11_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3])

universe3 = openmc.Universe(universe_id=3, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Lttc
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5)

# Else
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.region = (-surf4 & +surf4_zmin & -surf4_zmax) & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5)

# Else
cell14 = openmc.Cell(cell_id=14, fill=universe1)
cell14.region = (+surf13 | -surf13_zmin | +surf13_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell14])
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
source.space = openmc.stats.Point((0.0, 0.0, 41.5825))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
