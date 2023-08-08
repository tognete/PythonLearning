
# Understand 1:

# Whenever you think, "I can't do this," there's a high chance that it's a
# limiting belief you can overcome!

# Understand 2:

def greeting(name):
    print("Hey there, " + name + "!")

# Example function call:
# greeting("Tony")
# >> Hey there, Tony!

# Understand 3:

def greeting(name):
    print("Hey there, {}!".format(name))

# Example function call:
# greeting("Tony")
# >> Hey there, Tony!

# Understand 4:

def greeting(name):
    print(f"Hey there, {name}!") # single quotes work as well

# Example function call:
# greeting("Tony")
# >> Hey there, Tony!

# Understand 5:

print("{0:10} | {1:10}".format("value 0", "value 1")) # two columns and one row
print("{0:20} | {1:15}".format("value 0", "value 1")) # same as above, but with different min widths
print("{0:^20} | {1:>15}".format("value 0", "value 1")) # same as above, but with different text alignments
