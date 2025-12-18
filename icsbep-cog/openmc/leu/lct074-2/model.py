"""
LEU-COMP-THERM-074-2: MIRTE-1 Experiment 1A-Al-200; 17x17; Hc=80.268cm
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

# Z3CN18-10
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

# Aluminum
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Al", 6.023770e-02)

# Water
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 6.672200e-02)
mat6.add_nuclide("O16", 3.336100e-02)
mat6.add_s_alpha_beta("c_H_in_H2O")

# Air
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("N", 4.198500e-05)
mat7.add_nuclide("O16", 1.126300e-05)

# Aluminum
mat8 = openmc.Material(material_id=8)
mat8.set_density("sum")
mat8.add_element("Pb", 1.039800e-07)
mat8.add_element("Ti", 1.003800e-05)
mat8.add_element("Zn", 1.343300e-03)
mat8.add_element("Zr", 1.380700e-05)
mat8.add_element("Cu", 4.433600e-05)
mat8.add_element("Fe", 2.937900e-05)
mat8.add_element("Mg", 1.909200e-03)
mat8.add_element("Mn", 1.508300e-03)
mat8.add_element("Ni", 1.694300e-05)
mat8.add_nuclide("O16", 1.760900e-04)
mat8.add_element("Al", 5.607200e-02)
mat8.add_element("Hf", 4.456800e-09)
mat8.add_element("Gd", 4.215700e-10)
mat8.add_element("B", 1.839600e-06)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7, mat8])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf2
u1_cell1 = openmc.Cell(fill=mat7)
u1_cell1.region = +surf1 & -surf2
u1_cell2 = openmc.Cell(fill=mat2)
u1_cell2.region = +surf1 & +surf2 & -surf3
u1_cell3 = openmc.Cell(fill=mat4)
u1_cell3.region = -surf4 & -surf8
u1_cell4 = openmc.Cell(fill=mat6)
u1_cell4.region = +surf3 & -surf5 & -surf6
u1_cell5 = openmc.Cell(fill=mat3)
u1_cell5.region = +surf5 & -surf6 & -surf8
u1_cell6 = openmc.Cell(fill=mat7)
u1_cell6.region = +surf3 & -surf5 & -surf7
u1_cell7 = openmc.Cell(fill=mat3)
u1_cell7.region = +surf5 & -surf7 & -surf8
u1_cell8 = openmc.Cell(fill=mat6)
u1_cell8.region = +surf3 & +surf4 & +surf6 & +surf7 & -surf8 & -surf9
u1_cell9 = openmc.Cell(fill=mat7)
u1_cell9.region = +surf3 & +surf4 & +surf6 & +surf7 & -surf8 & +surf9
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9])

# Lattice 2: 17x17 array
lattice2 = openmc.RectLattice(lattice_id=2)
lattice2.lower_left = [-13.6, -13.6]
lattice2.pitch = [1.600000, 1.600000]
lattice2.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe2 = openmc.Universe(universe_id=2)
universe2.add_cell(openmc.Cell(fill=lattice2))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# core
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.region = -surf8 & -surf10

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = -surf8 & +surf10 & -surf4

# Al
cell3 = openmc.Cell(cell_id=3, fill=mat8)
cell3.region = -surf8 & +surf10 & +surf4 & +surf11 & -surf12

# H2O
cell4 = openmc.Cell(cell_id=4, fill=mat6)
cell4.region = -surf8 & +surf10 & +surf4 & -surf11 & -surf12 & -surf9

# Air
cell5 = openmc.Cell(cell_id=5, fill=mat7)
cell5.region = -surf8 & +surf10 & +surf4 & -surf11 & -surf12 & +surf9

# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = -surf8 & +surf10 & +surf4 & +surf11 & +surf12 & -surf9

# Air
cell7 = openmc.Cell(cell_id=7, fill=mat7)
cell7.region = -surf8 & +surf10 & +surf4 & +surf11 & +surf12 & +surf9

# Air
cell18 = openmc.Cell(cell_id=18, fill=mat7)
cell18.region = +surf3 & +surf4 & +surf6 & +surf7 & -surf8 & +surf9

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell18])
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
source.space = openmc.stats.Point((0.0, 0.0, 40.134))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
