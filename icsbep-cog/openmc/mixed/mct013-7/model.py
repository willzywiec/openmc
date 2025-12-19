"""
MCT013-7: MOX/Polystyrene with H/X=226 with 5.12 SST absorber and 15.24cm Lucite reflector
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 1.951600e-04)
mat1.add_nuclide("Pu240", 1.701600e-05)
mat1.add_nuclide("Pu241", 9.553300e-07)
mat1.add_nuclide("Pu242", 8.035800e-08)
mat1.add_nuclide("U235", 1.903400e-06)
mat1.add_nuclide("U238", 1.251000e-03)
mat1.add_nuclide("Am241", 7.344000e-07)
mat1.add_nuclide("H1", 4.483100e-02)
mat1.add_element("C", 4.410100e-02)
mat1.add_nuclide("O16", 3.017500e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cr", 1.531600e-02)
mat2.add_element("Ni", 6.030700e-03)
mat2.add_element("Fe", 5.862400e-02)

mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 5.664200e-02)
mat3.add_element("C", 3.564800e-02)
mat3.add_nuclide("O16", 1.427300e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Height of lower fuel + absorber + upper fuel = 14.6714 + 5.12 + 19.5766 = 36.6297 cm
surf1 = openmc.model.RectangularParallelepiped(-20.36, 20.36, -20.38, 20.38, -14.671400000000002, 24.6966)
# Absorber, lower
surf2 = openmc.ZPlane(surface_id=2, z0=0.00)
# Absorber, upper
surf3 = openmc.ZPlane(surface_id=3, z0=5.12)
# Lucite reflector, 15.24 cm thick
surf4 = openmc.model.RectangularParallelepiped(-35.6, 35.6, -35.62, 35.62, -29.9114, 39.9366, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Fuel
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# Absrb
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = -surf1 & +surf2 & -surf3

# Fuel
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = -surf1 & +surf3

# Lucite
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf1 & -surf4

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
source.space = openmc.stats.Box((-1.0, -1.0, -8.34), (1.0, 1.0, 15.91))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
