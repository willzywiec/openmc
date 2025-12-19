"""
IEU-MET-FAST-020-9: FR0 experiment 1H-D (case 9 detailed model)
Converted from COG to OpenMC
"""

import openmc

# ==============================================================================
# Materials
# ==============================================================================

# Fuel and teflon
mat1 = openmc.Material(material_id=1)
mat1.set_density("sum")
mat1.add_nuclide("U234", 9.616200e-05)
mat1.add_nuclide("U235", 9.599100e-03)
mat1.add_nuclide("U238", 3.769900e-02)
mat1.add_element("C", 4.918000e-05)
mat1.add_element("F", 9.836200e-05)

# Copper blocks
mat2 = openmc.Material(material_id=2)
mat2.set_density("sum")
mat2.add_element("Cu", 8.417400e-02)
mat2.add_element("Ag", 7.950000e-05)
mat2.add_nuclide("O16", 1.340000e-04)

# Copper plates
mat3 = openmc.Material(material_id=3)
mat3.set_density("sum")
mat3.add_element("Cu", 8.339200e-02)
mat3.add_element("Ag", 7.876000e-05)
mat3.add_nuclide("O16", 1.327500e-04)

# SST frames & inner part end blocks
mat4 = openmc.Material(material_id=4)
mat4.set_density("sum")
mat4.add_element("Fe", 5.857800e-02)
mat4.add_element("Cr", 1.595100e-02)
mat4.add_element("Ni", 7.458200e-03)
mat4.add_element("Mn", 8.387000e-04)
mat4.add_element("Si", 8.202900e-04)

# SST outer part end blocks
mat5 = openmc.Material(material_id=5)
mat5.set_density("sum")
mat5.add_element("Fe", 4.761000e-02)
mat5.add_element("Cr", 1.296400e-02)
mat5.add_element("Ni", 6.061800e-03)
mat5.add_element("Mn", 6.816600e-04)
mat5.add_element("Si", 6.667000e-04)

# Steel (iron)
mat6 = openmc.Material(material_id=6)
mat6.set_density("sum")
mat6.add_element("Fe", 8.410900e-02)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6])

# ==============================================================================
# Geometry
# ==============================================================================

# Reset surface ID counter to avoid conflicts with composite surfaces
openmc.Surface.next_id = 10000

# Vertical structure, inner
surf20 = openmc.model.RectangularParallelepiped(-63.4, 63.4, -61, 59.4, -30.05, 96.25)
# Vertical structure, outer
surf21 = openmc.model.RectangularParallelepiped(-65, 65, -61, 61, -30.05, 96.25)
# Table top
surf22 = openmc.ZPlane(surface_id=22, z0=-30.05)
# BCD
surf23 = openmc.model.RectangularParallelepiped(-75, 75, -71, 71, -46.05, 96.25, boundary_type="vacuum")
surf10400 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf10401 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf10402 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf10403 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf10404 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf10405 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf10600 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -1.43333, 31.541)
surf10601 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf10602 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf10603 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf10604 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf10605 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf10606 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf10700 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -0.71667, 30.824)
surf10701 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf10702 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf10703 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf10704 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf10705 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf10706 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf10800 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, 0.71667, 29.390)
surf10801 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf10802 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf10803 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf10804 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf10805 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf10806 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf10900 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 1.5333, 8.60, 21.503)
surf10901 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 1.5333, 6.45, 23.654)
surf10902 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 2.25, 6.45, 23.654)
surf10903 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 2.25, 4.30, 25.805)
surf10904 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 3.6833, 4.30, 25.805)
surf10905 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 3.6833, 2.15, 27.956)
surf10906 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 4.40, 2.15, 27.956)
surf10907 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf10908 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf10909 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf10910 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf10911 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf10912 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf11000 = openmc.model.RectangularParallelepiped(0.1, 4.4, 2.9667, 4.4, 8.60, 21.503)
surf11001 = openmc.model.RectangularParallelepiped(0.1, 4.4, 2.9667, 4.4, 6.45, 23.654)
surf11002 = openmc.model.RectangularParallelepiped(0.1, 4.4, 2.25, 4.4, 6.45, 23.654)
surf11003 = openmc.model.RectangularParallelepiped(0.1, 4.4, 2.25, 4.4, 4.30, 25.805)
surf11004 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.8167, 4.4, 4.30, 25.805)
surf11005 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.8167, 4.4, 2.15, 27.956)
surf11006 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.10, 4.4, 2.15, 27.956)
surf11007 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf11008 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf11009 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf11010 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf11011 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf11012 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf11600 = openmc.model.RectangularParallelepiped(2.9667, 4.4, 0.1, 4.4, -1.43333, 31.541)
surf11601 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -1.43333, 31.541)
surf11602 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf11603 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf11604 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf11605 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf11606 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf11607 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf11700 = openmc.model.RectangularParallelepiped(2.9667, 4.4, 0.1, 4.4, -0.71667, 30.824)
surf11701 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -0.71667, 30.824)
surf11702 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf11703 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf11704 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf11705 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf11706 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf11707 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf11800 = openmc.model.RectangularParallelepiped(2.9667, 4.4, 0.1, 4.4, 0.71667, 29.39)
surf11801 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, 0.71667, 29.39)
surf11802 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf11803 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf11804 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf11805 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf11806 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf11807 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf11900 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 0.1, 1.53, 8.60, 21.503)
surf11901 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 0.1, 1.53, 6.45, 23.654)
surf11902 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 0.1, 2.25, 6.45, 23.654)
surf11903 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 0.1, 2.25, 4.30, 25.805)
surf11904 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 0.1, 3.69, 4.30, 25.805)
surf11905 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 0.1, 3.69, 2.15, 27.956)
surf11906 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 0.1, 4.40, 2.15, 27.956)
surf11907 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 4.40, 2.15, 27.956)
surf11908 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf11909 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf11910 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf11911 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf11912 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf11913 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf12000 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 2.9667, 4.4, 8.60, 21.503)
surf12001 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 2.9667, 4.4, 6.45, 23.654)
surf12002 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 2.25, 4.4, 6.45, 23.654)
surf12003 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 2.25, 4.4, 4.30, 25.805)
surf12004 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 0.8167, 4.4, 4.30, 25.805)
surf12005 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 0.8167, 4.4, 2.15, 27.956)
surf12006 = openmc.model.RectangularParallelepiped(2.9667, 4.40, 0.1, 4.4, 2.15, 27.956)
surf12007 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 4.4, 2.15, 27.956)
surf12008 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf12009 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf12010 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf12011 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf12012 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf12013 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf12100 = openmc.model.RectangularParallelepiped(0.1, 4.40, 3.6833, 4.4, 10.75, 19.352)
surf12101 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 4.4, 10.75, 19.352)
surf12102 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf12103 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf12104 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf12105 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf12106 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf12107 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf12200 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 0.8167, 10.749, 19.351)
surf12201 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 4.4, 10.749, 19.351)
surf12202 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf12203 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf12204 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf12205 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf12206 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf12207 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf12500 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 0.1, 4.4, -1.43333, 31.541)
surf12501 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 4.4, -1.43333, 31.541)
surf12502 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf12503 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf12504 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf12505 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf12506 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf12507 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf12600 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 0.1, 4.40, -0.71667, 30.824)
surf12601 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 4.40, -0.71667, 30.824)
surf12602 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf12603 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf12604 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf12605 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf12606 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf12607 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf12700 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 0.1, 4.4, 0.71667, 29.39)
surf12701 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 4.4, 0.71667, 29.39)
surf12702 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf12703 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf12704 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf12705 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf12706 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf12707 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf12800 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 2.9667, 4.4, 8.60, 21.503)
surf12801 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 2.9667, 4.4, 6.45, 23.654)
surf12802 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 2.25, 4.4, 6.45, 23.654)
surf12803 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 2.25, 4.4, 4.30, 25.805)
surf12804 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 0.8167, 4.4, 4.30, 25.805)
surf12805 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 0.8167, 4.4, 2.15, 27.956)
surf12806 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 0.10, 4.4, 2.15, 27.956)
surf12807 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.10, 4.4, 2.15, 27.956)
surf12808 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf12809 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf12810 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf12811 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf12812 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf12813 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf14100 = openmc.model.RectangularParallelepiped(0.1, 4.4, 3.6833, 4.4, 10.75, 19.352)
surf14101 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.10, 4.4, 10.75, 19.352)
surf14102 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf14103 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf14104 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf14105 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf14106 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf14107 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf14400 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 0.81, 10.75, 19.352)
surf14401 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.10, 4.4, 10.75, 19.352)
surf14402 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf14403 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf14404 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf14405 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf14406 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf14407 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf20300 = openmc.model.RectangularParallelepiped(4.0417, 4.4, 0.1, 4.4, -1.43333, 30.824)
surf20301 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -1.43333, 31.541)
surf20302 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf20303 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf20304 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf20305 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf20306 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf20307 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf20400 = openmc.model.RectangularParallelepiped(4.0417, 4.4, 0.1, 4.4, -0.71667, 29.39)
surf20401 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -0.71667, 30.824)
surf20402 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf20403 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf20404 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf20405 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf20406 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf20407 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf20500 = openmc.model.RectangularParallelepiped(4.0417, 4.4, 0.1, 4.4, 0.71667, 28.673)
surf20501 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, 0.71667, 29.39)
surf20502 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf20503 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf20504 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf20505 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf20506 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf20507 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf20600 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 1.5333, 8.60, 21.503)
surf20601 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 1.5333, 6.45, 23.645)
surf20602 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 2.25, 6.45, 23.645)
surf20603 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 2.25, 4.30, 25.805)
surf20604 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 3.6833, 4.30, 25.805)
surf20605 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 3.6833, 2.15, 27.956)
surf20606 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.40, 2.15, 27.956)
surf20607 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf20608 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf20609 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf20610 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf20611 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf20612 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf20700 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 2.9667, 4.4, 8.60, 21.503)
surf20701 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 2.9667, 4.4, 6.45, 23.645)
surf20702 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 2.25, 4.4, 6.45, 23.645)
surf20703 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 2.25, 4.4, 4.30, 25.805)
surf20704 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 0.8167, 4.4, 4.30, 25.805)
surf20705 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 0.8167, 4.4, 2.15, 27.956)
surf20706 = openmc.model.RectangularParallelepiped(0.1, 3.6833, 0.1, 4.4, 2.15, 27.956)
surf20707 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, 2.15, 27.956)
surf20708 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf20709 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf20710 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf20711 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf20712 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf20713 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf23700 = openmc.model.RectangularParallelepiped(0.1, 4.4, 3.6833, 4.4, 10.75, 19.352)
surf23701 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, 10.75, 19.352)
surf23702 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf23703 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf23704 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf23705 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf23706 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf23707 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf23800 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 0.8167, 10.75, 19.352)
surf23801 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, 10.75, 19.352)
surf23802 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf23803 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf23804 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf23805 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf23806 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf23807 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

