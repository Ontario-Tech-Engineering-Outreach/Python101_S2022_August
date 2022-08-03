# We talked about boolean values being true and false
# These are very powerful tools in programming because they allow us to start asking questions
# For example
storeHasMilk = True

if(storeHasMilk):
    print("Buy some milk")

# In the above example we ask if storeHasMilk. In this case storeHasMilk is either True or False (because it is a boolean)
# It will print "Buy some milk" if whatever is in those brackets is true, and it will skip if it is false


# Alternatively, we can use an if/else statement to do something different depending on if storeHasMilk is true or false
# In this case, it will print "buy some milk" if storeHasMilk, otherwise it prints "Maybe Nexttime"
if(storeHasMilk):
    print("Buy some milk")
else:
    print("maybe next time")