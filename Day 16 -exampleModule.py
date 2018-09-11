# example Module

itsAVarible = "Nihil"

sayHi = lambda x : print("Hello dear", x)

def h2so4(*arg):
    """
    Toplama islemi yapar.

    """
    result = 0
    for number in arg:
        result += number

    return result