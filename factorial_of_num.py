"""import math module"""
import math


def factorial_number(number):
    """printing fact of a number"""
    try:
        return math.factorial(number)
    except ValueError:
        print 'Enter positive Integer'
    except TypeError:
        print 'enter a Integer'


FACT_NUM = input("enter Number:")

# printing value
print factorial_number(FACT_NUM)
