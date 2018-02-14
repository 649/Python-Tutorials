#!/usr/bin/python

x = 34 - 23 # x is equivalent to 11
y = "Hello" # y is string "Hello"
z = 3.45    
if z == 3.45 or y == "Hello": # if either is true, then execute
    x = x + 1 # x is equivalent to 12
    y = y + " World" # original y (Hello) added to another string " World"

print(x) # prints 12
print(y) # prints "Hello World"

# Same thing below but with "and"

x = 34 - 23 # x is equivalent to 11
y = "Hello" # y is string "Hello"
z = 3.45    
if z == 3.1 and y == "Hello": # if BOTH is true, then execute
    x = x + 1 
    y = y + " World" 
    # None of this will execute because both conditions are not true

print(x) # prints 11
print(y) # prints "Hello"

