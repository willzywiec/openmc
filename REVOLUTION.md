# Revolution Surfaces in OpenMC

This guide explains how to use OpenMC's Revolution (Solid of Revolution) surface type for creating complex axisymmetric geometries.

## Overview

A Revolution surface creates a 3D shape by rotating a 2D profile around an axis. This is useful for modeling:

- Cylindrical vessels with varying radii
- Conical shapes and frustums
- Vase-like containers
- Nozzles and funnels
- Any geometry with rotational symmetry

The profile is defined as a series of (r, z) coordinate pairs, where:
- **r**: Radial distance from the axis of revolution (must be non-negative)
- **z**: Position along the axis of revolution

Adjacent profile points are connected by straight line segments, which form conical frustums when revolved.

## Quick Start

### Basic Cylinder

```python
import openmc

# Define profile: constant radius from z=0 to z=5
profile = [(1.0, 0.0), (1.0, 5.0)]

# Create revolution surface around z-axis
cylinder = openmc.Revolution(rz=profile, axis='z')

# Use in a cell (inside the cylinder)
cell = openmc.Cell(region=-cylinder)
```

### Cone Frustum

```python
# Profile: radius changes from 0.5 to 1.0 over z=0 to z=2
cone = openmc.Revolution(
    rz=[(0.5, 0.0), (1.0, 2.0)],
    axis='z'
)
```

### Complex Vase Shape

```python
vase_profile = [
    (0.5, 0.0),   # Narrow bottom
    (1.0, 1.0),   # Widening
    (0.8, 2.0),   # Slight narrowing
    (1.2, 3.0),   # Bulge (widest point)
    (0.3, 4.0)    # Narrow top/neck
]

vase = openmc.Revolution(rz=vase_profile, axis='z')
```

## API Reference

### Constructor

```python
openmc.Revolution(
    rz,                          # Required: list of (r, z) tuples
    axis='z',                    # Axis of revolution: 'x', 'y', or 'z'
    origin=(0., 0., 0.),         # Origin point on the axis
    boundary_type='transmission', # Boundary condition
    albedo=1.0,                  # Boundary albedo
    name='',                     # Surface name
    surface_id=None              # Unique surface ID
)
```

### Parameters

| Parameter | Type | Default | Description |
|-----------|------|---------|-------------|
| `rz` | list of 2-tuples | Required | Profile coordinates as (r, z) pairs. Minimum 2 points. |
| `axis` | str | `'z'` | Axis of revolution: `'x'`, `'y'`, or `'z'` |
| `origin` | 3-tuple | `(0., 0., 0.)` | Origin point on the revolution axis |
| `boundary_type` | str | `'transmission'` | One of: `'transmission'`, `'vacuum'`, `'reflective'`, `'white'` |
| `albedo` | float | `1.0` | Albedo for reflective boundaries |
| `name` | str | `''` | Optional descriptive name |
| `surface_id` | int | None | Unique identifier (auto-assigned if None) |

### Properties

```python
surface.rz           # Get/set profile points
surface.axis         # Get axis ('x', 'y', or 'z')
surface.origin       # Get/set origin as (x0, y0, z0)
surface.x0           # Origin x-coordinate
surface.y0           # Origin y-coordinate
surface.z0           # Origin z-coordinate
surface.type         # Returns 'solid-of-revolution'
surface.boundary_type # Get/set boundary condition
surface.albedo       # Get/set albedo value
```

### Methods

```python
# Evaluate surface equation at a point
# Returns: negative if inside, positive if outside, zero on surface
value = surface.evaluate((x, y, z))

# Translate the surface by a vector
translated_surface = surface.translate((dx, dy, dz))

# Get bounding box
# side: '-' for inside (negative halfspace), '+' for outside
lower_left, upper_right = surface.bounding_box(side)

# Export to XML
xml_element = surface.to_xml_element()

# Create from coefficient array
surface = openmc.Revolution.from_coefficients(coeffs)
```

## Examples

### Example 1: Simple Container

