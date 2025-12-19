"""
PU-SOL-THERM-024 (Case 9) 14.916 kg Pu(80.45) at H/X = 179 with H/SQRT(A) = 0.272; 18.40 wt-% Pu-240
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# 160.0 gPu/L
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 7.690500e-07)
mat1.add_nuclide("Pu239", 3.060100e-04)
mat1.add_nuclide("Pu240", 7.385500e-05)
mat1.add_nuclide("Pu241", 1.810700e-05)
mat1.add_nuclide("Pu242", 3.821400e-06)
mat1.add_nuclide("Am241", 1.119200e-06)
mat1.add_element("N", 3.444300e-03)
mat1.add_nuclide("O16", 3.845800e-02)
mat1.add_nuclide("H1", 5.808000e-02)
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

# Concrete per PUST026
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("P", 2.330000e+00)
mat3.add_nuclide("O16", 5.191000e+01)
mat3.add_element("Si", 2.310000e+01)
mat3.add_element("Ca", 1.200000e+01)
mat3.add_element("Al", 4.790000e+00)
mat3.add_element("Fe", 3.370000e+00)
mat3.add_element("Na", 1.430000e+00)
mat3.add_nuclide("H1", 1.050000e+00)
mat3.add_element("Mg", 9.200000e-01)
mat3.add_element("K", 7.200000e-01)
mat3.add_element("S", 3.800000e-01)
mat3.add_element("Ti", 3.300000e-01)
mat3.add_s_alpha_beta("c_H_in_H2O")

# Plexiglas
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 5.678200e-02)
mat4.add_element("C", 3.548900e-02)
mat4.add_nuclide("O16", 1.419600e-02)
mat4.add_s_alpha_beta("c_H_in_CH2")

materials = openmc.Materials([mat1, mat2, mat3, mat4])

# ==============================================================================
# Geometry
# ==============================================================================

# Hc
surf1 = openmc.ZPlane(surface_id=1, z0=45.8724)
# Tank/Inner:  Width = Tc
surf2 = openmc.model.RectangularParallelepiped(-337.509, -230.82899999999998, 139.345, 158.395, -192.929, -86.249)
# Tank/Outer:  Width = Tc +  0.318
surf3 = openmc.model.RectangularParallelepiped(-337.959, -230.379, 139.186, 158.554, -193.379, -85.799)
# Plex/Outer:  Width = Tc +  5.398
surf4 = openmc.model.RectangularParallelepiped(-337.959, -230.379, 136.64600000000002, 161.094, -193.379, -85.799)
# Frame/Outer: Width = Tc + 23.178
surf5 = openmc.model.RectangularParallelepiped(-337.959, -230.379, 127.756, 169.984, -193.379, -85.799)
# U-Frame/Inner
surf6 = openmc.model.RectangularParallelepiped(-355.289, -213.04899999999998, 111.87, 180.45, -211.344, -67.834)
# U-Frame/Outer
surf7 = openmc.model.RectangularParallelepiped(-355.765, -212.57299999999998, 111.87, 180.45, -211.82, -67.834)
# Hood/Inner
surf8 = openmc.model.RectangularParallelepiped(-380.365, -103.113, 76.83500000000001, 319.405, -311.78499999999997, 144.145)
# Hood/Outer
surf9 = openmc.model.RectangularParallelepiped(-381.0, -102.47800000000001, 76.2, 320.04, -312.41999999999996, 144.78)
# Room/Inner
surf10 = openmc.model.RectangularParallelepiped(-533.4, 533.4, -563.88, 502.91999999999996, -312.42, 312.42)
# Room/Outer
surf11 = openmc.model.RectangularParallelepiped(-685.8, 685.8, -655.32, 655.32, -373.38, 373.38, boundary_type="vacuum")
# Square Holes
surf12 = openmc.model.RectangularParallelepiped(-5.14125, 5.14125, -500.0, 500.0, -5.14125, 5.14125)
# surf101: Unsupported surface type "sameas" with params ['12', 'tr', '-331.869', '0.0', '-187.289', '102', 'sameas', '12', 'tr', '-321.269', '0.0', '-187.289']
# surf103: Unsupported surface type "sameas" with params ['12', 'tr', '-310.669', '0.0', '-187.289', '104', 'sameas', '12', 'tr', '-300.069', '0.0', '-187.289']
# surf105: Unsupported surface type "sameas" with params ['12', 'tr', '-289.469', '0.0', '-187.289', '106', 'sameas', '12', 'tr', '-278.869', '0.0', '-187.289']
# surf107: Unsupported surface type "sameas" with params ['12', 'tr', '-268.269', '0.0', '-187.289', '108', 'sameas', '12', 'tr', '-257.669', '0.0', '-187.289']
# surf109: Unsupported surface type "sameas" with params ['12', 'tr', '-247.069', '0.0', '-187.289', '110', 'sameas', '12', 'tr', '-236.469', '0.0', '-187.289']
# surf111: Unsupported surface type "sameas" with params ['12', 'tr', '-331.869', '0.0', '-176.689', '112', 'sameas', '12', 'tr', '-321.269', '0.0', '-176.689']
# surf113: Unsupported surface type "sameas" with params ['12', 'tr', '-310.669', '0.0', '-176.689', '114', 'sameas', '12', 'tr', '-300.069', '0.0', '-176.689']
# surf115: Unsupported surface type "sameas" with params ['12', 'tr', '-289.469', '0.0', '-176.689', '116', 'sameas', '12', 'tr', '-278.869', '0.0', '-176.689']
# surf117: Unsupported surface type "sameas" with params ['12', 'tr', '-268.269', '0.0', '-176.689', '118', 'sameas', '12', 'tr', '-257.669', '0.0', '-176.689']
# surf119: Unsupported surface type "sameas" with params ['12', 'tr', '-247.069', '0.0', '-176.689', '120', 'sameas', '12', 'tr', '-236.469', '0.0', '-176.689']
# surf121: Unsupported surface type "sameas" with params ['12', 'tr', '-331.869', '0.0', '-166.089', '122', 'sameas', '12', 'tr', '-321.269', '0.0', '-166.089']
# surf123: Unsupported surface type "sameas" with params ['12', 'tr', '-310.669', '0.0', '-166.089', '124', 'sameas', '12', 'tr', '-300.069', '0.0', '-166.089']
# surf125: Unsupported surface type "sameas" with params ['12', 'tr', '-289.469', '0.0', '-166.089', '126', 'sameas', '12', 'tr', '-278.869', '0.0', '-166.089']
# surf127: Unsupported surface type "sameas" with params ['12', 'tr', '-268.269', '0.0', '-166.089', '128', 'sameas', '12', 'tr', '-257.669', '0.0', '-166.089']
# surf129: Unsupported surface type "sameas" with params ['12', 'tr', '-247.069', '0.0', '-166.089', '130', 'sameas', '12', 'tr', '-236.469', '0.0', '-166.089']
# surf131: Unsupported surface type "sameas" with params ['12', 'tr', '-331.869', '0.0', '-155.489', '132', 'sameas', '12', 'tr', '-321.269', '0.0', '-155.489']
# surf133: Unsupported surface type "sameas" with params ['12', 'tr', '-310.669', '0.0', '-155.489', '134', 'sameas', '12', 'tr', '-300.069', '0.0', '-155.489']
# surf135: Unsupported surface type "sameas" with params ['12', 'tr', '-289.469', '0.0', '-155.489', '136', 'sameas', '12', 'tr', '-278.869', '0.0', '-155.489']
# surf137: Unsupported surface type "sameas" with params ['12', 'tr', '-268.269', '0.0', '-155.489', '138', 'sameas', '12', 'tr', '-257.669', '0.0', '-155.489']
# surf139: Unsupported surface type "sameas" with params ['12', 'tr', '-247.069', '0.0', '-155.489', '140', 'sameas', '12', 'tr', '-236.469', '0.0', '-155.489']
# surf141: Unsupported surface type "sameas" with params ['12', 'tr', '-331.869', '0.0', '-144.889', '142', 'sameas', '12', 'tr', '-321.269', '0.0', '-144.889']
# surf143: Unsupported surface type "sameas" with params ['12', 'tr', '-310.669', '0.0', '-144.889', '144', 'sameas', '12', 'tr', '-300.069', '0.0', '-144.889']
# surf145: Unsupported surface type "sameas" with params ['12', 'tr', '-289.469', '0.0', '-144.889', '146', 'sameas', '12', 'tr', '-278.869', '0.0', '-144.889']
# surf147: Unsupported surface type "sameas" with params ['12', 'tr', '-268.269', '0.0', '-144.889', '148', 'sameas', '12', 'tr', '-257.669', '0.0', '-144.889']
# surf149: Unsupported surface type "sameas" with params ['12', 'tr', '-247.069', '0.0', '-144.889', '150', 'sameas', '12', 'tr', '-236.469', '0.0', '-144.889']
# surf151: Unsupported surface type "sameas" with params ['12', 'tr', '-331.869', '0.0', '-134.289', '152', 'sameas', '12', 'tr', '-321.269', '0.0', '-134.289']
# surf153: Unsupported surface type "sameas" with params ['12', 'tr', '-310.669', '0.0', '-134.289', '154', 'sameas', '12', 'tr', '-300.069', '0.0', '-134.289']
# surf155: Unsupported surface type "sameas" with params ['12', 'tr', '-289.469', '0.0', '-134.289', '156', 'sameas', '12', 'tr', '-278.869', '0.0', '-134.289']
# surf157: Unsupported surface type "sameas" with params ['12', 'tr', '-268.269', '0.0', '-134.289', '158', 'sameas', '12', 'tr', '-257.669', '0.0', '-134.289']
# surf159: Unsupported surface type "sameas" with params ['12', 'tr', '-247.069', '0.0', '-134.289', '160', 'sameas', '12', 'tr', '-236.469', '0.0', '-134.289']
# surf161: Unsupported surface type "sameas" with params ['12', 'tr', '-331.869', '0.0', '-123.689', '162', 'sameas', '12', 'tr', '-321.269', '0.0', '-123.689']
# surf163: Unsupported surface type "sameas" with params ['12', 'tr', '-310.669', '0.0', '-123.689', '164', 'sameas', '12', 'tr', '-300.069', '0.0', '-123.689']
# surf165: Unsupported surface type "sameas" with params ['12', 'tr', '-289.469', '0.0', '-123.689', '166', 'sameas', '12', 'tr', '-278.869', '0.0', '-123.689']
# surf167: Unsupported surface type "sameas" with params ['12', 'tr', '-268.269', '0.0', '-123.689', '168', 'sameas', '12', 'tr', '-257.669', '0.0', '-123.689']
# surf169: Unsupported surface type "sameas" with params ['12', 'tr', '-247.069', '0.0', '-123.689', '170', 'sameas', '12', 'tr', '-236.469', '0.0', '-123.689']
# surf171: Unsupported surface type "sameas" with params ['12', 'tr', '-331.869', '0.0', '-113.089', '172', 'sameas', '12', 'tr', '-321.269', '0.0', '-113.089']
# surf173: Unsupported surface type "sameas" with params ['12', 'tr', '-310.669', '0.0', '-113.089', '174', 'sameas', '12', 'tr', '-300.069', '0.0', '-113.089']
# surf175: Unsupported surface type "sameas" with params ['12', 'tr', '-289.469', '0.0', '-113.089', '176', 'sameas', '12', 'tr', '-278.869', '0.0', '-113.089']
# surf177: Unsupported surface type "sameas" with params ['12', 'tr', '-268.269', '0.0', '-113.089', '178', 'sameas', '12', 'tr', '-257.669', '0.0', '-113.089']
# surf179: Unsupported surface type "sameas" with params ['12', 'tr', '-247.069', '0.0', '-113.089', '180', 'sameas', '12', 'tr', '-236.469', '0.0', '-113.089']
# surf181: Unsupported surface type "sameas" with params ['12', 'tr', '-331.869', '0.0', '-102.489', '182', 'sameas', '12', 'tr', '-321.269', '0.0', '-102.489']
# surf183: Unsupported surface type "sameas" with params ['12', 'tr', '-310.669', '0.0', '-102.489', '184', 'sameas', '12', 'tr', '-300.069', '0.0', '-102.489']
# surf185: Unsupported surface type "sameas" with params ['12', 'tr', '-289.469', '0.0', '-102.489', '186', 'sameas', '12', 'tr', '-278.869', '0.0', '-102.489']
# surf187: Unsupported surface type "sameas" with params ['12', 'tr', '-268.269', '0.0', '-102.489', '188', 'sameas', '12', 'tr', '-257.669', '0.0', '-102.489']
# surf189: Unsupported surface type "sameas" with params ['12', 'tr', '-247.069', '0.0', '-102.489', '190', 'sameas', '12', 'tr', '-236.469', '0.0', '-102.489']
# surf191: Unsupported surface type "sameas" with params ['12', 'tr', '-331.869', '0.0', '-91.889', '192', 'sameas', '12', 'tr', '-321.269', '0.0', '-91.889']
# surf193: Unsupported surface type "sameas" with params ['12', 'tr', '-310.669', '0.0', '-91.889', '194', 'sameas', '12', 'tr', '-300.069', '0.0', '-91.889']
# surf195: Unsupported surface type "sameas" with params ['12', 'tr', '-289.469', '0.0', '-91.889', '196', 'sameas', '12', 'tr', '-278.869', '0.0', '-91.889']
# surf197: Unsupported surface type "sameas" with params ['12', 'tr', '-268.269', '0.0', '-91.889', '198', 'sameas', '12', 'tr', '-257.669', '0.0', '-91.889']
# surf199: Unsupported surface type "sameas" with params ['12', 'tr', '-247.069', '0.0', '-91.889', '200', 'sameas', '12', 'tr', '-236.469', '0.0', '-91.889']

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# Soln
cell1 = openmc.Cell(cell_id=1, fill=mat1)
cell1.region = -surf1 & -surf2

# Tank
cell2 = openmc.Cell(cell_id=2, fill=mat2)
cell2.region = +surf2 & -surf3 & -surf5

# Crate
cell3 = openmc.Cell(cell_id=3, fill=mat2)
cell3.region = +surf3 & -surf5 & +surf101 & +surf103 & +surf105 & +surf107 & +surf109

# Plex
cell4 = openmc.Cell(cell_id=4, fill=mat4)
cell4.region = +surf3 & -surf4 & -surf101 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf103

# Plex
cell5 = openmc.Cell(cell_id=5, fill=mat4)
cell5.region = +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf105 & +surf4 & +surf3 & -surf4

# Plex
cell6 = openmc.Cell(cell_id=6, fill=mat4)
cell6.region = +surf3 & -surf4 & -surf107 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf109

# Plex
cell7 = openmc.Cell(cell_id=7, fill=mat4)
cell7.region = +surf3 & -surf4

# Plex
cell8 = openmc.Cell(cell_id=8, fill=mat4)
cell8.region = +surf3 & -surf4 & -surf111 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf113

# Plex
cell9 = openmc.Cell(cell_id=9, fill=mat4)
cell9.region = +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf115 & +surf4 & +surf3 & -surf4

# Plex
cell10 = openmc.Cell(cell_id=10, fill=mat4)
cell10.region = +surf3 & -surf4 & -surf117 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf119

# Plex
cell11 = openmc.Cell(cell_id=11, fill=mat4)
cell11.region = +surf3 & -surf4

# Plex
cell12 = openmc.Cell(cell_id=12, fill=mat4)
cell12.region = +surf3 & -surf4 & -surf121 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf123

# Plex
cell13 = openmc.Cell(cell_id=13, fill=mat4)
cell13.region = +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf125 & +surf4 & +surf3 & -surf4

# Plex
cell14 = openmc.Cell(cell_id=14, fill=mat4)
cell14.region = +surf3 & -surf4 & -surf127 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf129

# Plex
cell15 = openmc.Cell(cell_id=15, fill=mat4)
cell15.region = +surf3 & -surf4

# Plex
cell16 = openmc.Cell(cell_id=16, fill=mat4)
cell16.region = +surf3 & -surf4 & -surf131 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf133

# Plex
cell17 = openmc.Cell(cell_id=17, fill=mat4)
cell17.region = +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf135 & +surf4 & +surf3 & -surf4

# Plex
cell18 = openmc.Cell(cell_id=18, fill=mat4)
cell18.region = +surf3 & -surf4 & -surf137 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf139

# Plex
cell19 = openmc.Cell(cell_id=19, fill=mat4)
cell19.region = +surf3 & -surf4

# Plex
cell20 = openmc.Cell(cell_id=20, fill=mat4)
cell20.region = +surf3 & -surf4 & -surf141 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf143

# Plex
cell21 = openmc.Cell(cell_id=21, fill=mat4)
cell21.region = +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf145 & +surf4 & +surf3 & -surf4

# Plex
cell22 = openmc.Cell(cell_id=22, fill=mat4)
cell22.region = +surf3 & -surf4 & -surf147 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf149

# Plex
cell23 = openmc.Cell(cell_id=23, fill=mat4)
cell23.region = +surf3 & -surf4

# Plex
cell24 = openmc.Cell(cell_id=24, fill=mat4)
cell24.region = +surf3 & -surf4 & -surf151 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf153

# Plex
cell25 = openmc.Cell(cell_id=25, fill=mat4)
cell25.region = +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf155 & +surf4 & +surf3 & -surf4

# Plex
cell26 = openmc.Cell(cell_id=26, fill=mat4)
cell26.region = +surf3 & -surf4 & -surf157 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf159

# Plex
cell27 = openmc.Cell(cell_id=27, fill=mat4)
cell27.region = +surf3 & -surf4

# Plex
cell28 = openmc.Cell(cell_id=28, fill=mat4)
cell28.region = +surf3 & -surf4 & -surf161 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf163

# Plex
cell29 = openmc.Cell(cell_id=29, fill=mat4)
cell29.region = +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf165 & +surf4 & +surf3 & -surf4

# Plex
cell30 = openmc.Cell(cell_id=30, fill=mat4)
cell30.region = +surf3 & -surf4 & -surf167 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf169

# Plex
cell31 = openmc.Cell(cell_id=31, fill=mat4)
cell31.region = +surf3 & -surf4

# Plex
cell32 = openmc.Cell(cell_id=32, fill=mat4)
cell32.region = +surf3 & -surf4 & -surf171 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf173

# Plex
cell33 = openmc.Cell(cell_id=33, fill=mat4)
cell33.region = +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf175 & +surf4 & +surf3 & -surf4

# Plex
cell34 = openmc.Cell(cell_id=34, fill=mat4)
cell34.region = +surf3 & -surf4 & -surf177 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf179

# Plex
cell35 = openmc.Cell(cell_id=35, fill=mat4)
cell35.region = +surf3 & -surf4

# Plex
cell36 = openmc.Cell(cell_id=36, fill=mat4)
cell36.region = +surf3 & -surf4 & -surf181 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf183

# Plex
cell37 = openmc.Cell(cell_id=37, fill=mat4)
cell37.region = +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf185 & +surf4 & +surf3 & -surf4

# Plex
cell38 = openmc.Cell(cell_id=38, fill=mat4)
cell38.region = +surf3 & -surf4 & -surf187 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf189

# Plex
cell39 = openmc.Cell(cell_id=39, fill=mat4)
cell39.region = +surf3 & -surf4

# Plex
cell40 = openmc.Cell(cell_id=40, fill=mat4)
cell40.region = +surf3 & -surf4 & -surf191 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf193

# Plex
cell41 = openmc.Cell(cell_id=41, fill=mat4)
cell41.region = +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf195 & +surf4 & +surf3 & -surf4

# Plex
cell42 = openmc.Cell(cell_id=42, fill=mat4)
cell42.region = +surf3 & -surf4 & -surf197 & +surf4 & +surf3 & -surf4 & +surf4 & +surf3 & -surf4 & -surf199

# Plex
cell43 = openmc.Cell(cell_id=43, fill=mat4)
cell43.region = +surf3 & -surf4

# Frame
cell44 = openmc.Cell(cell_id=44, fill=mat2)
cell44.region = +surf6 & -surf7

# Hood
cell45 = openmc.Cell(cell_id=45, fill=mat2)
cell45.region = +surf8 & -surf9

# Room
cell46 = openmc.Cell(cell_id=46, fill=mat3)
cell46.region = +surf10 & -surf11

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6, cell7, cell8, cell9, cell10, cell11, cell12, cell13, cell14, cell15, cell16, cell17, cell18, cell19, cell20, cell21, cell22, cell23, cell24, cell25, cell26, cell27, cell28, cell29, cell30, cell31, cell32, cell33, cell34, cell35, cell36, cell37, cell38, cell39, cell40, cell41, cell42, cell43, cell44, cell45, cell46])
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
source.space = openmc.stats.Point((-284.0, 149.0, -170.0))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