# Lattice 1: 21x21 array
lattice1 = openmc.RectLattice(lattice_id=1)
lattice1.lower_left = [-47.985, -47.985]
lattice1.pitch = [4.570000, 4.570000]
lattice1.universes = [
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe121, universe121, universe121, universe121, universe121, universe121, universe121, universe237, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe109, universe109, universe109, universe109, universe109, universe109, universe109, universe206, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe108, universe108, universe108, universe108, universe108, universe108, universe108, universe205, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe107, universe107, universe107, universe107, universe107, universe107, universe107, universe204, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe106, universe106, universe106, universe106, universe106, universe106, universe106, universe203, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe107, universe107, universe107, universe107, universe107, universe107, universe107, universe204, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe108, universe108, universe108, universe108, universe108, universe108, universe108, universe205, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe110, universe110, universe110, universe110, universe110, universe110, universe110, universe207, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe122, universe122, universe122, universe122, universe122, universe122, universe122, universe238, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
]
universe1 = openmc.Universe(universe_id=1)
universe1.add_cell(openmc.Cell(fill=lattice1))

u104_cell0 = openmc.Cell(fill=mat2)
u104_cell0.region = -surf10400
u104_cell1 = openmc.Cell()
u104_cell1.region = +surf10400 & -surf10401
u104_cell2 = openmc.Cell(fill=mat4)
u104_cell2.region = +surf10400 & +surf10401 & -surf10402
u104_cell3 = openmc.Cell()
u104_cell3.region = +surf10400 & +surf10401 & +surf10402 & -surf10403
u104_cell4 = openmc.Cell(fill=mat5)
u104_cell4.region = +surf10400 & +surf10401 & +surf10402 & +surf10403 & -surf10404
u104_cell5 = openmc.Cell(fill=mat6)
u104_cell5.region = +surf10400 & +surf10401 & +surf10402 & +surf10403 & +surf10404 & -surf10405
universe104 = openmc.Universe(universe_id=104, cells=[u104_cell0, u104_cell1, u104_cell2, u104_cell3, u104_cell4, u104_cell5])

u106_cell0 = openmc.Cell(fill=mat1)
u106_cell0.region = -surf10600
u106_cell1 = openmc.Cell(fill=mat2)
u106_cell1.region = +surf10600 & -surf10601
u106_cell2 = openmc.Cell()
u106_cell2.region = +surf10600 & +surf10601 & -surf10602
u106_cell3 = openmc.Cell(fill=mat4)
u106_cell3.region = +surf10600 & +surf10601 & +surf10602 & -surf10603
u106_cell4 = openmc.Cell()
u106_cell4.region = +surf10600 & +surf10601 & +surf10602 & +surf10603 & -surf10604
u106_cell5 = openmc.Cell(fill=mat5)
u106_cell5.region = +surf10600 & +surf10601 & +surf10602 & +surf10603 & +surf10604 & -surf10605
u106_cell6 = openmc.Cell(fill=mat6)
u106_cell6.region = +surf10600 & +surf10601 & +surf10602 & +surf10603 & +surf10604 & +surf10605 & -surf10606
universe106 = openmc.Universe(universe_id=106, cells=[u106_cell0, u106_cell1, u106_cell2, u106_cell3, u106_cell4, u106_cell5, u106_cell6])

u107_cell0 = openmc.Cell(fill=mat1)
u107_cell0.region = -surf10700
u107_cell1 = openmc.Cell(fill=mat2)
u107_cell1.region = +surf10700 & -surf10701
u107_cell2 = openmc.Cell()
u107_cell2.region = +surf10700 & +surf10701 & -surf10702
u107_cell3 = openmc.Cell(fill=mat4)
u107_cell3.region = +surf10700 & +surf10701 & +surf10702 & -surf10703
u107_cell4 = openmc.Cell()
u107_cell4.region = +surf10700 & +surf10701 & +surf10702 & +surf10703 & -surf10704
u107_cell5 = openmc.Cell(fill=mat5)
u107_cell5.region = +surf10700 & +surf10701 & +surf10702 & +surf10703 & +surf10704 & -surf10705
u107_cell6 = openmc.Cell(fill=mat6)
u107_cell6.region = +surf10700 & +surf10701 & +surf10702 & +surf10703 & +surf10704 & +surf10705 & -surf10706
universe107 = openmc.Universe(universe_id=107, cells=[u107_cell0, u107_cell1, u107_cell2, u107_cell3, u107_cell4, u107_cell5, u107_cell6])

