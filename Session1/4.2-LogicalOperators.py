# We talked about earlier how booleans are the a type of logical system we use in math
# We will learn how it gets applied in programming now!

# We know that values can be true or false, but let's look at some examples
# In the following example, we have two variables that represent whether or not
# we have hotdogs and hotdog buns. We want to then use this information to figure out
# if we should have a barbecue
hasHotdogs = True
hasHotdogBuns = True

shouldHaveBarbecue = hasHotdogs and hasHotdogBuns

if(shouldHaveBarbecue):
    print("Let's have a barbecue!")
else:
    print("we don't have the stuff")


# In the above example, we used what is called an and statement, which gives us true if we have both htodogs and hotdog buns
# there are 3 basic logical operators:

myBool = hasHotdogBuns and hasHotdogs # And returns true if both values are true
myBool = hasHotdogBuns & hasHotdogs # 
myBool = not hasHotdogs # not returns