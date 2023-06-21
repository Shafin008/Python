# class Employee:
#     """A sample Employee class"""

#     def __init__(self, first, last):
#         self.first = first
#         self.last = last
#         print('Created Employee: {} - {}'.format(self.fullname, self.email))
#     @property
#     def email(self):
#         return '{}.{}@email.com'.format(self.first, self.last)

#     @property
#     def fullname(self):
#         return '{} {}'.format(self.first, self.last)


# emp_1 = Employee('John', 'Smith')
# emp_2 = Employee('Corey', 'Schafer')
# https://docs.python.org/3/library/logging.html#logrecord-attributes

## 2nd Example
import logging
logging.basicConfig(filename='employee.log',
level=logging.INFO, format = '%(asctime)s : %(levelname)s : %(message)s')
class Employee:
    """A sample Employee class"""

    def __init__(self, first, last):
        self.first = first
        self.last = last

        logging.info('Created Employee: {} - {}'.format(self.fullname, self.email))
        
    @property
    def email(self):
        return '{}.{}@email.com'.format(self.first, self.last)

    @property
    def fullname(self):
        return '{} {}'.format(self.first, self.last)


emp_1 = Employee('John', 'Smith')
emp_2 = Employee('Corey', 'Schafer')
emp_3 = Employee('Jane', 'Doe')