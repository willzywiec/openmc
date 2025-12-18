"""
LST021-3: Unreflected 80-cm diameter cylindrical tank with 10% enriched uranyl nitrate solution @ H/X=1,168 (Run 221)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution: Run 221
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.213700e-07)
mat1.add_nuclide("U235", 5.228900e-05)
mat1.add_nuclide("U236", 5.222400e-08)
mat1.add_nuclide("U238", 4.657500e-04)
mat1.add_nuclide("H1", 6.107300e-02)
mat1.add_element("N", 1.633200e-03)
mat1.add_nuclide("O16", 3.617500e-02)
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

# Tank/inner
surf1 = openmc.ZCylinder(surface_id=1, x0=0.0, y0=149.71, r=39.505)
# Tank/outer
surf2 = openmc.ZCylinder(surface_id=2, x0=-2.06, y0=152.64, r=39.815)
# Base plate
surf3 = openmc.model.RectangularParallelepiped(-60.2, 39.8, -50.0, 50.0, -19.0, -16.0)
# Hole in base plate
surf4_cyl = openmc.ZCylinder(surface_id=4, x0=tr, y0=24.8, r=7.76)
surf4_zmin = openmc.ZPlane(z0=17.0)
surf4_zmax = openmc.ZPlane(z0=0.0)
surf4 = (surf4_cyl, surf4_zmin, surf4_zmax)
# boundary condition
surf5 = openmc.ZCylinder(surface_id=5, x0=-34.5, y0=169.71, r=79.815, boundary_type="vacuum")
# Hc
surf6 = openmc.ZPlane(surface_id=6, z0=69.09)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf6

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

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
source.space = openmc.stats.Point((0.0, 0.0, 34.545))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
