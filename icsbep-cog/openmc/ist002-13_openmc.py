"""
IEU-SOL-THERM-002-13: Unreflected 22-inch i.d. U(30.45) solution hemisphere
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Solution
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.332300e-04)
mat1.add_nuclide("U234", 1.669800e-06)
mat1.add_nuclide("U236", 3.485400e-07)
mat1.add_nuclide("U238", 2.984800e-04)
mat1.add_nuclide("H1", 6.520900e-02)
mat1.add_element("F", 8.674500e-04)
mat1.add_nuclide("O16", 3.347200e-02)
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

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=27.9377)
surf2 = openmc.Sphere(surface_id=2, r=28.2628, boundary_type="vacuum")
surf3 = openmc.ZPlane(surface_id=3, z0=0.0)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf3

# BA27
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
source.space = openmc.stats.Box((-1.0, -1.0, -8.0), (1.0, 1.0, -2.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
