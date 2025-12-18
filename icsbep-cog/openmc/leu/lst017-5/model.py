"""
LST017-5: Unreflected 28-cm-thick slab tank with 10% enriched uranyl nitrate solution @ H/X=699 (Run 130)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution: Run 130
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 6.770300e-07)
mat1.add_nuclide("U235", 8.401500e-05)
mat1.add_nuclide("U236", 8.391000e-08)
mat1.add_nuclide("U238", 7.483300e-04)
mat1.add_nuclide("H1", 5.874400e-02)
mat1.add_element("N", 2.148000e-03)
mat1.add_nuclide("O16", 3.724100e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless Steel
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 7.156700e-05)
mat2.add_element("Si", 7.141500e-04)
mat2.add_element("Mn", 9.909500e-04)
mat2.add_element("P", 5.087900e-05)
mat2.add_element("S", 1.042400e-05)
mat2.add_element("Ni", 8.560000e-03)
mat2.add_element("Cr", 1.672500e-02)
mat2.add_element("Fe", 5.956000e-02)

# Air
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("N", 3.901400e-05)
mat3.add_nuclide("O16", 1.041000e-05)

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Slab tank/inner
surf1 = openmc.model.RectangularParallelepiped(-14.04, 14.04, -34.515, 34.515, 0.0, 149.75)
# Slab tank/outer
surf2 = openmc.model.RectangularParallelepiped(-16.57, 16.57, -37.045, 37.045, -2.039999999999992, 152.63)
# Base plate
surf3 = openmc.model.RectangularParallelepiped(-83.0, 17.0, -50.0, 50.0, -19.0, -16.0)
# Hole in base plate
surf4 = openmc.ZCylinder(surface_id=4, x0=2.0, y0=17.0, r=7.76)
# Water-reflector pool tank wall /inner
surf6 = openmc.model.RectangularParallelepiped(-118.0, 282.0, -100.0, 100.0, -499.995, 499.995, boundary_type="vacuum")
# Water-reflector pool tank wall /outer
surf7 = openmc.model.RectangularParallelepiped(-119.0, 283.0, -101.0, 101.0, -499.995, 499.995)
# Water-reflector pool tank floor/outer
surf8 = openmc.ZPlane(surface_id=8, z0=-36.5)
# Water-reflector pool tank floor/inner
surf9 = openmc.ZPlane(surface_id=9, z0=-35.0)
# Hc
surf10 = openmc.ZPlane(surface_id=10, z0=84.49)
# Water-reflector pool tank open top
surf11 = openmc.ZPlane(surface_id=11, z0=203.5)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf10

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

# SST
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = -surf3 & +surf4

# SST
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = -surf7 & +surf8 & -surf9

# SST
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf6 & -surf7 & +surf9 & -surf11

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5])
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
source.space = openmc.stats.Point((0.0, 0.0, 42.245))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