```python
import openmc

# Materials
water = openmc.Material()
water.add_nuclide('H1', 2.0)
water.add_nuclide('O16', 1.0)
water.set_density('g/cm3', 1.0)

steel = openmc.Material()
steel.add_element('Fe', 1.0)
steel.set_density('g/cm3', 7.8)

materials = openmc.Materials([water, steel])
materials.export_to_xml()

# Create a cylindrical container with walls
# Inner surface (water region)
inner_profile = [(4.0, 0.0), (4.0, 10.0)]
inner_surface = openmc.Revolution(rz=inner_profile, axis='z', name='Inner')

# Outer surface (steel wall)
outer_profile = [(5.0, -1.0), (5.0, 11.0)]
outer_surface = openmc.Revolution(rz=outer_profile, axis='z', name='Outer')

# Bottom and top planes
bottom = openmc.ZPlane(z0=0.0)
top = openmc.ZPlane(z0=10.0)
outer_bottom = openmc.ZPlane(z0=-1.0, boundary_type='vacuum')
outer_top = openmc.ZPlane(z0=11.0, boundary_type='vacuum')

# Cells
water_cell = openmc.Cell(name='Water', fill=water)
water_cell.region = -inner_surface & +bottom & -top

wall_cell = openmc.Cell(name='Steel Wall', fill=steel)
wall_cell.region = (+inner_surface & -outer_surface & +outer_bottom & -outer_top) | \
                   (-inner_surface & -bottom & +outer_bottom) | \
                   (-inner_surface & +top & -outer_top)

outer_cell = openmc.Cell(name='Outside')
outer_cell.region = +outer_surface | +outer_top | -outer_bottom

universe = openmc.Universe(cells=[water_cell, wall_cell, outer_cell])
geometry = openmc.Geometry(universe)
geometry.export_to_xml()
```

### Example 2: Vase-Shaped Container with Sphere Inside

```python
import openmc

# Materials
aluminum = openmc.Material(name='Aluminum')
aluminum.add_element('Al', 1.0)
aluminum.set_density('g/cm3', 2.7)

heu = openmc.Material(name='HEU')
heu.add_nuclide('U235', 0.93)
heu.add_nuclide('U238', 0.07)
heu.set_density('g/cm3', 18.7)

air = openmc.Material(name='Air')
air.add_element('N', 0.78)
air.add_element('O', 0.22)
air.set_density('g/cm3', 0.001225)

materials = openmc.Materials([aluminum, heu, air])
materials.export_to_xml()

# Vase profiles
wall_thickness = 0.5

outer_profile = [
    (2.0, 0.0),     # Base
    (4.0, 2.0),     # Widening
    (5.0, 5.0),     # Maximum width
    (4.0, 8.0),     # Narrowing
    (3.0, 10.0),    # Neck
    (3.5, 11.0),    # Flared rim
]

# Inner profile (offset by wall thickness)
inner_profile = [
    (1.5, 0.5),     # Base (with bottom thickness)
    (3.5, 2.0),
    (4.5, 5.0),
    (3.5, 8.0),
    (2.5, 10.0),
    (3.0, 10.5),    # Inner rim
]

outer_vase = openmc.Revolution(rz=outer_profile, axis='z', name='Outer Vase')
inner_vase = openmc.Revolution(rz=inner_profile, axis='z', name='Inner Vase')

# HEU sphere inside the vase
sphere = openmc.Sphere(x0=0, y0=0, z0=5.0, r=2.0, name='HEU Sphere')

# Bounding surfaces
bottom_plane = openmc.ZPlane(z0=0.0, boundary_type='vacuum')
top_plane = openmc.ZPlane(z0=11.0, boundary_type='vacuum')
outer_cyl = openmc.ZCylinder(r=6.0, boundary_type='vacuum')

# Cells
heu_cell = openmc.Cell(name='HEU Sphere', fill=heu)
heu_cell.region = -sphere

vase_wall = openmc.Cell(name='Vase Wall', fill=aluminum)
vase_wall.region = -outer_vase & +inner_vase & +bottom_plane & -top_plane

air_inside = openmc.Cell(name='Air Inside Vase', fill=air)
air_inside.region = -inner_vase & +sphere & +bottom_plane & -top_plane

air_outside = openmc.Cell(name='Air Outside', fill=air)
air_outside.region = +outer_vase & -outer_cyl & +bottom_plane & -top_plane

universe = openmc.Universe(cells=[heu_cell, vase_wall, air_inside, air_outside])
geometry = openmc.Geometry(universe)
geometry.export_to_xml()

# Settings
settings = openmc.Settings()
settings.batches = 100
settings.inactive = 20
settings.particles = 5000
settings.source = openmc.IndependentSource(
    space=openmc.stats.Point((0, 0, 5))
)
settings.export_to_xml()

# Create plots
plot_xz = openmc.Plot()
plot_xz.basis = 'xz'
plot_xz.origin = (0, 0, 5.5)
plot_xz.width = (14, 14)
plot_xz.pixels = (700, 700)
plot_xz.color_by = 'material'

plot_xy = openmc.Plot()
plot_xy.basis = 'xy'
plot_xy.origin = (0, 0, 5.0)
plot_xy.width = (14, 14)
plot_xy.pixels = (700, 700)
plot_xy.color_by = 'material'

plots = openmc.Plots([plot_xz, plot_xy])
plots.export_to_xml()
```

