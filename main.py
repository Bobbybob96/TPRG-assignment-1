"""
main.py - Area/Volume Calculator Main Program
Author: Thomas Heine
Student ID: 100777741
Date: October 17th 2025
Purpose: Menu-driven interface for calculating volumes of various 3D shapes
"""

import shapedef


def get_float_input(prompt):
    """
    Get a valid float input from the user.

    Args:
        prompt: Message to display to user

    Returns:
        float: Valid float value, or None if invalid
    """
    try:
        value = float(input(prompt))
        if value < 0:
            print("Error: Please enter a positive number.")
            return None
        return value
    except ValueError as e:
        print(f"Error: Please enter a valid number. {e}")
        return None


def calculate_box():
    """Calculate volume of a box."""
    try:
        length = get_float_input("Enter length: ")
        if length is None:
            return
        width = get_float_input("Enter width: ")
        if width is None:
            return
        height = get_float_input("Enter height: ")
        if height is None:
            return
        result = shapedef.volume_box(length, width, height)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating box volume: {e}\n")


def calculate_cone():
    """Calculate volume of a cone."""
    try:
        radius = get_float_input("Enter radius: ")
        if radius is None:
            return
        height = get_float_input("Enter height: ")
        if height is None:
            return
        result = shapedef.volume_cone(radius, height)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating cone volume: {e}\n")


def calculate_sphere():
    """Calculate volume of a sphere."""
    try:
        radius = get_float_input("Enter radius: ")
        if radius is None:
            return
        result = shapedef.volume_sphere(radius)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating sphere volume: {e}\n")


def calculate_cylinder():
    """Calculate volume of a cylinder."""
    try:
        radius = get_float_input("Enter radius: ")
        if radius is None:
            return
        height = get_float_input("Enter height: ")
        if height is None:
            return
        result = shapedef.volume_cylinder(radius, height)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating cylinder volume: {e}\n")


def calculate_torus():
    """Calculate volume of a torus (donut)."""
    try:
        small_radius = get_float_input("Enter small radius (r): ")
        if small_radius is None:
            return
        large_radius = get_float_input("Enter large radius (R): ")
        if large_radius is None:
            return
        result = shapedef.volume_torus(small_radius, large_radius)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating torus volume: {e}\n")


def calculate_pyramid():
    """Calculate volume of a square pyramid."""
    try:
        base = get_float_input("Enter base side length: ")
        if base is None:
            return
        height = get_float_input("Enter height: ")
        if height is None:
            return
        result = shapedef.volume_square_pyramid(base, height)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating pyramid volume: {e}\n")


def calculate_tetrahedron():
    """Calculate volume of an equilateral tetrahedron."""
    try:
        edge = get_float_input("Enter edge length: ")
        if edge is None:
            return
        result = shapedef.volume_equilateral_tetrahedron(edge)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating tetrahedron volume: {e}\n")


def calculate_ring():
    """Calculate volume of a ring (hollow cylinder)."""
    try:
        outer_radius = get_float_input("Enter outer radius: ")
        if outer_radius is None:
            return
        inner_radius = get_float_input("Enter inner radius: ")
        if inner_radius is None:
            return
        height = get_float_input("Enter height: ")
        if height is None:
            return
        result = shapedef.volume_ring(outer_radius, inner_radius, height)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating ring volume: {e}\n")


def calculate_half_sphere():
    """Calculate volume of a half sphere (hemisphere)."""
    try:
        radius = get_float_input("Enter radius: ")
        if radius is None:
            return
        result = shapedef.volume_half_sphere(radius)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating hemisphere volume: {e}\n")


def calculate_triangular_prism():
    """Calculate volume of a triangular prism."""
    try:
        base = get_float_input("Enter triangle base: ")
        if base is None:
            return
        tri_height = get_float_input("Enter triangle height: ")
        if tri_height is None:
            return
        prism_height = get_float_input("Enter prism height: ")
        if prism_height is None:
            return
        result = shapedef.volume_triangular_prism(base, tri_height,
                                                   prism_height)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating triangular prism volume: {e}\n")


