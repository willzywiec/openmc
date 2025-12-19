"""
LCT024-2: Uniform staggered 57x23 + 43 lattice of 1,297 fuel rods with 0.8768 cm pitch.  Modelled as a 114x23 array with 0.62 cm pitch.
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
# Lattice plate - hole
surf11 = openmc.ZCylinder(surface_id=11, r=0.26)
# Lattice plate - lower
surf12 = openmc.ZCylinder(surface_id=12, r=99.9)
# Lattice plate - upper
surf13 = openmc.ZCylinder(surface_id=13, r=99.9)
# Boundary condition
surf99 = openmc.ZCylinder(surface_id=99, r=60.0)

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
surf12_zmin = openmc.ZPlane(z0=0.4)
surf12_zmax = openmc.ZPlane(z0=0.7)
surf13_zmin = openmc.ZPlane(z0=81.8)
surf13_zmax = openmc.ZPlane(z0=82.1)
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
u1_cell9 = openmc.Cell(fill=mat3)
u1_cell9.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)
u1_cell10 = openmc.Cell(fill=mat3)
u1_cell10.region = +surf11 & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)
u1_cell11 = openmc.Cell(fill=mat3)
u1_cell11.region = +surf11 & (-surf13 & +surf13_zmin & -surf13_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = +surf11 & (-surf12 & +surf12_zmin & -surf12_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf11 & (-surf13 & +surf13_zmin & -surf13_zmax) & (-surf99 & +surf99_zmin & -surf99_zmax)
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

# Lattice 3: 114x23 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-35.34, -7.13]
lattice3.pitch = [0.620000, 0.620000]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
    [universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
    [universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
    [universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
    [universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
    [universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
    [universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
    [universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
    [universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
    [universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
    [universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
    [universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1],
    [universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2, universe1, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = (-surf99 & +surf99_zmin & -surf99_zmax)

# h2o
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = (-surf99 & +surf99_zmin & -surf99_zmax)

# h2o
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = (-surf99 & +surf99_zmin & -surf99_zmax)

# h2o
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = (-surf99 & +surf99_zmin & -surf99_zmax)

# h2o
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = (-surf99 & +surf99_zmin & -surf99_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5])
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
