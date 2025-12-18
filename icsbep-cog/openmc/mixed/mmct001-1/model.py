"""
MMCT001-1: Experiment 106 with 996 FFTF rods immersed in 0.88 gPu/l and 2.7 gU/l solution
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

# Water (case 106)
mat9 = openmc.Material(material_id=9)
mat9.set_density("sum")
mat9.add_nuclide("H1", 6.667500e-02)
mat9.add_nuclide("O16", 3.333800e-02)
mat9.add_s_alpha_beta("c_H_in_H2O")

# Plutonium-uranium
mat10 = openmc.Material(material_id=10)
mat10.set_density("sum")
mat10.add_nuclide("Pu238", 9.016100e-10)
mat10.add_nuclide("Pu239", 2.019900e-06)
mat10.add_nuclide("Pu240", 1.838900e-07)
mat10.add_nuclide("Pu241", 9.211400e-09)
mat10.add_nuclide("Pu242", 2.090800e-09)
mat10.add_nuclide("Am241", 1.237400e-08)
mat10.add_nuclide("U238", 6.777900e-06)
mat10.add_nuclide("U236", 3.650800e-09)
mat10.add_nuclide("U235", 4.890800e-08)
mat10.add_nuclide("U234", 4.863200e-10)
mat10.add_nuclide("H1", 6.609200e-02)
mat10.add_element("N", 2.694300e-04)
mat10.add_nuclide("O16", 3.374500e-02)
mat10.add_element("B", 3.977200e-10)
mat10.add_element("Mn", 1.487000e-09)
mat10.add_element("Cd", 2.741300e-10)
mat10.add_element("Fe", 3.165600e-08)
mat10.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8, mat9, mat10])

# ==============================================================================
# Geometry
# ==============================================================================

# Polyethylene spacer
surf1 = openmc.ZCylinder(surface_id=1, x0=0.922, y0=22.106, r=26.503)
# SS304L middle lattice spacer
surf2 = openmc.ZCylinder(surface_id=2, x0=121.202, y0=121.68, r=26.213)
# SS304L tube tank, inner
surf3 = openmc.ZCylinder(surface_id=3, x0=0.0, y0=180.603, r=26.503)
# SS304L tube tank, outer
surf4 = openmc.ZCylinder(surface_id=4, x0=-1.586, y0=182.533, r=26.594)
# Carbon steel reflector tank, inner
surf5 = openmc.model.RectangularParallelepiped(-47.48, 131.30, -49.38, 49.38, -17.586, 139.279)
# Carbon steel reflector tank, outer & bcd
surf6 = openmc.model.RectangularParallelepiped(-47.63, 131.45, -49.53, 49.53, -18.221, 239.276, boundary_type="vacuum")
# Carbon steel reflector tank, top
surf7 = openmc.ZPlane(surface_id=7, z0=139.279)
# Water height
surf8 = openmc.ZPlane(surface_id=8, z0=126.533)
# Solution height (case 106)
surf9 = openmc.ZPlane(surface_id=9, z0=18.41)
# SS316 clad, inner
surf10 = openmc.ZCylinder(surface_id=10, x0=5.596, y0=228.816, r=0.254)
# Inconel 600 reflector, lower
surf11 = openmc.ZCylinder(surface_id=11, x0=5.596, y0=20.074, r=0.240665)
# Nat-UO2, lower
surf12 = openmc.ZCylinder(surface_id=12, x0=20.074, y0=22.16, r=0.2413)
# Active fuel
surf13 = openmc.ZCylinder(surface_id=13, x0=22.16, y0=113.546, r=0.247015)
# Nat-UO2, upper
surf14 = openmc.ZCylinder(surface_id=14, x0=113.546, y0=115.578, r=0.2413)
# Inconel 600 reflector, upper
surf15 = openmc.ZCylinder(surface_id=15, x0=115.578, y0=130.056, r=0.240665)
# SS302 spring, homog.
surf16 = openmc.ZCylinder(surface_id=16, x0=130.056, y0=142.606, r=0.254)
# SS316 plenum, inner
surf17 = openmc.ZCylinder(surface_id=17, r=0.23114)
# SS316 plenum, outer
surf18 = openmc.ZCylinder(surface_id=18, x0=142.606, y0=228.816, r=0.24511)
# SS316 clad, outer
surf19 = openmc.ZCylinder(surface_id=19, x0=1.536, y0=239.276, r=0.2921)
# SS304L guide tube, inner
surf20 = openmc.ZCylinder(surface_id=20, x0=1.536, y0=182.533, r=0.30415)
# SS304L guide tube, outer
surf21 = openmc.ZCylinder(surface_id=21, x0=0.922, y0=182.533, r=0.32315)
# surf22: Unsupported surface type "rev" with params ['4', '0.922', '0.3505', '29.999', '0.3505', '30.999', '0.3231', '239.276', '0.3231']
surf98 = openmc.ZCylinder(surface_id=98, r=26.503)
# Array outer x-y boundaries
surf99 = openmc.model.RectangularParallelepiped(-25.2, 25.2, -25.2, 25.2, -499.95, 499.95)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat8)
u1_cell0.region = -surf1
u1_cell1 = openmc.Cell(fill=mat10)
u1_cell1.region = +surf1 & -surf3 & -surf9
u1_cell2 = openmc.Cell(fill=mat6)
u1_cell2.region = -surf2
u1_cell3 = openmc.Cell(fill=mat6)
u1_cell3.region = +surf3 & -surf4
u1_cell4 = openmc.Cell(fill=mat9)
u1_cell4.region = +surf4 & -surf5 & -surf6 & -surf7
u1_cell5 = openmc.Cell(fill=mat7)
u1_cell5.region = +surf5 & -surf6 & -surf7
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = -surf10 & -surf11
u2_cell1 = openmc.Cell(fill=mat2)
u2_cell1.region = -surf10 & +surf11 & -surf12
u2_cell2 = openmc.Cell(fill=mat1)
u2_cell2.region = -surf10 & +surf12 & -surf13
u2_cell3 = openmc.Cell(fill=mat2)
u2_cell3.region = -surf10 & +surf13 & -surf14
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = -surf10 & +surf14 & -surf15
u2_cell5 = openmc.Cell(fill=mat4)
u2_cell5.region = -surf10 & +surf15 & -surf16
u2_cell6 = openmc.Cell(fill=mat5)
u2_cell6.region = -surf10 & +surf16 & +surf17 & -surf18
u2_cell7 = openmc.Cell(fill=mat5)
u2_cell7.region = +surf10 & -surf19
u2_cell8 = openmc.Cell(fill=mat6)
u2_cell8.region = +surf19 & +surf20 & -surf21
u2_cell9 = openmc.Cell(fill=mat10)
u2_cell9.region = +surf19 & +surf21 & -surf9
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
source.space = openmc.stats.Box((-1.7, -1.7, 30.311), (1.7, 1.7, 32.311))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
