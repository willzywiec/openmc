"""
LCT022-4: 462 U(10)O2 rods with 1.22 cm hexagonal pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(10)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 1.763600e-05)
mat1.add_nuclide("U235", 2.157700e-03)
mat1.add_nuclide("U236", 1.530000e-05)
mat1.add_nuclide("U238", 1.951000e-02)
mat1.add_nuclide("O16", 4.466100e-02)

# SST
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.889400e-02)
mat2.add_element("Cr", 1.646900e-02)
mat2.add_element("Ni", 8.106100e-03)
mat2.add_element("Si", 1.355100e-03)
mat2.add_element("Mn", 1.299000e-03)
mat2.add_element("C", 2.376600e-04)
mat2.add_element("Ti", 4.471300e-04)

# Al-alloy
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 1.498900e-04)
mat3.add_element("Si", 2.980400e-04)
mat3.add_element("Cu", 1.146000e-03)
mat3.add_element("Al", 5.711500e-02)
mat3.add_element("Mg", 1.033200e-03)
mat3.add_element("Mn", 1.828400e-04)
mat3.add_element("Ti", 3.496500e-05)
mat3.add_element("Zn", 7.680700e-05)
mat3.add_element("Ni", 2.852500e-05)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.673600e-02)
mat4.add_nuclide("O16", 3.336800e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Void
surf1 = openmc.ZCylinder(surface_id=1, r=0.1)
# Clad - lower
surf2 = openmc.ZCylinder(surface_id=2, r=0.2)
# Clad - lower
surf3 = openmc.ZCylinder(surface_id=3, r=0.255)
# Fuel
surf4 = openmc.ZCylinder(surface_id=4, r=0.208)
# Void
surf5 = openmc.ZCylinder(surface_id=5, r=0.215)
# Void
surf6 = openmc.ZCylinder(surface_id=6, r=0.1)
# Clad - middle
surf7 = openmc.ZCylinder(surface_id=7, r=0.255)
# Clad - top
surf8 = openmc.ZCylinder(surface_id=8, r=0.187)
# Support plate
surf10 = openmc.ZCylinder(surface_id=10, r=99.9)
# Lattice plate hole - 1
surf11 = openmc.ZCylinder(surface_id=11, r=0.26)
# Lattice plate hole - 2
surf12 = openmc.ZCylinder(surface_id=12, x0=-0.61, y0=1.056551, r=0.26)
# Lattice plate hole - 3
surf13 = openmc.ZCylinder(surface_id=13, x0=-0.61, y0=-1.056551, r=0.26)
# Lattice plate hole - 4
surf14 = openmc.ZCylinder(surface_id=14, x0=0.61, y0=1.056551, r=0.26)
# Lattice plate hole - 5
surf15 = openmc.ZCylinder(surface_id=15, x0=0.61, y0=-1.056551, r=0.26)
# Lattice plate - lower
surf16 = openmc.ZCylinder(surface_id=16, r=99.9)
# Lattice plate - upper
surf17 = openmc.ZCylinder(surface_id=17, r=99.9)
surf21 = openmc.ZCylinder(surface_id=21, x0=-3.05, y0=13.735163, r=0.26)
surf22 = openmc.ZCylinder(surface_id=22, x0=-1.83, y0=13.735163, r=0.26)
surf23 = openmc.ZCylinder(surface_id=23, x0=1.83, y0=13.735163, r=0.26)
surf24 = openmc.ZCylinder(surface_id=24, x0=3.05, y0=13.735163, r=0.26)
surf25 = openmc.ZCylinder(surface_id=25, x0=-10.37, y0=9.508959, r=0.26)
surf26 = openmc.ZCylinder(surface_id=26, x0=10.37, y0=9.508959, r=0.26)
surf27 = openmc.ZCylinder(surface_id=27, x0=-10.98, y0=8.452408, r=0.26)
surf28 = openmc.ZCylinder(surface_id=28, x0=10.98, y0=8.452408, r=0.26)
surf29 = openmc.ZCylinder(surface_id=29, x0=-11.59, y0=7.395857, r=0.26)
surf30 = openmc.ZCylinder(surface_id=30, x0=-12.81, y0=5.282755, r=0.26)
surf31 = openmc.ZCylinder(surface_id=31, x0=12.81, y0=5.282755, r=0.26)
surf32 = openmc.ZCylinder(surface_id=32, x0=-13.42, y0=4.226204, r=0.26)
surf33 = openmc.ZCylinder(surface_id=33, x0=13.42, y0=4.226204, r=0.26)
surf34 = openmc.ZCylinder(surface_id=34, x0=-3.05, y0=-13.735163, r=0.26)
surf35 = openmc.ZCylinder(surface_id=35, x0=-1.83, y0=-13.735163, r=0.26)
surf36 = openmc.ZCylinder(surface_id=36, x0=1.83, y0=-13.735163, r=0.26)
surf37 = openmc.ZCylinder(surface_id=37, x0=3.05, y0=-13.735163, r=0.26)
surf38 = openmc.ZCylinder(surface_id=38, x0=-10.37, y0=-9.508959, r=0.26)
surf39 = openmc.ZCylinder(surface_id=39, x0=10.37, y0=-9.508959, r=0.26)
surf40 = openmc.ZCylinder(surface_id=40, x0=-10.98, y0=-8.452408, r=0.26)
surf41 = openmc.ZCylinder(surface_id=41, x0=10.98, y0=-8.452408, r=0.26)
surf42 = openmc.ZCylinder(surface_id=42, x0=-12.81, y0=-5.282755, r=0.26)
surf43 = openmc.ZCylinder(surface_id=43, x0=12.81, y0=-5.282755, r=0.26)
surf44 = openmc.ZCylinder(surface_id=44, x0=-13.42, y0=-4.226204, r=0.26)
surf45 = openmc.ZCylinder(surface_id=45, x0=13.42, y0=-4.226204, r=0.26)
# Prism 81: 12-sided polygon
surf81_0 = openmc.Plane(a=0.4999999632, b=-0.8660254250, c=0, d=13.7249998554)
surf81_1 = openmc.Plane(a=0.8660253825, b=-0.5000000368, c=0, d=14.2634385502)
surf81_2 = openmc.Plane(a=1.0000000000, b=0.0000000000, c=0, d=13.7250000000)
surf81_3 = openmc.Plane(a=0.8660253825, b=0.5000000368, c=0, d=14.2634385502)
surf81_4 = openmc.Plane(a=0.4999999632, b=0.8660254250, c=0, d=13.7249998554)
surf81_5 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=14.2634380000)
surf81_6 = openmc.Plane(a=-0.4999999632, b=0.8660254250, c=0, d=13.7249998554)
surf81_7 = openmc.Plane(a=-0.8660253825, b=0.5000000368, c=0, d=14.2634385502)
surf81_8 = openmc.Plane(a=-1.0000000000, b=0.0000000000, c=0, d=13.7250000000)
surf81_9 = openmc.Plane(a=-0.8660253825, b=-0.5000000368, c=0, d=14.2634385502)
surf81_10 = openmc.Plane(a=-0.4999999632, b=-0.8660254250, c=0, d=13.7249998554)
surf81_11 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=14.2634380000)
# Boundary condition
surf99 = openmc.ZCylinder(surface_id=99, r=44.65)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(z0=-0.8)
surf1_zmax = openmc.ZPlane(z0=0.0)
surf2_zmin = openmc.ZPlane(z0=-1.1)
surf2_zmax = openmc.ZPlane(z0=-0.1)
surf3_zmin = openmc.ZPlane(z0=-0.1)
surf3_zmax = openmc.ZPlane(z0=0.0)
surf4_zmin = openmc.ZPlane(z0=0.0)
surf4_zmax = openmc.ZPlane(z0=85.6)
surf5_zmin = openmc.ZPlane(z0=0.0)
surf5_zmax = openmc.ZPlane(z0=85.9)
surf6_zmin = openmc.ZPlane(z0=85.9)
surf6_zmax = openmc.ZPlane(z0=86.7)
surf7_zmin = openmc.ZPlane(z0=0.0)
surf7_zmax = openmc.ZPlane(z0=87.3)
surf8_zmin = openmc.ZPlane(z0=87.3)
surf8_zmax = openmc.ZPlane(z0=92.5)
surf10_zmin = openmc.ZPlane(z0=-2.3)
surf10_zmax = openmc.ZPlane(z0=-1.1)
surf16_zmin = openmc.ZPlane(z0=0.4)
surf16_zmax = openmc.ZPlane(z0=0.7)
surf17_zmin = openmc.ZPlane(z0=81.8)
surf17_zmax = openmc.ZPlane(z0=82.1)
surf99_zmin = openmc.ZPlane(z0=-20.0, boundary_type="vacuum")
surf99_zmax = openmc.ZPlane(z0=105.6, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell()
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell1 = openmc.Cell()
u1_cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell3 = openmc.Cell(fill=mat2)
u1_cell3.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell4 = openmc.Cell(fill=mat1)
u1_cell4.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell5 = openmc.Cell()
u1_cell5.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)
u1_cell6 = openmc.Cell()
u1_cell6.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax)
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf2 | -surf2_zmin | +surf2_zmax) & (+surf3 | -surf3_zmin | +surf3_zmax) & (+surf4 | -surf4_zmin | +surf4_zmax) & (+surf5 | -surf5_zmin | +surf5_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (-surf7 & +surf7_zmin & -surf7_zmax)
u1_cell8 = openmc.Cell(fill=mat2)
u1_cell8.region = (+surf7 | -surf7_zmin | +surf7_zmax) & (-surf8 & +surf8_zmin & -surf8_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = (-surf10 & +surf10_zmin & -surf10_zmax) & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & (-surf99 & +surf99_zmin & -surf99_zmax)
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & (-surf16 & +surf16_zmin & -surf16_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & (-surf17 & +surf17_zmin & -surf17_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

# Lattice 3: 23x15 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-14.03, -15.848265]
lattice3.pitch = [1.220000, 2.113102]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = (-surf81_0 & -surf81_1 & -surf81_2 & -surf81_3 & -surf81_4 & -surf81_5 & -surf81_6 & -surf81_7 & -surf81_8 & -surf81_9 & -surf81_10 & -surf81_11) & (-surf99 & +surf99_zmin & -surf99_zmax) & +surf21 & +surf22 & +surf23 & +surf24 & +surf25 & +surf26 & +surf27 & +surf28 & +surf29 & +surf30 & +surf31 & +surf32 & +surf33 & +surf34 & +surf35 & +surf36 & +surf37 & +surf38 & +surf39 & +surf40 & +surf41 & +surf42 & +surf43 & +surf44 & +surf45

root_universe = openmc.Universe(cells=[cell1])
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
source.space = openmc.stats.Point((0.0, 0.0, 42.8))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
