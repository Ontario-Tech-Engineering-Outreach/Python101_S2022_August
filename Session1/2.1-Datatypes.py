# What you might have noticed with the print statement is that you can't run the following:
#
# print("Hello " + 5)

# This is because they aren't the same *Datatype*
# In programming we have 4 main data types
myInteger = 12 # Integers represent whole numbers
myFloat = 3.14 # Floats represent decimal numbers
myString = "Hello" # Strings store text, and are always surrounded by quotation ("") marks
myBoolean = True # Booleans store true or false values


# What the computer is thinking is that it doesn't make sense to add a piece of text and a number together
# 5 + 5 is 10, but what would 3 + "John" be?
# In order to fix this, we can do something called casting

print("Hello " + str(5)) # casting our integer to a string makes it so instead of the number being 5, it is treated as "5" which lets us add it to text

# The same thing can be done for other data types! here are some examples
print(int(3.14)) # This will ignore the decimals in the number 3.14 and turns it into an integer
print(float(67)) # This will add decimals to the number and turn it into a float
print(str(97)) # Like we mention earlier, str() will make whatever is in the brackets into a string