u108_cell0 = openmc.Cell(fill=mat1)
u108_cell0.region = -surf10800
u108_cell1 = openmc.Cell(fill=mat2)
u108_cell1.region = +surf10800 & -surf10801
u108_cell2 = openmc.Cell()
u108_cell2.region = +surf10800 & +surf10801 & -surf10802
u108_cell3 = openmc.Cell(fill=mat4)
u108_cell3.region = +surf10800 & +surf10801 & +surf10802 & -surf10803
u108_cell4 = openmc.Cell()
u108_cell4.region = +surf10800 & +surf10801 & +surf10802 & +surf10803 & -surf10804
u108_cell5 = openmc.Cell(fill=mat5)
u108_cell5.region = +surf10800 & +surf10801 & +surf10802 & +surf10803 & +surf10804 & -surf10805
u108_cell6 = openmc.Cell(fill=mat6)
u108_cell6.region = +surf10800 & +surf10801 & +surf10802 & +surf10803 & +surf10804 & +surf10805 & -surf10806
universe108 = openmc.Universe(universe_id=108, cells=[u108_cell0, u108_cell1, u108_cell2, u108_cell3, u108_cell4, u108_cell5, u108_cell6])

u109_cell0 = openmc.Cell(fill=mat1)
u109_cell0.region = -surf10900
u109_cell1 = openmc.Cell(fill=mat3)
u109_cell1.region = +surf10900 & -surf10901
u109_cell2 = openmc.Cell(fill=mat1)
u109_cell2.region = +surf10900 & +surf10901 & -surf10902
u109_cell3 = openmc.Cell(fill=mat3)
u109_cell3.region = +surf10900 & +surf10901 & +surf10902 & -surf10903
u109_cell4 = openmc.Cell(fill=mat1)
u109_cell4.region = +surf10900 & +surf10901 & +surf10902 & +surf10903 & -surf10904
u109_cell5 = openmc.Cell(fill=mat3)
u109_cell5.region = +surf10900 & +surf10901 & +surf10902 & +surf10903 & +surf10904 & -surf10905
u109_cell6 = openmc.Cell(fill=mat1)
u109_cell6.region = +surf10900 & +surf10901 & +surf10902 & +surf10903 & +surf10904 & +surf10905 & -surf10906
u109_cell7 = openmc.Cell(fill=mat2)
u109_cell7.region = +surf10900 & +surf10901 & +surf10902 & +surf10903 & +surf10904 & +surf10905 & +surf10906 & -surf10907
u109_cell8 = openmc.Cell()
u109_cell8.region = +surf10900 & +surf10901 & +surf10902 & +surf10903 & +surf10904 & +surf10905 & +surf10906 & +surf10907 & -surf10908
u109_cell9 = openmc.Cell(fill=mat4)
u109_cell9.region = +surf10900 & +surf10901 & +surf10902 & +surf10903 & +surf10904 & +surf10905 & +surf10906 & +surf10907 & +surf10908 & -surf10909
u109_cell10 = openmc.Cell()
u109_cell10.region = +surf10900 & +surf10901 & +surf10902 & +surf10903 & +surf10904 & +surf10905 & +surf10906 & +surf10907 & +surf10908 & +surf10909 & -surf10910
u109_cell11 = openmc.Cell(fill=mat5)
u109_cell11.region = +surf10900 & +surf10901 & +surf10902 & +surf10903 & +surf10904 & +surf10905 & +surf10906 & +surf10907 & +surf10908 & +surf10909 & +surf10910 & -surf10911
u109_cell12 = openmc.Cell(fill=mat6)
u109_cell12.region = +surf10900 & +surf10901 & +surf10902 & +surf10903 & +surf10904 & +surf10905 & +surf10906 & +surf10907 & +surf10908 & +surf10909 & +surf10910 & +surf10911 & -surf10912
universe109 = openmc.Universe(universe_id=109, cells=[u109_cell0, u109_cell1, u109_cell2, u109_cell3, u109_cell4, u109_cell5, u109_cell6, u109_cell7, u109_cell8, u109_cell9, u109_cell10, u109_cell11, u109_cell12])

u110_cell0 = openmc.Cell(fill=mat1)
u110_cell0.region = -surf11000
u110_cell1 = openmc.Cell(fill=mat3)
u110_cell1.region = +surf11000 & -surf11001
u110_cell2 = openmc.Cell(fill=mat1)
u110_cell2.region = +surf11000 & +surf11001 & -surf11002
u110_cell3 = openmc.Cell(fill=mat3)
u110_cell3.region = +surf11000 & +surf11001 & +surf11002 & -surf11003
u110_cell4 = openmc.Cell(fill=mat1)
u110_cell4.region = +surf11000 & +surf11001 & +surf11002 & +surf11003 & -surf11004
u110_cell5 = openmc.Cell(fill=mat3)
u110_cell5.region = +surf11000 & +surf11001 & +surf11002 & +surf11003 & +surf11004 & -surf11005
u110_cell6 = openmc.Cell(fill=mat1)
u110_cell6.region = +surf11000 & +surf11001 & +surf11002 & +surf11003 & +surf11004 & +surf11005 & -surf11006
u110_cell7 = openmc.Cell(fill=mat2)
u110_cell7.region = +surf11000 & +surf11001 & +surf11002 & +surf11003 & +surf11004 & +surf11005 & +surf11006 & -surf11007
u110_cell8 = openmc.Cell()
u110_cell8.region = +surf11000 & +surf11001 & +surf11002 & +surf11003 & +surf11004 & +surf11005 & +surf11006 & +surf11007 & -surf11008
u110_cell9 = openmc.Cell(fill=mat4)
u110_cell9.region = +surf11000 & +surf11001 & +surf11002 & +surf11003 & +surf11004 & +surf11005 & +surf11006 & +surf11007 & +surf11008 & -surf11009
u110_cell10 = openmc.Cell()
u110_cell10.region = +surf11000 & +surf11001 & +surf11002 & +surf11003 & +surf11004 & +surf11005 & +surf11006 & +surf11007 & +surf11008 & +surf11009 & -surf11010
u110_cell11 = openmc.Cell(fill=mat5)
u110_cell11.region = +surf11000 & +surf11001 & +surf11002 & +surf11003 & +surf11004 & +surf11005 & +surf11006 & +surf11007 & +surf11008 & +surf11009 & +surf11010 & -surf11011
u110_cell12 = openmc.Cell(fill=mat6)
u110_cell12.region = +surf11000 & +surf11001 & +surf11002 & +surf11003 & +surf11004 & +surf11005 & +surf11006 & +surf11007 & +surf11008 & +surf11009 & +surf11010 & +surf11011 & -surf11012
universe110 = openmc.Universe(universe_id=110, cells=[u110_cell0, u110_cell1, u110_cell2, u110_cell3, u110_cell4, u110_cell5, u110_cell6, u110_cell7, u110_cell8, u110_cell9, u110_cell10, u110_cell11, u110_cell12])

