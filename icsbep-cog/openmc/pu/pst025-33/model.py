"""
PU-SOL-THERM-025 (Case 33) 19.738 kg Pu(80.45) at H/X = 109 with H/SQRT(A) = 0.256; 18.4 wt-% Pu-240
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 240.8 gPu/L
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 1.157400e-06)
mat1.add_nuclide("Pu239", 4.605400e-04)
mat1.add_nuclide("Pu240", 1.111500e-04)
mat1.add_nuclide("Pu241", 2.725100e-05)
mat1.add_nuclide("Pu242", 5.751200e-06)
mat1.add_nuclide("Am241", 1.684400e-06)
mat1.add_nuclide("H1", 5.314400e-02)
mat1.add_element("N", 4.921600e-03)
mat1.add_nuclide("O16", 4.009000e-02)
mat1.add_s_alpha_beta("c_H_in_H2O")

# SS-304L
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("P", 8.020000e+00)
mat2.add_element("Fe", 6.944800e+01)
mat2.add_element("Cr", 1.900000e+01)
mat2.add_element("Ni", 1.000000e+01)
mat2.add_element("Mn", 1.000000e+00)
mat2.add_element("C", 1.500000e-02)
mat2.add_element("Si", 5.000000e-01)
mat2.add_element("S", 1.500000e-02)
mat2.add_element("P", 2.200000e-02)

# Water
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_nuclide("H1", 6.669100e-02)
mat3.add_nuclide("O16", 3.334500e-02)
mat3.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Hc (Solution)
surf1 = openmc.ZPlane(surface_id=1, z0=43.840)
# Sol'n Tank/Inner: Width = Tc
surf2 = openmc.model.RectangularParallelepiped(-53.34, 53.34, -6.053, 11.472999999999999, 0.0, 106.68)
# Sol'n Tank/Outer: Width = Tc +  0.318
surf3 = openmc.model.RectangularParallelepiped(-53.656, 53.656, -6.212000000000001, 11.632000000000001, -0.3159999999999954, 106.99600000000001)
# Egg Crate /Outer: Width = Tc + 23.178
surf4 = openmc.model.RectangularParallelepiped(-53.656, 53.656, -17.642, 23.062, -0.3159999999999954, 106.99600000000001)
# Water Reflector Level
surf5 = openmc.ZPlane(surface_id=5, z0=106.680)
# Water Tank/Inner
surf6 = openmc.model.RectangularParallelepiped(-71.12, 71.12, -34.29, 34.29, -18.414999999999992, 125.095)
# Water Tank/Outer
surf7 = openmc.model.RectangularParallelepiped(-71.596, 71.596, -34.925, 34.925, -18.891, 125.095, boundary_type="vacuum")
# Square Holes
surf8 = openmc.model.RectangularParallelepiped(-5.14125, 5.14125, -500.0, 500.0, -5.14125, 5.14125)
# surf101: Unsupported surface type "sameas" with params ['8', 'tr', '-47.7', '0.0', '5.64', '102', 'sameas', '8', 'tr', '-37.1', '0.0', '5.64']
# surf103: Unsupported surface type "sameas" with params ['8', 'tr', '-26.5', '0.0', '5.64', '104', 'sameas', '8', 'tr', '-15.9', '0.0', '5.64']
# surf105: Unsupported surface type "sameas" with params ['8', 'tr', '-5.3', '0.0', '5.64', '106', 'sameas', '8', 'tr', '5.3', '0.0', '5.64']
# surf107: Unsupported surface type "sameas" with params ['8', 'tr', '15.9', '0.0', '5.64', '108', 'sameas', '8', 'tr', '26.5', '0.0', '5.64']
# surf109: Unsupported surface type "sameas" with params ['8', 'tr', '37.1', '0.0', '5.64', '110', 'sameas', '8', 'tr', '47.7', '0.0', '5.64']
# surf111: Unsupported surface type "sameas" with params ['8', 'tr', '-47.7', '0.0', '16.24', '112', 'sameas', '8', 'tr', '-37.1', '0.0', '16.24']
# surf113: Unsupported surface type "sameas" with params ['8', 'tr', '-26.5', '0.0', '16.24', '114', 'sameas', '8', 'tr', '-15.9', '0.0', '16.24']
# surf115: Unsupported surface type "sameas" with params ['8', 'tr', '-5.3', '0.0', '16.24', '116', 'sameas', '8', 'tr', '5.3', '0.0', '16.24']
# surf117: Unsupported surface type "sameas" with params ['8', 'tr', '15.9', '0.0', '16.24', '118', 'sameas', '8', 'tr', '26.5', '0.0', '16.24']
# surf119: Unsupported surface type "sameas" with params ['8', 'tr', '37.1', '0.0', '16.24', '120', 'sameas', '8', 'tr', '47.7', '0.0', '16.24']
# surf121: Unsupported surface type "sameas" with params ['8', 'tr', '-47.7', '0.0', '26.84', '122', 'sameas', '8', 'tr', '-37.1', '0.0', '26.84']
# surf123: Unsupported surface type "sameas" with params ['8', 'tr', '-26.5', '0.0', '26.84', '124', 'sameas', '8', 'tr', '-15.9', '0.0', '26.84']
# surf125: Unsupported surface type "sameas" with params ['8', 'tr', '-5.3', '0.0', '26.84', '126', 'sameas', '8', 'tr', '5.3', '0.0', '26.84']
# surf127: Unsupported surface type "sameas" with params ['8', 'tr', '15.9', '0.0', '26.84', '128', 'sameas', '8', 'tr', '26.5', '0.0', '26.84']
# surf129: Unsupported surface type "sameas" with params ['8', 'tr', '37.1', '0.0', '26.84', '130', 'sameas', '8', 'tr', '47.7', '0.0', '26.84']
# surf131: Unsupported surface type "sameas" with params ['8', 'tr', '-47.7', '0.0', '37.44', '132', 'sameas', '8', 'tr', '-37.1', '0.0', '37.44']
# surf133: Unsupported surface type "sameas" with params ['8', 'tr', '-26.5', '0.0', '37.44', '134', 'sameas', '8', 'tr', '-15.9', '0.0', '37.44']
# surf135: Unsupported surface type "sameas" with params ['8', 'tr', '-5.3', '0.0', '37.44', '136', 'sameas', '8', 'tr', '5.3', '0.0', '37.44']
# surf137: Unsupported surface type "sameas" with params ['8', 'tr', '15.9', '0.0', '37.44', '138', 'sameas', '8', 'tr', '26.5', '0.0', '37.44']
# surf139: Unsupported surface type "sameas" with params ['8', 'tr', '37.1', '0.0', '37.44', '140', 'sameas', '8', 'tr', '47.7', '0.0', '37.44']
# surf141: Unsupported surface type "sameas" with params ['8', 'tr', '-47.7', '0.0', '48.04', '142', 'sameas', '8', 'tr', '-37.1', '0.0', '48.04']
# surf143: Unsupported surface type "sameas" with params ['8', 'tr', '-26.5', '0.0', '48.04', '144', 'sameas', '8', 'tr', '-15.9', '0.0', '48.04']
# surf145: Unsupported surface type "sameas" with params ['8', 'tr', '-5.3', '0.0', '48.04', '146', 'sameas', '8', 'tr', '5.3', '0.0', '48.04']
# surf147: Unsupported surface type "sameas" with params ['8', 'tr', '15.9', '0.0', '48.04', '148', 'sameas', '8', 'tr', '26.5', '0.0', '48.04']
# surf149: Unsupported surface type "sameas" with params ['8', 'tr', '37.1', '0.0', '48.04', '150', 'sameas', '8', 'tr', '47.7', '0.0', '48.04']
# surf151: Unsupported surface type "sameas" with params ['8', 'tr', '-47.7', '0.0', '58.64', '152', 'sameas', '8', 'tr', '-37.1', '0.0', '58.64']
# surf153: Unsupported surface type "sameas" with params ['8', 'tr', '-26.5', '0.0', '58.64', '154', 'sameas', '8', 'tr', '-15.9', '0.0', '58.64']
# surf155: Unsupported surface type "sameas" with params ['8', 'tr', '-5.3', '0.0', '58.64', '156', 'sameas', '8', 'tr', '5.3', '0.0', '58.64']
# surf157: Unsupported surface type "sameas" with params ['8', 'tr', '15.9', '0.0', '58.64', '158', 'sameas', '8', 'tr', '26.5', '0.0', '58.64']
# surf159: Unsupported surface type "sameas" with params ['8', 'tr', '37.1', '0.0', '58.64', '160', 'sameas', '8', 'tr', '47.7', '0.0', '58.64']
# surf161: Unsupported surface type "sameas" with params ['8', 'tr', '-47.7', '0.0', '69.24', '162', 'sameas', '8', 'tr', '-37.1', '0.0', '69.24']
# surf163: Unsupported surface type "sameas" with params ['8', 'tr', '-26.5', '0.0', '69.24', '164', 'sameas', '8', 'tr', '-15.9', '0.0', '69.24']
# surf165: Unsupported surface type "sameas" with params ['8', 'tr', '-5.3', '0.0', '69.24', '166', 'sameas', '8', 'tr', '5.3', '0.0', '69.24']
# surf167: Unsupported surface type "sameas" with params ['8', 'tr', '15.9', '0.0', '69.24', '168', 'sameas', '8', 'tr', '26.5', '0.0', '69.24']
# surf169: Unsupported surface type "sameas" with params ['8', 'tr', '37.1', '0.0', '69.24', '170', 'sameas', '8', 'tr', '47.7', '0.0', '69.24']
# surf171: Unsupported surface type "sameas" with params ['8', 'tr', '-47.7', '0.0', '79.84', '172', 'sameas', '8', 'tr', '-37.1', '0.0', '79.84']
# surf173: Unsupported surface type "sameas" with params ['8', 'tr', '-26.5', '0.0', '79.84', '174', 'sameas', '8', 'tr', '-15.9', '0.0', '79.84']
# surf175: Unsupported surface type "sameas" with params ['8', 'tr', '-5.3', '0.0', '79.84', '176', 'sameas', '8', 'tr', '5.3', '0.0', '79.84']
# surf177: Unsupported surface type "sameas" with params ['8', 'tr', '15.9', '0.0', '79.84', '178', 'sameas', '8', 'tr', '26.5', '0.0', '79.84']
# surf179: Unsupported surface type "sameas" with params ['8', 'tr', '37.1', '0.0', '79.84', '180', 'sameas', '8', 'tr', '47.7', '0.0', '79.84']
# surf181: Unsupported surface type "sameas" with params ['8', 'tr', '-47.7', '0.0', '90.44', '182', 'sameas', '8', 'tr', '-37.1', '0.0', '90.44']
# surf183: Unsupported surface type "sameas" with params ['8', 'tr', '-26.5', '0.0', '90.44', '184', 'sameas', '8', 'tr', '-15.9', '0.0', '90.44']
# surf185: Unsupported surface type "sameas" with params ['8', 'tr', '-5.3', '0.0', '90.44', '186', 'sameas', '8', 'tr', '5.3', '0.0', '90.44']
# surf187: Unsupported surface type "sameas" with params ['8', 'tr', '15.9', '0.0', '90.44', '188', 'sameas', '8', 'tr', '26.5', '0.0', '90.44']
# surf189: Unsupported surface type "sameas" with params ['8', 'tr', '37.1', '0.0', '90.44', '190', 'sameas', '8', 'tr', '47.7', '0.0', '90.44']
# surf191: Unsupported surface type "sameas" with params ['8', 'tr', '-47.7', '0.0', '101.04', '192', 'sameas', '8', 'tr', '-37.1', '0.0', '101.04']
# surf193: Unsupported surface type "sameas" with params ['8', 'tr', '-26.5', '0.0', '101.04', '194', 'sameas', '8', 'tr', '-15.9', '0.0', '101.04']
# surf195: Unsupported surface type "sameas" with params ['8', 'tr', '-5.3', '0.0', '101.04', '196', 'sameas', '8', 'tr', '5.3', '0.0', '101.04']
# surf197: Unsupported surface type "sameas" with params ['8', 'tr', '15.9', '0.0', '101.04', '198', 'sameas', '8', 'tr', '26.5', '0.0', '101.04']
# surf199: Unsupported surface type "sameas" with params ['8', 'tr', '37.1', '0.0', '101.04', '200', 'sameas', '8', 'tr', '47.7', '0.0', '101.04']

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# Tank
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3 & -surf4

# Crate
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf3 & -surf4 & +surf101 & +surf103 & +surf105 & +surf107 & +surf109

# Water
cell4 = openmc.Cell(cell_id=4, fill=mat3)
cell4.region = +surf3 & -surf4 & -surf101 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf103

# Water
cell5 = openmc.Cell(cell_id=5, fill=mat3)
cell5.region = +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf105 & +surf3 & +surf3 & -surf4

# Water
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf3 & -surf4 & -surf107 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf109

# Water
cell7 = openmc.Cell(cell_id=7, fill=mat3)
cell7.region = +surf3 & -surf4

# Water
cell8 = openmc.Cell(cell_id=8, fill=mat3)
cell8.region = +surf3 & -surf4 & -surf111 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf113

# Water
cell9 = openmc.Cell(cell_id=9, fill=mat3)
cell9.region = +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf115 & +surf3 & +surf3 & -surf4

# Water
cell10 = openmc.Cell(cell_id=10, fill=mat3)
cell10.region = +surf3 & -surf4 & -surf117 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf119

# Water
cell11 = openmc.Cell(cell_id=11, fill=mat3)
cell11.region = +surf3 & -surf4

# Water
cell12 = openmc.Cell(cell_id=12, fill=mat3)
cell12.region = +surf3 & -surf4 & -surf121 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf123

# Water
cell13 = openmc.Cell(cell_id=13, fill=mat3)
cell13.region = +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf125 & +surf3 & +surf3 & -surf4

# Water
cell14 = openmc.Cell(cell_id=14, fill=mat3)
cell14.region = +surf3 & -surf4 & -surf127 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf129

# Water
cell15 = openmc.Cell(cell_id=15, fill=mat3)
cell15.region = +surf3 & -surf4

# Water
cell16 = openmc.Cell(cell_id=16, fill=mat3)
cell16.region = +surf3 & -surf4 & -surf131 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf133

# Water
cell17 = openmc.Cell(cell_id=17, fill=mat3)
cell17.region = +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf135 & +surf3 & +surf3 & -surf4

# Water
cell18 = openmc.Cell(cell_id=18, fill=mat3)
cell18.region = +surf3 & -surf4 & -surf137 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf139

# Water
cell19 = openmc.Cell(cell_id=19, fill=mat3)
cell19.region = +surf3 & -surf4

# Water
cell20 = openmc.Cell(cell_id=20, fill=mat3)
cell20.region = +surf3 & -surf4 & -surf141 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf143

# Water
cell21 = openmc.Cell(cell_id=21, fill=mat3)
cell21.region = +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf145 & +surf3 & +surf3 & -surf4

# Water
cell22 = openmc.Cell(cell_id=22, fill=mat3)
cell22.region = +surf3 & -surf4 & -surf147 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf149

# Water
cell23 = openmc.Cell(cell_id=23, fill=mat3)
cell23.region = +surf3 & -surf4

# Water
cell24 = openmc.Cell(cell_id=24, fill=mat3)
cell24.region = +surf3 & -surf4 & -surf151 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf153

# Water
cell25 = openmc.Cell(cell_id=25, fill=mat3)
cell25.region = +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf155 & +surf3 & +surf3 & -surf4

# Water
cell26 = openmc.Cell(cell_id=26, fill=mat3)
cell26.region = +surf3 & -surf4 & -surf157 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf159

# Water
cell27 = openmc.Cell(cell_id=27, fill=mat3)
cell27.region = +surf3 & -surf4

# Water
cell28 = openmc.Cell(cell_id=28, fill=mat3)
cell28.region = +surf3 & -surf4 & -surf161 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf163

# Water
cell29 = openmc.Cell(cell_id=29, fill=mat3)
cell29.region = +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf165 & +surf3 & +surf3 & -surf4

# Water
cell30 = openmc.Cell(cell_id=30, fill=mat3)
cell30.region = +surf3 & -surf4 & -surf167 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf169

# Water
cell31 = openmc.Cell(cell_id=31, fill=mat3)
cell31.region = +surf3 & -surf4

# Water
cell32 = openmc.Cell(cell_id=32, fill=mat3)
cell32.region = +surf3 & -surf4 & -surf171 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf173

# Water
cell33 = openmc.Cell(cell_id=33, fill=mat3)
cell33.region = +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf175 & +surf3 & +surf3 & -surf4

# Water
cell34 = openmc.Cell(cell_id=34, fill=mat3)
cell34.region = +surf3 & -surf4 & -surf177 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf179

# Water
cell35 = openmc.Cell(cell_id=35, fill=mat3)
cell35.region = +surf3 & -surf4

# Water
cell36 = openmc.Cell(cell_id=36, fill=mat3)
cell36.region = +surf3 & -surf4 & -surf181 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf183

# Water
cell37 = openmc.Cell(cell_id=37, fill=mat3)
cell37.region = +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf185 & +surf3 & +surf3 & -surf4

# Water
cell38 = openmc.Cell(cell_id=38, fill=mat3)
cell38.region = +surf3 & -surf4 & -surf187 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf189

# Water
cell39 = openmc.Cell(cell_id=39, fill=mat3)
cell39.region = +surf3 & -surf4

# Water
cell40 = openmc.Cell(cell_id=40, fill=mat3)
cell40.region = +surf3 & -surf4 & -surf191 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf193

# Water
cell41 = openmc.Cell(cell_id=41, fill=mat3)
cell41.region = +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf195 & +surf3 & +surf3 & -surf4

# Water
cell42 = openmc.Cell(cell_id=42, fill=mat3)
cell42.region = +surf3 & -surf4 & -surf197 & +surf3 & +surf3 & -surf4 & +surf3 & +surf3 & -surf4 & -surf199

# Water
cell43 = openmc.Cell(cell_id=43, fill=mat3)
cell43.region = +surf3 & -surf4

# Water
cell44 = openmc.Cell(cell_id=44, fill=mat3)
cell44.region = +surf3 & +surf4 & -surf5 & -surf6

# Tank
cell45 = openmc.Cell(cell_id=45, fill=mat2)
cell45.region = +surf6 & -surf7

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45])
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
source.space = openmc.stats.Point((0.0, 2.71, 21.9))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
