import pytest
from calc_mod.calculator import Calculator

def test_zero_division():
    with pytest.raises(ZeroDivisionError):
        1 / 0

def test_simple_instance():
    calculator = Calculator()
    isinstance(calculator,Calculator)

def test_calculator_add():
    calculator = Calculator()
    answer = calculator.add(1,2)
    assert answer == 3

def test_calculator_subtract():
    calculator = Calculator()
    answer = calculator.subtract(1,2)

    assert answer == -1

def test_calculator_multiply():
    calculator = Calculator()
    answer = calculator.multiply(6,2)

    assert answer == 12

def test_calculator_divide():
    calculator = Calculator()
    answer = calculator.divide(4,2)
    assert answer == 2