u116_cell0 = openmc.Cell(fill=mat1)
u116_cell0.region = -surf11600
u116_cell1 = openmc.Cell(fill=mat3)
u116_cell1.region = +surf11600 & -surf11601
u116_cell2 = openmc.Cell(fill=mat2)
u116_cell2.region = +surf11600 & +surf11601 & -surf11602
u116_cell3 = openmc.Cell()
u116_cell3.region = +surf11600 & +surf11601 & +surf11602 & -surf11603
u116_cell4 = openmc.Cell(fill=mat4)
u116_cell4.region = +surf11600 & +surf11601 & +surf11602 & +surf11603 & -surf11604
u116_cell5 = openmc.Cell()
u116_cell5.region = +surf11600 & +surf11601 & +surf11602 & +surf11603 & +surf11604 & -surf11605
u116_cell6 = openmc.Cell(fill=mat5)
u116_cell6.region = +surf11600 & +surf11601 & +surf11602 & +surf11603 & +surf11604 & +surf11605 & -surf11606
u116_cell7 = openmc.Cell(fill=mat6)
u116_cell7.region = +surf11600 & +surf11601 & +surf11602 & +surf11603 & +surf11604 & +surf11605 & +surf11606 & -surf11607
universe116 = openmc.Universe(universe_id=116, cells=[u116_cell0, u116_cell1, u116_cell2, u116_cell3, u116_cell4, u116_cell5, u116_cell6, u116_cell7])

u117_cell0 = openmc.Cell(fill=mat1)
u117_cell0.region = -surf11700
u117_cell1 = openmc.Cell(fill=mat3)
u117_cell1.region = +surf11700 & -surf11701
u117_cell2 = openmc.Cell(fill=mat2)
u117_cell2.region = +surf11700 & +surf11701 & -surf11702
u117_cell3 = openmc.Cell()
u117_cell3.region = +surf11700 & +surf11701 & +surf11702 & -surf11703
u117_cell4 = openmc.Cell(fill=mat4)
u117_cell4.region = +surf11700 & +surf11701 & +surf11702 & +surf11703 & -surf11704
u117_cell5 = openmc.Cell()
u117_cell5.region = +surf11700 & +surf11701 & +surf11702 & +surf11703 & +surf11704 & -surf11705
u117_cell6 = openmc.Cell(fill=mat5)
u117_cell6.region = +surf11700 & +surf11701 & +surf11702 & +surf11703 & +surf11704 & +surf11705 & -surf11706
u117_cell7 = openmc.Cell(fill=mat6)
u117_cell7.region = +surf11700 & +surf11701 & +surf11702 & +surf11703 & +surf11704 & +surf11705 & +surf11706 & -surf11707
universe117 = openmc.Universe(universe_id=117, cells=[u117_cell0, u117_cell1, u117_cell2, u117_cell3, u117_cell4, u117_cell5, u117_cell6, u117_cell7])

u118_cell0 = openmc.Cell(fill=mat1)
u118_cell0.region = -surf11800
u118_cell1 = openmc.Cell(fill=mat3)
u118_cell1.region = +surf11800 & -surf11801
u118_cell2 = openmc.Cell(fill=mat2)
u118_cell2.region = +surf11800 & +surf11801 & -surf11802
u118_cell3 = openmc.Cell()
u118_cell3.region = +surf11800 & +surf11801 & +surf11802 & -surf11803
u118_cell4 = openmc.Cell(fill=mat4)
u118_cell4.region = +surf11800 & +surf11801 & +surf11802 & +surf11803 & -surf11804
u118_cell5 = openmc.Cell()
u118_cell5.region = +surf11800 & +surf11801 & +surf11802 & +surf11803 & +surf11804 & -surf11805
u118_cell6 = openmc.Cell(fill=mat5)
u118_cell6.region = +surf11800 & +surf11801 & +surf11802 & +surf11803 & +surf11804 & +surf11805 & -surf11806
u118_cell7 = openmc.Cell(fill=mat6)
u118_cell7.region = +surf11800 & +surf11801 & +surf11802 & +surf11803 & +surf11804 & +surf11805 & +surf11806 & -surf11807
universe118 = openmc.Universe(universe_id=118, cells=[u118_cell0, u118_cell1, u118_cell2, u118_cell3, u118_cell4, u118_cell5, u118_cell6, u118_cell7])

u119_cell0 = openmc.Cell(fill=mat1)
u119_cell0.region = -surf11900
u119_cell1 = openmc.Cell(fill=mat3)
u119_cell1.region = +surf11900 & -surf11901
u119_cell2 = openmc.Cell(fill=mat1)
u119_cell2.region = +surf11900 & +surf11901 & -surf11902
u119_cell3 = openmc.Cell(fill=mat3)
u119_cell3.region = +surf11900 & +surf11901 & +surf11902 & -surf11903
u119_cell4 = openmc.Cell(fill=mat1)
u119_cell4.region = +surf11900 & +surf11901 & +surf11902 & +surf11903 & -surf11904
u119_cell5 = openmc.Cell(fill=mat3)
u119_cell5.region = +surf11900 & +surf11901 & +surf11902 & +surf11903 & +surf11904 & -surf11905
u119_cell6 = openmc.Cell(fill=mat1)
u119_cell6.region = +surf11900 & +surf11901 & +surf11902 & +surf11903 & +surf11904 & +surf11905 & -surf11906
u119_cell7 = openmc.Cell(fill=mat3)
u119_cell7.region = +surf11900 & +surf11901 & +surf11902 & +surf11903 & +surf11904 & +surf11905 & +surf11906 & -surf11907
u119_cell8 = openmc.Cell(fill=mat2)
u119_cell8.region = +surf11900 & +surf11901 & +surf11902 & +surf11903 & +surf11904 & +surf11905 & +surf11906 & +surf11907 & -surf11908
u119_cell9 = openmc.Cell()
u119_cell9.region = +surf11900 & +surf11901 & +surf11902 & +surf11903 & +surf11904 & +surf11905 & +surf11906 & +surf11907 & +surf11908 & -surf11909
u119_cell10 = openmc.Cell(fill=mat4)
u119_cell10.region = +surf11900 & +surf11901 & +surf11902 & +surf11903 & +surf11904 & +surf11905 & +surf11906 & +surf11907 & +surf11908 & +surf11909 & -surf11910
u119_cell11 = openmc.Cell()
u119_cell11.region = +surf11900 & +surf11901 & +surf11902 & +surf11903 & +surf11904 & +surf11905 & +surf11906 & +surf11907 & +surf11908 & +surf11909 & +surf11910 & -surf11911
u119_cell12 = openmc.Cell(fill=mat5)
u119_cell12.region = +surf11900 & +surf11901 & +surf11902 & +surf11903 & +surf11904 & +surf11905 & +surf11906 & +surf11907 & +surf11908 & +surf11909 & +surf11910 & +surf11911 & -surf11912
u119_cell13 = openmc.Cell(fill=mat6)
u119_cell13.region = +surf11900 & +surf11901 & +surf11902 & +surf11903 & +surf11904 & +surf11905 & +surf11906 & +surf11907 & +surf11908 & +surf11909 & +surf11910 & +surf11911 & +surf11912 & -surf11913
universe119 = openmc.Universe(universe_id=119, cells=[u119_cell0, u119_cell1, u119_cell2, u119_cell3, u119_cell4, u119_cell5, u119_cell6, u119_cell7, u119_cell8, u119_cell9, u119_cell10, u119_cell11, u119_cell12, u119_cell13])

