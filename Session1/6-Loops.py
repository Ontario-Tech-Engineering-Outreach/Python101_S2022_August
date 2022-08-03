# Now, one of the most powerful things we have access to in python are loops. These things let us repeat code over and over
# One thing we can do is print out a bunch of stuff in an array

groceryStore = ["Apple", "Orange", "Green Apple", "Strawberry", "Grape"]

for item in groceryStore:
    print(item)

# In the above, we take all the items in the groceryStore array, and we print them out
# A for loop will repeat something for everything inside of a list of things

# Sometimes in code we only want to repeat something a specific number of times
# In python we can create an empty array with range(), and it will repeat our code over and over
# that many times
for number in range(12):
    print("Hello!")
