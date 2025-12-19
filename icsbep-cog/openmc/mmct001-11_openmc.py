"""
MMCT001-11: Experiment 117 with 996 FFTF empty tubes immersed in 83.30 gPu/l and 286.57 gU/l solution
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

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

# Water (case 117)
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_nuclide("H1", 6.671500e-02)
mat9.add_nuclide("O16", 3.335800e-02)
mat9.add_s_alpha_beta("c_H_in_H2O")

# Plutonium-uranium
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_nuclide("Pu238", 8.534500e-08)
mat10.add_nuclide("Pu239", 1.912000e-04)
mat10.add_nuclide("Pu240", 1.740700e-05)
mat10.add_nuclide("Pu241", 8.719400e-07)
mat10.add_nuclide("Pu242", 1.979100e-07)
mat10.add_nuclide("Am241", 1.131700e-06)
mat10.add_nuclide("U238", 7.193900e-04)
mat10.add_nuclide("U236", 3.874900e-07)
mat10.add_nuclide("U235", 5.191000e-06)
mat10.add_nuclide("U234", 5.161600e-08)
mat10.add_nuclide("H1", 5.726500e-02)
mat10.add_element("N", 2.831100e-03)
mat10.add_nuclide("O16", 3.830500e-02)
mat10.add_element("B", 3.764800e-08)
mat10.add_element("Mn", 1.407600e-07)
mat10.add_element("Cd", 2.594900e-08)
mat10.add_element("Fe", 2.996600e-06)
mat10.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat5, mat6, mat7, mat8, mat9, mat10])

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
# Solution height (case 117)
surf9 = openmc.ZPlane(surface_id=9, z0=27.42)
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
surf22 = openmc.Revolution(surface_id=22, rz=[(0.922, 0.3505), (29.999, 0.3505), (30.999, 0.3231), (239.276, 0.3231)], axis="x")
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

u2_cell0 = openmc.Cell(fill=mat5)
u2_cell0.region = (+surf10 | -surf10_zmin | +surf10_zmax) & (-surf19 & +surf19_zmin & -surf19_zmax) & -surf22
u2_cell1 = openmc.Cell(fill=mat6)
u2_cell1.region = (+surf19 | -surf19_zmin | +surf19_zmax) & (+surf20 | -surf20_zmin | +surf20_zmax) & (-surf21 & +surf21_zmin & -surf21_zmax) & -surf22
u2_cell2 = openmc.Cell(fill=mat10)
u2_cell2.region = (+surf19 | -surf19_zmin | +surf19_zmax) & (+surf21 | -surf21_zmin | +surf21_zmax) & -surf22 & -surf9
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

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
source.space = openmc.stats.Box((-1.7, -1.7, 34.816), (1.7, 1.7, 36.816))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
