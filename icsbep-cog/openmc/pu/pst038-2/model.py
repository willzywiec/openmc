"""
PU-SOL-THERM-038-2: Experiment 3000
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Plutonium
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 9.819300e-08)
mat1.add_nuclide("Pu239", 3.890200e-05)
mat1.add_nuclide("Pu240", 1.046500e-05)
mat1.add_nuclide("Pu241", 5.496800e-07)
mat1.add_nuclide("Pu242", 5.495900e-07)
mat1.add_nuclide("H1", 6.475200e-02)
mat1.add_nuclide("O16", 3.457600e-02)
mat1.add_element("N", 8.394500e-04)
mat1.add_nuclide("Am241", 3.993700e-08)
mat1.add_element("B", 1.224400e-07)
mat1.add_element("Ba", 6.572200e-09)
mat1.add_element("Ca", 7.206300e-08)
mat1.add_element("Cr", 7.753200e-08)
mat1.add_element("Fe", 3.663200e-07)
mat1.add_element("Mg", 5.693900e-08)
mat1.add_element("Ni", 2.009400e-07)
mat1.add_element("Pb", 1.045400e-09)
mat1.add_nuclide("Th232", 5.186200e-09)
mat1.add_element("Zn", 3.220600e-08)
mat1.add_s_alpha_beta("c_H_in_H2O")

# Water
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 6.670700e-02)
mat2.add_nuclide("O16", 3.335300e-02)
mat2.add_s_alpha_beta("c_H_in_H2O")

# Air
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("N", 4.198500e-05)
mat3.add_nuclide("O16", 1.126300e-05)

# Z2 CND 17-12
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Cr", 1.565300e-02)
mat4.add_element("Ni", 9.788900e-03)
mat4.add_element("Mo", 1.122800e-03)
mat4.add_element("Mn", 8.714500e-04)
mat4.add_element("Si", 1.704600e-03)
mat4.add_element("P", 6.182700e-05)
mat4.add_element("S", 4.478600e-05)
mat4.add_element("C", 1.195800e-04)
mat4.add_element("Fe", 5.713700e-02)

# Z2 CND 18-10
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Cr", 1.647000e-02)
mat5.add_element("Ni", 8.106100e-03)
mat5.add_element("Mn", 8.659700e-04)
mat5.add_element("Si", 1.693900e-03)
mat5.add_element("P", 6.143900e-03)
mat5.add_element("S", 4.451200e-05)
mat5.add_element("C", 1.188300e-04)
mat5.add_element("Fe", 5.954600e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5])

# ==============================================================================
# Geometry
# ==============================================================================


# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = 

# Air
cell2 = openmc.Cell(cell_id=2, fill=mat3)
cell2.region = 

# SS1712
cell3 = openmc.Cell(cell_id=3, fill=mat4)
cell3.region = 

# SS1712
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = 

# Water
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = 

# Air
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = 

# SS1810
cell7 = openmc.Cell(cell_id=7, fill=mat5)
cell7.region = 

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7])
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
source.space = openmc.stats.Point((0.0, 0.0, 18.815))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
