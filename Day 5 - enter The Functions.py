# enter The Functions!

# there is Two ways to create a function

# Way One - Without Parameter

def exampleF():
    print("This is an example!")

exampleF()

# Way Two - With Parameter

def exampleY(sayHello):
    print("Hello", sayHello)

exampleY("Nihil!")

#If you want you can make default parameter

def exampleZ(sayHello = "it's Nihil"):
    print("Hey", sayHello)

exampleZ() #Using Without Parameter
exampleZ("Okan")