"""
PU-COMP-MIXED-001 (Case 1) 114.574 kg Pu @ H/X = 0.05 with 18.35 wt-% Pu-240
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 3.380700e-05)
mat1.add_nuclide("Pu239", 1.091900e-02)
mat1.add_nuclide("Pu240", 2.652900e-03)
mat1.add_nuclide("Pu241", 7.265700e-04)
mat1.add_nuclide("Pu242", 1.631200e-04)
mat1.add_nuclide("H1", 5.506600e-04)
mat1.add_nuclide("O16", 3.088800e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("P", 2.330000e+00)
mat2.add_nuclide("O16", 5.191000e+01)
mat2.add_element("Si", 2.310000e+01)
mat2.add_element("Ca", 1.200000e+01)
mat2.add_element("Al", 4.790000e+00)
mat2.add_element("Na", 1.430000e+00)
mat2.add_element("Fe", 3.370000e+00)
mat2.add_nuclide("H1", 1.050000e+00)
mat2.add_element("Mg", 9.200000e-01)
mat2.add_element("K", 7.200000e-01)
mat2.add_element("S", 3.800000e-01)
mat2.add_element("Ti", 3.300000e-01)
mat2.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# FUEL
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1

# VOID
cell2 = openmc.Cell(cell_id=2)
cell2.region = +surf1 & -surf2

# CONC
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf2 & -surf3

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
source.space = openmc.stats.Point((241.42, 228.28, -213.025))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
