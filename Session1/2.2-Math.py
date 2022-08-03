# What you might have noticed is that we used some math operators in our code already
# This is just a brief go over of what the math operators are/do

print(2 + 5) # The + symbol represents addition
print(6 - 4) # The - symbol represents subtraction
print(4 * 5) # The * symbol represents multiplication
print(6 / 2) # The / symbol represents division

print(7 % 3) # The % symbol represents modulo

# Modulo is the symbol that doesn't make as much sense
# This operator will give us the remainder after we divide the two numbers
# For the example above, we know that 7 divded by 3 is equal to 2 with 1 remainder
# So 7 % 3 will give us the number 1, since it is the remainder


# Example of practical application
# We want to figure out what the equivalent angle of something is between 0 and 360 degrees so we can use modulo
angle = 2700
equivalentAngle = angle % 360 # This will evenly divide the number by 360 then give us some angle that is between 0 and 360


# We can also do some things like iterating. Let's say I just want to add some number to an existing variable
myNumber = 12

# I can add to that number by just sayin
myNumber += 1

# Then we change the value of myNumber to whatever it was, plus one.