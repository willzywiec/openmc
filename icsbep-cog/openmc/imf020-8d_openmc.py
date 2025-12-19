"""
IEU-MET-FAST-020-8: FR0 experiment 1G-D (case 8 detailed model)
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

# Copper tubes
mat7 = openmc.Material(material_id=7)
mat7.set_density("sum")
mat7.add_element("Cu", 4.598100e-03)
mat7.add_element("Ag", 4.342700e-06)
mat7.add_nuclide("O16", 7.319700e-06)

materials = openmc.Materials([mat1, mat2, mat3, mat4, mat5, mat6, mat7])

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
surf12500 = openmc.model.RectangularParallelepiped(3.6833, 4.4, 0.1, 4.4, -1.43333, 30.824)
surf12501 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 4.4, -1.43333, 31.541)
surf12502 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf12503 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf12504 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf12505 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf12506 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf12507 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf12600 = openmc.model.RectangularParallelepiped(3.6833, 4.40, 0.1, 4.40, -0.71667, 29.39)
surf12601 = openmc.model.RectangularParallelepiped(0.1, 4.40, 0.1, 4.40, -0.71667, 30.824)
surf12602 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf12603 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf12604 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf12605 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf12606 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf12607 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf12700 = openmc.model.RectangularParallelepiped(3.6833, 4.40, 0.1, 4.4, 0.71667, 28.673)
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
surf14900 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, -40.85, 70.957)
surf14901 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf14902 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf14903 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf14904 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf14905 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf14906 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf15100 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, -1.43333, 31.541)
surf15101 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, -40.85, 70.957)
surf15102 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf15103 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf15104 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf15105 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf15106 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf15107 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf15500 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, -0.71667, 30.824)
surf15501 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, -40.85, 70.957)
surf15502 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf15503 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf15504 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf15505 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf15506 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf15507 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf15700 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, 0.71667, 29.390)
surf15701 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, -40.85, 70.957)
surf15702 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf15703 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf15704 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf15705 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf15706 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf15707 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf16600 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 1.5333, 8.60, 21.503)
surf16601 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 1.5333, 6.45, 23.654)
surf16602 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 2.25, 6.45, 23.654)
surf16603 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 2.25, 4.30, 25.805)
surf16604 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 3.6833, 4.30, 25.805)
surf16605 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 3.6833, 2.15, 27.956)
surf16606 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.40, 2.15, 27.956)
surf16607 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, -40.85, 70.957)
surf16608 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf16609 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf16610 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf16611 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf16612 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf16613 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf16700 = openmc.model.RectangularParallelepiped(2.25, 4.4, 2.9667, 4.4, 8.60, 21.503)
surf16701 = openmc.model.RectangularParallelepiped(2.25, 4.4, 2.9667, 4.4, 6.45, 23.654)
surf16702 = openmc.model.RectangularParallelepiped(2.25, 4.4, 2.25, 4.4, 6.45, 23.654)
surf16703 = openmc.model.RectangularParallelepiped(2.25, 4.4, 2.25, 4.4, 4.30, 25.805)
surf16704 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.8167, 4.4, 4.30, 25.805)
surf16705 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.8167, 4.4, 2.15, 27.956)
surf16706 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.10, 4.4, 2.15, 27.956)
surf16707 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, -40.85, 70.957)
surf16708 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf16709 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf16710 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf16711 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf16712 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf16713 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf16800 = openmc.model.RectangularParallelepiped(2.25, 4.4, 3.6833, 4.4, 10.75, 19.352)
surf16801 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, 10.75, 19.352)
surf16802 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, -40.85, 70.957)
surf16803 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf16804 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf16805 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf16806 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf16807 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf16808 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)
surf17100 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 0.8167, 10.75, 19.352)
surf17101 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, 10.75, 19.352)
surf17102 = openmc.model.RectangularParallelepiped(2.25, 4.4, 0.1, 4.4, -40.85, 70.957)
surf17103 = openmc.model.RectangularParallelepiped(0.1, 4.4, 0.1, 4.4, -40.85, 70.957)
surf17104 = openmc.model.RectangularParallelepiped(0.08, 4.42, 0.08, 4.42, -42.4, 73.3)
surf17105 = openmc.model.RectangularParallelepiped(0, 4.5, 0, 4.5, -44.7, 75.3)
surf17106 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -44.7, 75.3)
surf17107 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 77.0)
surf17108 = openmc.model.RectangularParallelepiped(-0.035, 4.535, -0.035, 4.535, -46.5, 79.8)

# ------------------------------------------------------------------------------
# Universes
# ------------------------------------------------------------------------------

# Lattice 1: 20x21 array
lattice1 = openmc.RectLattice(lattice_id=1)
lattice1.lower_left = [-45.7, -47.985]
lattice1.pitch = [4.570000, 4.570000]
lattice1.universes = [
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe149, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe149, universe104, universe104, universe104, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe149, universe104, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe149, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe149, universe104],
    [universe141, universe141, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe149, universe104],
    [universe109, universe109, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe141, universe141, universe141, universe168, universe141],
    [universe108, universe127, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe119, universe109, universe109, universe109, universe166, universe109],
    [universe107, universe126, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe118, universe108, universe108, universe108, universe157, universe108],
    [universe106, universe125, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe117, universe107, universe107, universe107, universe155, universe107],
    [universe107, universe126, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe116, universe106, universe106, universe106, universe151, universe106],
    [universe108, universe127, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe117, universe107, universe107, universe107, universe155, universe107],
    [universe110, universe128, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe118, universe108, universe108, universe108, universe157, universe108],
    [universe144, universe144, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe120, universe110, universe110, universe110, universe167, universe110],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe144, universe144, universe144, universe171, universe144],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe149, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe149, universe104],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe149, universe104],
    [universe104, universe104, universe149, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe149],
    [universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe149, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104, universe104],
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

u125_cell0 = openmc.Cell(fill=mat3)
u125_cell0.region = -surf12500
u125_cell1 = openmc.Cell(fill=mat1)
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

u126_cell0 = openmc.Cell(fill=mat3)
u126_cell0.region = -surf12600
u126_cell1 = openmc.Cell(fill=mat1)
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

u127_cell0 = openmc.Cell(fill=mat3)
u127_cell0.region = -surf12700
u127_cell1 = openmc.Cell(fill=mat1)
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

u149_cell0 = openmc.Cell(fill=mat2)
u149_cell0.region = -surf14900
u149_cell1 = openmc.Cell(fill=mat7)
u149_cell1.region = +surf14900 & -surf14901
u149_cell2 = openmc.Cell()
u149_cell2.region = +surf14900 & +surf14901 & -surf14902
u149_cell3 = openmc.Cell(fill=mat4)
u149_cell3.region = +surf14900 & +surf14901 & +surf14902 & -surf14903
u149_cell4 = openmc.Cell()
u149_cell4.region = +surf14900 & +surf14901 & +surf14902 & +surf14903 & -surf14904
u149_cell5 = openmc.Cell(fill=mat5)
u149_cell5.region = +surf14900 & +surf14901 & +surf14902 & +surf14903 & +surf14904 & -surf14905
u149_cell6 = openmc.Cell(fill=mat6)
u149_cell6.region = +surf14900 & +surf14901 & +surf14902 & +surf14903 & +surf14904 & +surf14905 & -surf14906
universe149 = openmc.Universe(universe_id=149, cells=[u149_cell0, u149_cell1, u149_cell2, u149_cell3, u149_cell4, u149_cell5, u149_cell6])

u151_cell0 = openmc.Cell(fill=mat1)
u151_cell0.region = -surf15100
u151_cell1 = openmc.Cell(fill=mat2)
u151_cell1.region = +surf15100 & -surf15101
u151_cell2 = openmc.Cell(fill=mat7)
u151_cell2.region = +surf15100 & +surf15101 & -surf15102
u151_cell3 = openmc.Cell()
u151_cell3.region = +surf15100 & +surf15101 & +surf15102 & -surf15103
u151_cell4 = openmc.Cell(fill=mat4)
u151_cell4.region = +surf15100 & +surf15101 & +surf15102 & +surf15103 & -surf15104
u151_cell5 = openmc.Cell()
u151_cell5.region = +surf15100 & +surf15101 & +surf15102 & +surf15103 & +surf15104 & -surf15105
u151_cell6 = openmc.Cell(fill=mat5)
u151_cell6.region = +surf15100 & +surf15101 & +surf15102 & +surf15103 & +surf15104 & +surf15105 & -surf15106
u151_cell7 = openmc.Cell(fill=mat6)
u151_cell7.region = +surf15100 & +surf15101 & +surf15102 & +surf15103 & +surf15104 & +surf15105 & +surf15106 & -surf15107
universe151 = openmc.Universe(universe_id=151, cells=[u151_cell0, u151_cell1, u151_cell2, u151_cell3, u151_cell4, u151_cell5, u151_cell6, u151_cell7])

u155_cell0 = openmc.Cell(fill=mat1)
u155_cell0.region = -surf15500
u155_cell1 = openmc.Cell(fill=mat2)
u155_cell1.region = +surf15500 & -surf15501
u155_cell2 = openmc.Cell(fill=mat7)
u155_cell2.region = +surf15500 & +surf15501 & -surf15502
u155_cell3 = openmc.Cell()
u155_cell3.region = +surf15500 & +surf15501 & +surf15502 & -surf15503
u155_cell4 = openmc.Cell(fill=mat4)
u155_cell4.region = +surf15500 & +surf15501 & +surf15502 & +surf15503 & -surf15504
u155_cell5 = openmc.Cell()
u155_cell5.region = +surf15500 & +surf15501 & +surf15502 & +surf15503 & +surf15504 & -surf15505
u155_cell6 = openmc.Cell(fill=mat5)
u155_cell6.region = +surf15500 & +surf15501 & +surf15502 & +surf15503 & +surf15504 & +surf15505 & -surf15506
u155_cell7 = openmc.Cell(fill=mat6)
u155_cell7.region = +surf15500 & +surf15501 & +surf15502 & +surf15503 & +surf15504 & +surf15505 & +surf15506 & -surf15507
universe155 = openmc.Universe(universe_id=155, cells=[u155_cell0, u155_cell1, u155_cell2, u155_cell3, u155_cell4, u155_cell5, u155_cell6, u155_cell7])

u157_cell0 = openmc.Cell(fill=mat1)
u157_cell0.region = -surf15700
u157_cell1 = openmc.Cell(fill=mat2)
u157_cell1.region = +surf15700 & -surf15701
u157_cell2 = openmc.Cell(fill=mat7)
u157_cell2.region = +surf15700 & +surf15701 & -surf15702
u157_cell3 = openmc.Cell()
u157_cell3.region = +surf15700 & +surf15701 & +surf15702 & -surf15703
u157_cell4 = openmc.Cell(fill=mat4)
u157_cell4.region = +surf15700 & +surf15701 & +surf15702 & +surf15703 & -surf15704
u157_cell5 = openmc.Cell()
u157_cell5.region = +surf15700 & +surf15701 & +surf15702 & +surf15703 & +surf15704 & -surf15705
u157_cell6 = openmc.Cell(fill=mat5)
u157_cell6.region = +surf15700 & +surf15701 & +surf15702 & +surf15703 & +surf15704 & +surf15705 & -surf15706
u157_cell7 = openmc.Cell(fill=mat6)
u157_cell7.region = +surf15700 & +surf15701 & +surf15702 & +surf15703 & +surf15704 & +surf15705 & +surf15706 & -surf15707
universe157 = openmc.Universe(universe_id=157, cells=[u157_cell0, u157_cell1, u157_cell2, u157_cell3, u157_cell4, u157_cell5, u157_cell6, u157_cell7])

u166_cell0 = openmc.Cell(fill=mat1)
u166_cell0.region = -surf16600
u166_cell1 = openmc.Cell(fill=mat3)
u166_cell1.region = +surf16600 & -surf16601
u166_cell2 = openmc.Cell(fill=mat1)
u166_cell2.region = +surf16600 & +surf16601 & -surf16602
u166_cell3 = openmc.Cell(fill=mat3)
u166_cell3.region = +surf16600 & +surf16601 & +surf16602 & -surf16603
u166_cell4 = openmc.Cell(fill=mat1)
u166_cell4.region = +surf16600 & +surf16601 & +surf16602 & +surf16603 & -surf16604
u166_cell5 = openmc.Cell(fill=mat3)
u166_cell5.region = +surf16600 & +surf16601 & +surf16602 & +surf16603 & +surf16604 & -surf16605
u166_cell6 = openmc.Cell(fill=mat1)
u166_cell6.region = +surf16600 & +surf16601 & +surf16602 & +surf16603 & +surf16604 & +surf16605 & -surf16606
u166_cell7 = openmc.Cell(fill=mat2)
u166_cell7.region = +surf16600 & +surf16601 & +surf16602 & +surf16603 & +surf16604 & +surf16605 & +surf16606 & -surf16607
u166_cell8 = openmc.Cell(fill=mat7)
u166_cell8.region = +surf16600 & +surf16601 & +surf16602 & +surf16603 & +surf16604 & +surf16605 & +surf16606 & +surf16607 & -surf16608
u166_cell9 = openmc.Cell()
u166_cell9.region = +surf16600 & +surf16601 & +surf16602 & +surf16603 & +surf16604 & +surf16605 & +surf16606 & +surf16607 & +surf16608 & -surf16609
u166_cell10 = openmc.Cell(fill=mat4)
u166_cell10.region = +surf16600 & +surf16601 & +surf16602 & +surf16603 & +surf16604 & +surf16605 & +surf16606 & +surf16607 & +surf16608 & +surf16609 & -surf16610
u166_cell11 = openmc.Cell()
u166_cell11.region = +surf16600 & +surf16601 & +surf16602 & +surf16603 & +surf16604 & +surf16605 & +surf16606 & +surf16607 & +surf16608 & +surf16609 & +surf16610 & -surf16611
u166_cell12 = openmc.Cell(fill=mat5)
u166_cell12.region = +surf16600 & +surf16601 & +surf16602 & +surf16603 & +surf16604 & +surf16605 & +surf16606 & +surf16607 & +surf16608 & +surf16609 & +surf16610 & +surf16611 & -surf16612
u166_cell13 = openmc.Cell(fill=mat6)
u166_cell13.region = +surf16600 & +surf16601 & +surf16602 & +surf16603 & +surf16604 & +surf16605 & +surf16606 & +surf16607 & +surf16608 & +surf16609 & +surf16610 & +surf16611 & +surf16612 & -surf16613
universe166 = openmc.Universe(universe_id=166, cells=[u166_cell0, u166_cell1, u166_cell2, u166_cell3, u166_cell4, u166_cell5, u166_cell6, u166_cell7, u166_cell8, u166_cell9, u166_cell10, u166_cell11, u166_cell12, u166_cell13])

u167_cell0 = openmc.Cell(fill=mat1)
u167_cell0.region = -surf16700
u167_cell1 = openmc.Cell(fill=mat3)
u167_cell1.region = +surf16700 & -surf16701
u167_cell2 = openmc.Cell(fill=mat1)
u167_cell2.region = +surf16700 & +surf16701 & -surf16702
u167_cell3 = openmc.Cell(fill=mat3)
u167_cell3.region = +surf16700 & +surf16701 & +surf16702 & -surf16703
u167_cell4 = openmc.Cell(fill=mat1)
u167_cell4.region = +surf16700 & +surf16701 & +surf16702 & +surf16703 & -surf16704
u167_cell5 = openmc.Cell(fill=mat3)
u167_cell5.region = +surf16700 & +surf16701 & +surf16702 & +surf16703 & +surf16704 & -surf16705
u167_cell6 = openmc.Cell(fill=mat1)
u167_cell6.region = +surf16700 & +surf16701 & +surf16702 & +surf16703 & +surf16704 & +surf16705 & -surf16706
u167_cell7 = openmc.Cell(fill=mat2)
u167_cell7.region = +surf16700 & +surf16701 & +surf16702 & +surf16703 & +surf16704 & +surf16705 & +surf16706 & -surf16707
u167_cell8 = openmc.Cell(fill=mat7)
u167_cell8.region = +surf16700 & +surf16701 & +surf16702 & +surf16703 & +surf16704 & +surf16705 & +surf16706 & +surf16707 & -surf16708
u167_cell9 = openmc.Cell()
u167_cell9.region = +surf16700 & +surf16701 & +surf16702 & +surf16703 & +surf16704 & +surf16705 & +surf16706 & +surf16707 & +surf16708 & -surf16709
u167_cell10 = openmc.Cell(fill=mat4)
u167_cell10.region = +surf16700 & +surf16701 & +surf16702 & +surf16703 & +surf16704 & +surf16705 & +surf16706 & +surf16707 & +surf16708 & +surf16709 & -surf16710
u167_cell11 = openmc.Cell()
u167_cell11.region = +surf16700 & +surf16701 & +surf16702 & +surf16703 & +surf16704 & +surf16705 & +surf16706 & +surf16707 & +surf16708 & +surf16709 & +surf16710 & -surf16711
u167_cell12 = openmc.Cell(fill=mat5)
u167_cell12.region = +surf16700 & +surf16701 & +surf16702 & +surf16703 & +surf16704 & +surf16705 & +surf16706 & +surf16707 & +surf16708 & +surf16709 & +surf16710 & +surf16711 & -surf16712
u167_cell13 = openmc.Cell(fill=mat6)
u167_cell13.region = +surf16700 & +surf16701 & +surf16702 & +surf16703 & +surf16704 & +surf16705 & +surf16706 & +surf16707 & +surf16708 & +surf16709 & +surf16710 & +surf16711 & +surf16712 & -surf16713
universe167 = openmc.Universe(universe_id=167, cells=[u167_cell0, u167_cell1, u167_cell2, u167_cell3, u167_cell4, u167_cell5, u167_cell6, u167_cell7, u167_cell8, u167_cell9, u167_cell10, u167_cell11, u167_cell12, u167_cell13])

u168_cell0 = openmc.Cell(fill=mat1)
u168_cell0.region = -surf16800
u168_cell1 = openmc.Cell(fill=mat3)
u168_cell1.region = +surf16800 & -surf16801
u168_cell2 = openmc.Cell(fill=mat2)
u168_cell2.region = +surf16800 & +surf16801 & -surf16802
u168_cell3 = openmc.Cell(fill=mat7)
u168_cell3.region = +surf16800 & +surf16801 & +surf16802 & -surf16803
u168_cell4 = openmc.Cell()
u168_cell4.region = +surf16800 & +surf16801 & +surf16802 & +surf16803 & -surf16804
u168_cell5 = openmc.Cell(fill=mat4)
u168_cell5.region = +surf16800 & +surf16801 & +surf16802 & +surf16803 & +surf16804 & -surf16805
u168_cell6 = openmc.Cell()
u168_cell6.region = +surf16800 & +surf16801 & +surf16802 & +surf16803 & +surf16804 & +surf16805 & -surf16806
u168_cell7 = openmc.Cell(fill=mat5)
u168_cell7.region = +surf16800 & +surf16801 & +surf16802 & +surf16803 & +surf16804 & +surf16805 & +surf16806 & -surf16807
u168_cell8 = openmc.Cell(fill=mat6)
u168_cell8.region = +surf16800 & +surf16801 & +surf16802 & +surf16803 & +surf16804 & +surf16805 & +surf16806 & +surf16807 & -surf16808
universe168 = openmc.Universe(universe_id=168, cells=[u168_cell0, u168_cell1, u168_cell2, u168_cell3, u168_cell4, u168_cell5, u168_cell6, u168_cell7, u168_cell8])

u171_cell0 = openmc.Cell(fill=mat1)
u171_cell0.region = -surf17100
u171_cell1 = openmc.Cell(fill=mat3)
u171_cell1.region = +surf17100 & -surf17101
u171_cell2 = openmc.Cell(fill=mat2)
u171_cell2.region = +surf17100 & +surf17101 & -surf17102
u171_cell3 = openmc.Cell(fill=mat7)
u171_cell3.region = +surf17100 & +surf17101 & +surf17102 & -surf17103
u171_cell4 = openmc.Cell()
u171_cell4.region = +surf17100 & +surf17101 & +surf17102 & +surf17103 & -surf17104
u171_cell5 = openmc.Cell(fill=mat4)
u171_cell5.region = +surf17100 & +surf17101 & +surf17102 & +surf17103 & +surf17104 & -surf17105
u171_cell6 = openmc.Cell()
u171_cell6.region = +surf17100 & +surf17101 & +surf17102 & +surf17103 & +surf17104 & +surf17105 & -surf17106
u171_cell7 = openmc.Cell(fill=mat5)
u171_cell7.region = +surf17100 & +surf17101 & +surf17102 & +surf17103 & +surf17104 & +surf17105 & +surf17106 & -surf17107
u171_cell8 = openmc.Cell(fill=mat6)
u171_cell8.region = +surf17100 & +surf17101 & +surf17102 & +surf17103 & +surf17104 & +surf17105 & +surf17106 & +surf17107 & -surf17108
universe171 = openmc.Universe(universe_id=171, cells=[u171_cell0, u171_cell1, u171_cell2, u171_cell3, u171_cell4, u171_cell5, u171_cell6, u171_cell7, u171_cell8])

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
source.space = openmc.stats.Box((-7.855, -10.14, 30.5), (12.425, 10.14, 32.5))
settings.source = source

# ==============================================================================
# Export
# ==============================================================================

materials.export_to_xml()
geometry.export_to_xml()
settings.export_to_xml()
