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
# Lattice plate - hole
surf11 = openmc.ZCylinder(surface_id=11, r=0.26)
# Lattice plate - lower
surf12 = openmc.ZCylinder(surface_id=12, x0=0.4, y0=0.7, r=99.9)
# Lattice plate - upper
surf13 = openmc.ZCylinder(surface_id=13, x0=81.8, y0=82.1, r=99.9)
# Boundary condition
surf99 = openmc.ZCylinder(surface_id=99, x0=-20.0, y0=105.6, r=60.0, boundary_type="vacuum")

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
u1_cell9 = openmc.Cell(fill=mat3)
u1_cell9.region = +surf2 & -surf10 & -surf99
u1_cell10 = openmc.Cell(fill=mat3)
u1_cell10.region = +surf11 & -surf12 & -surf99
u1_cell11 = openmc.Cell(fill=mat3)
u1_cell11.region = +surf11 & -surf13 & -surf99
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = -surf10 & -surf99
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = +surf11 & -surf12 & -surf99
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf11 & -surf13 & -surf99
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
cell1.region = -surf99

# h2o
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = -surf99

# h2o
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = -surf99

# h2o
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = -surf99

# h2o
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = -surf99

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
