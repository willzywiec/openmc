"""
PU-SOL-THERM-026 (Case 20) 36.582 kg Pu(81.6) at H/X = 109 with H/SQRT(A) = 0.275
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

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

materials = openmc.Materials([mat1, mat2, mat3])

# ==============================================================================
# Geometry
# ==============================================================================

# Hc
surf1 = openmc.ZPlane(surface_id=1, z0=63.170)
# Tank/Inner:  Width = Tc
surf2 = openmc.model.RectangularParallelepiped(-337.509, -230.82899999999998, 137.5985, 160.1415, -192.929, -86.249)
# Tank/Outer:  Width = Tc +  0.318
surf3 = openmc.model.RectangularParallelepiped(-337.959, -230.379, 137.4395, 160.3005, -193.379, -85.799)
# Frame/Outer: Width = Tc + 23.178
surf4 = openmc.model.RectangularParallelepiped(-337.959, -230.379, 126.0095, 171.7305, -193.379, -85.799)
# U-Frame/Inner
surf5 = openmc.model.RectangularParallelepiped(-355.289, -213.04899999999998, 111.87, 180.45, -211.344, -67.834)
# U-Frame/Outer
surf6 = openmc.model.RectangularParallelepiped(-355.765, -212.57299999999998, 111.87, 180.45, -211.82, -67.834)
# Hood/Inner
surf7 = openmc.model.RectangularParallelepiped(-380.365, -103.113, 76.83500000000001, 319.405, -311.78499999999997, 144.145)
# Hood/Outer
surf8 = openmc.model.RectangularParallelepiped(-381.0, -102.47800000000001, 76.2, 320.04, -312.41999999999996, 144.78)
# Room/Inner
surf9 = openmc.model.RectangularParallelepiped(-533.4, 533.4, -563.88, 502.91999999999996, -312.42, 312.42)
# Room/Outer
surf10 = openmc.model.RectangularParallelepiped(-685.8, 685.8, -655.32, 655.32, -373.38, 373.38, boundary_type="vacuum")
# Square Holes
surf11 = openmc.model.RectangularParallelepiped(-5.14125, 5.14125, -500.0, 500.0, -5.14125, 5.14125)
# surf101: Unsupported surface type "sameas" with params ['11', 'tr', '-331.869', '0.0', '-187.289', '102', 'sameas', '11', 'tr', '-321.269', '0.0', '-187.289']
# surf103: Unsupported surface type "sameas" with params ['11', 'tr', '-310.669', '0.0', '-187.289', '104', 'sameas', '11', 'tr', '-300.069', '0.0', '-187.289']
# surf105: Unsupported surface type "sameas" with params ['11', 'tr', '-289.469', '0.0', '-187.289', '106', 'sameas', '11', 'tr', '-278.869', '0.0', '-187.289']
# surf107: Unsupported surface type "sameas" with params ['11', 'tr', '-268.269', '0.0', '-187.289', '108', 'sameas', '11', 'tr', '-257.669', '0.0', '-187.289']
# surf109: Unsupported surface type "sameas" with params ['11', 'tr', '-247.069', '0.0', '-187.289', '110', 'sameas', '11', 'tr', '-236.469', '0.0', '-187.289']
# surf111: Unsupported surface type "sameas" with params ['11', 'tr', '-331.869', '0.0', '-176.689', '112', 'sameas', '11', 'tr', '-321.269', '0.0', '-176.689']
# surf113: Unsupported surface type "sameas" with params ['11', 'tr', '-310.669', '0.0', '-176.689', '114', 'sameas', '11', 'tr', '-300.069', '0.0', '-176.689']
# surf115: Unsupported surface type "sameas" with params ['11', 'tr', '-289.469', '0.0', '-176.689', '116', 'sameas', '11', 'tr', '-278.869', '0.0', '-176.689']
# surf117: Unsupported surface type "sameas" with params ['11', 'tr', '-268.269', '0.0', '-176.689', '118', 'sameas', '11', 'tr', '-257.669', '0.0', '-176.689']
# surf119: Unsupported surface type "sameas" with params ['11', 'tr', '-247.069', '0.0', '-176.689', '120', 'sameas', '11', 'tr', '-236.469', '0.0', '-176.689']
# surf121: Unsupported surface type "sameas" with params ['11', 'tr', '-331.869', '0.0', '-166.089', '122', 'sameas', '11', 'tr', '-321.269', '0.0', '-166.089']
# surf123: Unsupported surface type "sameas" with params ['11', 'tr', '-310.669', '0.0', '-166.089', '124', 'sameas', '11', 'tr', '-300.069', '0.0', '-166.089']
# surf125: Unsupported surface type "sameas" with params ['11', 'tr', '-289.469', '0.0', '-166.089', '126', 'sameas', '11', 'tr', '-278.869', '0.0', '-166.089']
# surf127: Unsupported surface type "sameas" with params ['11', 'tr', '-268.269', '0.0', '-166.089', '128', 'sameas', '11', 'tr', '-257.669', '0.0', '-166.089']
# surf129: Unsupported surface type "sameas" with params ['11', 'tr', '-247.069', '0.0', '-166.089', '130', 'sameas', '11', 'tr', '-236.469', '0.0', '-166.089']
# surf131: Unsupported surface type "sameas" with params ['11', 'tr', '-331.869', '0.0', '-155.489', '132', 'sameas', '11', 'tr', '-321.269', '0.0', '-155.489']
# surf133: Unsupported surface type "sameas" with params ['11', 'tr', '-310.669', '0.0', '-155.489', '134', 'sameas', '11', 'tr', '-300.069', '0.0', '-155.489']
# surf135: Unsupported surface type "sameas" with params ['11', 'tr', '-289.469', '0.0', '-155.489', '136', 'sameas', '11', 'tr', '-278.869', '0.0', '-155.489']
# surf137: Unsupported surface type "sameas" with params ['11', 'tr', '-268.269', '0.0', '-155.489', '138', 'sameas', '11', 'tr', '-257.669', '0.0', '-155.489']
# surf139: Unsupported surface type "sameas" with params ['11', 'tr', '-247.069', '0.0', '-155.489', '140', 'sameas', '11', 'tr', '-236.469', '0.0', '-155.489']
# surf141: Unsupported surface type "sameas" with params ['11', 'tr', '-331.869', '0.0', '-144.889', '142', 'sameas', '11', 'tr', '-321.269', '0.0', '-144.889']
# surf143: Unsupported surface type "sameas" with params ['11', 'tr', '-310.669', '0.0', '-144.889', '144', 'sameas', '11', 'tr', '-300.069', '0.0', '-144.889']
# surf145: Unsupported surface type "sameas" with params ['11', 'tr', '-289.469', '0.0', '-144.889', '146', 'sameas', '11', 'tr', '-278.869', '0.0', '-144.889']
# surf147: Unsupported surface type "sameas" with params ['11', 'tr', '-268.269', '0.0', '-144.889', '148', 'sameas', '11', 'tr', '-257.669', '0.0', '-144.889']
# surf149: Unsupported surface type "sameas" with params ['11', 'tr', '-247.069', '0.0', '-144.889', '150', 'sameas', '11', 'tr', '-236.469', '0.0', '-144.889']
# surf151: Unsupported surface type "sameas" with params ['11', 'tr', '-331.869', '0.0', '-134.289', '152', 'sameas', '11', 'tr', '-321.269', '0.0', '-134.289']
# surf153: Unsupported surface type "sameas" with params ['11', 'tr', '-310.669', '0.0', '-134.289', '154', 'sameas', '11', 'tr', '-300.069', '0.0', '-134.289']
# surf155: Unsupported surface type "sameas" with params ['11', 'tr', '-289.469', '0.0', '-134.289', '156', 'sameas', '11', 'tr', '-278.869', '0.0', '-134.289']
# surf157: Unsupported surface type "sameas" with params ['11', 'tr', '-268.269', '0.0', '-134.289', '158', 'sameas', '11', 'tr', '-257.669', '0.0', '-134.289']
# surf159: Unsupported surface type "sameas" with params ['11', 'tr', '-247.069', '0.0', '-134.289', '160', 'sameas', '11', 'tr', '-236.469', '0.0', '-134.289']
# surf161: Unsupported surface type "sameas" with params ['11', 'tr', '-331.869', '0.0', '-123.689', '162', 'sameas', '11', 'tr', '-321.269', '0.0', '-123.689']
# surf163: Unsupported surface type "sameas" with params ['11', 'tr', '-310.669', '0.0', '-123.689', '164', 'sameas', '11', 'tr', '-300.069', '0.0', '-123.689']
# surf165: Unsupported surface type "sameas" with params ['11', 'tr', '-289.469', '0.0', '-123.689', '166', 'sameas', '11', 'tr', '-278.869', '0.0', '-123.689']
# surf167: Unsupported surface type "sameas" with params ['11', 'tr', '-268.269', '0.0', '-123.689', '168', 'sameas', '11', 'tr', '-257.669', '0.0', '-123.689']
# surf169: Unsupported surface type "sameas" with params ['11', 'tr', '-247.069', '0.0', '-123.689', '170', 'sameas', '11', 'tr', '-236.469', '0.0', '-123.689']
# surf171: Unsupported surface type "sameas" with params ['11', 'tr', '-331.869', '0.0', '-113.089', '172', 'sameas', '11', 'tr', '-321.269', '0.0', '-113.089']
# surf173: Unsupported surface type "sameas" with params ['11', 'tr', '-310.669', '0.0', '-113.089', '174', 'sameas', '11', 'tr', '-300.069', '0.0', '-113.089']
# surf175: Unsupported surface type "sameas" with params ['11', 'tr', '-289.469', '0.0', '-113.089', '176', 'sameas', '11', 'tr', '-278.869', '0.0', '-113.089']
# surf177: Unsupported surface type "sameas" with params ['11', 'tr', '-268.269', '0.0', '-113.089', '178', 'sameas', '11', 'tr', '-257.669', '0.0', '-113.089']
# surf179: Unsupported surface type "sameas" with params ['11', 'tr', '-247.069', '0.0', '-113.089', '180', 'sameas', '11', 'tr', '-236.469', '0.0', '-113.089']
# surf181: Unsupported surface type "sameas" with params ['11', 'tr', '-331.869', '0.0', '-102.489', '182', 'sameas', '11', 'tr', '-321.269', '0.0', '-102.489']
# surf183: Unsupported surface type "sameas" with params ['11', 'tr', '-310.669', '0.0', '-102.489', '184', 'sameas', '11', 'tr', '-300.069', '0.0', '-102.489']
# surf185: Unsupported surface type "sameas" with params ['11', 'tr', '-289.469', '0.0', '-102.489', '186', 'sameas', '11', 'tr', '-278.869', '0.0', '-102.489']
# surf187: Unsupported surface type "sameas" with params ['11', 'tr', '-268.269', '0.0', '-102.489', '188', 'sameas', '11', 'tr', '-257.669', '0.0', '-102.489']
# surf189: Unsupported surface type "sameas" with params ['11', 'tr', '-247.069', '0.0', '-102.489', '190', 'sameas', '11', 'tr', '-236.469', '0.0', '-102.489']
# surf191: Unsupported surface type "sameas" with params ['11', 'tr', '-331.869', '0.0', '-91.889', '192', 'sameas', '11', 'tr', '-321.269', '0.0', '-91.889']
# surf193: Unsupported surface type "sameas" with params ['11', 'tr', '-310.669', '0.0', '-91.889', '194', 'sameas', '11', 'tr', '-300.069', '0.0', '-91.889']
# surf195: Unsupported surface type "sameas" with params ['11', 'tr', '-289.469', '0.0', '-91.889', '196', 'sameas', '11', 'tr', '-278.869', '0.0', '-91.889']
# surf197: Unsupported surface type "sameas" with params ['11', 'tr', '-268.269', '0.0', '-91.889', '198', 'sameas', '11', 'tr', '-257.669', '0.0', '-91.889']
# surf199: Unsupported surface type "sameas" with params ['11', 'tr', '-247.069', '0.0', '-91.889', '200', 'sameas', '11', 'tr', '-236.469', '0.0', '-91.889']

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
cell3.region = +surf3 & -surf4

# Frame
cell4 = openmc.Cell(cell_id=4, fill=mat2)
cell4.region = +surf5 & -surf6

# Hood
cell5 = openmc.Cell(cell_id=5, fill=mat2)
cell5.region = +surf7 & -surf8

# Room
cell6 = openmc.Cell(cell_id=6, fill=mat3)
cell6.region = +surf9 & -surf10

root_universe = openmc.Universe(cells=[cell1, cell2, cell3, cell4, cell5, cell6])
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
source.space = openmc.stats.Point((-284.0, 149.0, -161.3))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
