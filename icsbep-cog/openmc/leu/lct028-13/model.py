"""
LCT028-13: 232 U(4.31)O2 rods with 2.794 cm triangular pitch in water with 0.0547 gGd/l
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

# Water with Gd (Case 13)
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.672800e-02)
mat5.add_element("N", 1.893100e-06)
mat5.add_nuclide("O16", 3.336900e-02)
mat5.add_element("Gd", 2.094800e-07)
mat5.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================

# Lexan  lattice plate
surf1 = openmc.ZCylinder(surface_id=1, x0=83.165, y0=83.800, r=34.0)
# SS304L lattice plate
surf2 = openmc.ZCylinder(surface_id=2, x0=-2.225, y0=-0.635, r=34.0)
# Al6061 lattice plate
surf3 = openmc.ZCylinder(surface_id=3, x0=-2.860, y0=-2.225, r=34.0)
# Water and boundary condition
surf4 = openmc.ZCylinder(surface_id=4, x0=-33.34, y0=146.66, r=50.8, boundary_type="vacuum")
# Al6061 tie rod
# surf5: Error converting surface type "c": could not convert string to float: 'tr'
# Al6061 tie rod
# surf6: Error converting surface type "c": could not convert string to float: 'tr'
# Al6061 tie rod
# surf7: Error converting surface type "c": could not convert string to float: 'tr'
# U(4.31)O2 fuel
surf11 = openmc.ZCylinder(surface_id=11, x0=0.0, y0=82.72, r=0.63245)
# Void
surf12 = openmc.ZCylinder(surface_id=12, x0=0.0, y0=85.831, r=0.6387)
# SS304L clad
surf13 = openmc.ZCylinder(surface_id=13, x0=-0.635, y0=86.141, r=0.72)
# SS304L cap
surf14 = openmc.ZCylinder(surface_id=14, x0=86.141, y0=90.461, r=0.397)
# Prism 21: 6-sided polygon
surf21_0 = openmc.Plane(a=0.8660276426, b=0.4999961222, c=0, d=24.1968123356)
surf21_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=24.1970000000)
surf21_2 = openmc.Plane(a=-0.8660276426, b=0.4999961222, c=0, d=24.1968123356)
surf21_3 = openmc.Plane(a=-0.8660276426, b=-0.4999961222, c=0, d=24.1968123356)
surf21_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=24.1970000000)
surf21_5 = openmc.Plane(a=0.8660276426, b=-0.4999961222, c=0, d=24.1968123356)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat4)
u1_cell0.region = -surf1
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = -surf2
u1_cell2 = openmc.Cell(fill=mat3)
u1_cell2.region = +surf2 & -surf3
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = +surf1 & +surf2 & +surf3 & -surf5
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = +surf1 & +surf2 & +surf3 & -surf6
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = +surf1 & +surf2 & +surf3 & -surf7
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = +surf1 & +surf2 & +surf3 & -surf4
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf11
u2_cell1 = openmc.Cell()
u2_cell1.region = +surf11 & -surf12
u2_cell2 = openmc.Cell(fill=mat2)
u2_cell2.region = +surf11 & +surf12 & -surf13
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = +surf13 & -surf14
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3])

universe3 = openmc.Universe(universe_id=3, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Lttc
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf4 & (-surf21_0 & -surf21_1 & -surf21_2 & -surf21_3 & -surf21_4 & -surf21_5)

# Else
cell2 = openmc.Cell(cell_id=2, fill=universe1)
cell2.region = -surf4 & (+surf21_0 | +surf21_1 | +surf21_2 | +surf21_3 | +surf21_4 | +surf21_5)

# Else
cell14 = openmc.Cell(cell_id=14, fill=universe1)
cell14.region = +surf13 & +surf14 & -surf4

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
