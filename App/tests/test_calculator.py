"""Testing the Calculator"""
import pprint
import pytest
from calculator.calculator import Calculator

#this is how you define a function that will run each time
# you pass it to a test, it is called a fixture

@pytest.fixture(name="clear_history")
def fixture_clear_history():
    """ clear_history"""
    Calculator.clear_history()

def test_calculator_add(clear_history):
    """Testing the Add function of the calculator"""
    # pylint: disable=unused-argument
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.get_result_of_last_calculation_added_to_history() == 6
    pprint.pprint(Calculator.history)

def test_clear_history(clear_history):
    # pylint: disable=unused-argument
    """ test_clear_history"""
    assert Calculator.add_number(1,2) == 3
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.add_number(4, 2) == 6
    assert Calculator.history_count() == 4
    assert Calculator.clear_history() is True
    assert Calculator.history_count() == 0

def test_count_history(clear_history):
    # pylint: disable=unused-argument
    """ test_count_history"""
    assert Calculator.history_count() == 0
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.history_count() == 2

def test_get_last_calculation_result(clear_history):
    # pylint: disable=unused-argument
    """ test_get_last_calculation_result"""
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_last_calculation_added_to_history() == 5

def test_get_first_calculation_result(clear_history):
    """test_get_first_calculation_result"""
    # pylint: disable=unused-argument
    assert Calculator.add_number(2, 2) == 4
    assert Calculator.add_number(3, 2) == 5
    assert Calculator.get_result_of_first_calculation_added_to_history() == 4

def test_calculator_subtract(clear_history):
    # pylint: disable=unused-argument
    """Testing the subtract method of the calculator"""
    assert Calculator.subtract_number(1, 2) == -1

def test_calculator_divide(clear_history):
    # pylint: disable=unused-argument
    """Testing the subtract method of the calculator"""
    assert Calculator.divide_numbers(4, 2) == 2

def test_calculator_multiply(clear_history):
    # pylint: disable=unused-argument
    """ tests multiplication of two numbers"""
    assert Calculator.multiply_numbers(1,2) == 2

def test_zero_divide(clear_history):
    # pylint: disable=unused-argument
    """Testing the subtract method of the calculator"""
    with pytest.raises(ZeroDivisionError):
        Calculator.divide_numbers(4, 0)
