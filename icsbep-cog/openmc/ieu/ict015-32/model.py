"""
ICT015-32: Bare heterogeneous lattice arrangement (Het B) of batch 40 UO2/wax "cubes" and plain wax "cubes"
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Batch 40
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 6.097900e-02)
mat1.add_element("C", 3.020500e-02)
mat1.add_nuclide("O16", 1.065700e-02)
mat1.add_element("Al", 6.483300e-05)
mat1.add_nuclide("U234", 1.974000e-05)
mat1.add_nuclide("U235", 1.559000e-03)
mat1.add_nuclide("U236", 3.605400e-06)
mat1.add_nuclide("U238", 3.544900e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

# Plain wax
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 7.871200e-02)
mat2.add_element("C", 3.896600e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

# Polythene
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 7.891100e-02)
mat3.add_element("C", 3.945500e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.model.RectangularParallelepiped(-10.16, 10.16, -10.16, 10.16, -9.0932, 9.0932)
surf2 = openmc.model.RectangularParallelepiped(-30.48, 30.48, -30.48, 30.48, -29.4132, 29.4132, boundary_type="vacuum")
surf10 = openmc.XPlane(surface_id=10, x0=-10.16)
surf11 = openmc.XPlane(surface_id=11, x0=-7.62)
surf12 = openmc.XPlane(surface_id=12, x0=-5.08)
surf13 = openmc.XPlane(surface_id=13, x0=-2.54)
surf14 = openmc.XPlane(surface_id=14, x0=0.)
surf15 = openmc.XPlane(surface_id=15, x0=2.54)
surf16 = openmc.XPlane(surface_id=16, x0=5.08)
surf17 = openmc.XPlane(surface_id=17, x0=7.62)
surf18 = openmc.XPlane(surface_id=18, x0=10.16)
surf20 = openmc.YPlane(surface_id=20, y0=-10.16)
surf21 = openmc.YPlane(surface_id=21, y0=-7.62)
surf22 = openmc.YPlane(surface_id=22, y0=-5.08)
surf23 = openmc.YPlane(surface_id=23, y0=-2.54)
surf24 = openmc.YPlane(surface_id=24, y0=0.)
surf25 = openmc.YPlane(surface_id=25, y0=2.54)
surf26 = openmc.YPlane(surface_id=26, y0=5.08)
surf27 = openmc.YPlane(surface_id=27, y0=7.62)
surf28 = openmc.YPlane(surface_id=28, y0=10.16)
surf30 = openmc.ZPlane(surface_id=30, z0=-9.093)
surf31 = openmc.ZPlane(surface_id=31, z0=9.093)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0])

u2_cell0 = openmc.Cell(fill=mat2)
u2_cell0.region = -surf1
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0])

universe3 = openmc.Universe(universe_id=3, cells=[])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# HetB
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf1

# CH2
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = +surf1 & -surf2

# UO2WAX
cell4 = openmc.Cell(cell_id=4, fill=mat1)
cell4.region = -surf1

# WAX
cell6 = openmc.Cell(cell_id=6, fill=mat2)
cell6.region = -surf1

# unit1
cell7 = openmc.Cell(cell_id=7, fill=universe1)
cell7.translation = (8.89, -8.89, 0.0)
cell7.region = +surf17 & -surf18 & +surf20 & -surf21 & +surf30 & -surf31

root_universe = openmc.Universe(cells=[cell1, cell2, cell4, cell6, cell7])
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
