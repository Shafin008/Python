import logging

# ## Create a logger
# logger = logging.getLogger(__name__)

# ## setting the log level
# logger.setLevel(logging.DEBUG)

# ## Create a file handler
# file_handler = logging.FileHandler('logger_test_new.log')

# ## Create a formatter to add to the file handler
# formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')

# ## set the formatter to file handler
# file_handler.setFormatter(formatter)

# ## add the file handler to our logger
# logger.addHandler(file_handler)



# def add(x, y):
#     """Add Function"""
#     return x + y


# def subtract(x, y):
#     """Subtract Function"""
#     return x - y


# def multiply(x, y):
#     """Multiply Function"""
#     return x * y


# def divide(x, y):
#     """Divide Function"""
#     return x / y


# num_1 = 20
# num_2 = 10

# add_result = add(num_1, num_2)
# logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

# sub_result = subtract(num_1, num_2)
# logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

# mul_result = multiply(num_1, num_2)
# logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# div_result = divide(num_1, num_2)
# logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))


## Example 2: Adding error level

## Create a logger
# logger = logging.getLogger(__name__)

# ## setting the log level
# logger.setLevel(logging.DEBUG)

# ## Create a file handler
# file_handler = logging.FileHandler('logger_test_new.log')

# ## Create a formatter to add to the file handler
# formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')

# ## set the formatter to file handler
# file_handler.setFormatter(formatter)

# ## Add error level
# file_handler.setLevel(logging.ERROR)

# ## add the file handler to our logger
# logger.addHandler(file_handler)

# def add(x, y):
#     """Add Function"""
#     return x + y


# def subtract(x, y):
#     """Subtract Function"""
#     return x - y


# def multiply(x, y):
#     """Multiply Function"""
#     return x * y


# def divide(x, y):
#     """Divide Function"""
#     try:
#         result = x/y
#     except ZeroDivisionError:
#         logger.error('Tried to divide by zero.')

#     else:
#         return result


# num_1 = 20
# num_2 = 0

# add_result = add(num_1, num_2)
# logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

# sub_result = subtract(num_1, num_2)
# logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

# mul_result = multiply(num_1, num_2)
# logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# div_result = divide(num_1, num_2)
# logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))


## Example 3: Adding a tracrback to the error

# ## Create a logger
# logger = logging.getLogger(__name__)

# ## setting the log level
# logger.setLevel(logging.DEBUG)

# ## Create a file handler
# file_handler = logging.FileHandler('logger_test_new.log')

# ## Create a formatter to add to the file handler
# formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')

# ## set the formatter to file handler
# file_handler.setFormatter(formatter)

# ## Add error level
# file_handler.setLevel(logging.ERROR)

# ## add the file handler to our logger
# logger.addHandler(file_handler)

# def add(x, y):
#     """Add Function"""
#     return x + y


# def subtract(x, y):
#     """Subtract Function"""
#     return x - y


# def multiply(x, y):
#     """Multiply Function"""
#     return x * y


# def divide(x, y):
#     """Divide Function"""
#     try:
#         result = x/y
#     except ZeroDivisionError:
#         ## Traceback adding by exception
#         logger.exception('Tried to divide by zero.')

#     else:
#         return result


# num_1 = 20
# num_2 = 0

# add_result = add(num_1, num_2)
# logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

# sub_result = subtract(num_1, num_2)
# logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

# mul_result = multiply(num_1, num_2)
# logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

# div_result = divide(num_1, num_2)
# logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))


## Example 4: Adding Strean Handler a tracrback to the error

## Create a logger
logger = logging.getLogger(__name__)

## setting the log level
logger.setLevel(logging.DEBUG)

## Create a file handler
file_handler = logging.FileHandler('logger_test_new.log')

## Create a formatter to add to the file handler
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')

## set the formatter to file handler
file_handler.setFormatter(formatter)

## Add error level
file_handler.setLevel(logging.ERROR)

## creating a stream handler
stream_handler = logging.StreamHandler()

## adding the formatter to stream handler
stream_handler.setFormatter(formatter)

## add the file handler and stream handler to our logger
logger.addHandler(file_handler)
logger.addHandler(stream_handler)

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
    try:
        result = x/y
    except ZeroDivisionError:
        ## Traceback adding by exception
        logger.exception('Tried to divide by zero.')

    else:
        return result


num_1 = 20
num_2 = 0

add_result = add(num_1, num_2)
logger.debug('Add: {} + {} = {}'.format(num_1, num_2, add_result))

sub_result = subtract(num_1, num_2)
logger.debug('Sub: {} - {} = {}'.format(num_1, num_2, sub_result))

mul_result = multiply(num_1, num_2)
logger.debug('Mul: {} * {} = {}'.format(num_1, num_2, mul_result))

div_result = divide(num_1, num_2)
logger.debug('Div: {} / {} = {}'.format(num_1, num_2, div_result))