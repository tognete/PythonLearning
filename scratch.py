#!/usr/bin/env python3

class Student():
    """ Represents a student """

    def __init__(self, name, year):
        """ Initializes a Student instance """

        self.name = name
        print('The type of self: {}'.format(type(self)))
        print('The id of self: {}'.format(id(self)))
        print('Self printed: {}'.format(self))
    
    def change_name(self, new_name):
        """ Updates the name attribute of the instance """

        self.name = new_name
    
    def __call__(self):
        return None
    
    def __str__(self):
        return 'this is __str__'

    def __repr__(self):
        return 'this is __repr__'

def say_hi(name='tony', last):
    """ prints greeting to the screen """

    print(f'{name} {last}')

# mystudent = Student('Tony', 'senior')

""" print(type(mystudent))
print(type(mystudent.change_name))
print(type(mystudent()))
print(type(None))
print(type(say_hi))
print(id(mystudent))
print('Instance printed: {}'.format(mystudent))
print(hex(id(mystudent)))
print(str(mystudent)) """

say_hi(last='alamo', name='tony')