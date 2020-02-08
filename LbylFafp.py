"""
Look before you leap

It `s Easier to ASK Forgiveness Than Permission
"""


# LBYL
def divide_LBYL(x, y):
    if y == 0:
        print("Error you have attempt to divide by 0")
    else:
        return x / y


# EAFP
def divide_EAFP(x, y):

    try:
        return x / y
    except ZeroDivisionError:
        pass
