import logging
# logger = logging.getLogger(__name__)
# logging.basicConfig(filename='logger_employee.log',
# level=logging.INFO, format = '%(asctime)s : %(levelname)s : %(message)s')
# class Employee:
#     """A sample Employee class"""

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last

#         logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))
        
#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first, self.last)

#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)


# emp_1 = Employee('John', 'Smith')
# emp_2 = Employee('Corey', 'Schafer')
# emp_3 = Employee('Jane', 'Doe')

#### Example 2: Without basic configuration

## Create a logger
logger = logging.getLogger(__name__)

## setting the log level
logger.setLevel(logging.INFO)

## Create a file handler
file_handler = logging.FileHandler('logger_employee_new.log')

## Create a formatter to add to the file handler
formatter = logging.Formatter('%(asctime)s : %(levelname)s : %(message)s')

## set the formatter to file handler
file_handler.setFormatter(formatter)

## add the file handler to our logger
logger.addHandler(file_handler)

class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logger.info('Created Employee: {} - {}'.format(self.fullname, self.email))
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')