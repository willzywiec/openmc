"""
LST021-4: Unreflected 80-cm diameter cylindrical tank with 10% enriched uranyl nitrate solution @ H/X=1,239 (Run 223)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution: Run 223
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 3.987300e-07)
mat1.add_nuclide("U235", 4.947900e-05)
mat1.add_nuclide("U236", 4.941800e-08)
mat1.add_nuclide("U238", 4.407200e-04)
mat1.add_nuclide("H1", 6.129800e-02)
mat1.add_element("N", 1.571500e-03)
mat1.add_nuclide("O16", 3.605000e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless Steel
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 4.373600e-05)
mat2.add_element("Si", 1.062700e-03)
mat2.add_element("Mn", 1.156100e-03)
mat2.add_element("P", 4.317000e-05)
mat2.add_element("S", 2.978200e-06)
mat2.add_element("Ni", 8.340300e-03)
mat2.add_element("Cr", 1.677500e-02)
mat2.add_element("Fe", 5.942100e-02)

# Air
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("N", 3.901400e-05)
mat3.add_nuclide("O16", 1.041000e-05)

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Tank/inner
surf1 = openmc.ZCylinder(surface_id=1, r=39.505)
# Tank/outer
surf2 = openmc.ZCylinder(surface_id=2, r=39.815)
# Base plate
surf3 = openmc.model.RectangularParallelepiped(-60.2, 39.8, -50.0, 50.0, -19.0, -16.0)
# Hole in base plate
surf4 = openmc.ZCylinder(surface_id=4, x0=24.8, y0=17.0, r=7.76)
# boundary condition
surf5 = openmc.ZCylinder(surface_id=5, r=79.815, boundary_type="vacuum")
# Hc
surf6 = openmc.ZPlane(surface_id=6, z0=95.95)

# Z-plane surfaces for bounded cylinders
surf1_zmin = openmc.ZPlane(surface_id=1006, z0=0.0)
surf1_zmax = openmc.ZPlane(surface_id=1007, z0=149.71)
surf2_zmin = openmc.ZPlane(surface_id=1008, z0=-2.06)
surf2_zmax = openmc.ZPlane(surface_id=1009, z0=152.64)
surf5_zmin = openmc.ZPlane(surface_id=1010, z0=-34.5, boundary_type="vacuum")
surf5_zmax = openmc.ZPlane(surface_id=1011, z0=169.71, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = (-surf1 & +surf1_zmin & -surf1_zmax) & -surf6

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = (+surf1 | -surf1_zmin | +surf1_zmax) & (-surf2 & +surf2_zmin & -surf2_zmax)

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = -surf3 & +surf4

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
source.space = openmc.stats.Point((0.0, 0.0, 47.975))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
