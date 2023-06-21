import logging
## Now we'll give a filename, where our logging messages will reside
## This will create a file with the given name on our current directory
## Example 1
# logging.basicConfig(filename = 'test.log',level = logging.DEBUG)

# def add(x,y):
#     return x+y

# def subtract(x,y):
#     return x-y

# def multiply(x,y):
#     return x*y

# def divide(x,y):
#     return x/y


# num1 = 10
# num2 = 5


# add_result = add(num1, num2)
# logging.debug(f"add: {num1} + {num2} = {add_result}")

# subtract_result = subtract(num1, num2)
# logging.debug(f"subtract: {num1} - {num2} = {subtract_result}")

# multiply_result = multiply(num1, num2)
# logging.debug(f"multiply: {num1} * {num2} = {multiply_result}")

# divide_result = divide(num1, num2)
# logging.debug(f"divide: {num1} / {num2} = {divide_result}")

## Example 2
## Now we'll change the num1, num2, it'll now update the 'test.log' file
# def add(x,y):
#     return x+y

# def subtract(x,y):
#     return x-y

# def multiply(x,y):
#     return x*y

# def divide(x,y):
#     return x/y

# logging.basicConfig(filename = 'test.log',level = logging.DEBUG)
# num1 = 20
# num2 = 10

# add_result = add(num1, num2)
# logging.debug(f"add: {num1} + {num2} = {add_result}")

# subtract_result = subtract(num1, num2)
# logging.debug(f"subtract: {num1} - {num2} = {subtract_result}")

# multiply_result = multiply(num1, num2)
# logging.debug(f"multiply: {num1} * {num2} = {multiply_result}")

# divide_result = divide(num1, num2)
# logging.debug(f"divide: {num1} / {num2} = {divide_result}")


## 3rd Example: Formatting
## We'll format our log message to understand it better
## We'll use 'Time : LogLevel: Message' format
logging.basicConfig(filename='test.log', level=logging.DEBUG,
                    format='%(asctime)s : %(levelname)s : %(message)s')


def add(x, y):
    """Add Function"""
    return x + y


def subtract(x, y):
    """Subtract Function"""
    return x - y


def multiply(x, y):
    """Multiply Function"""
    return x * y


def divide(x, y):
    """Divide Function"""
    return x / y


num_1 = 20
num_2 = 10

add_result = add(num_1, num_2)
logging.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logging.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logging.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logging.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))