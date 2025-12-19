"""
MIX-MET-FAST-008-7: ZEBRA-8H (in IRPhE: ZEBRA-FUND-RESR-001)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(37.5) Metal
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.773000e-02)
mat1.add_nuclide("U238", 2.895800e-02)
mat1.add_element("C", 1.844000e-04)
mat1.add_nuclide("O16", 3.460800e-04)
mat1.add_element("Fe", 5.949200e-05)
mat1.add_element("Al", 4.104300e-05)
mat1.add_nuclide("H1", 4.394800e-05)
mat1.add_element("Si", 3.943000e-05)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Nat-U Metal
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U235", 3.331700e-04)
mat2.add_nuclide("U238", 4.594900e-02)
mat2.add_element("C", 4.924100e-04)
mat2.add_element("Fe", 1.059100e-04)
mat2.add_nuclide("H1", 4.378900e-05)
mat2.add_element("Si", 2.105800e-04)
mat2.add_s_alpha_beta("c_H_in_H2O")

# Sheath
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 7.781500e-04)
mat3.add_element("Fe", 5.662600e-02)
mat3.add_element("Cr", 1.610700e-02)
mat3.add_element("Cu", 7.383500e-05)
mat3.add_element("Mo", 1.463900e-04)
mat3.add_element("Mn", 1.191700e-03)
mat3.add_element("Ni", 9.004200e-03)
mat3.add_element("Al", 3.464000e-04)
mat3.add_element("Ti", 2.933100e-04)
mat3.add_nuclide("H1", 2.320500e-05)
mat3.add_element("Si", 9.998500e-04)
mat3.add_element("V", 9.210400e-05)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.model.RectangularParallelepiped(-2.5335, 2.5335, -2.5335, 2.5335, -49.95, 49.95)
surf2 = openmc.model.RectangularParallelepiped(-2.551, 2.551, -2.551, 2.551, -49.95, 49.95)
surf3 = openmc.model.RectangularParallelepiped(-2.6272, 2.6272, -2.6272, 2.6272, -49.95, 49.95, boundary_type="reflecting")
surf4 = openmc.ZPlane(surface_id=4, z0=0.0, boundary_type="periodic")
surf5 = openmc.ZPlane(surface_id=5, z0=0.9525)
surf6 = openmc.ZPlane(surface_id=6, z0=1.2700)
surf7 = openmc.ZPlane(surface_id=7, z0=2.2225, boundary_type="periodic")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Nat-U
cell1 = openmc.Cell(cell_id=1, fill=mat2)
cell1.region = -surf1 & +surf6 & -surf7

# U(37.5)
cell2 = openmc.Cell(cell_id=2, fill=mat1)
cell2.region = -surf1 & +surf5 & -surf6

# Nat-U
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = -surf1 & +surf4 & -surf5

# Sheath
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf2 & -surf3 & +surf4 & -surf7

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4])
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
source.space = openmc.stats.Point((0.0, 0.0, 1.11125))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