u120_cell0 = openmc.Cell(fill=mat1)
u120_cell0.region = -surf12000
u120_cell1 = openmc.Cell(fill=mat3)
u120_cell1.region = +surf12000 & -surf12001
u120_cell2 = openmc.Cell(fill=mat1)
u120_cell2.region = +surf12000 & +surf12001 & -surf12002
u120_cell3 = openmc.Cell(fill=mat3)
u120_cell3.region = +surf12000 & +surf12001 & +surf12002 & -surf12003
u120_cell4 = openmc.Cell(fill=mat1)
u120_cell4.region = +surf12000 & +surf12001 & +surf12002 & +surf12003 & -surf12004
u120_cell5 = openmc.Cell(fill=mat3)
u120_cell5.region = +surf12000 & +surf12001 & +surf12002 & +surf12003 & +surf12004 & -surf12005
u120_cell6 = openmc.Cell(fill=mat1)
u120_cell6.region = +surf12000 & +surf12001 & +surf12002 & +surf12003 & +surf12004 & +surf12005 & -surf12006
u120_cell7 = openmc.Cell(fill=mat3)
u120_cell7.region = +surf12000 & +surf12001 & +surf12002 & +surf12003 & +surf12004 & +surf12005 & +surf12006 & -surf12007
u120_cell8 = openmc.Cell(fill=mat2)
u120_cell8.region = +surf12000 & +surf12001 & +surf12002 & +surf12003 & +surf12004 & +surf12005 & +surf12006 & +surf12007 & -surf12008
u120_cell9 = openmc.Cell()
u120_cell9.region = +surf12000 & +surf12001 & +surf12002 & +surf12003 & +surf12004 & +surf12005 & +surf12006 & +surf12007 & +surf12008 & -surf12009
u120_cell10 = openmc.Cell(fill=mat4)
u120_cell10.region = +surf12000 & +surf12001 & +surf12002 & +surf12003 & +surf12004 & +surf12005 & +surf12006 & +surf12007 & +surf12008 & +surf12009 & -surf12010
u120_cell11 = openmc.Cell()
u120_cell11.region = +surf12000 & +surf12001 & +surf12002 & +surf12003 & +surf12004 & +surf12005 & +surf12006 & +surf12007 & +surf12008 & +surf12009 & +surf12010 & -surf12011
u120_cell12 = openmc.Cell(fill=mat5)
u120_cell12.region = +surf12000 & +surf12001 & +surf12002 & +surf12003 & +surf12004 & +surf12005 & +surf12006 & +surf12007 & +surf12008 & +surf12009 & +surf12010 & +surf12011 & -surf12012
u120_cell13 = openmc.Cell(fill=mat6)
u120_cell13.region = +surf12000 & +surf12001 & +surf12002 & +surf12003 & +surf12004 & +surf12005 & +surf12006 & +surf12007 & +surf12008 & +surf12009 & +surf12010 & +surf12011 & +surf12012 & -surf12013
universe120 = openmc.Universe(universe_id=120, cells=[u120_cell0, u120_cell1, u120_cell2, u120_cell3, u120_cell4, u120_cell5, u120_cell6, u120_cell7, u120_cell8, u120_cell9, u120_cell10, u120_cell11, u120_cell12, u120_cell13])

u121_cell0 = openmc.Cell(fill=mat1)
u121_cell0.region = -surf12100
u121_cell1 = openmc.Cell(fill=mat3)
u121_cell1.region = +surf12100 & -surf12101
u121_cell2 = openmc.Cell(fill=mat2)
u121_cell2.region = +surf12100 & +surf12101 & -surf12102
u121_cell3 = openmc.Cell()
u121_cell3.region = +surf12100 & +surf12101 & +surf12102 & -surf12103
u121_cell4 = openmc.Cell(fill=mat4)
u121_cell4.region = +surf12100 & +surf12101 & +surf12102 & +surf12103 & -surf12104
u121_cell5 = openmc.Cell()
u121_cell5.region = +surf12100 & +surf12101 & +surf12102 & +surf12103 & +surf12104 & -surf12105
u121_cell6 = openmc.Cell(fill=mat5)
u121_cell6.region = +surf12100 & +surf12101 & +surf12102 & +surf12103 & +surf12104 & +surf12105 & -surf12106
u121_cell7 = openmc.Cell(fill=mat6)
u121_cell7.region = +surf12100 & +surf12101 & +surf12102 & +surf12103 & +surf12104 & +surf12105 & +surf12106 & -surf12107
universe121 = openmc.Universe(universe_id=121, cells=[u121_cell0, u121_cell1, u121_cell2, u121_cell3, u121_cell4, u121_cell5, u121_cell6, u121_cell7])

u122_cell0 = openmc.Cell(fill=mat1)
u122_cell0.region = -surf12200
u122_cell1 = openmc.Cell(fill=mat3)
u122_cell1.region = +surf12200 & -surf12201
u122_cell2 = openmc.Cell(fill=mat2)
u122_cell2.region = +surf12200 & +surf12201 & -surf12202
u122_cell3 = openmc.Cell()
u122_cell3.region = +surf12200 & +surf12201 & +surf12202 & -surf12203
u122_cell4 = openmc.Cell(fill=mat4)
u122_cell4.region = +surf12200 & +surf12201 & +surf12202 & +surf12203 & -surf12204
u122_cell5 = openmc.Cell()
u122_cell5.region = +surf12200 & +surf12201 & +surf12202 & +surf12203 & +surf12204 & -surf12205
u122_cell6 = openmc.Cell(fill=mat5)
u122_cell6.region = +surf12200 & +surf12201 & +surf12202 & +surf12203 & +surf12204 & +surf12205 & -surf12206
u122_cell7 = openmc.Cell(fill=mat6)
u122_cell7.region = +surf12200 & +surf12201 & +surf12202 & +surf12203 & +surf12204 & +surf12205 & +surf12206 & -surf12207
universe122 = openmc.Universe(universe_id=122, cells=[u122_cell0, u122_cell1, u122_cell2, u122_cell3, u122_cell4, u122_cell5, u122_cell6, u122_cell7])

u125_cell0 = openmc.Cell(fill=mat1)
u125_cell0.region = -surf12500
u125_cell1 = openmc.Cell(fill=mat3)
u125_cell1.region = +surf12500 & -surf12501
u125_cell2 = openmc.Cell(fill=mat2)
u125_cell2.region = +surf12500 & +surf12501 & -surf12502
u125_cell3 = openmc.Cell()
u125_cell3.region = +surf12500 & +surf12501 & +surf12502 & -surf12503
u125_cell4 = openmc.Cell(fill=mat4)
u125_cell4.region = +surf12500 & +surf12501 & +surf12502 & +surf12503 & -surf12504
u125_cell5 = openmc.Cell()
u125_cell5.region = +surf12500 & +surf12501 & +surf12502 & +surf12503 & +surf12504 & -surf12505
u125_cell6 = openmc.Cell(fill=mat5)
u125_cell6.region = +surf12500 & +surf12501 & +surf12502 & +surf12503 & +surf12504 & +surf12505 & -surf12506
u125_cell7 = openmc.Cell(fill=mat6)
u125_cell7.region = +surf12500 & +surf12501 & +surf12502 & +surf12503 & +surf12504 & +surf12505 & +surf12506 & -surf12507
universe125 = openmc.Universe(universe_id=125, cells=[u125_cell0, u125_cell1, u125_cell2, u125_cell3, u125_cell4, u125_cell5, u125_cell6, u125_cell7])

