"""
test_shapedef.py - Unit Tests for Volume Calculator
Author: Thomas Heine
Student ID: 100777741
Date: October 17th 2025
Purpose: Test all volume calculation functions using pytest
"""

import math
import shapedef


class TestVolumeBox:
    """Tests for volume_box function."""

    def test_volume_box_basic(self):
        """Test basic box volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_box(6, 2, 3)
        assert "6 * 2 * 3 = 36" in result

    def test_volume_box_second(self):
        """Test second box volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_box(4, 5, 1)
        assert "4 * 5 * 1 = 20" in result

    def test_volume_box_third(self):
        """Test third box volume calculation with decimals."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_box(2.5, 2, 4)
        assert "2.5 * 2 * 4 = 20.0" in result

    def test_volume_box_calculated_view(self):
        """Test box volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_box(3, 3, 3)
        assert "(l * w * h)" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeCone:
    """Tests for volume_cone function."""

    def test_volume_cone_basic(self):
        """Test basic cone volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_cone(3, 5)
        expected = round((1/3) * math.pi * 3**2 * 5, 2)
        assert str(expected) in result

    def test_volume_cone_second(self):
        """Test second cone volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_cone(2, 10)
        expected = round((1/3) * math.pi * 2**2 * 10, 2)
        assert str(expected) in result

    def test_volume_cone_third(self):
        """Test third cone volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_cone(4, 6)
        expected = round((1/3) * math.pi * 4**2 * 6, 2)
        assert str(expected) in result

    def test_volume_cone_calculated_view(self):
        """Test cone volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_cone(3, 5)
        assert "((1/3)*π*r²*h)" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeSphere:
    """Tests for volume_sphere function."""

    def test_volume_sphere_basic(self):
        """Test basic sphere volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_sphere(3)
        expected = round((4/3) * math.pi * 3**3, 2)
        assert str(expected) in result

    def test_volume_sphere_second(self):
        """Test second sphere volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_sphere(1)
        expected = round((4/3) * math.pi * 1**3, 2)
        assert str(expected) in result

    def test_volume_sphere_third(self):
        """Test third sphere volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_sphere(5)
        expected = round((4/3) * math.pi * 5**3, 2)
        assert str(expected) in result

    def test_volume_sphere_calculated_view(self):
        """Test sphere volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_sphere(2)
        assert "((4/3)*π*r³)" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeCylinder:
    """Tests for volume_cylinder function."""

    def test_volume_cylinder_basic(self):
        """Test basic cylinder volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_cylinder(2, 4)
        expected = round(math.pi * 2**2 * 4, 2)
        assert str(expected) in result

    def test_volume_cylinder_second(self):
        """Test second cylinder volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_cylinder(3, 5)
        expected = round(math.pi * 3**2 * 5, 2)
        assert str(expected) in result

    def test_volume_cylinder_third(self):
        """Test third cylinder volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_cylinder(1, 10)
        expected = round(math.pi * 1**2 * 10, 2)
        assert str(expected) in result

    def test_volume_cylinder_calculated_view(self):
        """Test cylinder volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_cylinder(2, 4)
        assert "(π*r²*h)" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeTorus:
    """Tests for volume_torus function."""

    def test_volume_torus_basic(self):
        """Test basic torus volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_torus(1, 3)
        expected = round((math.pi * 1**2) * (2 * math.pi * 3), 2)
        assert str(expected) in result

    def test_volume_torus_second(self):
        """Test second torus volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_torus(2, 4)
        expected = round((math.pi * 2**2) * (2 * math.pi * 4), 2)
        assert str(expected) in result

    def test_volume_torus_third(self):
        """Test third torus volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_torus(1.5, 5)
        expected = round((math.pi * 1.5**2) * (2 * math.pi * 5), 2)
        assert str(expected) in result

    def test_volume_torus_calculated_view(self):
        """Test torus volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_torus(1, 3)
        assert "((π*r²)*(2πR))" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeSquarePyramid:
    """Tests for volume_square_pyramid function."""

    def test_volume_pyramid_basic(self):
        """Test basic pyramid volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_square_pyramid(4, 9)
        expected = round((1/3) * 4**2 * 9, 2)
        assert str(expected) in result

    def test_volume_pyramid_second(self):
        """Test second pyramid volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_square_pyramid(5, 6)
        expected = round((1/3) * 5**2 * 6, 2)
        assert str(expected) in result

    def test_volume_pyramid_third(self):
        """Test third pyramid volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_square_pyramid(3, 12)
        expected = round((1/3) * 3**2 * 12, 2)
        assert str(expected) in result

    def test_volume_pyramid_calculated_view(self):
        """Test pyramid volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_square_pyramid(4, 9)
        assert "((1/3)*b²*h)" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeEquilateralTetrahedron:
    """Tests for volume_equilateral_tetrahedron function."""

    def test_volume_tetrahedron_basic(self):
        """Test basic tetrahedron volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_equilateral_tetrahedron(2)
        expected = round((2**3) / (6 * math.sqrt(2)), 2)
        assert str(expected) in result

    def test_volume_tetrahedron_second(self):
        """Test second tetrahedron volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_equilateral_tetrahedron(4)
        expected = round((4**3) / (6 * math.sqrt(2)), 2)
        assert str(expected) in result

    def test_volume_tetrahedron_third(self):
        """Test third tetrahedron volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_equilateral_tetrahedron(3)
        expected = round((3**3) / (6 * math.sqrt(2)), 2)
        assert str(expected) in result

    def test_volume_tetrahedron_calculated_view(self):
        """Test tetrahedron volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_equilateral_tetrahedron(2)
        assert "(a³ / (6√2))" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeRing:
    """Tests for volume_ring function."""

    def test_volume_ring_basic(self):
        """Test basic ring volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_ring(5, 3, 2)
        expected = round(math.pi * 2 * (5**2 - 3**2), 2)
        assert str(expected) in result

    def test_volume_ring_second(self):
        """Test second ring volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_ring(4, 2, 3)
        expected = round(math.pi * 3 * (4**2 - 2**2), 2)
        assert str(expected) in result

    def test_volume_ring_third(self):
        """Test third ring volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_ring(6, 4, 1.5)
        expected = round(math.pi * 1.5 * (6**2 - 4**2), 2)
        assert str(expected) in result

    def test_volume_ring_calculated_view(self):
        """Test ring volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_ring(5, 3, 2)
        assert "(π*h*(R²-r²))" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeHalfSphere:
    """Tests for volume_half_sphere function."""

    def test_volume_half_sphere_basic(self):
        """Test basic hemisphere volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_half_sphere(3)
        expected = round((2/3) * math.pi * 3**3, 2)
        assert str(expected) in result

    def test_volume_half_sphere_second(self):
        """Test second hemisphere volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_half_sphere(2)
        expected = round((2/3) * math.pi * 2**3, 2)
        assert str(expected) in result

    def test_volume_half_sphere_third(self):
        """Test third hemisphere volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_half_sphere(4)
        expected = round((2/3) * math.pi * 4**3, 2)
        assert str(expected) in result

    def test_volume_half_sphere_calculated_view(self):
        """Test hemisphere volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_half_sphere(3)
        assert "((2/3)*π*r³)" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeTriangularPrism:
    """Tests for volume_triangular_prism function."""

    def test_volume_triangular_prism_basic(self):
        """Test basic triangular prism volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_triangular_prism(4, 3, 5)
        expected = round((1/2) * 4 * 3 * 5, 2)
        assert str(expected) in result

    def test_volume_triangular_prism_second(self):
        """Test second triangular prism volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_triangular_prism(6, 4, 8)
        expected = round((1/2) * 6 * 4 * 8, 2)
        assert str(expected) in result

    def test_volume_triangular_prism_third(self):
        """Test third triangular prism volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_triangular_prism(5, 3, 7)
        expected = round((1/2) * 5 * 3 * 7, 2)
        assert str(expected) in result

    def test_volume_triangular_prism_calculated_view(self):
        """Test triangular prism volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_triangular_prism(4, 3, 5)
        assert "((1/2)*b*h*pH)" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeOctahedron:
    """Tests for volume_octahedron function."""

    def test_volume_octahedron_basic(self):
        """Test basic octahedron volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_octahedron(2)
        expected = round((math.sqrt(2) / 3) * 2**3, 2)
        assert str(expected) in result

    def test_volume_octahedron_second(self):
        """Test second octahedron volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_octahedron(3)
        expected = round((math.sqrt(2) / 3) * 3**3, 2)
        assert str(expected) in result

    def test_volume_octahedron_third(self):
        """Test third octahedron volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_octahedron(4)
        expected = round((math.sqrt(2) / 3) * 4**3, 2)
        assert str(expected) in result

    def test_volume_octahedron_calculated_view(self):
        """Test octahedron volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_octahedron(2)
        assert "((√2/3)*a³)" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeHexagonalPrism:
    """Tests for volume_hexagonal_prism function."""

    def test_volume_hexagonal_prism_basic(self):
        """Test basic hexagonal prism volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_hexagonal_prism(2, 5)
        expected = round((3 * math.sqrt(3) / 2) * 2**2 * 5, 2)
        assert str(expected) in result

    def test_volume_hexagonal_prism_second(self):
        """Test second hexagonal prism volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_hexagonal_prism(3, 4)
        expected = round((3 * math.sqrt(3) / 2) * 3**2 * 4, 2)
        assert str(expected) in result

    def test_volume_hexagonal_prism_third(self):
        """Test third hexagonal prism volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_hexagonal_prism(1, 6)
        expected = round((3 * math.sqrt(3) / 2) * 1**2 * 6, 2)
        assert str(expected) in result

    def test_volume_hexagonal_prism_calculated_view(self):
        """Test hexagonal prism volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_hexagonal_prism(2, 5)
        assert "((3√3/2)*a²*h)" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeIcosahedron:
    """Tests for volume_icosahedron function."""

    def test_volume_icosahedron_basic(self):
        """Test basic icosahedron volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_icosahedron(2)
        expected = round((5 * (3 + math.sqrt(5)) / 12) * 2**3, 2)
        assert str(expected) in result

    def test_volume_icosahedron_second(self):
        """Test second icosahedron volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_icosahedron(3)
        expected = round((5 * (3 + math.sqrt(5)) / 12) * 3**3, 2)
        assert str(expected) in result

    def test_volume_icosahedron_third(self):
        """Test third icosahedron volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_icosahedron(1)
        expected = round((5 * (3 + math.sqrt(5)) / 12) * 1**3, 2)
        assert str(expected) in result

    def test_volume_icosahedron_calculated_view(self):
        """Test icosahedron volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_icosahedron(2)
        assert "((5*(3+√5)/12)*a³)" in result
        shapedef.CALCULATED_VIEW = False


