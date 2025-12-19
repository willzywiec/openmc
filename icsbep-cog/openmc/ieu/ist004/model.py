"""
IEU-SOL-THERM-004: 564.8 grams U-235 in U(14.67) @ H/X = 646 (Lopo)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Uranly Sulfate Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 9.679500e-05)
mat1.add_nuclide("U234", 7.425700e-07)
mat1.add_nuclide("U238", 5.551800e-04)
mat1.add_element("S", 6.527200e-04)
mat1.add_nuclide("O16", 3.518500e-02)
mat1.add_nuclide("H1", 6.253800e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS-347
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 3.208800e-04)
mat2.add_element("Mn", 1.753900e-03)
mat2.add_element("P", 6.999300e-05)
mat2.add_element("S", 4.506700e-05)
mat2.add_element("Si", 1.715400e-03)
mat2.add_element("Ni", 6.567000e-03)
mat2.add_element("Cr", 1.667800e-02)
mat2.add_element("Nb", 4.926200e-04)
mat2.add_element("Fe", 6.029500e-02)

# BeO
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("Be9", 6.621000e-02)
mat3.add_nuclide("O16", 6.621000e-02)
mat3.add_element("B", 3.063700e-07)
mat3.add_element("Co", 5.620200e-07)
mat3.add_element("Ag", 3.070600e-08)
mat3.add_element("Cd", 7.366200e-08)
mat3.add_element("In", 1.442300e-08)
mat3.add_s_alpha_beta("c_Be_in_BeO")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# SST/Inner
surf1 = openmc.Sphere(surface_id=1, r=15.2820)
# SST/Outer
surf2 = openmc.Sphere(surface_id=2, r=15.3614)
# BeO/Inner
surf3 = openmc.Sphere(surface_id=3, r=15.4614)
# BeO/Outer
surf4 = openmc.Sphere(surface_id=4, r=47.4210, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# SOL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# GAP
cell3 = openmc.Cell(cell_id=3)
cell3.region = +surf2 & -surf3

# BEO
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf3 & -surf4

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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
