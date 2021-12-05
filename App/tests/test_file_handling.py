"""This function reads the csv data from data folder and performs
and tests calculation and saves the logs files in results folder"""
import os

from file_handler.read_data import pd,read_data
from App.calc.perform_test import perform_test_on_df

MAIN_PATH = os.getcwd() + "/data/"
RESULT_PATH = os.getcwd() + "/results/"


def test_file_handling():
    """This function calls the appropriate function to perform calculations"""
    print(os.getcwd())
    for filename in os.listdir(MAIN_PATH):

        column_names = ["TimeStamp", "FileName", "Record_Number", "Operation", "Result"]
        if filename == "addition_test.csv":
            perform_add_test(filename, column_names)

        elif filename == "division_test.csv":
            perform_div_test(filename,column_names)


        elif filename == "multiplication_test.csv":
            perform_mul_test(filename, column_names)


        elif filename == 'subtraction_test.csv':
            perform_sub_test(filename, column_names)


def perform_add_test(filename,column_names):
    """Reads csv addition data and performs and test calculations and stores log file in results"""
    operation = 'add'
    operand = '+'
    filepath = MAIN_PATH + filename
    data_frame = read_data(filepath)
    result_list, returned_result, \
    expected_result, dbz_list = perform_test_on_df(data_frame, filename, operation, operand)
    del dbz_list
    assert returned_result, expected_result == returned_result
    result_df = pd.DataFrame(result_list, columns=column_names)
    output_file = os.path.join(RESULT_PATH, filename)
    result_df.to_csv(output_file, index=False)


def perform_div_test(filename,column_names):
    """Reads csv division data and performs and test calculations and stores log file in results"""
    dbz_column_names = ["TimeStamp", "FileName", "Record_Number", "Error"]
    operation = 'divide'
    operation = operation.strip()
    operand = '/'
    filepath = MAIN_PATH + filename
    data_frame = read_data(filepath)
    result_list, \
    returned_result, \
    expected_result, dbz_list = perform_test_on_df(data_frame, filename, operation, operand)
    assert returned_result, expected_result == returned_result
    result_df = pd.DataFrame(result_list, columns=column_names)
    output_file = os.path.join(RESULT_PATH, filename)
    result_df.to_csv(output_file, index=False)
    dbz_list = pd.DataFrame(dbz_list, columns=dbz_column_names)
    output_file_2 = os.path.join(RESULT_PATH, "Divide_By_Zero_Error_logs.csv")
    dbz_list.to_csv(output_file_2, index=False)

def perform_mul_test(filename,column_names):
    """Reads csv multiplication data and performs and
    test calculations and stores log file in results"""
    operation = 'multiply'
    filepath = MAIN_PATH + filename
    operand = '*'
    data_frame = read_data(filepath)
    result_list, \
    returned_result, \
    expected_result, dbz_list = perform_test_on_df(data_frame, filename, operation, operand)
    del dbz_list
    assert returned_result, expected_result == returned_result
    result_df = pd.DataFrame(result_list, columns=column_names)
    output_file = os.path.join(RESULT_PATH, filename)
    result_df.to_csv(output_file, index=False)

def perform_sub_test(filename,column_names):
    """Reads csv subtraction data and performs and
    test calculations and stores log file in results"""
    operation = 'subtract'
    operand = '-'
    filepath = MAIN_PATH + filename
    data_frame = read_data(filepath)
    result_list, \
    returned_result, \
    expected_result, dbz_list = perform_test_on_df(data_frame, filename, operation, operand)
    del dbz_list
    assert returned_result == expected_result
    result_df = pd.DataFrame(result_list, columns=column_names)
    output_file = os.path.join(RESULT_PATH, filename)
    result_df.to_csv(output_file, index=False)
