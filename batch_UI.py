# ECOR 1042 Lab 6 - Template Individual submission for batch_UI

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nitish Grover"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101324174"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-77"

#==========================================#
# Place your script for your batch_UI after this line
from load_data import *

from sort import *

from curve_fit import*

from histogram import *

import ast


user_input = input(
    "Please enter the name of the file where your commands are stored: ")
in_file = open(user_input)

input_list = []

for line in in_file:
    line = line.strip('\n').split(';')
    if line[0] == 'L':
        load_file = line[1]
        filter_term = line[2]
        target_term = line[3]
        if filter_term == 'Strength':
            target_term = tuple(map(int, target_term.split(',')))
        elif filter_term == 'Luck':
            target_term = float(target_term)
        input_list = load_data(load_file, (filter_term, target_term))
        print("Data Loaded")
    elif line[0] == 'S':
        filter_term = line[1]
        sort_order = line[2]
        display_data = line[3]
        input_list = sort(input_list, sort_order, filter_term)
        print("Data Sorted")
        if display_data == 'Y':
            print(input_list)
    elif line[0] == 'C':
        curve_list = line[1]
        target_term = line[2]
        poly_order = int(line[3])
        print(curve_fit(ast.literal_eval(curve_list), target_term, poly_order))

    elif line[0] == 'H':
        target_term = line[1]
        input_list = calculate_health(input_list)
        histogram(input_list, target_term)
in_file.close()



