# Lambda Expressions

# But first, let's remember List Comprehensions

aList = [1, 2, 3, 4, 5]
bList = [f * 2 for f in aList]
print(bList)

# Now let's Lambda!

sumUp = lambda a = 2 , b = 3 : print(a + b)
sumUp(5, 6)

#Another Example

def x2(a):
    return a * 2

print("With classic way:", x2(3)) #Result = 6

x3 = lambda a : a * 2

print("With Lambda:", x3(3))

#Examples, examples...

def Socratica(x, y, z):
    return x + y + z

print("With classic way:", Socratica(2, 3, 4))

SocraticaX2 = lambda x, y , z : x + y + z

print("With Lambda:", SocraticaX2(2, 3, 4))


#

def UserSumUp():
    x = int(input("x: "))
    y = int(input("y: "))
    z = int(input("z: "))
    return x + y + z

print("With Classic Way:", UserSumUp())

UserSumUpX2 = lambda x = int(input("x: ")), y = int(input("y: ")), z = int(input("z: ")) : x + y + z
print("With Lambda:", UserSumUpX2())


#

def Toplama(x, y, z):
    return x + y + z

print("With Classic Way:", Toplama(2, 3, 45))

ToplamaX2 = lambda x, y, z : x + y + z
print("With Lambda:", ToplamaX2(2, 3, 45))

# Reverse String

def ReverseIt(string):
    return string[::-1]

print("With Classic Way:", ReverseIt("Nihil"))

ReverseItX2 = lambda string : string[::-1]

print("With Lambda:", ReverseItX2("Velour"))

# Even Number or Not?

def EvenOrNot():
    userInput = int(input("Give me a number: "))
    return userInput % 2 == 0

print("With classic way:", EvenOrNot())

EvenOrNotX2 = lambda userInput = int(input("Number please: ")) : userInput % 2 == 0

print("With Lambda:", EvenOrNotX2())