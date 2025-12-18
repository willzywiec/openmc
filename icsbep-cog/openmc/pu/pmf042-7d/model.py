"""
PMF042-7D: Pu hemisphere reflected by 6x0.3228cm steel shells and infinite oil; detailed model
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Pu
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("Pu238", 4.908500e-06)
mat1.add_nuclide("Pu239", 4.574100e-02)
mat1.add_nuclide("Pu240", 2.871800e-03)
mat1.add_nuclide("Pu241", 2.375200e-04)
mat1.add_nuclide("Pu242", 9.654400e-06)

# Grease, oil & air
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_nuclide("H1", 3.988400e-02)
mat2.add_nuclide("Li6", 1.459700e-05)
mat2.add_nuclide("Li6", 1.543500e-04)
mat2.add_element("C", 2.056200e-02)
mat2.add_element("N", 1.068400e-05)
mat2.add_nuclide("O16", 2.100500e-03)
mat2.add_element("Si", 1.813200e-03)
mat2.add_element("Ar", 6.390000e-08)
mat2.add_s_alpha_beta("c_H_in_H2O")

# Steel
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("C", 6.708000e-04)
mat3.add_element("P", 3.118300e-05)
mat3.add_element("S", 3.694600e-05)
mat3.add_element("Mn", 6.470100e-04)
mat3.add_element("Fe", 8.404500e-02)

# Oil & air between steel shells
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_nuclide("H1", 3.398100e-02)
mat4.add_element("C", 1.939000e-02)
mat4.add_element("N", 1.602600e-05)
mat4.add_nuclide("O16", 4.401700e-06)
mat4.add_element("Ar", 9.585000e-08)
mat4.add_s_alpha_beta("c_H_in_H2O")

# Oil
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_nuclide("H1", 6.796200e-02)
mat5.add_element("C", 3.878100e-02)
mat5.add_s_alpha_beta("c_H_in_H2O")

# Air
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_nuclide("H1", 4.104900e-07)
mat6.add_element("N", 3.205300e-05)
mat6.add_nuclide("O16", 8.803400e-06)
mat6.add_element("Ar", 1.917000e-07)
mat6.add_s_alpha_beta("c_H_in_H2O")

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Hemi
surf1 = openmc.XPlane(surface_id=1, x0=-2.37375)
# Hc
surf2 = openmc.ZPlane(surface_id=2, z0=0.47)
# BCD
surf3 = openmc.ZCylinder(surface_id=3, x0=-31.333, y0=18.667, r=25.0, boundary_type="vacuum")
# Pu1
# surf11: Unsupported surface type "s" with params ['2.0000', 'tr', '-2.37375', '0', '-6.333']
# Pu2
# surf12: Unsupported surface type "s" with params ['2.0100', 'tr', '-2.37375', '0', '-6.333']
# Pu2
# surf13: Unsupported surface type "s" with params ['2.1542', 'tr', '-2.37375', '0', '-6.333']
# Pu3
# surf14: Unsupported surface type "s" with params ['2.1764', 'tr', '-2.37375', '0', '-6.333']
# Pu3
# surf15: Unsupported surface type "s" with params ['2.3206', 'tr', '-2.37375', '0', '-6.333']
# Pu4
# surf16: Unsupported surface type "s" with params ['2.3428', 'tr', '-2.37375', '0', '-6.333']
# Pu4
# surf17: Unsupported surface type "s" with params ['2.4870', 'tr', '-2.37375', '0', '-6.333']
# Pu5
# surf18: Unsupported surface type "s" with params ['2.5092', 'tr', '-2.37375', '0', '-6.333']
# Pu5
# surf19: Unsupported surface type "s" with params ['2.6534', 'tr', '-2.37375', '0', '-6.333']
# Pu6
# surf20: Unsupported surface type "s" with params ['2.6756', 'tr', '-2.37375', '0', '-6.333']
# Pu6
# surf21: Unsupported surface type "s" with params ['2.8198', 'tr', '-2.37375', '0', '-6.333']
# Pu7
# surf22: Unsupported surface type "s" with params ['2.8420', 'tr', '-2.37375', '0', '-6.333']
# Pu7
# surf23: Unsupported surface type "s" with params ['2.9862', 'tr', '-2.37375', '0', '-6.333']
# Pu8
# surf24: Unsupported surface type "s" with params ['3.0084', 'tr', '-2.37375', '0', '-6.333']
# Pu8
# surf25: Unsupported surface type "s" with params ['3.1526', 'tr', '-2.37375', '0', '-6.333']
# Pu9
# surf26: Unsupported surface type "s" with params ['3.1748', 'tr', '-2.37375', '0', '-6.333']
# Pu9
# surf27: Unsupported surface type "s" with params ['3.3190', 'tr', '-2.37375', '0', '-6.333']
# Pu10
# surf28: Unsupported surface type "s" with params ['3.3412', 'tr', '-2.37375', '0', '-6.333']
# Pu10
# surf29: Unsupported surface type "s" with params ['3.4854', 'tr', '-2.37375', '0', '-6.333']
# Pu11
# surf30: Unsupported surface type "s" with params ['3.5076', 'tr', '-2.37375', '0', '-6.333']
# Pu11
# surf31: Unsupported surface type "s" with params ['3.6518', 'tr', '-2.37375', '0', '-6.333']
# Pu12
# surf32: Unsupported surface type "s" with params ['3.6740', 'tr', '-2.37375', '0', '-6.333']
# Pu12
# surf33: Unsupported surface type "s" with params ['3.8182', 'tr', '-2.37375', '0', '-6.333']
# Pu13
# surf34: Unsupported surface type "s" with params ['3.8404', 'tr', '-2.37375', '0', '-6.333']
# Pu13
# surf35: Unsupported surface type "s" with params ['3.9846', 'tr', '-2.37375', '0', '-6.333']
# Pu14
# surf36: Unsupported surface type "s" with params ['4.0068', 'tr', '-2.37375', '0', '-6.333']
# Pu14
# surf37: Unsupported surface type "s" with params ['4.1510', 'tr', '-2.37375', '0', '-6.333']
# Pu15
# surf38: Unsupported surface type "s" with params ['4.1732', 'tr', '-2.37375', '0', '-6.333']
# Pu15
# surf39: Unsupported surface type "s" with params ['4.3174', 'tr', '-2.37375', '0', '-6.333']
# Pu16
# surf40: Unsupported surface type "s" with params ['4.3396', 'tr', '-2.37375', '0', '-6.333']
# Pu16
# surf41: Unsupported surface type "s" with params ['4.4838', 'tr', '-2.37375', '0', '-6.333']
# Pu17
# surf42: Unsupported surface type "s" with params ['4.5060', 'tr', '-2.37375', '0', '-6.333']
# Pu17
# surf43: Unsupported surface type "s" with params ['4.6502', 'tr', '-2.37375', '0', '-6.333']
# Pu18
# surf44: Unsupported surface type "s" with params ['4.6724', 'tr', '-2.37375', '0', '-6.333']
# Pu18
# surf45: Unsupported surface type "s" with params ['4.8166', 'tr', '-2.37375', '0', '-6.333']
# Pu19
# surf46: Unsupported surface type "s" with params ['4.8388', 'tr', '-2.37375', '0', '-6.333']
# Pu19
# surf47: Unsupported surface type "s" with params ['4.9830', 'tr', '-2.37375', '0', '-6.333']
# Pu20
# surf48: Unsupported surface type "s" with params ['5.0052', 'tr', '-2.37375', '0', '-6.333']
# Pu20
# surf49: Unsupported surface type "s" with params ['5.1494', 'tr', '-2.37375', '0', '-6.333']
# Pu21
# surf50: Unsupported surface type "s" with params ['5.1716', 'tr', '-2.37375', '0', '-6.333']
# Pu21
# surf51: Unsupported surface type "s" with params ['5.3158', 'tr', '-2.37375', '0', '-6.333']
# Pu22
# surf52: Unsupported surface type "s" with params ['5.3380', 'tr', '-2.37375', '0', '-6.333']
# Pu22
# surf53: Unsupported surface type "s" with params ['5.4822', 'tr', '-2.37375', '0', '-6.333']
# Pu23
# surf54: Unsupported surface type "s" with params ['5.5044', 'tr', '-2.37375', '0', '-6.333']
# Pu23
# surf55: Unsupported surface type "s" with params ['5.6486', 'tr', '-2.37375', '0', '-6.333']
# Pu24
# surf56: Unsupported surface type "s" with params ['5.6708', 'tr', '-2.37375', '0', '-6.333']
# Pu24
# surf57: Unsupported surface type "s" with params ['5.8150', 'tr', '-2.37375', '0', '-6.333']
# Pu25
# surf58: Unsupported surface type "s" with params ['5.8372', 'tr', '-2.37375', '0', '-6.333']
# Pu25
# surf59: Unsupported surface type "s" with params ['5.9814', 'tr', '-2.37375', '0', '-6.333']
# Pu26
# surf60: Unsupported surface type "s" with params ['6.0036', 'tr', '-2.37375', '0', '-6.333']
# Pu26
# surf61: Unsupported surface type "s" with params ['6.1478', 'tr', '-2.37375', '0', '-6.333']
# Pu27
# surf62: Unsupported surface type "s" with params ['6.1700', 'tr', '-2.37375', '0', '-6.333']
# Pu27
# surf63: Unsupported surface type "s" with params ['6.3142', 'tr', '-2.37375', '0', '-6.333']
# S1
# surf64: Unsupported surface type "s" with params ['6.3386', 'tr', '-2.37375', '0', '-6.333']
# S1
# surf65: Unsupported surface type "s" with params ['6.6614', 'tr', '-2.37375', '0', '-6.333']
# S2
# surf66: Unsupported surface type "s" with params ['6.6720', 'tr', '-2.37375', '0', '-6.333']
# S2
# surf67: Unsupported surface type "s" with params ['6.9947', 'tr', '-2.37375', '0', '-6.333']
# S3
# surf68: Unsupported surface type "s" with params ['7.0053', 'tr', '-2.37375', '0', '-6.333']
# S3
# surf69: Unsupported surface type "s" with params ['7.3280', 'tr', '-2.37375', '0', '-6.333']
# S4
# surf70: Unsupported surface type "s" with params ['7.3386', 'tr', '-2.37375', '0', '-6.333']
# S4
# surf71: Unsupported surface type "s" with params ['7.6614', 'tr', '-2.37375', '0', '-6.333']
# S5
# surf72: Unsupported surface type "s" with params ['7.6720', 'tr', '-2.37375', '0', '-6.333']
# S5
# surf73: Unsupported surface type "s" with params ['7.9947', 'tr', '-2.37375', '0', '-6.333']
# S6
# surf74: Unsupported surface type "s" with params ['8.0053', 'tr', '-2.37375', '0', '-6.333']
# S6
# surf75: Unsupported surface type "s" with params ['8.3280', 'tr', '-2.37375', '0', '-6.333']

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

u1_cell0 = openmc.Cell(fill=mat1)
u1_cell0.region = +surf1 & -surf11
u1_cell1 = openmc.Cell(fill=mat1)
u1_cell1.region = +surf1 & +surf12 & -surf13
u1_cell2 = openmc.Cell(fill=mat1)
u1_cell2.region = +surf1 & +surf14 & -surf15
u1_cell3 = openmc.Cell(fill=mat1)
u1_cell3.region = +surf1 & +surf16 & -surf17
u1_cell4 = openmc.Cell(fill=mat1)
u1_cell4.region = +surf1 & +surf18 & -surf19
u1_cell5 = openmc.Cell(fill=mat1)
u1_cell5.region = +surf1 & +surf20 & -surf21
u1_cell6 = openmc.Cell(fill=mat1)
u1_cell6.region = +surf1 & +surf22 & -surf23
u1_cell7 = openmc.Cell(fill=mat1)
u1_cell7.region = +surf1 & +surf24 & -surf25
u1_cell8 = openmc.Cell(fill=mat1)
u1_cell8.region = +surf1 & +surf26 & -surf27
u1_cell9 = openmc.Cell(fill=mat1)
u1_cell9.region = +surf1 & +surf28 & -surf29
u1_cell10 = openmc.Cell(fill=mat1)
u1_cell10.region = +surf1 & +surf30 & -surf31
u1_cell11 = openmc.Cell(fill=mat1)
u1_cell11.region = +surf1 & +surf32 & -surf33
u1_cell12 = openmc.Cell(fill=mat1)
u1_cell12.region = +surf1 & +surf34 & -surf35
u1_cell13 = openmc.Cell(fill=mat1)
u1_cell13.region = +surf1 & +surf36 & -surf37
u1_cell14 = openmc.Cell(fill=mat1)
u1_cell14.region = +surf1 & +surf38 & -surf39
u1_cell15 = openmc.Cell(fill=mat1)
u1_cell15.region = +surf1 & +surf40 & -surf41
u1_cell16 = openmc.Cell(fill=mat1)
u1_cell16.region = +surf1 & +surf42 & -surf43
u1_cell17 = openmc.Cell(fill=mat1)
u1_cell17.region = +surf1 & +surf44 & -surf45
u1_cell18 = openmc.Cell(fill=mat1)
u1_cell18.region = +surf1 & +surf46 & -surf47
u1_cell19 = openmc.Cell(fill=mat1)
u1_cell19.region = +surf1 & +surf48 & -surf49
u1_cell20 = openmc.Cell(fill=mat1)
u1_cell20.region = +surf1 & +surf50 & -surf51
u1_cell21 = openmc.Cell(fill=mat1)
u1_cell21.region = +surf1 & +surf52 & -surf53
u1_cell22 = openmc.Cell(fill=mat1)
u1_cell22.region = +surf1 & +surf54 & -surf55
u1_cell23 = openmc.Cell(fill=mat1)
u1_cell23.region = +surf1 & +surf56 & -surf57
u1_cell24 = openmc.Cell(fill=mat1)
u1_cell24.region = +surf1 & +surf58 & -surf59
u1_cell25 = openmc.Cell(fill=mat1)
u1_cell25.region = +surf1 & +surf60 & -surf61
u1_cell26 = openmc.Cell(fill=mat1)
u1_cell26.region = +surf1 & +surf62 & -surf63
universe1 = openmc.Universe(universe_id=1, cells=[u1_cell0, u1_cell1, u1_cell2, u1_cell3, u1_cell4, u1_cell5, u1_cell6, u1_cell7, u1_cell8, u1_cell9, u1_cell10, u1_cell11, u1_cell12, u1_cell13, u1_cell14, u1_cell15, u1_cell16, u1_cell17, u1_cell18, u1_cell19, u1_cell20, u1_cell21, u1_cell22, u1_cell23, u1_cell24, u1_cell25, u1_cell26])

u2_cell0 = openmc.Cell(fill=mat3)
u2_cell0.region = +surf1 & +surf64 & -surf65
u2_cell1 = openmc.Cell(fill=mat3)
u2_cell1.region = +surf1 & +surf66 & -surf67
u2_cell2 = openmc.Cell(fill=mat3)
u2_cell2.region = +surf1 & +surf68 & -surf69
u2_cell3 = openmc.Cell(fill=mat3)
u2_cell3.region = +surf1 & +surf70 & -surf71
u2_cell4 = openmc.Cell(fill=mat3)
u2_cell4.region = +surf1 & +surf72 & -surf73
u2_cell5 = openmc.Cell(fill=mat3)
u2_cell5.region = +surf1 & +surf74 & -surf75
universe2 = openmc.Universe(universe_id=2, cells=[u2_cell0, u2_cell1, u2_cell2, u2_cell3, u2_cell4, u2_cell5])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# pshls
cell1 = openmc.Cell(cell_id=1, fill=universe1)
cell1.region = +surf1 & -surf64

# sshls
cell2 = openmc.Cell(cell_id=2, fill=universe2)
cell2.region = +surf1 & +surf64 & -surf75

# Oil
cell3 = openmc.Cell(cell_id=3, fill=mat5)
cell3.region = +surf1 & -surf2 & -surf3 & +surf75

# Oil
cell4 = openmc.Cell(cell_id=4, fill=mat5)
cell4.region = -surf1 & -surf2 & -surf3

# Air
cell5 = openmc.Cell(cell_id=5, fill=mat6)
cell5.region = -surf1 & +surf2 & -surf3

# Air
cell6 = openmc.Cell(cell_id=6, fill=mat6)
cell6.region = +surf1 & +surf2 & -surf3 & +surf75

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
source.space = openmc.stats.Point((0.0, 0.0, -6.333))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
