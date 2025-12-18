"""
U233-COMP-THERM-001: SB-2-1/2
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Water at 20C
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("H1", 6.673500e-02)
mat1.add_nuclide("O16", 3.336800e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Borated SST
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.925900e-02)
mat2.add_element("Cr", 1.742800e-02)
mat2.add_element("Mn", 8.681600e-04)
mat2.add_element("Ni", 7.517100e-03)
mat2.add_nuclide("B10", 3.748800e-03)

# 233UO2-ZrO2 Seed
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("U233", 3.989100e-03)
mat3.add_nuclide("U234", 6.369000e-05)
mat3.add_nuclide("U238", 4.575900e-05)
mat3.add_nuclide("O16", 5.393200e-02)
mat3.add_element("Zr", 2.286700e-02)

# Zircalloy-2
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Zr", 4.253700e-02)
mat4.add_element("Sn", 4.991800e-04)

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Water/OR
surf1 = openmc.ZCylinder(surface_id=1, x0=-56.2991, y0=56.2991, r=91.44, boundary_type="vacuum")
# Z-Lo = -200/2 + 116.05 = 16.05 cm
surf2 = openmc.model.RectangularParallelepiped(-3.81, 3.81, -5.605779999999999, -5.42798, 16.049999999999997, 216.05)
surf3 = openmc.model.RectangularParallelepiped(-3.81, 3.81, -1.92786, -1.75006, 16.049999999999997, 216.05)
surf4 = openmc.model.RectangularParallelepiped(-3.81, 3.81, 1.75006, 1.92786, 16.049999999999997, 216.05)
surf5 = openmc.model.RectangularParallelepiped(-3.81, 3.81, 5.42798, 5.605779999999999, 16.049999999999997, 216.05)
# Fuel/OR
surf10 = openmc.ZCylinder(surface_id=10, r=0.26797)
# Clad/IR
surf11 = openmc.ZCylinder(surface_id=11, r=0.2794)
# Clad/OR
# surf12: Error converting surface type "cylinder": could not convert string to float: 'tr'
# Fuel/Lower
surf13 = openmc.ZPlane(surface_id=13, z0=-19.05)
# Fuel/Upper
surf14 = openmc.ZPlane(surface_id=14, z0=19.05)
surf100 = openmc.model.RectangularParallelepiped(-500.0, 500.0, -500.0, 500.0, -500.0, 500.0)
# surf101: Unsupported surface type "sameas" with params ['12', 'tr', '-7.81558', '-6.89610', '0', '102', 'sameas', '12', 'tr', '-6.89610', '-6.89610', '0', '103', 'sameas', '12', 'tr', '-5.97662', '-6.89610', '0']
# surf104: Unsupported surface type "sameas" with params ['12', 'tr', '-5.05714', '-6.89610', '0', '105', 'sameas', '12', 'tr', '-4.13766', '-6.89610', '0', '106', 'sameas', '12', 'tr', '-3.21818', '-6.89610', '0']
# surf107: Unsupported surface type "sameas" with params ['12', 'tr', '-2.29870', '-6.89610', '0', '108', 'sameas', '12', 'tr', '-1.37922', '-6.89610', '0', '109', 'sameas', '12', 'tr', '-0.45974', '-6.89610', '0']
# surf110: Unsupported surface type "sameas" with params ['12', 'tr', '0.45974', '-6.89610', '0', '111', 'sameas', '12', 'tr', '1.37922', '-6.89610', '0', '112', 'sameas', '12', 'tr', '2.29870', '-6.89610', '0']
# surf113: Unsupported surface type "sameas" with params ['12', 'tr', '3.21818', '-6.89610', '0', '114', 'sameas', '12', 'tr', '4.13766', '-6.89610', '0', '115', 'sameas', '12', 'tr', '5.05714', '-6.89610', '0']
# surf116: Unsupported surface type "sameas" with params ['12', 'tr', '5.97662', '-6.89610', '0', '117', 'sameas', '12', 'tr', '6.89610', '-6.89610', '0', '118', 'sameas', '12', 'tr', '7.81558', '-6.89610', '0']
surf121 = openmc.YPlane(surface_id=121, y0=-6.43636)
surf126 = openmc.YPlane(surface_id=126, y0=-1.83896)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat3)
u1_cell0.region = -surf10 & +surf13 & -surf14
u1_cell1 = openmc.Cell(fill=mat4)
u1_cell1.region = -surf10 & -surf13
u1_cell2 = openmc.Cell(fill=mat4)
u1_cell2.region = -surf10 & +surf14
u1_cell3 = openmc.Cell()
u1_cell3.region = +surf10 & -surf11
u1_cell4 = openmc.Cell(fill=mat4)
u1_cell4.region = +surf11
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4])

u2_cell0 = openmc.Cell(fill=mat1)
u2_cell0.region = -surf100
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0])

u3_cell0 = openmc.Cell(fill=mat1)
u3_cell0.region = -surf100
universe3 = openmc.Universe(universe_id=3, cells=[u3_cell0])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Cntrl
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = -surf1 & -surf2

# Cntrl
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = -surf1 & -surf3

# Cntrl
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = -surf1 & -surf4

# Cntrl
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = -surf1 & -surf5

# Zr2
cell12 = openmc.Cell(cell_id=12, fill=mat4)
cell12.region = +surf11

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell12])
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
source.space = openmc.stats.Box((-1.4, -1.4, -1.0), (1.4, 1.4, 1.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
