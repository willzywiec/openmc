"""
PU-MET-FAST-006: 6.060 kg Pu(4.80)-1.l0Ga @ 15.53 g/cc in 19.6088 cm Nat-U @ 19.0 g/cc
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu239", 3.669700e-02)
mat1.add_nuclide("Pu240", 1.870000e-03)
mat1.add_nuclide("Pu241", 1.163900e-04)
mat1.add_element("Ga", 1.475500e-03)

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("U234", 2.643800e-06)
mat2.add_nuclide("U235", 3.461000e-04)
mat2.add_nuclide("U238", 4.772100e-02)

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# per Section 3.2
surf1 = openmc.Sphere(surface_id=1, r=4.5332)
# THK = 19.6088 cm
surf2 = openmc.Sphere(surface_id=2, r=24.1420, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# core
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# refl
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
