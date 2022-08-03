# One question that is really important, is what it means to be something
# We ask it everyday and in coding it is a very important concept
valueOne = 15
valueTwo = 20

myBool = (valueOne is valueTwo)
myBool = (valueOne == valueTwo)

# In the above example, we are asking if valueOne is equal to valueTwo. In this case, because they are not the same, we get false
# you can either use ==, or is depending on what you prefer in python! Most languages will use ==, but using "is" is a bit more readable


# We can do the same thing with other data types
valueOne = "Nice"
valueTwo = "Nice"
myBool = (valueOne is valueTwo)

# in this case myBool is true because valueOne is the same as valueTwo



# We can also ask if they aren't the same, which is simply done using isnot or !=
myBool = (valueOne is not valueTwo)
myBool = (valueOne != valueTwo)