def calculate_octahedron():
    """Calculate volume of a regular octahedron."""
    try:
        edge = get_float_input("Enter edge length: ")
        if edge is None:
            return
        result = shapedef.volume_octahedron(edge)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating octahedron volume: {e}\n")


def calculate_hexagonal_prism():
    """Calculate volume of a regular hexagonal prism."""
    try:
        edge = get_float_input("Enter hexagon edge length: ")
        if edge is None:
            return
        height = get_float_input("Enter prism height: ")
        if height is None:
            return
        result = shapedef.volume_hexagonal_prism(edge, height)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating hexagonal prism volume: {e}\n")


def calculate_icosahedron():
    """Calculate volume of a regular icosahedron."""
    try:
        edge = get_float_input("Enter edge length: ")
        if edge is None:
            return
        result = shapedef.volume_icosahedron(edge)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating icosahedron volume: {e}\n")


def calculate_truncated_cone():
    """Calculate volume of a truncated cone (frustum)."""
    try:
        radius_bottom = get_float_input("Enter bottom radius: ")
        if radius_bottom is None:
            return
        radius_top = get_float_input("Enter top radius: ")
        if radius_top is None:
            return
        height = get_float_input("Enter height: ")
        if height is None:
            return
        result = shapedef.volume_truncated_cone(radius_bottom, radius_top,
                                                 height)
        print(f"Result: {result}\n")
    except ValueError as e:
        print(f"Error calculating truncated cone volume: {e}\n")


def display_menu():
    """Display the main menu."""
    current_mode = "CALCULATED" if shapedef.CALCULATED_VIEW else "DEFAULT"
    print("\n" + "="*50)
    print("       A/V CALCULATOR MENU")
    print("="*50)
    print("Q/q - Quit the program")
    print("V/v - Change to CALCULATED view")
    print("D/d - Change to DEFAULT view")
    print(f"Current View Mode: {current_mode}")
    print("-"*50)
    print("1  - Volume of Box")
    print("2  - Volume of Cone")
    print("3  - Volume of Sphere")
    print("4  - Volume of Cylinder")
    print("5  - Volume of Torus (Donut)")
    print("6  - Volume of Square Pyramid")
    print("7  - Volume of Equilateral Tetrahedron")
    print("8  - Volume of Ring")
    print("9  - Volume of Half Sphere (Hemisphere)")
    print("10 - Volume of Triangular Prism")
    print("11 - Volume of Octahedron")
    print("12 - Volume of Hexagonal Prism")
    print("13 - Volume of Icosahedron")
    print("14 - Volume of Truncated Cone")
    print("="*50)


def handle_menu_choice(choice):
    """
    Handle menu choice and execute corresponding calculation.

    Args:
        choice: User's menu selection
    """
    menu_actions = {
        '1': calculate_box,
        '2': calculate_cone,
        '3': calculate_sphere,
        '4': calculate_cylinder,
        '5': calculate_torus,
        '6': calculate_pyramid,
        '7': calculate_tetrahedron,
        '8': calculate_ring,
        '9': calculate_half_sphere,
        '10': calculate_triangular_prism,
        '11': calculate_octahedron,
        '12': calculate_hexagonal_prism,
        '13': calculate_icosahedron,
        '14': calculate_truncated_cone,
    }

    if choice in menu_actions:
        menu_actions[choice]()
    elif choice == 'q':
        shapedef.CALCULATED_VIEW = False
        print("\nThank you for using the calculator. Goodbye!\n")
        return False
    elif choice == 'v':
        shapedef.CALCULATED_VIEW = True
        print("View mode set to CALCULATED VIEW.\n")
    elif choice == 'd':
        shapedef.CALCULATED_VIEW = False
        print("View mode set to DEFAULT VIEW.\n")
    else:
        print("Error: Invalid input. Please try again.\n")

    return True


def main():
    """Main program loop."""
    print("Welcome to the Area/Volume Calculator!")
    running = True
    while running:
        try:
            display_menu()
            choice = input("Enter your choice: ").strip().lower()
            running = handle_menu_choice(choice)
        except KeyboardInterrupt:
            print("\n\nProgram interrupted by user. Exiting...\n")
            break
        except ValueError as e:
            print(f"An error occurred: {e}\n")


if __name__ == "__main__":
    main()
