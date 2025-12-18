"""
LCT011-4: B&W CX-10 Core IIIB
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(2.459)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.868700e-06)
mat1.add_nuclide("U235", 5.675700e-04)
mat1.add_nuclide("U236", 2.193000e-06)
mat1.add_nuclide("U238", 2.222200e-02)
mat1.add_nuclide("O16", 4.559600e-02)

# Al-6061-T6
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Si", 3.473600e-04)
mat2.add_element("Mn", 2.959600e-05)
mat2.add_element("Zn", 3.729900e-05)
mat2.add_element("Fe", 1.019000e-04)
mat2.add_element("Mg", 6.689800e-04)
mat2.add_element("Ti", 3.395900e-05)
mat2.add_element("Cu", 5.117400e-05)
mat2.add_element("Cr", 6.254200e-05)
mat2.add_element("Al", 5.806500e-02)

# Water with 764 ppm B, Core IIIB
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.671000e-02)
mat3.add_nuclide("O16", 3.341900e-02)
mat3.add_nuclide("B10", 8.479600e-06)
mat3.add_nuclide("B11", 3.413200e-05)
mat3.add_s_alpha_beta("c_H_in_H2O")

# "Air"
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.666700e-06)
mat4.add_nuclide("O16", 3.333300e-06)
mat4.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Water height above base plate
surf1 = openmc.ZPlane(surface_id=1, z0=144.88)
# Tank inner
surf2 = openmc.ZCylinder(surface_id=2, x0=-7.62, y0=180.04, r=76.2)
# Tank outer
surf3 = openmc.ZCylinder(surface_id=3, x0=-8.89, y0=180.04, r=77.47, boundary_type="vacuum")
# U(2.459)O2
surf10 = openmc.ZCylinder(surface_id=10, x0=0.30, y0=153.66, r=0.515)
# Gap
surf11 = openmc.ZCylinder(surface_id=11, x0=0.30, y0=156.16, r=0.522)
# Al-6061-T6 clad
surf12 = openmc.ZCylinder(surface_id=12, x0=0.30, y0=156.478, r=0.603)
# Grid inner
surf13 = openmc.model.RectangularParallelepiped(-0.615, 0.615, -0.615, 0.615, -499.9995, 499.9995)
# Base plate bottom
surf14 = openmc.ZPlane(surface_id=14, z0=-5.08)
# Base plate top
surf15 = openmc.ZPlane(surface_id=15, z0=0.00)
# Lower grid bottom
surf16 = openmc.ZPlane(surface_id=16, z0=0.30)
# Lower grid top
surf17 = openmc.ZPlane(surface_id=17, z0=2.84)
# Upper grid bottom
surf18 = openmc.ZPlane(surface_id=18, z0=150.00)
# Upper grid bottom
surf19 = openmc.ZPlane(surface_id=19, z0=152.54)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf10 & -surf11 & -surf12 & +surf16
u1_cell1 = openmc.Cell()
u1_cell1.region = +surf10 & -surf11 & -surf12 & +surf16
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf10 & +surf11 & -surf12 & +surf16
u1_cell3 = openmc.Cell(fill=mat3)
u1_cell3.region = -surf2 & +surf10 & +surf11 & +surf12 & +surf15 & -surf16
u1_cell4 = openmc.Cell(fill=mat2)
u1_cell4.region = -surf2 & +surf14 & -surf15
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = -surf2 & -surf14
u1_cell6 = openmc.Cell(fill=mat2)
u1_cell6.region = -surf2 & +surf13 & +surf16 & -surf17
u1_cell7 = openmc.Cell(fill=mat2)
u1_cell7.region = -surf2 & +surf13 & +surf18 & -surf19
u1_cell8 = openmc.Cell(fill=mat3)
u1_cell8.region = -surf1 & -surf2 & +surf12 & -surf13 & +surf16 & -surf17
u1_cell9 = openmc.Cell(fill=mat3)
u1_cell9.region = -surf1 & -surf2 & +surf12 & +surf17
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9])

u2_cell0 = openmc.Cell(fill=mat2)
u2_cell0.region = -surf2 & +surf13 & +surf18 & -surf19
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = -surf1 & -surf2 & +surf17
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = -surf1 & -surf2 & -surf13 & +surf16 & -surf17
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = -surf2 & +surf13 & +surf16 & -surf17
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = -surf2 & +surf15 & -surf16
u2_cell5 = openmc.Cell(fill=mat2)
u2_cell5.region = -surf2 & +surf14 & -surf15
u2_cell6 = openmc.Cell(fill=mat3)
u2_cell6.region = -surf2 & -surf14
u2_cell7 = openmc.Cell(fill=mat3)
u2_cell7.region = -surf1 & -surf2 & +surf12 & +surf17
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7])

# Lattice 3: 44x44 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-35.992, -35.992]
lattice3.pitch = [1.636000, 1.636000]
lattice3.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CORE
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf2 & -surf3

# Water
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = -surf1 & -surf2 & -surf3

# Water
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = -surf1 & -surf2 & -surf3

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = -surf1 & -surf2 & -surf3

# Water
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = -surf1 & -surf2 & -surf3

# Air
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf1 & -surf2 & -surf3

# Air
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf1 & -surf2 & -surf3

# Air
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = +surf1 & -surf2 & -surf3

# Air
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = +surf1 & -surf2 & -surf3

# Tank
cell10 = openmc.Cell(cell_id=10, fill=mat2)
cell10.region = +surf2 & -surf3

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10])
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
source.space = openmc.stats.Box((-1.818, -1.818, 71.44), (1.818, 1.818, 73.44))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
