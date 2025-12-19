"""
IEU-SOL-THERM-002-10: Partially reflected 16-inch i.d. U(30.45) solution sphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 8.581800e-05)
mat1.add_nuclide("U234", 1.075600e-06)
mat1.add_nuclide("U236", 2.245100e-07)
mat1.add_nuclide("U238", 1.922600e-04)
mat1.add_nuclide("H1", 6.566800e-02)
mat1.add_element("F", 5.587500e-04)
mat1.add_nuclide("O16", 3.339300e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Aluminum
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Mg", 2.315400e-03)
mat2.add_element("Al", 5.616500e-02)
mat2.add_element("Si", 2.862500e-04)
mat2.add_element("Ti", 6.716300e-05)
mat2.add_element("Cr", 7.730900e-05)
mat2.add_element("Mn", 1.463400e-04)
mat2.add_element("Fe", 1.439500e-04)
mat2.add_element("Cu", 2.530300e-05)
mat2.add_element("Zn", 4.917800e-05)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.678500e-02)
mat3.add_nuclide("O16", 3.339300e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# r=a
surf1 = openmc.Sphere(surface_id=1, r=20.2747)
# r=b
surf2 = openmc.Sphere(surface_id=2, r=20.5998)
# r=d/2; Z1=c; Z2=-Z1 (bcd)
surf3 = openmc.ZCylinder(surface_id=3, r=45.72, boundary_type="vacuum")
# Z2=c+e
surf4 = openmc.ZPlane(surface_id=4, z0=20.2747)

# Z-plane surfaces for bounded cylinders
surf3_zmin = openmc.ZPlane(surface_id=1004, z0=-38.3798, boundary_type="vacuum")
surf3_zmax = openmc.ZPlane(surface_id=1005, z0=38.3798, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# BA27
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# H2O
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf2 & (-surf3 & +surf3_zmin & -surf3_zmax) & -surf4

root_universe = openmc.Universe(cells=[cell1, cell2, cell3])
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
