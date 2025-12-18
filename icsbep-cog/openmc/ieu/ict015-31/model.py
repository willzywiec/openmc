"""
ICT015-31: Bare heterogeneous lattice arrangement (Het A) of batch 40 UO2/wax "cubes" and plain wax "cubes"
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

surf1 = openmc.model.RectangularParallelepiped(-8.89, 8.89, -8.89, 8.89, -11.049, 11.049)
surf2 = openmc.model.RectangularParallelepiped(-29.21, 29.21, -29.21, 29.21, -31.369, 31.369, boundary_type="vacuum")
surf11 = openmc.XPlane(surface_id=11, x0=-8.89)
surf12 = openmc.XPlane(surface_id=12, x0=-6.35)
surf13 = openmc.XPlane(surface_id=13, x0=-3.81)
surf14 = openmc.XPlane(surface_id=14, x0=-1.27)
surf15 = openmc.XPlane(surface_id=15, x0=1.27)
surf16 = openmc.XPlane(surface_id=16, x0=3.81)
surf17 = openmc.XPlane(surface_id=17, x0=6.35)
surf18 = openmc.XPlane(surface_id=18, x0=8.89)
surf21 = openmc.YPlane(surface_id=21, y0=-8.89)
surf22 = openmc.YPlane(surface_id=22, y0=-6.35)
surf23 = openmc.YPlane(surface_id=23, y0=-3.81)
surf24 = openmc.YPlane(surface_id=24, y0=-1.27)
surf25 = openmc.YPlane(surface_id=25, y0=1.27)
surf26 = openmc.YPlane(surface_id=26, y0=3.81)
surf27 = openmc.YPlane(surface_id=27, y0=6.35)
surf28 = openmc.YPlane(surface_id=28, y0=8.89)
surf31 = openmc.ZPlane(surface_id=31, z0=-11.049)
surf32 = openmc.ZPlane(surface_id=32, z0=-8.28675)
surf33 = openmc.ZPlane(surface_id=33, z0=-5.5245)
surf34 = openmc.ZPlane(surface_id=34, z0=-2.76225)
surf35 = openmc.ZPlane(surface_id=35, z0=0.)
surf36 = openmc.ZPlane(surface_id=36, z0=2.76225)
surf37 = openmc.ZPlane(surface_id=37, z0=5.5245)
surf38 = openmc.ZPlane(surface_id=38, z0=8.28675)
surf39 = openmc.ZPlane(surface_id=39, z0=11.049)

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

# HetA
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
cell7.translation = (7.62, -7.62, -9.667875)
cell7.region = +surf17 & -surf18 & +surf21 & -surf22 & +surf31 & -surf32

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
