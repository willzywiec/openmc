"""
MIX-COMP-THERM-001-3: 205 MOX pins with 2 x 0.7671 cm = 1.5342 cm pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# MOX
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 7.385700e-06)
mat1.add_nuclide("Pu239", 4.201900e-03)
mat1.add_nuclide("Pu240", 5.606000e-04)
mat1.add_nuclide("Pu241", 8.752300e-05)
mat1.add_nuclide("Pu242", 1.697200e-05)
mat1.add_nuclide("Am241", 3.425800e-05)
mat1.add_nuclide("U235", 1.222300e-04)
mat1.add_nuclide("U238", 1.687600e-02)
mat1.add_nuclide("O16", 4.371300e-02)

# Natural UO2 insulator
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 1.340600e-06)
mat2.add_nuclide("U235", 1.716600e-04)
mat2.add_nuclide("U238", 2.306600e-02)
mat2.add_nuclide("O16", 4.647600e-02)

# Inconol 600 reflector
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Ni", 6.307000e-02)
mat3.add_element("Cr", 1.657800e-02)
mat3.add_element("Fe", 9.079500e-03)

# SS302 spring
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 1.301700e-04)
mat4.add_element("Mn", 1.735600e-03)
mat4.add_element("Si", 8.678100e-04)
mat4.add_element("Cr", 1.562100e-02)
mat4.add_element("Ni", 7.810300e-03)
mat4.add_element("P", 3.905200e-05)
mat4.add_element("S", 2.603400e-05)
mat4.add_element("Fe", 6.055200e-02)

# SS316 plenum
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 6.773800e-05)
mat5.add_element("Mn", 1.693500e-05)
mat5.add_element("Si", 8.467300e-04)
mat5.add_element("Cr", 1.439400e-02)
mat5.add_element("Ni", 1.016100e-02)
mat5.add_element("P", 3.810300e-05)
mat5.add_element("S", 2.540200e-05)
mat5.add_element("Mo", 2.116800e-03)
mat5.add_element("Fe", 5.533000e-02)

# Plexiglas base plate
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 5.678400e-02)
mat6.add_element("C", 3.548900e-02)
mat6.add_nuclide("O16", 1.419500e-02)
mat6.add_s_alpha_beta("c_H_in_CH2")

# SS304L grid plates
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Fe", 6.327800e-02)
mat7.add_element("Cr", 1.653200e-02)
mat7.add_element("Ni", 6.509500e-03)

# Polypropolyne grid plates
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_nuclide("H1", 7.770900e-02)
mat8.add_element("C", 3.885400e-02)
mat8.add_s_alpha_beta("c_H_in_CH2")

# Carbon steel tank
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_element("Fe", 8.405800e-02)
mat9.add_element("C", 3.947900e-03)

# Concrete
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_nuclide("H1", 1.727100e-02)
mat10.add_element("K", 4.343500e-04)
mat10.add_element("Ca", 2.613000e-03)
mat10.add_element("Al", 3.356800e-03)
mat10.add_element("Fe", 1.343100e-03)
mat10.add_nuclide("O16", 4.537700e-02)
mat10.add_element("Si", 1.290000e-02)
mat10.add_element("Na", 1.231200e-04)
mat10.add_element("Mg", 7.569500e-04)
mat10.add_s_alpha_beta("c_H_in_H2O")

# Al-6061
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_element("Al", 5.763800e-02)
mat11.add_element("Si", 4.614400e-04)
mat11.add_element("Fe", 2.030500e-04)
mat11.add_element("Mn", 4.423000e-05)
mat11.add_element("Mg", 7.998100e-04)
mat11.add_element("Cr", 1.090400e-04)
mat11.add_element("Cu", 1.019700e-04)

# Water
mat12 = openmc.Material(material_id=12)
mat12.set_density("sum")
mat12.add_nuclide("H1", 6.673300e-02)
mat12.add_nuclide("O16", 3.336800e-02)
mat12.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10, mat11, mat12])

# ==============================================================================
# Geometry
# ==============================================================================

# Inconel 600 reflector
surf1 = openmc.ZCylinder(surface_id=1, r=0.240665)
# Natural UO2 isolator
surf2 = openmc.ZCylinder(surface_id=2, r=0.2413)
# MOX fuel
surf3 = openmc.ZCylinder(surface_id=3, r=0.2407)
# Natural UO2 isolator
surf4 = openmc.ZCylinder(surface_id=4, r=0.2413)
# Inconel 600 reflector
surf5 = openmc.ZCylinder(surface_id=5, r=0.240665)
# SS302 spring
surf6 = openmc.ZCylinder(surface_id=6, r=0.254)
# SS316 plenum, inner
surf7 = openmc.ZCylinder(surface_id=7, r=0.23114)
# SS316 plenum, outer
surf8 = openmc.ZCylinder(surface_id=8, r=0.24511)
# SS316 clad, inner
surf9 = openmc.ZCylinder(surface_id=9, r=0.254)
# SS316 clad, outer (or hole)
surf10 = openmc.ZCylinder(surface_id=10, r=0.2921)
# Upper  SS304L plate
surf11 = openmc.model.RectangularParallelepiped(-13.8078, 13.8078, -13.8078, 13.8078, 182.89999999999998, 185.745)
# Minimum water level
surf12 = openmc.ZPlane(surface_id=12, z0=127.0)
# Middle SS304L plate
surf13 = openmc.model.RectangularParallelepiped(-13.8078, 13.8078, -13.8078, 13.8078, 121.76, 124.605)
# Polypropolyne spacer plate
surf14 = openmc.model.RectangularParallelepiped(-13.8078, 13.8078, -13.8078, 13.8078, 56.330000000000005, 57.698)
# Bottom SS304L plate
surf15 = openmc.model.RectangularParallelepiped(-13.8078, 13.8078, -13.8078, 13.8078, 9.850000000000001, 12.695)
# Plexiglas base plate
surf16 = openmc.model.RectangularParallelepiped(-13.8078, 13.8078, -13.8078, 13.8078, -2.54, 0.0)
# Al-6061 channel, outer
surf17 = openmc.model.RectangularParallelepiped(-13.8078, 13.8078, -13.8078, 13.8078, -17.84, -2.539999999999999)
# Al-6061 channel, inner
surf18 = openmc.model.RectangularParallelepiped(-8.7278, 8.7278, -499.95, 499.95, -499.95, 499.95)
# Al-6061 channel, lhs
surf19 = openmc.model.RectangularParallelepiped(-18.2528, -9.3628, -499.95, 499.95, -17.205, -3.175)
# Al-6061 channel, rhs
surf20 = openmc.model.RectangularParallelepiped(9.3628, 18.2528, -499.95, 499.95, -17.205, -3.175)
# Carbon steel tank floor
surf21 = openmc.ZPlane(surface_id=21, z0=-17.84)
# Top of concrete
surf22 = openmc.ZPlane(surface_id=22, z0=-18.792)
# BCD
surf23 = openmc.ZCylinder(surface_id=23, r=60.0, boundary_type="vacuum")
# Bottom of fuel
surf98 = openmc.ZPlane(surface_id=98, z0=0.0)
# Lattice external boundary
surf99 = openmc.model.RectangularParallelepiped(-13.8078, 13.8078, -13.8078, 13.8078, -499.95, 499.95)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1099, z0=4.06)
surf1_zmax = openmc.ZPlane(surface_id=1100, z0=18.538)
surf2_zmin = openmc.ZPlane(surface_id=1101, z0=18.538)
surf2_zmax = openmc.ZPlane(surface_id=1102, z0=20.57)
surf3_zmin = openmc.ZPlane(surface_id=1103, z0=20.57)
surf3_zmax = openmc.ZPlane(surface_id=1104, z0=112.01)
surf4_zmin = openmc.ZPlane(surface_id=1105, z0=112.01)
surf4_zmax = openmc.ZPlane(surface_id=1106, z0=114.042)
surf5_zmin = openmc.ZPlane(surface_id=1107, z0=114.042)
surf5_zmax = openmc.ZPlane(surface_id=1108, z0=128.52)
surf6_zmin = openmc.ZPlane(surface_id=1109, z0=128.52)
surf6_zmax = openmc.ZPlane(surface_id=1110, z0=141.07)
surf8_zmin = openmc.ZPlane(surface_id=1111, z0=141.07)
surf8_zmax = openmc.ZPlane(surface_id=1112, z0=227.284)
surf9_zmin = openmc.ZPlane(surface_id=1113, z0=4.06)
surf9_zmax = openmc.ZPlane(surface_id=1114, z0=227.284)
surf10_zmin = openmc.ZPlane(surface_id=1115, z0=0.0)
surf10_zmax = openmc.ZPlane(surface_id=1116, z0=237.744)
surf23_zmin = openmc.ZPlane(surface_id=1117, z0=-48.792, boundary_type="vacuum")
surf23_zmax = openmc.ZPlane(surface_id=1118, z0=237.744, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax) & (-surf9 & +surf9_zmin & -surf9_zmax)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell2 = openmc.Cell(fill=mat1)
u1_cell2.region = (+surf2 | -surf2_zmin | +surf2_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax)
u1_cell3 = openmc.Cell(fill=mat2)
u1_cell3.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell4 = openmc.Cell(fill=mat3)
u1_cell4.region = (+surf4 | -surf4_zmin | +surf4_zmax) & (-surf5 & +surf5_zmin & -surf5_zmax)
u1_cell5 = openmc.Cell(fill=mat4)
u1_cell5.region = (+surf5 | -surf5_zmin | +surf5_zmax) & (-surf6 & +surf6_zmin & -surf6_zmax) & (-surf9 & +surf9_zmin & -surf9_zmax)
u1_cell6 = openmc.Cell(fill=mat5)
u1_cell6.region = (+surf6 | -surf6_zmin | +surf6_zmax) & +surf7 & (-surf8 & +surf8_zmin & -surf8_zmax) & (-surf9 & +surf9_zmin & -surf9_zmax)
u1_cell7 = openmc.Cell(fill=mat5)
u1_cell7.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax) & (+surf9 | -surf9_zmin | +surf9_zmax) & (-surf10 & +surf10_zmin & -surf10_zmax)
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7])

u2_cell0 = openmc.Cell(fill=mat12)
u2_cell0.region = (-surf10 & +surf10_zmin & -surf10_zmax) & -surf12 & (-surf23 & +surf23_zmin & -surf23_zmax)
u2_cell1 = openmc.Cell(fill=mat7)
u2_cell1.region = (+surf10 | -surf10_zmin | +surf10_zmax) & -surf11
u2_cell2 = openmc.Cell(fill=mat7)
u2_cell2.region = (+surf10 | -surf10_zmin | +surf10_zmax) & -surf13
u2_cell3 = openmc.Cell(fill=mat8)
u2_cell3.region = (+surf10 | -surf10_zmin | +surf10_zmax) & -surf14
u2_cell4 = openmc.Cell(fill=mat7)
u2_cell4.region = (+surf10 | -surf10_zmin | +surf10_zmax) & -surf15
u2_cell5 = openmc.Cell(fill=mat6)
u2_cell5.region = (+surf10 | -surf10_zmin | +surf10_zmax) & -surf16
u2_cell6 = openmc.Cell(fill=mat11)
u2_cell6.region = +surf16 & -surf17 & +surf18 & +surf19 & +surf20 & +surf21
u2_cell7 = openmc.Cell(fill=mat12)
u2_cell7.region = +surf16 & -surf17 & -surf18 & +surf19 & +surf20 & +surf21
u2_cell8 = openmc.Cell(fill=mat12)
u2_cell8.region = +surf16 & -surf17 & +surf18 & -surf19 & +surf20 & +surf21
u2_cell9 = openmc.Cell(fill=mat12)
u2_cell9.region = +surf16 & -surf17 & +surf18 & +surf19 & -surf20 & +surf21
u2_cell10 = openmc.Cell(fill=mat9)
u2_cell10.region = -surf21 & +surf22 & (-surf23 & +surf23_zmin & -surf23_zmax)
u2_cell11 = openmc.Cell(fill=mat10)
u2_cell11.region = -surf22 & (-surf23 & +surf23_zmin & -surf23_zmax)
u2_cell12 = openmc.Cell(fill=mat12)
u2_cell12.region = (+surf10 | -surf10_zmin | +surf10_zmax) & +surf11 & -surf12 & +surf13 & +surf14
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8, u2_cell9, u2_cell10, u2_cell11, u2_cell12])

universe3 = openmc.Universe(universe_id=3, cells=[])

# Lattice 4: 36x36 array
lattice4 = openmc.RectLattice(lattice_id=4)
lattice4.lower_left = [-13.8078, -13.8078]
lattice4.pitch = [0.767100, 0.767100]
lattice4.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2, universe3, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe4 = openmc.Universe(universe_id=4)
universe4.add_cell(openmc.Cell(fill=lattice4))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# lttc
cell1 = openmc.Cell(cell_id=1, fill=universe4)
cell1.region = (-surf23 & +surf23_zmin & -surf23_zmax) & +surf98 & -surf99

# stuff
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.region = (-surf23 & +surf23_zmin & -surf23_zmax) & +surf98 & +surf99

# stuff
cell3 = openmc.Cell(cell_id=3, fill=universe2)
cell3.region = (-surf23 & +surf23_zmin & -surf23_zmax) & -surf98

# SS316
cell12 = openmc.Cell(cell_id=12, fill=mat5)
cell12.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (+surf6 | -surf6_zmin | +surf6_zmax) & (+surf8 | -surf8_zmin | +surf8_zmax) & (+surf9 | -surf9_zmin | +surf9_zmax) & (-surf10 & +surf10_zmin & -surf10_zmax)

# Stuff
cell26 = openmc.Cell(cell_id=26, fill=universe2)
cell26.region = (+surf10 | -surf10_zmin | +surf10_zmax) & (-surf23 & +surf23_zmin & -surf23_zmax)

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell12, cell26])
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
source.space = openmc.stats.Box((-2.2, 0.8999999999999999, 72.785), (4.8, 2.9, 74.785))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
