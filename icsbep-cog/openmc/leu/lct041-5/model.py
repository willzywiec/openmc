"""
LCT041-5: CRISTO II Configuration E
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# UO2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.556800e-06)
mat1.add_nuclide("U235", 6.924100e-04)
mat1.add_nuclide("U236", 5.468100e-06)
mat1.add_nuclide("U238", 2.208200e-02)
mat1.add_nuclide("O16", 4.556800e-02)

# Zr (clad)
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 1.330000e-04)
mat2.add_element("Cr", 7.850000e-05)
mat2.add_element("Zr", 3.678000e-02)
mat2.add_element("Sn", 4.290000e-04)

# Zr (tube)
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 1.500000e-04)
mat3.add_element("Cr", 8.880000e-05)
mat3.add_element("Zr", 4.158000e-02)
mat3.add_element("Sn", 4.850000e-04)

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.673400e-02)
mat4.add_nuclide("O16", 3.336700e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Stainless
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("C", 9.430000e-05)
mat5.add_element("Si", 7.720000e-04)
mat5.add_element("Cr", 1.623100e-02)
mat5.add_element("Ni", 7.312000e-03)
mat5.add_element("B", 4.370000e-06)
mat5.add_element("Fe", 6.001200e-02)
mat5.add_element("Mo", 2.460000e-05)
mat5.add_element("Mn", 1.244600e-03)

# Cadmium
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Cd", 4.668600e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# UO2
surf1 = openmc.ZCylinder(surface_id=1, r=4.015)
# Zr clad
surf2 = openmc.ZCylinder(surface_id=2, r=4.7)
# Zr tube, inner
surf3 = openmc.ZCylinder(surface_id=3, r=4.1)
# Zr tube, outer
surf4 = openmc.ZCylinder(surface_id=4, r=4.7)
# Core boundary
surf5 = openmc.model.RectangularParallelepiped(-88.2, 88.2, -88.2, 88.2, -499.95, 499.95)
# Water gap
surf6 = openmc.model.RectangularParallelepiped(-94.1, 94.1, -94.1, 94.1, -499.95, 499.95)
# SS
surf7 = openmc.model.RectangularParallelepiped(-94.6, 94.6, -94.6, 94.6, -499.95, 499.95)
# Cd
surf8 = openmc.model.RectangularParallelepiped(-95.3, 95.3, -95.3, 95.3, -499.95, 499.95)
# SS
surf9 = openmc.model.RectangularParallelepiped(-95.8, 95.8, -95.8, 95.8, -499.95, 499.95)
# Reflector
surf10 = openmc.model.RectangularParallelepiped(-110.6, 110.6, -110.6, 110.6, -110.6, 110.6, boundary_type="reflecting")

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = -surf1 & -surf5
u1_cell1 = openmc.Cell(fill=mat2)
u1_cell1.region = +surf1 & -surf2 & -surf5
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = +surf2 & -surf5
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2])

u2_cell0 = openmc.Cell(fill=mat4)
u2_cell0.region = -surf3 & -surf5
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = +surf3 & -surf4 & -surf5
u2_cell2 = openmc.Cell(fill=mat4)
u2_cell2.region = +surf4 & -surf5
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2])

# Lattice 3: 14x14 array
lattice3 = openmc.RectLattice(lattice_id=3)
lattice3.lower_left = [-88.2, -88.2]
lattice3.pitch = [12.600000, 12.600000]
lattice3.universes = [
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe2, universe1, universe1, universe2, universe1, universe1, universe2, universe1, universe1, universe2, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe2, universe1, universe1, universe2, universe1, universe1, universe2, universe1, universe1, universe2, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe2, universe1, universe1, universe2, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
    [universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1, universe1],
]
universe3 = openmc.Universe(universe_id=3)
universe3.add_cell(openmc.Cell(fill=lattice3))

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# CORE
cell1 = openmc.Cell(cell_id=1, fill=universe3)
cell1.region = -surf5 & -surf10

# H2O
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = +surf5 & -surf6 & -surf10

# SS
cell3 = openmc.Cell(cell_id=3, fill=mat5)
cell3.region = +surf6 & -surf7 & -surf10

# Cd
cell4 = openmc.Cell(cell_id=4, fill=mat6)
cell4.region = +surf7 & -surf8 & -surf10

# SS
cell5 = openmc.Cell(cell_id=5, fill=mat5)
cell5.region = +surf8 & -surf9 & -surf10

# H2O
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf9 & -surf10

# H2O
cell10 = openmc.Cell(cell_id=10, fill=mat4)
cell10.region = +surf2 & -surf5

# H2O
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = +surf4 & -surf5

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell10, cell14])
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
source.space = openmc.stats.Box((-7.3, -7.3, -1.0), (7.3, 7.3, 1.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
