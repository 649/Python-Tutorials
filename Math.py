#!/usr/bin/env python """
import math
#import math library

stories = int(input("Enter the number of stories: ")) or 0
mass = []
k = []
ratio = []
x = []
i = 0
if (stories > 0):
    while i < stories:
        mass.append(int(input("Enter mass %d: " % (i+1))) or '0') # We ask for a string, if nothing, put 0
        # mass = int(mass) # We convert string to an integer
        # print("Your mass is %d" % mass) # We print variable
        k.append(int(input("Enter spring constant %d: " % (i+1))) or '0') # We ask for a string, if nothing, put 0
        # k = int(k) # We convert string to an integer
        ratio.append(k[i]/mass[i])
        print("x%d = cos(√(%s)*t) + sin(√(%s)*t)" % ((i+1), ratio[i], ratio[i]))
        x.append(math.sqrt(ratio[i]))
        # use math library we imported, dot the function you want to do, in this case square root
        print("Distane %d: %s" % ((i+1), x[i])) # Print the value of x
        # print distance calculated with math library
        print('') # Space for data
        i+=1 # Increment "i" for the loop
else:
    print("Your building has 0 stories.")