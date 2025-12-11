"""
Test suite for the Calculator class.
"""

import pytest
from calculator.calculator import Calculator, InvalidInputException


class TestAddition:
    """Tests for the add method."""

    def test_add_positive_numbers(self):
        """Test adding two positive numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 3
        expected = 8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_numbers(self):
        """Test adding two negative numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = -3
        expected = -8

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_and_negative(self):
        """Test adding positive and negative numbers."""
        # Arrange
        calc = Calculator()
        a = 5
        b = -3
        expected = 2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_negative_and_positive(self):
        """Test adding negative and positive numbers."""
        # Arrange
        calc = Calculator()
        a = -5
        b = 3
        expected = -2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_positive_with_zero(self):
        """Test adding positive number with zero."""
        # Arrange
        calc = Calculator()
        a = 5
        b = 0
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_zero_with_positive(self):
        """Test adding zero with positive number."""
        # Arrange
        calc = Calculator()
        a = 0
        b = 5
        expected = 5

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == expected

    def test_add_floats(self):
        """Test adding floating point numbers."""
        # Arrange
        calc = Calculator()
        a = 2.5
        b = 3.7
        expected = 6.2

        # Act
        result = calc.add(a, b)

        # Assert
        assert result == pytest.approx(expected)


class TestSubtraction:
    """Tests for the subtract method."""

    def test_subtract_positive_numbers(self):
        """Test subtracting positive numbers."""
        calc = Calculator()
        a = 10
        b = 3
        expected = 7
        result = calc.subtract(a, b)
        assert result == expected

    def test_subtract_negative_numbers(self):
        """Test subtracting negative numbers."""
        calc = Calculator()
        a = -5
        b = -3
        expected = -2
        result = calc.subtract(a, b)
        assert result == expected

    def test_subtract_mixed_numbers(self):
        """Test subtracting mixed numbers."""
        calc = Calculator()
        a = 5
        b = -3
        expected = 8
        result = calc.subtract(a, b)
        assert result == expected

class TestMultiplication:
    """Tests for the multiply method."""

    def test_multiply_positive_numbers(self):
        """Test multiplying positive numbers."""
        calc = Calculator()
        a = 4
        b = 5
        expected = 20
        result = calc.multiply(a, b)
        assert result == expected

    def test_multiply_with_zero(self):
        """Test multiplying with zero."""
        calc = Calculator()
        a = 4
        b = 0
        expected = 0
        result = calc.multiply(a, b)
        assert result == expected

    def test_multiply_negative_numbers(self):
        """Test multiplying negative numbers."""
        calc = Calculator()
        a = -4
        b = -3
        expected = 12
        result = calc.multiply(a, b)
        assert result == expected


class TestDivision:
    """Tests for the divide method."""

    def test_divide_positive_numbers(self):
        """Test dividing positive numbers."""
        calc = Calculator()
        a = 10
        b = 2
        expected = 5
        result = calc.divide(a, b)
        assert result == expected

    def test_divide_negative_numbers(self):
        """Test dividing negative numbers."""
        calc = Calculator()
        a = 10
        b = -2
        expected = -5
        result = calc.divide(a, b)
        assert result == expected

    def test_divide_by_zero(self):
        """Test dividing by zero to raise error."""
        calc = Calculator()
        with pytest.raises(ValueError):
            calc.divide(10, 0)