### Example 3: Different Axes

```python
import openmc

# Revolution around X-axis (horizontal cylinder/cone)
x_rev = openmc.Revolution(
    rz=[(1.0, 0.0), (2.0, 5.0)],
    axis='x',
    origin=(0., 0., 0.)
)

# Revolution around Y-axis
y_rev = openmc.Revolution(
    rz=[(1.0, 0.0), (1.0, 5.0)],
    axis='y',
    origin=(0., 0., 0.)
)

# Revolution around Z-axis (default)
z_rev = openmc.Revolution(
    rz=[(1.0, 0.0), (1.0, 5.0)],
    axis='z'
)
```

### Example 4: Translated Origin

```python
import openmc

# Vase centered at (10, 10, 0) instead of origin
profile = [
    (1.0, 0.0),
    (2.0, 3.0),
    (1.5, 5.0),
]

vase = openmc.Revolution(
    rz=profile,
    axis='z',
    origin=(10., 10., 0.)
)

# Or translate after creation
vase_at_origin = openmc.Revolution(rz=profile, axis='z')
vase_translated = vase_at_origin.translate((10., 10., 0.))
```

### Example 5: Nozzle/Funnel Shape

```python
import openmc

# Funnel profile
funnel_profile = [
    (0.5, 0.0),    # Narrow outlet
    (0.5, 2.0),    # Straight section
    (2.0, 3.0),    # Transition
    (4.0, 5.0),    # Wide inlet
    (4.0, 6.0),    # Inlet lip
]

funnel = openmc.Revolution(
    rz=funnel_profile,
    axis='z',
    name='Funnel'
)
```

## Halfspace Operations

Revolution surfaces define inside (negative halfspace) and outside (positive halfspace):

```python
rev_surface = openmc.Revolution(rz=[(1.0, 0.0), (1.0, 5.0)], axis='z')

# Inside the revolution surface (negative halfspace)
inside_region = -rev_surface

# Outside the revolution surface (positive halfspace)
outside_region = +rev_surface

# Combine with other surfaces
bottom = openmc.ZPlane(z0=0.0)
top = openmc.ZPlane(z0=5.0)

# Region inside cylinder, between planes
cell_region = -rev_surface & +bottom & -top
```

## XML Format

Revolution surfaces can be defined in XML:

```xml
<surface id="1" type="solid-of-revolution" boundary="vacuum" name="Vase">
  <!-- coeffs format: x0 y0 z0 axis_code n_points r1 z1 r2 z2 ... -->
  <!-- axis_code: 0=x, 1=y, 2=z -->
  <coeffs>0.0 0.0 0.0 2 4 1.0 0.0 2.0 2.0 1.5 4.0 1.0 5.0</coeffs>
</surface>
```

## Tips and Best Practices

1. **Order profile points**: Points should generally be ordered by increasing z-coordinate for clarity.

2. **Close shapes properly**: To create a closed container, ensure the first and/or last r values are 0, or use additional planes.

3. **Wall thickness**: For containers with walls, create two Revolution surfaces (inner and outer) with offset profiles.

4. **Avoid zero-length segments**: Don't use consecutive points with the same z-value unless intentional.

5. **Non-negative radii**: All r values must be >= 0. The axis of revolution is at r = 0.

6. **Combine with planes**: Use ZPlane, XPlane, or YPlane surfaces to cap open ends of revolution shapes.

7. **Visualization**: Always create plots to verify your geometry looks correct before running simulations.

## Limitations

- Profile segments are always straight lines (no curves between points)
- Cannot create shapes with negative radii or internal voids directly (use multiple surfaces)
- All segments share the same axis of revolution

## See Also

- `openmc.Surface` - Base surface class
- `openmc.ZCylinder`, `openmc.Cone` - Simpler alternatives for basic shapes
- `openmc.Plot` - Visualization tools
- `examples/` directory for more examples