u126_cell0 = openmc.Cell(fill=mat1)
u126_cell0.region = -surf12600
u126_cell1 = openmc.Cell(fill=mat3)
u126_cell1.region = +surf12600 & -surf12601
u126_cell2 = openmc.Cell(fill=mat2)
u126_cell2.region = +surf12600 & +surf12601 & -surf12602
u126_cell3 = openmc.Cell()
u126_cell3.region = +surf12600 & +surf12601 & +surf12602 & -surf12603
u126_cell4 = openmc.Cell(fill=mat4)
u126_cell4.region = +surf12600 & +surf12601 & +surf12602 & +surf12603 & -surf12604
u126_cell5 = openmc.Cell()
u126_cell5.region = +surf12600 & +surf12601 & +surf12602 & +surf12603 & +surf12604 & -surf12605
u126_cell6 = openmc.Cell(fill=mat5)
u126_cell6.region = +surf12600 & +surf12601 & +surf12602 & +surf12603 & +surf12604 & +surf12605 & -surf12606
u126_cell7 = openmc.Cell(fill=mat6)
u126_cell7.region = +surf12600 & +surf12601 & +surf12602 & +surf12603 & +surf12604 & +surf12605 & +surf12606 & -surf12607
universe126 = openmc.Universe(universe_id=126, cells=[u126_cell0, u126_cell1, u126_cell2, u126_cell3, u126_cell4, u126_cell5, u126_cell6, u126_cell7])

u127_cell0 = openmc.Cell(fill=mat1)
u127_cell0.region = -surf12700
u127_cell1 = openmc.Cell(fill=mat3)
u127_cell1.region = +surf12700 & -surf12701
u127_cell2 = openmc.Cell(fill=mat2)
u127_cell2.region = +surf12700 & +surf12701 & -surf12702
u127_cell3 = openmc.Cell()
u127_cell3.region = +surf12700 & +surf12701 & +surf12702 & -surf12703
u127_cell4 = openmc.Cell(fill=mat4)
u127_cell4.region = +surf12700 & +surf12701 & +surf12702 & +surf12703 & -surf12704
u127_cell5 = openmc.Cell()
u127_cell5.region = +surf12700 & +surf12701 & +surf12702 & +surf12703 & +surf12704 & -surf12705
u127_cell6 = openmc.Cell(fill=mat5)
u127_cell6.region = +surf12700 & +surf12701 & +surf12702 & +surf12703 & +surf12704 & +surf12705 & -surf12706
u127_cell7 = openmc.Cell(fill=mat6)
u127_cell7.region = +surf12700 & +surf12701 & +surf12702 & +surf12703 & +surf12704 & +surf12705 & +surf12706 & -surf12707
universe127 = openmc.Universe(universe_id=127, cells=[u127_cell0, u127_cell1, u127_cell2, u127_cell3, u127_cell4, u127_cell5, u127_cell6, u127_cell7])

u128_cell0 = openmc.Cell(fill=mat1)
u128_cell0.region = -surf12800
u128_cell1 = openmc.Cell(fill=mat3)
u128_cell1.region = +surf12800 & -surf12801
u128_cell2 = openmc.Cell(fill=mat1)
u128_cell2.region = +surf12800 & +surf12801 & -surf12802
u128_cell3 = openmc.Cell(fill=mat3)
u128_cell3.region = +surf12800 & +surf12801 & +surf12802 & -surf12803
u128_cell4 = openmc.Cell(fill=mat1)
u128_cell4.region = +surf12800 & +surf12801 & +surf12802 & +surf12803 & -surf12804
u128_cell5 = openmc.Cell(fill=mat3)
u128_cell5.region = +surf12800 & +surf12801 & +surf12802 & +surf12803 & +surf12804 & -surf12805
u128_cell6 = openmc.Cell(fill=mat1)
u128_cell6.region = +surf12800 & +surf12801 & +surf12802 & +surf12803 & +surf12804 & +surf12805 & -surf12806
u128_cell7 = openmc.Cell(fill=mat3)
u128_cell7.region = +surf12800 & +surf12801 & +surf12802 & +surf12803 & +surf12804 & +surf12805 & +surf12806 & -surf12807
u128_cell8 = openmc.Cell(fill=mat2)
u128_cell8.region = +surf12800 & +surf12801 & +surf12802 & +surf12803 & +surf12804 & +surf12805 & +surf12806 & +surf12807 & -surf12808
u128_cell9 = openmc.Cell()
u128_cell9.region = +surf12800 & +surf12801 & +surf12802 & +surf12803 & +surf12804 & +surf12805 & +surf12806 & +surf12807 & +surf12808 & -surf12809
u128_cell10 = openmc.Cell(fill=mat4)
u128_cell10.region = +surf12800 & +surf12801 & +surf12802 & +surf12803 & +surf12804 & +surf12805 & +surf12806 & +surf12807 & +surf12808 & +surf12809 & -surf12810
u128_cell11 = openmc.Cell()
u128_cell11.region = +surf12800 & +surf12801 & +surf12802 & +surf12803 & +surf12804 & +surf12805 & +surf12806 & +surf12807 & +surf12808 & +surf12809 & +surf12810 & -surf12811
u128_cell12 = openmc.Cell(fill=mat5)
u128_cell12.region = +surf12800 & +surf12801 & +surf12802 & +surf12803 & +surf12804 & +surf12805 & +surf12806 & +surf12807 & +surf12808 & +surf12809 & +surf12810 & +surf12811 & -surf12812
u128_cell13 = openmc.Cell(fill=mat6)
u128_cell13.region = +surf12800 & +surf12801 & +surf12802 & +surf12803 & +surf12804 & +surf12805 & +surf12806 & +surf12807 & +surf12808 & +surf12809 & +surf12810 & +surf12811 & +surf12812 & -surf12813
universe128 = openmc.Universe(universe_id=128, cells=[u128_cell0, u128_cell1, u128_cell2, u128_cell3, u128_cell4, u128_cell5, u128_cell6, u128_cell7, u128_cell8, u128_cell9, u128_cell10, u128_cell11, u128_cell12, u128_cell13])

u141_cell0 = openmc.Cell(fill=mat1)
u141_cell0.region = -surf14100
u141_cell1 = openmc.Cell(fill=mat3)
u141_cell1.region = +surf14100 & -surf14101
u141_cell2 = openmc.Cell(fill=mat2)
u141_cell2.region = +surf14100 & +surf14101 & -surf14102
u141_cell3 = openmc.Cell()
u141_cell3.region = +surf14100 & +surf14101 & +surf14102 & -surf14103
u141_cell4 = openmc.Cell(fill=mat4)
u141_cell4.region = +surf14100 & +surf14101 & +surf14102 & +surf14103 & -surf14104
u141_cell5 = openmc.Cell()
u141_cell5.region = +surf14100 & +surf14101 & +surf14102 & +surf14103 & +surf14104 & -surf14105
u141_cell6 = openmc.Cell(fill=mat5)
u141_cell6.region = +surf14100 & +surf14101 & +surf14102 & +surf14103 & +surf14104 & +surf14105 & -surf14106
u141_cell7 = openmc.Cell(fill=mat6)
u141_cell7.region = +surf14100 & +surf14101 & +surf14102 & +surf14103 & +surf14104 & +surf14105 & +surf14106 & -surf14107
universe141 = openmc.Universe(universe_id=141, cells=[u141_cell0, u141_cell1, u141_cell2, u141_cell3, u141_cell4, u141_cell5, u141_cell6, u141_cell7])

