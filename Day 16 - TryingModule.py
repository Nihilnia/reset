# trying to sayHi module from exampleModule

from exampleModule import sayHi, h2so4, itsAVarible

sayHi(input("What's your name? "))

print(help(h2so4))
print(h2so4(2, 20, 200))
print("This is from exampleModule", itsAVarible)

listem = list(itsAVarible)
print(listem)