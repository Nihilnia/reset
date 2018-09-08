# Parameters at Functions

# if we wanna give any parameters to a Function
#we should insert a value while using.

def EvilBoy(a, b):
    print("Function 'EvilBoy' Worked!")
    return a + b

print(EvilBoy(2, 3))

# that was a classic function as we know.
# But we can make it some default parameters.

def DoosDronk(a = 2, b = 3):
    print("Function 'DoosDrunk' Worked!")
    return a + b

# Now we have deafult values of parameters.
#If we don't give values while using that function
#Our default values works.


# Using without parameters:

print("Without Parameters:", DoosDronk())

#Using With Parameters:

print("With Parameteres:", DoosDronk(4, 8))