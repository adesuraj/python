"""import math module"""

import logging
file_name = 'new_file.log'
logging.basicConfig(filename=file_name,
                    format='%(asctime)s %(message)s',
                    filemode='w')
logger = logging.getLogger()


def factorial_number(number):
    """printing fact of a number"""
    try:
        if number == 0 or number == 1:
            return 1
        else:
            if number > 0:
                return number * factorial_number(number - 1)
            else:
                raise ValueError

    except ValueError as v:
        logger.error(v.message)
        print 'Enter positive Integer', v
    except TypeError as t:
        logger.error(t.message)
        print 'enter a Integer', t

print factorial_number(4)
print factorial_number(0)
print factorial_number(1)
print factorial_number(-1)
print factorial_number('a')


