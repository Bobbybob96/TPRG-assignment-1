"""
shapedef.py - Area/Volume Calculator Functions
Author: Thomas Heine
Student ID: 100777741
Date: October 17th 2025
Purpose: Calculate volumes of various 3D shapes
"""

import math

# View mode: False = default, True = calculated view
CALCULATED_VIEW = False


def volume_box(length, width, height):
    """
    Calculate the volume of a box (rectangular prism).
    Formula: V = l × w × h

    Args:
        length: Length of the box
        width: Width of the box
        height: Height of the box

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = length * width * height
        if CALCULATED_VIEW:
            return (f"{length} * {width} * {height} = {volume} "
                    f"(l * w * h)")
        return f"{length} * {width} * {height} = {volume}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for box dimensions - {e}"


def volume_cone(radius, height):
    """
    Calculate the volume of a cone.
    Formula: V = (1/3) × π × r² × h

    Args:
        radius: Radius of the cone's base
        height: Height of the cone

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = (1/3) * math.pi * radius**2 * height
        if CALCULATED_VIEW:
            return (f"(1/3) * π * {radius}^2 * {height} = {volume:.2f} "
                    f"((1/3)*π*r²*h)")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for cone dimensions - {e}"


def volume_sphere(radius):
    """
    Calculate the volume of a sphere.
    Formula: V = (4/3) × π × r³

    Args:
        radius: Radius of the sphere

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = (4/3) * math.pi * radius**3
        if CALCULATED_VIEW:
            return (f"(4/3) * π * {radius}^3 = {volume:.2f} "
                    f"((4/3)*π*r³)")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for sphere radius - {e}"


def volume_cylinder(radius, height):
    """
    Calculate the volume of a cylinder.
    Formula: V = π × r² × h

    Args:
        radius: Radius of the cylinder's base
        height: Height of the cylinder

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = math.pi * radius**2 * height
        if CALCULATED_VIEW:
            return (f"π * {radius}^2 * {height} = {volume:.2f} "
                    f"(π*r²*h)")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for cylinder dimensions - {e}"


def volume_torus(small_radius, large_radius):
    """
    Calculate the volume of a torus (donut shape).
    Formula: V = (π × r²) × (2π × R)

    Args:
        small_radius: Radius of the tube (small radius)
        large_radius: Radius from center to tube center (large radius)

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = (math.pi * small_radius**2) * (2 * math.pi * large_radius)
        if CALCULATED_VIEW:
            return (f"(π * {small_radius}^2) * (2 * π * {large_radius}) = "
                    f"{volume:.2f} ((π*r²)*(2πR))")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for torus dimensions - {e}"


def volume_square_pyramid(base, height):
    """
    Calculate the volume of a square pyramid.
    Formula: V = (1/3) × b² × h

    Args:
        base: Length of the base side
        height: Height of the pyramid

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = (1/3) * base**2 * height
        if CALCULATED_VIEW:
            return (f"(1/3) * {base}^2 * {height} = {volume:.2f} "
                    f"((1/3)*b²*h)")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for pyramid dimensions - {e}"


def volume_equilateral_tetrahedron(edge):
    """
    Calculate the volume of an equilateral tetrahedron.
    Formula: V = (a³) / (6 × √2)

    Args:
        edge: Length of one edge

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = (edge**3) / (6 * math.sqrt(2))
        if CALCULATED_VIEW:
            return (f"({edge}^3) / (6 * √2) = {volume:.2f} "
                    f"(a³ / (6√2))")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for tetrahedron dimensions - {e}"


def volume_ring(outer_radius, inner_radius, height):
    """
    Calculate the volume of a ring (hollow cylinder).
    Formula: V = π × h × (R² - r²)

    Args:
        outer_radius: Outer radius of the ring
        inner_radius: Inner radius of the ring
        height: Height of the ring

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = math.pi * height * (outer_radius**2 - inner_radius**2)
        if CALCULATED_VIEW:
            return (f"π * {height} * ({outer_radius}^2 - {inner_radius}^2) = "
                    f"{volume:.2f} (π*h*(R²-r²))")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for ring dimensions - {e}"


def volume_half_sphere(radius):
    """
    Calculate the volume of a half sphere (hemisphere).
    Formula: V = (2/3) × π × r³

    Args:
        radius: Radius of the hemisphere

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = (2/3) * math.pi * radius**3
        if CALCULATED_VIEW:
            return (f"(2/3) * π * {radius}^3 = {volume:.2f} "
                    f"((2/3)*π*r³)")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for hemisphere radius - {e}"


def volume_triangular_prism(base, height, prism_height):
    """
    Calculate the volume of a triangular prism.
    Formula: V = (1/2) × base × height × prism_height

    Args:
        base: Base of the triangle
        height: Height of the triangle
        prism_height: Height/length of the prism

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = (1/2) * base * height * prism_height
        if CALCULATED_VIEW:
            return (f"(1/2) * {base} * {height} * {prism_height} = "
                    f"{volume:.2f} ((1/2)*b*h*pH)")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for triangular prism dimensions - {e}"


def volume_octahedron(edge):
    """
    Calculate the volume of a regular octahedron.
    Formula: V = (√2 / 3) × a³

    Args:
        edge: Length of one edge

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = (math.sqrt(2) / 3) * edge**3
        if CALCULATED_VIEW:
            return (f"(√2 / 3) * {edge}^3 = {volume:.2f} "
                    f"((√2/3)*a³)")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for octahedron dimensions - {e}"


def volume_hexagonal_prism(edge, height):
    """
    Calculate the volume of a regular hexagonal prism.
    Formula: V = (3√3 / 2) × a² × h

    Args:
        edge: Length of one edge of the hexagon
        height: Height of the prism

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = (3 * math.sqrt(3) / 2) * edge**2 * height
        if CALCULATED_VIEW:
            return (f"(3√3 / 2) * {edge}^2 * {height} = {volume:.2f} "
                    f"((3√3/2)*a²*h)")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for hexagonal prism dimensions - {e}"


def volume_icosahedron(edge):
    """
    Calculate the volume of a regular icosahedron.
    Formula: V = (5 × (3 + √5) / 12) × a³

    Args:
        edge: Length of one edge

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = (5 * (3 + math.sqrt(5)) / 12) * edge**3
        if CALCULATED_VIEW:
            return (f"(5 * (3 + √5) / 12) * {edge}^3 = {volume:.2f} "
                    f"((5*(3+√5)/12)*a³)")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for icosahedron dimensions - {e}"


def volume_truncated_cone(radius_bottom, radius_top, height):
    """
    Calculate the volume of a truncated cone (frustum).
    Formula: V = (1/3) × π × h × (R² + R×r + r²)

    Args:
        radius_bottom: Radius of the bottom base
        radius_top: Radius of the top base
        height: Height of the truncated cone

    Returns:
        str: Formatted volume calculation result
    """
    try:
        volume = (1/3) * math.pi * height * (radius_bottom**2 +
                                             radius_bottom * radius_top +
                                             radius_top**2)
        if CALCULATED_VIEW:
            return (f"(1/3) * π * {height} * ({radius_bottom}^2 + "
                    f"{radius_bottom}*{radius_top} + {radius_top}^2) = "
                    f"{volume:.2f} ((1/3)*π*h*(R²+R*r+r²))")
        return f"{volume:.2f}"
    except (TypeError, ValueError) as e:
        return f"Error: Invalid input for truncated cone dimensions - {e}"