class TestVolumeTruncatedCone:
    """Tests for volume_truncated_cone function."""

    def test_volume_truncated_cone_basic(self):
        """Test basic truncated cone volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_truncated_cone(4, 2, 3)
        expected = round((1/3) * math.pi * 3 * (4**2 + 4*2 + 2**2), 2)
        assert str(expected) in result

    def test_volume_truncated_cone_second(self):
        """Test second truncated cone volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_truncated_cone(5, 3, 4)
        expected = round((1/3) * math.pi * 4 * (5**2 + 5*3 + 3**2), 2)
        assert str(expected) in result

    def test_volume_truncated_cone_third(self):
        """Test third truncated cone volume calculation."""
        shapedef.CALCULATED_VIEW = False
        result = shapedef.volume_truncated_cone(3, 1, 2)
        expected = round((1/3) * math.pi * 2 * (3**2 + 3*1 + 1**2), 2)
        assert str(expected) in result

    def test_volume_truncated_cone_calculated_view(self):
        """Test truncated cone volume with calculated view enabled."""
        shapedef.CALCULATED_VIEW = True
        result = shapedef.volume_truncated_cone(4, 2, 3)
        assert "((1/3)*π*h*(R²+R*r+r²))" in result
        shapedef.CALCULATED_VIEW = False