u144_cell0 = openmc.Cell(fill=mat1)
u144_cell0.region = -surf14400
u144_cell1 = openmc.Cell(fill=mat3)
u144_cell1.region = +surf14400 & -surf14401
u144_cell2 = openmc.Cell(fill=mat2)
u144_cell2.region = +surf14400 & +surf14401 & -surf14402
u144_cell3 = openmc.Cell()
u144_cell3.region = +surf14400 & +surf14401 & +surf14402 & -surf14403
u144_cell4 = openmc.Cell(fill=mat4)
u144_cell4.region = +surf14400 & +surf14401 & +surf14402 & +surf14403 & -surf14404
u144_cell5 = openmc.Cell()
u144_cell5.region = +surf14400 & +surf14401 & +surf14402 & +surf14403 & +surf14404 & -surf14405
u144_cell6 = openmc.Cell(fill=mat5)
u144_cell6.region = +surf14400 & +surf14401 & +surf14402 & +surf14403 & +surf14404 & +surf14405 & -surf14406
u144_cell7 = openmc.Cell(fill=mat6)
u144_cell7.region = +surf14400 & +surf14401 & +surf14402 & +surf14403 & +surf14404 & +surf14405 & +surf14406 & -surf14407
universe144 = openmc.Universe(universe_id=144, cells=[u144_cell0, u144_cell1, u144_cell2, u144_cell3, u144_cell4, u144_cell5, u144_cell6, u144_cell7])

u203_cell0 = openmc.Cell(fill=mat3)
u203_cell0.region = -surf20300
u203_cell1 = openmc.Cell(fill=mat1)
u203_cell1.region = +surf20300 & -surf20301
u203_cell2 = openmc.Cell(fill=mat2)
u203_cell2.region = +surf20300 & +surf20301 & -surf20302
u203_cell3 = openmc.Cell()
u203_cell3.region = +surf20300 & +surf20301 & +surf20302 & -surf20303
u203_cell4 = openmc.Cell(fill=mat4)
u203_cell4.region = +surf20300 & +surf20301 & +surf20302 & +surf20303 & -surf20304
u203_cell5 = openmc.Cell()
u203_cell5.region = +surf20300 & +surf20301 & +surf20302 & +surf20303 & +surf20304 & -surf20305
u203_cell6 = openmc.Cell(fill=mat5)
u203_cell6.region = +surf20300 & +surf20301 & +surf20302 & +surf20303 & +surf20304 & +surf20305 & -surf20306
u203_cell7 = openmc.Cell(fill=mat6)
u203_cell7.region = +surf20300 & +surf20301 & +surf20302 & +surf20303 & +surf20304 & +surf20305 & +surf20306 & -surf20307
universe203 = openmc.Universe(universe_id=203, cells=[u203_cell0, u203_cell1, u203_cell2, u203_cell3, u203_cell4, u203_cell5, u203_cell6, u203_cell7])

u204_cell0 = openmc.Cell(fill=mat3)
u204_cell0.region = -surf20400
u204_cell1 = openmc.Cell(fill=mat1)
u204_cell1.region = +surf20400 & -surf20401
u204_cell2 = openmc.Cell(fill=mat2)
u204_cell2.region = +surf20400 & +surf20401 & -surf20402
u204_cell3 = openmc.Cell()
u204_cell3.region = +surf20400 & +surf20401 & +surf20402 & -surf20403
u204_cell4 = openmc.Cell(fill=mat4)
u204_cell4.region = +surf20400 & +surf20401 & +surf20402 & +surf20403 & -surf20404
u204_cell5 = openmc.Cell()
u204_cell5.region = +surf20400 & +surf20401 & +surf20402 & +surf20403 & +surf20404 & -surf20405
u204_cell6 = openmc.Cell(fill=mat5)
u204_cell6.region = +surf20400 & +surf20401 & +surf20402 & +surf20403 & +surf20404 & +surf20405 & -surf20406
u204_cell7 = openmc.Cell(fill=mat6)
u204_cell7.region = +surf20400 & +surf20401 & +surf20402 & +surf20403 & +surf20404 & +surf20405 & +surf20406 & -surf20407
universe204 = openmc.Universe(universe_id=204, cells=[u204_cell0, u204_cell1, u204_cell2, u204_cell3, u204_cell4, u204_cell5, u204_cell6, u204_cell7])

u205_cell0 = openmc.Cell(fill=mat3)
u205_cell0.region = -surf20500
u205_cell1 = openmc.Cell(fill=mat1)
u205_cell1.region = +surf20500 & -surf20501
u205_cell2 = openmc.Cell(fill=mat2)
u205_cell2.region = +surf20500 & +surf20501 & -surf20502
u205_cell3 = openmc.Cell()
u205_cell3.region = +surf20500 & +surf20501 & +surf20502 & -surf20503
u205_cell4 = openmc.Cell(fill=mat4)
u205_cell4.region = +surf20500 & +surf20501 & +surf20502 & +surf20503 & -surf20504
u205_cell5 = openmc.Cell()
u205_cell5.region = +surf20500 & +surf20501 & +surf20502 & +surf20503 & +surf20504 & -surf20505
u205_cell6 = openmc.Cell(fill=mat5)
u205_cell6.region = +surf20500 & +surf20501 & +surf20502 & +surf20503 & +surf20504 & +surf20505 & -surf20506
u205_cell7 = openmc.Cell(fill=mat6)
u205_cell7.region = +surf20500 & +surf20501 & +surf20502 & +surf20503 & +surf20504 & +surf20505 & +surf20506 & -surf20507
universe205 = openmc.Universe(universe_id=205, cells=[u205_cell0, u205_cell1, u205_cell2, u205_cell3, u205_cell4, u205_cell5, u205_cell6, u205_cell7])

u206_cell0 = openmc.Cell(fill=mat1)
u206_cell0.region = -surf20600
u206_cell1 = openmc.Cell(fill=mat3)
u206_cell1.region = +surf20600 & -surf20601
u206_cell2 = openmc.Cell(fill=mat1)
u206_cell2.region = +surf20600 & +surf20601 & -surf20602
u206_cell3 = openmc.Cell(fill=mat3)
u206_cell3.region = +surf20600 & +surf20601 & +surf20602 & -surf20603
u206_cell4 = openmc.Cell(fill=mat1)
u206_cell4.region = +surf20600 & +surf20601 & +surf20602 & +surf20603 & -surf20604
u206_cell5 = openmc.Cell(fill=mat3)
u206_cell5.region = +surf20600 & +surf20601 & +surf20602 & +surf20603 & +surf20604 & -surf20605
u206_cell6 = openmc.Cell(fill=mat1)
u206_cell6.region = +surf20600 & +surf20601 & +surf20602 & +surf20603 & +surf20604 & +surf20605 & -surf20606
u206_cell7 = openmc.Cell(fill=mat2)
u206_cell7.region = +surf20600 & +surf20601 & +surf20602 & +surf20603 & +surf20604 & +surf20605 & +surf20606 & -surf20607
u206_cell8 = openmc.Cell()
u206_cell8.region = +surf20600 & +surf20601 & +surf20602 & +surf20603 & +surf20604 & +surf20605 & +surf20606 & +surf20607 & -surf20608
u206_cell9 = openmc.Cell(fill=mat4)
u206_cell9.region = +surf20600 & +surf20601 & +surf20602 & +surf20603 & +surf20604 & +surf20605 & +surf20606 & +surf20607 & +surf20608 & -surf20609
u206_cell10 = openmc.Cell()
u206_cell10.region = +surf20600 & +surf20601 & +surf20602 & +surf20603 & +surf20604 & +surf20605 & +surf20606 & +surf20607 & +surf20608 & +surf20609 & -surf20610
u206_cell11 = openmc.Cell(fill=mat5)
u206_cell11.region = +surf20600 & +surf20601 & +surf20602 & +surf20603 & +surf20604 & +surf20605 & +surf20606 & +surf20607 & +surf20608 & +surf20609 & +surf20610 & -surf20611
u206_cell12 = openmc.Cell(fill=mat6)
u206_cell12.region = +surf20600 & +surf20601 & +surf20602 & +surf20603 & +surf20604 & +surf20605 & +surf20606 & +surf20607 & +surf20608 & +surf20609 & +surf20610 & +surf20611 & -surf20612
universe206 = openmc.Universe(universe_id=206, cells=[u206_cell0, u206_cell1, u206_cell2, u206_cell3, u206_cell4, u206_cell5, u206_cell6, u206_cell7, u206_cell8, u206_cell9, u206_cell10, u206_cell11, u206_cell12])

