# Flexible Arguments

# Let's say we gave two parameters to a function while define that function.
#And gave four parameters while using?
# Example:

def Example(a, b):
    print(a + b)

Example(2, 3, 4) #We got error.

# So that's why we're using 'Flexible Arguments'!

def Example2(*arg):
    result = 0
    for f in arg:
        result += f
    print(result)

Example2(2, 3, 4 ,5)

# As you can see we can give much more.