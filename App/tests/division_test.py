"""Testing Division"""
from calc.calculations.division import Division

def test_calculation_division():
    """testing that our calculator has a static method for Division"""
    #Arrange
    my_numbers = (4.0,2.0)
    division = Division(my_numbers)
    #Act
    #Assert
    assert division.get_result() == 2.0
