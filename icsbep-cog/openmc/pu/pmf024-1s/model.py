"""
PMF024-1S: 1.550cm polyethylene reflected spherical assembly of 13.815 kg delta-239Pu(98%): simplified model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.662000e-02)
mat1.add_nuclide("Pu240", 6.694400e-04)
mat1.add_element("Ga", 2.196200e-03)
mat1.add_element("Fe", 1.412600e-04)
mat1.add_element("C", 2.897200e-04)
mat1.add_element("Ni", 1.974800e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 3.881400e-02)
mat2.add_nuclide("H1", 7.762800e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=6.000)
surf2 = openmc.Sphere(surface_id=2, r=7.550, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# dPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# CH2
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
source.space = openmc.stats.Point((0.0, 0.0, 0.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
