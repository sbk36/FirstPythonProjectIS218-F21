"""Testing the Calculator"""
import time
from calc.calculator import Calculator

def perform_test_on_df(dataframe,filename,operation,operand):
    """ This function takes the csv data and performs the desired calculation on them"""
    result_list = []
    dbz_list = []
    for record_number in range(len(dataframe)):

        first_value = dataframe.iat[record_number, 0]
        second_value = dataframe.iat[record_number, 1]
        third_value = dataframe.iat[record_number, 2]
        expected_result = dataframe.iat[record_number, 3]
        time_stamp = int(time.time())
        my_tuple = (first_value, second_value, third_value)
        if operation == 'add':
            Calculator.add_numbers(my_tuple)
        elif operation == 'divide':
            if second_value == 0 or third_value == 0:
                err = "Divide By Zero"
                dbz_list.append([time_stamp,filename,record_number,err])
            else:
                Calculator.divide_numbers(my_tuple)
        elif operation == 'multiply':
            Calculator.multiply_numbers(my_tuple)
        elif operation == 'subtract':
            Calculator.subtract_numbers(my_tuple)
        returned_result = Calculator.get_last_result_value()
        result_list.append([time_stamp, filename, record_number, operand, returned_result])
    return result_list, returned_result,expected_result, dbz_list
