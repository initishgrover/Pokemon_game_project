# ECOR 1042 Lab 6 - Template for curve_fit function

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nitish Grover"

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101324174"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-77"

#==========================================#
# Place your curve_fit function after this line
import numpy as np


def curve_fit(characters: list[dict], attribute: str, max_degree: int) -> str:

    avg_health = {}

    for item in characters:
        if attribute in item and "Health" in item:
            if item[attribute] not in avg_health:
                avg_health[item[attribute]] = [item["Health"]]
            else:
                avg_health[item[attribute]].append(item["Health"])

    for key in avg_health.keys():
        avg_health[key] = round(
            sum(avg_health[key]) / len(avg_health[key]), 2)

    x = list(avg_health.keys())
    y = list(avg_health.values())

    max_degree = int(max_degree)

    if len(x) > max_degree + 1:
        degree = max_degree
    else:
        degree = len(x) - 1

    z = np.polyfit(x, y, degree)

    s = ""
    order = len(z) - 1
    for item in z:
        if order == len(z) - 1:
            s += str(round(item, 2)) + "x^" + str(order)
        elif order > 1:
            s += " + " + str(round(item, 2)) + "x^" + str(order)
        elif order == 1:
            s += " + " + str(round(item, 2)) + "x"
        else:
            s += " + " + str(round(item, 2))
        order -= 1

    return s






