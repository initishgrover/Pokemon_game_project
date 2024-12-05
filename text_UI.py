# ECOR 1042 Lab 6 - Template text UI
# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nitish Grover"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101324174"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-77"

#==========================================#
# Place your script for your text_UI after this line
from load_data import*
from sort import*
from histogram import*
from curve_fit import*
import ast


def commands():
    print('The available commands are Load Data, Sort Data, Curve fit, Histogram, Exit')


valid_commands = ['l', 's', 'c', 'h', 'e']
commands()
command = input('please type your command: ')
data_loaded = False
while command.lower() != 'e':
    if command not in valid_commands:
        print('Invalid command')
    if command.lower() == 'l':
        file_name = input('please enter the file name: ')
        attribute_name = input(
            'please enter the attribute name to use as a filter: ')
        attribute_value = input('please enter the value of attribute: ')
        result = load_data(file_name, (attribute_name, attribute_value))
        print('Data Loaded')
        data_loaded = True

    if command.lower() == 's':
        if not data_loaded:
            print('file not loaded load file first')
        else:
            sorting_attribute = input(
                'please enter the attribute you want to use for sorting: ')
            sorting_order = input('Ascending (A) or Descending (D) order: ')
            user_command = input(
                'Data Sorted. Do you want to display the data?: ')
            sorting_result = sort(result, sorting_order, sorting_attribute)
            print(sorting_result)

    if command.lower() == 'c':
        if not data_loaded:
            print("File not loaded. Please, load a file first.")
        curve_list = input(
            "Please enter the list of health dictionaries you want to curve fit: ")
        attribute = input(
            "Please enter the attribute you want to use to find the best fit for Health: ")
        order = int(
            input("Please enter the order of the polynomial to be fitted: "))
        print(curve_fit(ast.literal_eval(curve_list), attribute, order))

    if command.lower() == 'h':
        attribute_ = input(
            'please enter the attribute you want to use for plotting: ')
        his_result = histogram(result, attribute_)
        print(his_result)

    commands()

    command = input('please type your command: ')




