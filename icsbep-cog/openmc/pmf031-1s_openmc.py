"""
PMF031-1S: 1.165cm cavity; 7.8734 kg alpha-239Pu(88%); 3.69cm Polyethylene reflected; simplified model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# a-Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu241", 6.697400e-04)
mat1.add_element("Fe", 2.859400e-04)
mat1.add_element("C", 1.250800e-03)
mat1.add_element("H", 3.176400e-04)
mat1.add_element("N", 3.428500e-05)
mat1.add_nuclide("O16", 5.082600e-05)

# Polyethylene (CH2)
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("C", 3.863400e-02)
mat2.add_nuclide("H1", 7.726700e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.Sphere(surface_id=1, r=1.165)
surf2 = openmc.Sphere(surface_id=2, r=4.66)
surf3 = openmc.Sphere(surface_id=3, r=8.35, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# aPu
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = +surf1 & -surf2

# CH2
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3

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
source.space = openmc.stats.Box((-3.0, -3.0, -3.0), (3.0, 3.0, 3.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
