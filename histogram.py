# ECOR 1042 Lab 6 - Template submission for histogram

# Remember to include docstring and type annotations for your functions

# Update "" with your name (e.g., Cristina Ruiz Martin)
__author__ = "Nitish Grover "

# Update "" with your student number (e.g., 100100100)
__student_number__ = "101324174"

# Update "" with your team (e.g. T-102, use the notation provided in the example)
__team__ = "T-77"

#==========================================#
# Place your histogram function after this line
import matplotlib.pyplot as plt


def histogram(a: list[dict], b: str):
    fig1 = plt.figure()
    plt.title("Simple Bar")
    plt.xlabel(b)
    returned = 0
    plt.ylabel('# of charachters:')
    x = []
    y = []

    for i in range(len(a)):
        if type(a[i][b]) is str:
            returned = -1
        if a[i][b] in x:
            for j in range(len(x)):
                if a[i][b] == x[j]:
                    y[j] += 1
                    break
        else:
            x.append(a[i][b])
            y.append(1)

    plt.bar(x, y, color='green')
    plt.show()

    if returned == -1:
        return returned
    else:
        return max(x)

        # Do NOT include a main script in your submission

