"""
LCT022-7: 504 U(10)O2 rods with 1.852026 cm hexagonal pitch
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
surf1 = openmc.ZCylinder(surface_id=1, x0=-0.8, y0=0.0, r=0.1)
# Clad - lower
surf2 = openmc.ZCylinder(surface_id=2, x0=-1.1, y0=-0.1, r=0.2)
# Clad - lower
surf3 = openmc.ZCylinder(surface_id=3, x0=-0.1, y0=0.0, r=0.255)
# Fuel
surf4 = openmc.ZCylinder(surface_id=4, x0=0.0, y0=85.6, r=0.208)
# Void
surf5 = openmc.ZCylinder(surface_id=5, x0=0.0, y0=85.9, r=0.215)
# Void
surf6 = openmc.ZCylinder(surface_id=6, x0=85.9, y0=86.7, r=0.1)
# Clad - middle
surf7 = openmc.ZCylinder(surface_id=7, x0=0.0, y0=87.3, r=0.255)
# Clad - top
surf8 = openmc.ZCylinder(surface_id=8, x0=87.3, y0=92.5, r=0.187)
# Support plate
surf10 = openmc.ZCylinder(surface_id=10, x0=-2.3, y0=-1.1, r=99.9)
# Lattice plate hole - 1
surf11 = openmc.ZCylinder(surface_id=11, r=0.26)
# Lattice plate hole - 2
surf12_cyl = openmc.ZCylinder(surface_id=12, x0=tr, y0=-0.926013, r=0.26)
surf12_zmin = openmc.ZPlane(z0=1.6039)
surf12_zmax = openmc.ZPlane(z0=0.0)
surf12 = (surf12_cyl, surf12_zmin, surf12_zmax)
# Lattice plate hole - 3
surf13_cyl = openmc.ZCylinder(surface_id=13, x0=tr, y0=-0.926013, r=0.26)
surf13_zmin = openmc.ZPlane(z0=-1.6039)
surf13_zmax = openmc.ZPlane(z0=0.0)
surf13 = (surf13_cyl, surf13_zmin, surf13_zmax)
# Lattice plate hole - 4
surf14_cyl = openmc.ZCylinder(surface_id=14, x0=tr, y0=0.926013, r=0.26)
surf14_zmin = openmc.ZPlane(z0=1.6039)
surf14_zmax = openmc.ZPlane(z0=0.0)
surf14 = (surf14_cyl, surf14_zmin, surf14_zmax)
# Lattice plate hole - 5
surf15_cyl = openmc.ZCylinder(surface_id=15, x0=tr, y0=0.926013, r=0.26)
surf15_zmin = openmc.ZPlane(z0=-1.6039)
surf15_zmax = openmc.ZPlane(z0=0.0)
surf15 = (surf15_cyl, surf15_zmin, surf15_zmax)
# Lattice plate - lower
surf16 = openmc.ZCylinder(surface_id=16, x0=0.4, y0=0.7, r=99.9)
# Lattice plate - upper
surf17 = openmc.ZCylinder(surface_id=17, x0=81.8, y0=82.1, r=99.9)
# Prism 81: 3-sided polygon
surf81_0 = openmc.Plane(a=0.8660254016, b=0.5000000037, c=0, d=15.2370651133)
surf81_1 = openmc.Plane(a=-0.8666622720, b=0.4988952858, c=0, d=15.2033997964)
surf81_2 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=15.2370650000)
# Prism 82: 3-sided polygon
surf82_0 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=15.2370650000)
surf82_1 = openmc.Plane(a=-0.8660254016, b=-0.5000000037, c=0, d=15.2370651133)
surf82_2 = openmc.Plane(a=0.8660254016, b=-0.5000000037, c=0, d=15.2370651133)
surf83 = openmc.YPlane(surface_id=83, y0=0)
surf84 = openmc.Plane(surface_id=84, a=21.2983, b=0, c=1, d=21.2983)
surf85 = openmc.Plane(surface_id=85, a=21.2983, b=0, c=1, d=21.2983)
# Prism 91: 6-sided polygon
surf91_0 = openmc.Plane(a=0.8660254179, b=0.4999999755, c=0, d=20.0487698834)
surf91_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=20.0487700000)
surf91_2 = openmc.Plane(a=-0.8660254179, b=0.4999999755, c=0, d=20.0487698834)
surf91_3 = openmc.Plane(a=-0.8660254179, b=-0.4999999755, c=0, d=20.0487698834)
surf91_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=20.0487700000)
surf91_5 = openmc.Plane(a=0.8660254179, b=-0.4999999755, c=0, d=20.0487698834)
# Prism 92: 6-sided polygon
surf92_0 = openmc.Plane(a=0.8660254012, b=0.5000000044, c=0, d=21.6526701907)
surf92_1 = openmc.Plane(a=0.0000000000, b=1.0000000000, c=0, d=21.6526700000)
surf92_2 = openmc.Plane(a=-0.8660254012, b=0.5000000044, c=0, d=21.6526701907)
surf92_3 = openmc.Plane(a=-0.8660254012, b=-0.5000000044, c=0, d=21.6526701907)
surf92_4 = openmc.Plane(a=0.0000000000, b=-1.0000000000, c=0, d=21.6526700000)
surf92_5 = openmc.Plane(a=0.8660254012, b=-0.5000000044, c=0, d=21.6526701907)
surf93 = openmc.XPlane(surface_id=93, x0=-5.5561)
surf94 = openmc.XPlane(surface_id=94, x0=5.5561)
surf95 = openmc.YPlane(surface_id=95, y0=-15.2371)
surf96 = openmc.YPlane(surface_id=96, y0=-5.6137)
surf97 = openmc.YPlane(surface_id=97, y0=5.6137)
surf98 = openmc.YPlane(surface_id=98, y0=15.2371)
# Boundary condition
surf99 = openmc.ZCylinder(surface_id=99, x0=-20.0, y0=105.6, r=53.2, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell()
u1_cell0.region = -surf1 & -surf2
u1_cell1 = openmc.Cell()
u1_cell1.region = -surf1 & -surf3
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf1 & -surf2
u1_cell3 = openmc.Cell(fill=mat2)
u1_cell3.region = +surf1 & +surf2 & -surf3
u1_cell4 = openmc.Cell(fill=mat1)
u1_cell4.region = +surf1 & +surf2 & +surf3 & -surf4
u1_cell5 = openmc.Cell()
u1_cell5.region = +surf1 & +surf2 & +surf3 & +surf4 & -surf5
u1_cell6 = openmc.Cell()
u1_cell6.region = +surf5 & -surf6
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = +surf1 & +surf2 & +surf3 & +surf4 & +surf5 & +surf6 & -surf7
u1_cell8 = openmc.Cell(fill=mat2)
u1_cell8.region = +surf7 & -surf8
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = -surf10 & +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & -surf99
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & -surf16 & -surf99
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf11 & +surf12 & +surf13 & +surf14 & +surf15 & -surf17 & -surf99
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

# Lattice 3: 29x15 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-26.854377, -24.0585]
lattice3.pitch = [1.852026, 3.207800]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = +surf83 & -surf84 & (-surf91_0 & -surf91_1 & -surf91_2 & -surf91_3 & -surf91_4 & -surf91_5) & -surf99

# core
cell2 = openmc.Cell(cell_id=2, fill=universe3)
cell2.region = -surf83 & -surf85 & (-surf91_0 & -surf91_1 & -surf91_2 & -surf91_3 & -surf91_4 & -surf91_5) & -surf99

# core
cell3 = openmc.Cell(cell_id=3, fill=universe3)
cell3.region = (-surf81_0 & -surf81_1 & -surf81_2) & (+surf91_0 | +surf91_1 | +surf91_2 | +surf91_3 | +surf91_4 | +surf91_5) & (-surf92_0 & -surf92_1 & -surf92_2 & -surf92_3 & -surf92_4 & -surf92_5) & -surf99

# core
cell4 = openmc.Cell(cell_id=4, fill=universe3)
cell4.region = (-surf82_0 & -surf82_1 & -surf82_2) & (+surf91_0 | +surf91_1 | +surf91_2 | +surf91_3 | +surf91_4 | +surf91_5) & (-surf92_0 & -surf92_1 & -surf92_2 & -surf92_3 & -surf92_4 & -surf92_5) & -surf99

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4])
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
