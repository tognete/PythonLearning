
# Understand 1:

# Active recall: producing the information on your own without
# the use of supporting material.

# Understand 2:

# Effort recalling information directly correlates with its
# retention, provided you succeed.

# Understand 3:

# ask input to enter score between 0-100 and prints grade

input_score = input('Please enter the score: ')
score = int(input_score)

if score >= 94:
    print('A')
elif score >= 80:
    print('B')
elif score >= 70:
    print('C')
else:
    print('F')

# Understand 4:

print(True and False) # >> False
print(False and True) # >> False
print(True and True) # >> True
print(False and False) # >> False
print(True or False) # >> True
print(False or True) # >> True
print(True or True) # >> True
print(False or False) # >> False

# Understand 5:

myvar = None

print('fire' if myvar else 'ice')
print('fire' if not myvar else 'ice')

# Understand 6:

myvar = None or ''
print(f'myvar: {myvar}')
myvar = '' and 'fire'
print(f'myvar: {myvar}')
