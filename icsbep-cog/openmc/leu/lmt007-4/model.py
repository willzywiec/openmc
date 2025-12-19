"""
LMT007-4: 195 U(4.948) Metal Rods in Water; Pitch=2.050cm; Hf=30cm; Hw=67.39-21.59=45.8cm
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# LEU
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 2.153100e-05)
mat1.add_nuclide("U235", 2.405400e-03)
mat1.add_nuclide("U236", 1.098900e-05)
mat1.add_nuclide("U238", 4.559300e-02)

# H2O @ 24.0 C for Case 4
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.669100e-02)
mat2.add_nuclide("O16", 3.334600e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Fuel rod
surf1 = openmc.ZCylinder(surface_id=1, r=0.38645)
# 15x15 lattice region
surf2 = openmc.model.RectangularParallelepiped(-15.375, 15.375, -15.375, 15.375, -499.95, 499.95)
# Water/boundary
surf3 = openmc.ZCylinder(surface_id=3, r=50.53, boundary_type="vacuum")

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1003, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1004, z0=30.0)
surf3_zmin = openmc.ZPlane(surface_id=1005, z0=-21.59, boundary_type="vacuum")
surf3_zmax = openmc.ZPlane(surface_id=1006, z0=45.8, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = (-surf1 & +surf1_zmin & -surf1_zmax)
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = (+surf1 | -surf1_zmin | +surf1_zmax) & -surf2
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1])

# Lattice 2: 15x15 array
lattice2 = openmc.RectLattice(lattice_id=2)
lattice2.lower_left = [-15.375, -15.375]
lattice2.pitch = [2.050000, 2.050000]
lattice2.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe2 = openmc.Universe(universe_id=2)
universe2.add_cell(openmc.Cell(fill=lattice2))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CORE
cell1 = openmc.Cell(cell_id=1, fill=universe2)
cell1.region = -surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)

# H2O
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax)

# H2O
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = (+surf1 | -surf1_zmin | +surf1_zmax) & -surf2

root_universe = openmc.Universe(cells=[cell1, cell2, cell5])
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
source.space = openmc.stats.Point((0.0, 0.0, 15.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
