"""
LCT033-22: U(3)F4-2, Polyethylene reflected on top and sides; Plexiglas on bottom
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# U(3)F4-2
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U235", 1.670500e-04)
mat1.add_nuclide("U238", 5.332000e-03)
mat1.add_nuclide("U234", 1.118400e-06)
mat1.add_nuclide("H1", 4.630800e-02)
mat1.add_element("C", 2.226300e-02)
mat1.add_element("F", 2.200100e-02)
mat1.add_s_alpha_beta("c_H_in_CH2")

# Plexiglas
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 5.212600e-02)
mat2.add_element("C", 3.257900e-02)
mat2.add_nuclide("O16", 1.303200e-02)
mat2.add_s_alpha_beta("c_H_in_CH2")

# Polyethylene
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 7.899600e-02)
mat3.add_element("C", 3.949800e-02)
mat3.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

surf1 = openmc.model.RectangularParallelepiped(-20.405, 20.405, -20.4, 20.4, -19.745, 19.745)
surf2 = openmc.model.RectangularParallelepiped(-35.605, 35.605, -35.6, 35.6, -34.945, 34.945, boundary_type="vacuum")
surf3 = openmc.ZPlane(surface_id=3, z0=-19.335)

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# UF4+
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# Plex
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf1 & -surf2 & -surf3

# Poly
cell3 = openmc.Cell(cell_id=3, fill=mat3)
cell3.region = +surf1 & -surf2 & +surf3

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
