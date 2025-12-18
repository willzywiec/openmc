"""
LEU-COMP-THERM-101-3: MIRTE-2.2 Experiment 2A-Rh(40-1N)-040-Zr-010; 9x28; Hc=74.613 cm
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(4.738)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("O16", 4.631100e-02)
mat1.add_element("Fe", 9.512100e-06)
mat1.add_element("Si", 2.247500e-05)
mat1.add_element("Al", 4.169300e-06)
mat1.add_nuclide("U234", 7.108700e-06)
mat1.add_nuclide("U235", 1.110400e-03)
mat1.add_nuclide("U236", 3.179200e-05)
mat1.add_nuclide("U238", 2.200600e-02)

# Zr-4
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("N", 8.730000e-06)
mat2.add_nuclide("O16", 3.372700e-04)
mat2.add_element("Sn", 4.538900e-04)
mat2.add_element("Fe", 1.568000e-04)
mat2.add_element("Cr", 8.951600e-05)
mat2.add_element("C", 4.223300e-05)
mat2.add_element("Si", 1.390400e-05)
mat2.add_element("Al", 2.836100e-06)
mat2.add_element("Zr", 4.242800e-02)
mat2.add_element("Hf", 1.228700e-06)
mat2.add_element("H", 1.448000e-05)

# AG3
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Si", 2.290000e-04)
mat3.add_element("Fe", 1.151600e-04)
mat3.add_element("Cu", 2.530300e-05)
mat3.add_element("Mn", 1.463400e-04)
mat3.add_element("Mg", 2.381600e-03)
mat3.add_element("Cr", 9.277100e-05)
mat3.add_element("Zn", 4.917900e-05)
mat3.add_element("Ti", 5.037300e-05)
mat3.add_element("Al", 5.622600e-02)

# Z2CN18-10
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 1.646900e-02)
mat4.add_element("Ni", 8.106100e-03)
mat4.add_element("Mn", 8.659700e-04)
mat4.add_element("Si", 1.693900e-03)
mat4.add_element("P", 6.143800e-05)
mat4.add_element("S", 4.450400e-05)
mat4.add_element("C", 1.188300e-04)
mat4.add_element("Fe", 5.954600e-02)

# Water
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.672200e-02)
mat5.add_nuclide("O16", 3.336100e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

# Air
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("N", 4.198500e-05)
mat6.add_nuclide("O16", 1.126300e-05)

# Rhodium
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("H1", 5.972000e-02)
mat7.add_element("Rh", 2.340800e-04)
mat7.add_element("S", 1.164100e-03)
mat7.add_nuclide("O16", 3.451700e-02)
mat7.add_element("Au", 3.057400e-10)
mat7.add_element("Ag", 8.932500e-09)
mat7.add_element("Pd", 2.829400e-09)
mat7.add_element("Al", 8.927800e-09)
mat7.add_element("B", 2.228100e-08)
mat7.add_element("Ba", 4.385200e-10)
mat7.add_element("Ca", 1.427500e-07)
mat7.add_element("Cr", 1.389800e-08)
mat7.add_element("Cu", 2.843000e-09)
mat7.add_element("Fe", 4.636800e-08)
mat7.add_element("Mn", 7.673100e-09)
mat7.add_element("Na", 9.692000e-08)
mat7.add_element("Ni", 1.847000e-08)
mat7.add_element("P", 5.832800e-09)
mat7.add_element("Zn", 1.381400e-08)
mat7.add_element("Te", 6.607300e-09)
mat7.add_s_alpha_beta("c_H_in_H2O")

# Zircaloy
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Zr", 4.134300e-02)
mat8.add_element("Fe", 1.384600e-04)
mat8.add_element("Cr", 7.435500e-05)
mat8.add_element("Ga", 3.271600e-05)
mat8.add_element("In", 6.734500e-06)
mat8.add_element("Sn", 6.188000e-04)
mat8.add_element("C", 6.437900e-05)
mat8.add_nuclide("O16", 3.624700e-04)
mat8.add_element("H", 4.602900e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf2
u1_cell1 = openmc.Cell(fill=mat6)
u1_cell1.region = +surf1 & -surf2
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf1 & +surf2 & -surf3
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = -surf4 & -surf8
u1_cell4 = openmc.Cell(fill=mat5)
u1_cell4.region = +surf3 & -surf5 & -surf6
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = +surf5 & -surf6 & -surf8
u1_cell6 = openmc.Cell(fill=mat6)
u1_cell6.region = +surf3 & -surf5 & -surf7
u1_cell7 = openmc.Cell(fill=mat3)
u1_cell7.region = +surf5 & -surf7 & -surf8
u1_cell8 = openmc.Cell(fill=mat5)
u1_cell8.region = +surf3 & +surf4 & +surf6 & +surf7 & -surf8 & -surf9
u1_cell9 = openmc.Cell(fill=mat6)
u1_cell9.region = +surf3 & +surf4 & +surf6 & +surf7 & -surf8 & +surf9
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9])

u2_cell0 = openmc.Cell(fill=mat4)
u2_cell0.region = -surf4 & -surf8
u2_cell1 = openmc.Cell(fill=mat5)
u2_cell1.region = -surf5 & -surf6
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf5 & -surf6 & -surf8
u2_cell3 = openmc.Cell(fill=mat6)
u2_cell3.region = -surf5 & -surf7
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = +surf5 & -surf7 & -surf8
u2_cell5 = openmc.Cell(fill=mat5)
u2_cell5.region = +surf4 & +surf6 & +surf7 & -surf8 & -surf9
u2_cell6 = openmc.Cell(fill=mat6)
u2_cell6.region = +surf4 & +surf6 & +surf7 & -surf8 & +surf9
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5, u2_cell6])

# Lattice 3: 62x10 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-49.51, 2.99865]
lattice3.pitch = [1.597097, 1.600000]
lattice3.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# Lattice 4: 62x10 array
lattice4 = openmc.RectLattice(lattice_id=4)
lattice4.lower_left = [-49.51, -18.99865]
lattice4.pitch = [1.597097, 1.600000]
lattice4.universes = [
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
    [universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2, universe2],
]
universe4 = openmc.Universe(universe_id=4)
universe4.add_cell(openmc.Cell(fill=lattice4))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# core
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf8 & -surf11

# core
cell2 = openmc.Cell(cell_id=2, fill=universe4)
cell2.region = -surf8 & -surf12

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = -surf4 & -surf8 & +surf11 & +surf12

# AG3
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf4 & -surf8 & +surf11 & +surf12 & -surf20

# Box
cell5 = openmc.Cell(cell_id=5, fill=mat8)
cell5.region = +surf4 & -surf8 & +surf11 & +surf12 & +surf20 & -surf21 & +surf22

# Air
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf4 & -surf8 & +surf11 & +surf12 & +surf20 & -surf21 & -surf22 & +surf23

# NaCl
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = +surf4 & -surf8 & +surf11 & +surf12 & +surf20 & -surf21 & -surf22 & -surf23

# H2O
cell8 = openmc.Cell(cell_id=8, fill=mat5)
cell8.region = +surf4 & -surf8 & +surf11 & +surf12 & +surf20 & +surf21 & -surf9

# Air
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = +surf4 & -surf8 & +surf11 & +surf12 & +surf20 & +surf21 & +surf9

# Air
cell20 = openmc.Cell(cell_id=20, fill=mat6)
cell20.region = +surf3 & +surf4 & +surf6 & +surf7 & -surf8 & +surf9

# Air
cell28 = openmc.Cell(cell_id=28, fill=mat6)
cell28.region = +surf4 & +surf6 & +surf7 & -surf8 & +surf9

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell20, cell28])
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
source.space = openmc.stats.Box((-1.8, -17.6, 36.3065), (1.8, 17.6, 38.3065))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