u207_cell0 = openmc.Cell(fill=mat1)
u207_cell0.region = -surf20700
u207_cell1 = openmc.Cell(fill=mat3)
u207_cell1.region = +surf20700 & -surf20701
u207_cell2 = openmc.Cell(fill=mat1)
u207_cell2.region = +surf20700 & +surf20701 & -surf20702
u207_cell3 = openmc.Cell(fill=mat3)
u207_cell3.region = +surf20700 & +surf20701 & +surf20702 & -surf20703
u207_cell4 = openmc.Cell(fill=mat1)
u207_cell4.region = +surf20700 & +surf20701 & +surf20702 & +surf20703 & -surf20704
u207_cell5 = openmc.Cell(fill=mat3)
u207_cell5.region = +surf20700 & +surf20701 & +surf20702 & +surf20703 & +surf20704 & -surf20705
u207_cell6 = openmc.Cell(fill=mat1)
u207_cell6.region = +surf20700 & +surf20701 & +surf20702 & +surf20703 & +surf20704 & +surf20705 & -surf20706
u207_cell7 = openmc.Cell(fill=mat3)
u207_cell7.region = +surf20700 & +surf20701 & +surf20702 & +surf20703 & +surf20704 & +surf20705 & +surf20706 & -surf20707
u207_cell8 = openmc.Cell(fill=mat2)
u207_cell8.region = +surf20700 & +surf20701 & +surf20702 & +surf20703 & +surf20704 & +surf20705 & +surf20706 & +surf20707 & -surf20708
u207_cell9 = openmc.Cell()
u207_cell9.region = +surf20700 & +surf20701 & +surf20702 & +surf20703 & +surf20704 & +surf20705 & +surf20706 & +surf20707 & +surf20708 & -surf20709
u207_cell10 = openmc.Cell(fill=mat4)
u207_cell10.region = +surf20700 & +surf20701 & +surf20702 & +surf20703 & +surf20704 & +surf20705 & +surf20706 & +surf20707 & +surf20708 & +surf20709 & -surf20710
u207_cell11 = openmc.Cell()
u207_cell11.region = +surf20700 & +surf20701 & +surf20702 & +surf20703 & +surf20704 & +surf20705 & +surf20706 & +surf20707 & +surf20708 & +surf20709 & +surf20710 & -surf20711
u207_cell12 = openmc.Cell(fill=mat5)
u207_cell12.region = +surf20700 & +surf20701 & +surf20702 & +surf20703 & +surf20704 & +surf20705 & +surf20706 & +surf20707 & +surf20708 & +surf20709 & +surf20710 & +surf20711 & -surf20712
u207_cell13 = openmc.Cell(fill=mat6)
u207_cell13.region = +surf20700 & +surf20701 & +surf20702 & +surf20703 & +surf20704 & +surf20705 & +surf20706 & +surf20707 & +surf20708 & +surf20709 & +surf20710 & +surf20711 & +surf20712 & -surf20713
universe207 = openmc.Universe(universe_id=207, cells=[u207_cell0, u207_cell1, u207_cell2, u207_cell3, u207_cell4, u207_cell5, u207_cell6, u207_cell7, u207_cell8, u207_cell9, u207_cell10, u207_cell11, u207_cell12, u207_cell13])

u237_cell0 = openmc.Cell(fill=mat1)
u237_cell0.region = -surf23700
u237_cell1 = openmc.Cell(fill=mat3)
u237_cell1.region = +surf23700 & -surf23701
u237_cell2 = openmc.Cell(fill=mat2)
u237_cell2.region = +surf23700 & +surf23701 & -surf23702
u237_cell3 = openmc.Cell()
u237_cell3.region = +surf23700 & +surf23701 & +surf23702 & -surf23703
u237_cell4 = openmc.Cell(fill=mat4)
u237_cell4.region = +surf23700 & +surf23701 & +surf23702 & +surf23703 & -surf23704
u237_cell5 = openmc.Cell()
u237_cell5.region = +surf23700 & +surf23701 & +surf23702 & +surf23703 & +surf23704 & -surf23705
u237_cell6 = openmc.Cell(fill=mat5)
u237_cell6.region = +surf23700 & +surf23701 & +surf23702 & +surf23703 & +surf23704 & +surf23705 & -surf23706
u237_cell7 = openmc.Cell(fill=mat6)
u237_cell7.region = +surf23700 & +surf23701 & +surf23702 & +surf23703 & +surf23704 & +surf23705 & +surf23706 & -surf23707
universe237 = openmc.Universe(universe_id=237, cells=[u237_cell0, u237_cell1, u237_cell2, u237_cell3, u237_cell4, u237_cell5, u237_cell6, u237_cell7])

u238_cell0 = openmc.Cell(fill=mat1)
u238_cell0.region = -surf23800
u238_cell1 = openmc.Cell(fill=mat3)
u238_cell1.region = +surf23800 & -surf23801
u238_cell2 = openmc.Cell(fill=mat2)
u238_cell2.region = +surf23800 & +surf23801 & -surf23802
u238_cell3 = openmc.Cell()
u238_cell3.region = +surf23800 & +surf23801 & +surf23802 & -surf23803
u238_cell4 = openmc.Cell(fill=mat4)
u238_cell4.region = +surf23800 & +surf23801 & +surf23802 & +surf23803 & -surf23804
u238_cell5 = openmc.Cell()
u238_cell5.region = +surf23800 & +surf23801 & +surf23802 & +surf23803 & +surf23804 & -surf23805
u238_cell6 = openmc.Cell(fill=mat5)
u238_cell6.region = +surf23800 & +surf23801 & +surf23802 & +surf23803 & +surf23804 & +surf23805 & -surf23806
u238_cell7 = openmc.Cell(fill=mat6)
u238_cell7.region = +surf23800 & +surf23801 & +surf23802 & +surf23803 & +surf23804 & +surf23805 & +surf23806 & -surf23807
universe238 = openmc.Universe(universe_id=238, cells=[u238_cell0, u238_cell1, u238_cell2, u238_cell3, u238_cell4, u238_cell5, u238_cell6, u238_cell7])

# ------------------------------------------------------------------------------
# Root Cells
# ------------------------------------------------------------------------------

# FuArry
cell1 = openmc.Cell(cell_id=1, fill=universe1)
cell1.region = -surf20

# VrtSt
cell2 = openmc.Cell(cell_id=2, fill=mat6)
cell2.region = +surf20 & -surf21

# Table
cell3 = openmc.Cell(cell_id=3, fill=mat6)
cell3.region = +surf20 & +surf21 & -surf22 & -surf23

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
source.space = openmc.stats.Box((-10.14, -10.14, 30.5), (10.14, 10.14, 32.5))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
