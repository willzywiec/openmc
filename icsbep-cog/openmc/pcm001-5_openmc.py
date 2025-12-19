"""
PU-COMP-MIXED-001 (Case 5) 33.555 kg Pu @ H/X = 61.89 with 18.50 wt-% Pu-240
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 2.159500e-06)
mat1.add_nuclide("Pu239", 6.996300e-04)
mat1.add_nuclide("Pu240", 1.699800e-04)
mat1.add_nuclide("Pu241", 3.936500e-05)
mat1.add_nuclide("Pu242", 1.044500e-05)
mat1.add_nuclide("Am241", 7.271700e-06)
mat1.add_element("C", 4.502400e-02)
mat1.add_nuclide("H1", 4.573600e-02)
mat1.add_nuclide("O16", 2.094800e-03)
mat1.add_s_alpha_beta("c_H_in_CH2")

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

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Fuel/Outer (Zo = Hc/2 - 223.52)
surf1 = openmc.model.RectangularParallelepiped(221.065, 261.775, 205.375, 251.185, -223.52, -174.4)
# Room/Inner
surf2 = openmc.model.RectangularParallelepiped(-533.4, 533.4, -533.4, 533.4, -304.8, 304.8)
# Room/Outer
surf3 = openmc.model.RectangularParallelepiped(-685.8, 685.8, -624.84, 685.8000000000001, -365.76, 365.76, boundary_type="vacuum")

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
source.space = openmc.stats.Point((241.42, 228.28, -198.96))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
