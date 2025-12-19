"""
PU-SOL-THERM-012 (Case 17) Hc = 28.80 @ H/X=1457; 18.91 wt-% Pu-240; no close water reflection
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 21.7 gPu/L
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 4.062700e-05)
mat1.add_nuclide("Pu240", 1.029430e-05)
mat1.add_nuclide("Pu241", 3.051540e-06)
mat1.add_nuclide("Pu242", 6.164200e-07)
mat1.add_nuclide("Am241", 3.306880e-07)
mat1.add_element("N", 1.417490e-03)
mat1.add_nuclide("O16", 3.549030e-02)
mat1.add_nuclide("H1", 6.365000e-02)
mat1.add_element("Fe", 5.391610e-06)
mat1.add_element("Cr", 1.733810e-06)
mat1.add_element("Ni", 1.228850e-06)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Water
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.668800e-02)
mat2.add_nuclide("O16", 3.334400e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

# SST
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Fe", 6.134400e-02)
mat3.add_element("Cr", 1.647200e-02)
mat3.add_element("Ni", 8.105000e-03)

# Lucoflex
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 4.104700e-02)
mat4.add_element("C", 2.736500e-02)
mat4.add_element("Cl", 1.368200e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Steel
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 8.508600e-02)
mat5.add_element("C", 5.554500e-04)

# Concrete
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 1.035000e-02)
mat6.add_nuclide("B10", 1.602000e-06)
mat6.add_nuclide("O16", 4.347000e-02)
mat6.add_element("Al", 1.563000e-03)
mat6.add_element("Si", 1.417000e-02)
mat6.add_element("Ca", 6.424000e-03)
mat6.add_element("Fe", 7.621000e-04)
mat6.add_s_alpha_beta("c_H_in_H2O")

# Air
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_nuclide("O16", 1.078400e-05)
mat7.add_element("N", 4.309000e-05)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# = Hc per Table 1b
surf1 = openmc.ZPlane(surface_id=1, z0=28.80)
# Lucoflex/Inner
surf2 = openmc.model.RectangularParallelepiped(-64.0, 64.0, -64.0, 64.0, 81.0, 99.0)
# Lucoflex/Outer
surf3 = openmc.model.RectangularParallelepiped(-65.0, 65.0, -65.0, 65.0, 80.0, 100.0)
# Tank/Inner
surf4 = openmc.model.RectangularParallelepiped(-65.0, 65.0, -65.0, 65.0, 0.0, 100.0)
# Tank/Outer
surf5 = openmc.model.RectangularParallelepiped(-65.5, 65.5, -65.5, 65.5, -0.5, 100.0)
# Pool/Inner
surf6 = openmc.model.RectangularParallelepiped(-105.0, 105.0, -160.0, 160.0, -50.5, 99.5)
# Pool/Outer
surf7 = openmc.model.RectangularParallelepiped(-105.4, 105.4, -160.4, 160.4, -51.300000000000004, 99.5)
# Room/Inner
surf8 = openmc.model.RectangularParallelepiped(-605.0, 605.0, -440.0, 440.0, -63.30000000000001, 936.7)
# Room/Inner
surf9 = openmc.model.RectangularParallelepiped(-655.0, 655.0, -490.0, 490.0, -103.30000000000001, 986.7, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# AIR
cell1 = openmc.Cell(cell_id=1, fill=mat7)
cell1.region = -surf2

# LCFLX
cell2 = openmc.Cell(cell_id=2, fill=mat4)
cell2.region = +surf2 & -surf3

# SOLN
cell3 = openmc.Cell(cell_id=3, fill=mat1)
cell3.region = -surf1 & -surf4

# AIR
cell4 = openmc.Cell(cell_id=4, fill=mat7)
cell4.region = +surf1 & +surf3 & -surf4

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf3 & +surf4 & -surf5

# AIR
cell6 = openmc.Cell(cell_id=6, fill=mat7)
cell6.region = +surf3 & +surf4 & +surf5 & -surf6 & -surf7

# STEEL
cell7 = openmc.Cell(cell_id=7, fill=mat5)
cell7.region = +surf6 & -surf7

# AIR
cell8 = openmc.Cell(cell_id=8, fill=mat7)
cell8.region = +surf3 & +surf4 & +surf5 & +surf6 & +surf7 & -surf8

# CNCRT
cell9 = openmc.Cell(cell_id=9, fill=mat6)
cell9.region = +surf8 & -surf9

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9])
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
source.space = openmc.stats.Point((0.0, 0.0, 14.4))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
