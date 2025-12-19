"""
LST003-5: Partially full sphere of 10% enriched uranyl nitrate solution at H/X=1173
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 4.627900e-07)
mat1.add_nuclide("U235", 5.239800e-05)
mat1.add_nuclide("U238", 4.613500e-04)
mat1.add_element("N", 1.576400e-03)
mat1.add_nuclide("O16", 3.622500e-02)
mat1.add_nuclide("H1", 6.148300e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Stainless Steel
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Fe", 5.908800e-02)
mat2.add_element("Cr", 1.653200e-02)
mat2.add_element("Ni", 8.136900e-03)
mat2.add_element("Mn", 1.303900e-03)
mat2.add_element("Si", 1.360300e-03)
mat2.add_element("Ti", 5.984400e-04)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=43.6303)
surf2 = openmc.Sphere(surface_id=2, r=43.8203, boundary_type="vacuum")
surf3 = openmc.ZPlane(surface_id=3, z0=28.0537)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf3

# SST
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2

root_universe = openmc.Universe(cells=[cell1, cell2])
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
source.space = openmc.stats.Box((-1.0, -1.0, -9.0), (1.0, 1.0, 1.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
