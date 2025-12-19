"""
PMF027-1D: 0.985cm void; 9.864 kg delta-239Pu(89%); 5.58cm CH2 Reflector; detailed model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# d-Pu
mat11 = openmc.Material(material_id=11)
mat11.set_density("sum")
mat11.add_nuclide("Pu241", 3.652700e-04)
mat11.add_element("Ga", 2.210000e-03)
mat11.add_element("Ni", 2.093800e-03)
mat11.add_element("Fe", 3.941600e-04)
mat11.add_element("C", 7.636300e-04)

# d-Pu
mat12 = openmc.Material(material_id=12)
mat12.set_density("sum")
mat12.add_nuclide("Pu241", 3.904000e-04)
mat12.add_element("Ga", 2.124900e-03)
mat12.add_element("Ni", 8.677400e-04)
mat12.add_element("Fe", 4.171100e-04)
mat12.add_element("C", 8.533500e-04)

# d-Pu
mat13 = openmc.Material(material_id=13)
mat13.set_density("sum")
mat13.add_nuclide("Pu241", 3.222100e-04)
mat13.add_element("Ga", 2.228000e-03)
mat13.add_element("Ni", 1.344400e-03)
mat13.add_element("Fe", 4.801400e-04)
mat13.add_element("C", 9.238000e-04)

# d-Pu
mat14 = openmc.Material(material_id=14)
mat14.set_density("sum")
mat14.add_nuclide("Pu241", 4.350600e-04)
mat14.add_element("Ga", 2.295800e-03)
mat14.add_element("Ni", 1.778200e-03)
mat14.add_element("Fe", 4.282900e-04)
mat14.add_element("C", 8.425100e-04)

# d-Pu
mat15 = openmc.Material(material_id=15)
mat15.set_density("sum")
mat15.add_nuclide("Pu241", 4.050300e-04)
mat15.add_element("Ga", 2.259000e-03)
mat15.add_element("Ni", 1.518700e-03)
mat15.add_element("Fe", 4.783000e-04)
mat15.add_element("C", 9.969300e-04)

# CH2 inner
mat21 = openmc.Material(material_id=21)
mat21.set_density("sum")
mat21.add_element("C", 3.822200e-02)
mat21.add_nuclide("H1", 7.644300e-02)
mat21.add_s_alpha_beta("c_H_in_CH2")

# CH2 outer
mat22 = openmc.Material(material_id=22)
mat22.set_density("sum")
mat22.add_element("C", 3.864300e-02)
mat22.add_nuclide("H1", 7.728500e-02)
mat22.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat11, mat12, mat13, mat14, mat15, mat21, mat22])

# ==============================================================================
# Geometry
# ==============================================================================

surf1 = openmc.Sphere(surface_id=1, r=0.985)
surf2 = openmc.Sphere(surface_id=2, r=1.400)
surf3 = openmc.Sphere(surface_id=3, r=3.150)
surf4 = openmc.Sphere(surface_id=4, r=4.020)
surf5 = openmc.Sphere(surface_id=5, r=4.660)
surf6 = openmc.Sphere(surface_id=6, r=5.350)
surf7 = openmc.Sphere(surface_id=7, r=8.35)
surf8 = openmc.Sphere(surface_id=8, r=10.93, boundary_type="vacuum")

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# dPu
cell1 = openmc.Cell(cell_id=1, fill=mat11)
cell1.region = +surf1 & -surf2

# dPu
cell2 = openmc.Cell(cell_id=2, fill=mat12)
cell2.region = +surf2 & -surf3

# dPu
cell3 = openmc.Cell(cell_id=3, fill=mat13)
cell3.region = +surf3 & -surf4

# dPu
cell4 = openmc.Cell(cell_id=4, fill=mat14)
cell4.region = +surf4 & -surf5

# dPu
cell5 = openmc.Cell(cell_id=5, fill=mat15)
cell5.region = +surf5 & -surf6

# CH2
cell6 = openmc.Cell(cell_id=6, fill=mat21)
cell6.region = +surf6 & -surf7

# CH2
cell7 = openmc.Cell(cell_id=7, fill=mat22)
cell7.region = +surf7 & -surf8

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
source.space = openmc.stats.Box((-3.0, -3.0, -3.0), (3.0, 3.0, 3.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
