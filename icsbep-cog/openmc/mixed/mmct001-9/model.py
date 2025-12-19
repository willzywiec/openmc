"""
MMCT001-9: Experiment 115 with 996 FFTF rods immersed in 102.68 gPu/l, 359.55 gU/l and 1.97 gGd/l solution
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Fuel
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.222300e-04)
mat1.add_nuclide("U238", 1.687600e-02)
mat1.add_nuclide("Pu238", 2.760300e-06)
mat1.add_nuclide("Pu239", 4.240700e-03)
mat1.add_nuclide("Pu240", 5.708800e-04)
mat1.add_nuclide("Pu242", 9.317600e-06)
mat1.add_nuclide("Pu241", 4.109600e-05)
mat1.add_nuclide("Am241", 4.696900e-05)
mat1.add_nuclide("O16", 4.371300e-02)

# Nat-UO2
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U238", 2.306800e-02)
mat2.add_nuclide("U235", 1.694400e-04)
mat2.add_nuclide("U234", 1.299900e-06)
mat2.add_nuclide("O16", 4.647700e-02)

# Inconel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 3.397400e-04)
mat3.add_element("Mn", 4.642300e-04)
mat3.add_element("Cu", 4.013400e-04)
mat3.add_element("Si", 3.632300e-04)
mat3.add_element("Cr", 1.520500e-02)
mat3.add_element("Fe", 7.306700e-03)
mat3.add_element("Ni", 6.537300e-02)

# SS-302 (homogenized)
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("C", 1.725500e-04)
mat4.add_element("N", 4.783000e-03)
mat4.add_element("Cr", 9.864200e-05)
mat4.add_element("Ni", 2.118700e-03)
mat4.add_element("Fe", 1.799800e-02)

# SS-316
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 3.108600e-04)
mat5.add_element("Cr", 2.244000e-02)
mat5.add_element("Ni", 1.630200e-02)
mat5.add_element("Fe", 4.547900e-02)

# SS-304L
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("C", 9.530300e-04)
mat6.add_element("Cu", 2.176600e-04)
mat6.add_element("Co", 1.537700e-04)
mat6.add_element("N", 2.043100e-04)
mat6.add_element("Mn", 1.337000e-03)
mat6.add_element("P", 4.157600e-05)
mat6.add_element("S", 7.436100e-06)
mat6.add_element("Si", 7.981600e-04)
mat6.add_element("Cr", 1.681400e-02)
mat6.add_element("Ni", 7.582100e-03)
mat6.add_element("Mo", 1.541100e-04)
mat6.add_element("Fe", 5.910600e-02)

# Carbon
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("C", 7.449500e-04)
mat7.add_element("P", 4.561200e-06)
mat7.add_element("Mn", 3.257400e-04)
mat7.add_element("S", 2.790000e-05)
mat7.add_element("Si", 3.186900e-04)
mat7.add_element("Fe", 8.366500e-02)

# Polyethylene
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_nuclide("H1", 7.727300e-02)
mat8.add_element("C", 3.864000e-02)
mat8.add_s_alpha_beta("c_H_in_CH2")

# Water (case 115)
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_nuclide("H1", 6.676900e-02)
mat9.add_nuclide("O16", 3.338400e-02)
mat9.add_s_alpha_beta("c_H_in_H2O")

# Plutonium-uranium
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_nuclide("Pu238", 1.052000e-07)
mat10.add_nuclide("Pu239", 2.356800e-04)
mat10.add_nuclide("Pu240", 2.145700e-05)
mat10.add_nuclide("Pu241", 1.074800e-06)
mat10.add_nuclide("Pu242", 2.439600e-07)
mat10.add_nuclide("Am241", 1.417400e-06)
mat10.add_nuclide("U238", 9.026000e-04)
mat10.add_nuclide("U236", 4.861700e-07)
mat10.add_nuclide("U235", 6.512900e-06)
mat10.add_nuclide("U234", 6.476100e-08)
mat10.add_nuclide("H1", 5.542900e-02)
mat10.add_element("N", 3.245000e-03)
mat10.add_element("Gd", 7.544400e-06)
mat10.add_nuclide("O16", 3.907300e-02)
mat10.add_element("B", 1.017600e-07)
mat10.add_element("Mn", 1.899400e-07)
mat10.add_element("Cd", 3.142900e-08)
mat10.add_element("Fe", 4.068000e-06)
mat10.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Polyethylene spacer
surf1 = openmc.ZCylinder(surface_id=1, r=26.503)
# SS304L middle lattice spacer
surf2 = openmc.ZCylinder(surface_id=2, r=26.213)
# SS304L tube tank, inner
surf3 = openmc.ZCylinder(surface_id=3, r=26.503)
# SS304L tube tank, outer
surf4 = openmc.ZCylinder(surface_id=4, r=26.594)
# Carbon steel reflector tank, inner
surf5 = openmc.model.RectangularParallelepiped(-47.48, 131.30, -49.38, 49.38, -17.586, 139.279)
# Carbon steel reflector tank, outer & bcd
surf6 = openmc.model.RectangularParallelepiped(-47.63, 131.45, -49.53, 49.53, -18.221, 239.276, boundary_type="vacuum")
# Carbon steel reflector tank, top
surf7 = openmc.ZPlane(surface_id=7, z0=139.279)
# Water height
surf8 = openmc.ZPlane(surface_id=8, z0=126.533)
# Solution height (case 115)
surf9 = openmc.ZPlane(surface_id=9, z0=73.08)
# SS316 clad, inner
surf10 = openmc.ZCylinder(surface_id=10, r=0.254)
# Inconel 600 reflector, lower
surf11 = openmc.ZCylinder(surface_id=11, r=0.240665)
# Nat-UO2, lower
surf12 = openmc.ZCylinder(surface_id=12, r=0.2413)
# Active fuel
surf13 = openmc.ZCylinder(surface_id=13, r=0.247015)
# Nat-UO2, upper
surf14 = openmc.ZCylinder(surface_id=14, r=0.2413)
# Inconel 600 reflector, upper
surf15 = openmc.ZCylinder(surface_id=15, r=0.240665)
# SS302 spring, homog.
surf16 = openmc.ZCylinder(surface_id=16, r=0.254)
# SS316 plenum, inner
surf17 = openmc.ZCylinder(surface_id=17, r=0.23114)
# SS316 plenum, outer
surf18 = openmc.ZCylinder(surface_id=18, r=0.24511)
# SS316 clad, outer
surf19 = openmc.ZCylinder(surface_id=19, r=0.2921)
# SS304L guide tube, inner
surf20 = openmc.ZCylinder(surface_id=20, r=0.30415)
# SS304L guide tube, outer
surf21 = openmc.ZCylinder(surface_id=21, r=0.32315)
# surf22: Unsupported surface type "rev" with params ['4', '0.922', '0.3505', '29.999', '0.3505', '30.999', '0.3231', '239.276', '0.3231']
surf98 = openmc.ZCylinder(surface_id=98, r=26.503)
# Array outer x-y boundaries
surf99 = openmc.model.RectangularParallelepiped(-25.2, 25.2, -25.2, 25.2, -499.95, 499.95)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1099, z0=0.922)
surf1_zmax = openmc.ZPlane(surface_id=1100, z0=22.106)
surf2_zmin = openmc.ZPlane(surface_id=1101, z0=121.202)
surf2_zmax = openmc.ZPlane(surface_id=1102, z0=121.68)
surf3_zmin = openmc.ZPlane(surface_id=1103, z0=0.0)
surf3_zmax = openmc.ZPlane(surface_id=1104, z0=180.603)
surf4_zmin = openmc.ZPlane(surface_id=1105, z0=-1.586)
surf4_zmax = openmc.ZPlane(surface_id=1106, z0=182.533)
surf10_zmin = openmc.ZPlane(surface_id=1107, z0=5.596)
surf10_zmax = openmc.ZPlane(surface_id=1108, z0=228.816)
surf11_zmin = openmc.ZPlane(surface_id=1109, z0=5.596)
surf11_zmax = openmc.ZPlane(surface_id=1110, z0=20.074)
surf12_zmin = openmc.ZPlane(surface_id=1111, z0=20.074)
surf12_zmax = openmc.ZPlane(surface_id=1112, z0=22.16)
surf13_zmin = openmc.ZPlane(surface_id=1113, z0=22.16)
surf13_zmax = openmc.ZPlane(surface_id=1114, z0=113.546)
surf14_zmin = openmc.ZPlane(surface_id=1115, z0=113.546)
surf14_zmax = openmc.ZPlane(surface_id=1116, z0=115.578)
surf15_zmin = openmc.ZPlane(surface_id=1117, z0=115.578)
surf15_zmax = openmc.ZPlane(surface_id=1118, z0=130.056)
surf16_zmin = openmc.ZPlane(surface_id=1119, z0=130.056)
surf16_zmax = openmc.ZPlane(surface_id=1120, z0=142.606)
surf18_zmin = openmc.ZPlane(surface_id=1121, z0=142.606)
surf18_zmax = openmc.ZPlane(surface_id=1122, z0=228.816)
surf19_zmin = openmc.ZPlane(surface_id=1123, z0=1.536)
surf19_zmax = openmc.ZPlane(surface_id=1124, z0=239.276)
surf20_zmin = openmc.ZPlane(surface_id=1125, z0=1.536)
surf20_zmax = openmc.ZPlane(surface_id=1126, z0=182.533)
surf21_zmin = openmc.ZPlane(surface_id=1127, z0=0.922)
surf21_zmax = openmc.ZPlane(surface_id=1128, z0=182.533)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat8)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax)
u1_cell1 = openmc.Cell(fill=mat10)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf9
u1_cell2 = openmc.Cell(fill=mat6)
u1_cell2.region = (-surf2 & +surf2_zmin & -surf2_zmax)
u1_cell3 = openmc.Cell(fill=mat6)
u1_cell3.region = (+surf3 | -surf3_zmin | +surf3_zmax) & (-surf4 & +surf4_zmin & -surf4_zmax)
u1_cell4 = openmc.Cell(fill=mat9)
u1_cell4.region = (+surf4 | -surf4_zmin | +surf4_zmax) & -surf5 & -surf6 & -surf7
u1_cell5 = openmc.Cell(fill=mat7)
u1_cell5.region = +surf5 & -surf6 & -surf7
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (-surf11 & +surf11_zmin & -surf11_zmax)
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (+surf11 | -surf11_zmin | +surf11_zmax) & (-surf12 & +surf12_zmin & -surf12_zmax)
u2_cell2 = openmc.Cell(fill=mat1)
u2_cell2.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (+surf12 | -surf12_zmin | +surf12_zmax) & (-surf13 & +surf13_zmin & -surf13_zmax)
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (+surf13 | -surf13_zmin | +surf13_zmax) & (-surf14 & +surf14_zmin & -surf14_zmax)
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (+surf14 | -surf14_zmin | +surf14_zmax) & (-surf15 & +surf15_zmin & -surf15_zmax)
u2_cell5 = openmc.Cell(fill=mat4)
u2_cell5.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (+surf15 | -surf15_zmin | +surf15_zmax) & (-surf16 & +surf16_zmin & -surf16_zmax)
u2_cell6 = openmc.Cell(fill=mat5)
u2_cell6.region = (-surf10 & +surf10_zmin & -surf10_zmax) & (+surf16 | -surf16_zmin | +surf16_zmax) & +surf17 & (-surf18 & +surf18_zmin & -surf18_zmax)
u2_cell7 = openmc.Cell(fill=mat5)
u2_cell7.region = (+surf10 | -surf10_zmin | +surf10_zmax) & (-surf19 & +surf19_zmin & -surf19_zmax) & -surf22
u2_cell8 = openmc.Cell(fill=mat6)
u2_cell8.region = (+surf19 | -surf19_zmin | +surf19_zmax) & (+surf20 | -surf20_zmin | +surf20_zmax) & (-surf21 & +surf21_zmin & -surf21_zmax) & -surf22
u2_cell9 = openmc.Cell(fill=mat10)
u2_cell9.region = (+surf19 | -surf19_zmin | +surf19_zmax) & (+surf21 | -surf21_zmin | +surf21_zmax) & -surf22 & -surf9
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6, u2_cell7, u2_cell8, u2_cell9])

# Lattice 3: 36x36 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-25.2, -25.2]
lattice3.pitch = [1.400000, 1.400000]
lattice3.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1],
    [universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1],
    [universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1],
    [universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1],
    [universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1],
    [universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1],
    [universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1],
    [universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1],
    [universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1],
    [universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1],
    [universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1],
    [universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1],
    [universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

root_universe = openmc.Universe(cells=[])
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
source.space = openmc.stats.Box((-1.7, -1.7, 57.646), (1.7, 1.7, 59.646))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
