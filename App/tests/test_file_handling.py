from calc.calculator import Calculator
from file_handler.read_data import *

AdditionPath = "/home/myuser/data/addition_test.csv"

def test_calculation_addition():
    """testing that our calculator has a static method for addition"""
    df = read_data(AdditionPath)
    for i in range(len(df)):
        a = df.iat[i, 0]
        b = df.iat[i, 1]
        c = df.iat[i, 2]
        d = df.iat[i, 3]
        my_tuple = (a,b,c)
        Calculator.add_numbers(my_tuple)
        print(Calculator.get_last_result_value(), float(d))
        assert Calculator.get_last_result_value() == float(d)
