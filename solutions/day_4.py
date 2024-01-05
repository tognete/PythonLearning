
# Understand 1:

print(len('this string'))

# Or this longer version:
mystring = 'this string'
mystring_len = len(mystring)
print(mystring_len)

# Understand 2:

def greeting():
  print('Hello, everyone! This is my greeting.')

# You can then call the function:
greeting()

# Understand 3:

def add(int1, int2):
  added_ints = int1 + int2
  print(added_ints)

# You can then call the function:
add(7, 10) # prints 17 (7+10)

# Understand 4:

# Here's an example of a new function with a doc string:
def print_temp():
  ''' Function that prints the temperature to the screen '''
  print('The temperature is 19 degrees Celsius right now.')
# In this exercise, use the doc string format from "print_temp()" above to add doc strings to the "greeting()" and "add()" functions.
# Then use the help() function to see the difference
help(greeting)
help(add)
help(print_temp) # Only applies to this explanation
