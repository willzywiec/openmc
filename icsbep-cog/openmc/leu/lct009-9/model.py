"""
LEU-COMP-THERM-009-9: (15x8)-3.0035cm-(0.713cm Boral)-3.0035cm-(15x8)-3.0035cm-(0.713cm Boral)-3.0035cm-(15x8) arrays U(4.31)O2 rods in water; 2.54 cm pitch
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(4.31)O2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 5.183500e-06)
mat1.add_nuclide("U235", 1.010200e-03)
mat1.add_nuclide("U236", 5.139500e-06)
mat1.add_nuclide("U238", 2.215700e-02)
mat1.add_nuclide("O16", 4.675300e-02)

# Al-6061
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Al", 5.843300e-02)
mat2.add_element("Cr", 6.231000e-05)
mat2.add_element("Cu", 6.373100e-05)
mat2.add_element("Mg", 6.665100e-04)
mat2.add_element("Mn", 2.211500e-05)
mat2.add_element("Ti", 2.537500e-05)
mat2.add_element("Zn", 3.096700e-05)
mat2.add_element("Si", 3.460700e-04)
mat2.add_element("Fe", 1.015200e-04)

# Rubber
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 5.817800e-02)
mat3.add_element("C", 4.356200e-02)
mat3.add_element("Ca", 2.566000e-03)
mat3.add_element("S", 4.782000e-04)
mat3.add_element("Si", 9.636000e-05)
mat3.add_nuclide("O16", 1.246100e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

# Water
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 6.667500e-02)
mat4.add_nuclide("O16", 3.333800e-02)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Acrylic
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 5.664200e-02)
mat5.add_element("C", 3.564800e-02)
mat5.add_nuclide("O16", 1.427300e-02)
mat5.add_s_alpha_beta("c_H_in_CH2")

# B4C-Al
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Al", 3.467300e-02)
mat6.add_nuclide("B10", 7.921700e-03)
mat6.add_nuclide("B11", 3.188600e-02)
mat6.add_element("C", 9.950100e-03)
mat6.add_element("Cr", 1.441900e-05)
mat6.add_element("Cu", 2.123700e-05)
mat6.add_element("Fe", 8.860600e-05)
mat6.add_element("Mg", 3.084800e-05)
mat6.add_element("Mn", 1.364700e-05)
mat6.add_element("Na", 1.304500e-05)
mat6.add_element("Ni", 5.109900e-06)
mat6.add_element("Si", 1.067800e-04)
mat6.add_element("S", 1.402700e-05)
mat6.add_element("Zn", 2.293200e-05)

# Al-1100
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Al", 5.966000e-02)
mat7.add_element("Cu", 3.070500e-05)
mat7.add_element("Mn", 7.399100e-06)
mat7.add_element("Zn", 1.243300e-05)
mat7.add_element("Si", 2.330200e-04)
mat7.add_element("Fe", 1.171900e-04)
mat7.add_nuclide("H1", 1.000000e+00)
mat7.add_nuclide("Al1100", -2.000000e+00)
mat7.add_nuclide("Al1100", -2.000000e+00)
mat7.add_nuclide("Al6061", -1.000000e+00)
mat7.add_nuclide("H1", -1.000000e+00)
mat7.add_nuclide("H1", -1.000000e+00)
mat7.add_element("Y", 2.010000e+02)
mat7.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

# ==============================================================================
# Geometry
# ==============================================================================

# Array Boundary
surf1 = openmc.model.RectangularParallelepiped(-63.87, 63.87, -10.16, 10.16, -499.995, 499.995)
# Entire Problem (BCD)
surf2 = openmc.model.RectangularParallelepiped(-93.87, 93.87, -40.16, 40.16, -20.0625, 107.075)
surf3 = openmc.XPlane(surface_id=3, x0=-25.77)
surf4 = openmc.XPlane(surface_id=4, x0=-19.05)
surf5 = openmc.XPlane(surface_id=5, x0=19.05)
surf6 = openmc.XPlane(surface_id=6, x0=25.77)
# Rubber
surf11 = openmc.ZCylinder(surface_id=11, x0=-2.2225, y0=0.0, r=0.6415)
# U(4.31)O2 fuel
surf12 = openmc.ZCylinder(surface_id=12, x0=0.0, y0=92.075, r=0.6325)
# Rubber
surf13 = openmc.ZCylinder(surface_id=13, x0=92.075, y0=94.2975, r=0.6415)
# Clad inner
surf14 = openmc.ZCylinder(surface_id=14, r=0.6415)
# Clad outer
surf15 = openmc.ZCylinder(surface_id=15, x0=-2.2225, y0=94.2975, r=0.7075)
# Acrylic base plate
surf16 = openmc.model.RectangularParallelepiped(-499.95, 499.95, -499.95, 499.95, -4.7625, -2.2225)
surf21 = openmc.model.RectangularParallelepiped(-22.7665, -22.0535, -17.8, 17.8, 0.0, 91.5)
surf22 = openmc.model.RectangularParallelepiped(-22.6645, -22.1555, -499.95, 499.95, -499.95, 499.95)
surf31 = openmc.model.RectangularParallelepiped(22.0535, 22.7665, -17.8, 17.8, 0.0, 91.5)
surf32 = openmc.model.RectangularParallelepiped(22.1555, 22.6645, -499.95, 499.95, -499.95, 499.95)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

root_universe = openmc.Universe(cells=[])
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
source.space = openmc.stats.Box((-45.82, -2.27, 45.0375), (45.82, 2.27, 47.0375))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
