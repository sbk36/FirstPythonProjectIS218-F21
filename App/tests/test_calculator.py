"""
Test some arithmetic functions
"""

import pytest
from calc_mod.calculator import Calculator

def test_zero_division():
    """test_zero_division"""
    with pytest.raises(ZeroDivisionError):
        calculator = Calculator()
        calculator.divide(4,0)

def test_division():
    """test_division"""
    calculator = Calculator()
    answer = calculator.divide(4, 2)
    assert answer == 2

def test_simple_instance():
    """test_simple_instance"""
    calculator = Calculator()
    isinstance(calculator,Calculator)

def test_calculator_add():
    """Test Addition"""
    calculator = Calculator()
    answer = calculator.add(1,2)
    assert answer == 3

def test_calculator_subtract():
    """Test Subtraction"""
    calculator = Calculator()
    answer = calculator.subtract(1,2)
    assert answer == -1

def test_calculator_multiply():
    """Test Multiplication"""
    calculator = Calculator()
    answer = calculator.multiply(6,2)
    assert answer == 12
