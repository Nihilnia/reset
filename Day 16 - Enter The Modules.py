# enter The Modules!

# import module_Name

# import math
# import time

# while True:
#     userChoice = input("Give me a number OR for quit 'Q': ")
#     if userChoice.lower() != "q":
#         result = math.factorial(int(userChoice))
#         print("Factorial of",userChoice, "=", result)
#     else:
#         print("Quiting..")
#         time.sleep(2)
#         break


# you can give any name to a module

# import math as magic
# import time as antiMagic

# while True:
#     userChoice = input("Give me a number or 'Q' for quit!: ")
#     if userChoice.lower() != "q":
#         userPow = int(input("Pow: "))
#         result = magic.pow(int(userChoice), userPow)
#         print("Pow of {} is => {}".format(userChoice, result))
#     else:
#         print("Quiting..")
#         antiMagic.sleep(2)
#         break


# SECOND DEFINE WAY - DON'T NEED TO USE MODULE NAME WHILE USING FUNCTION

# from math import *
# print(ceil(2.3)) #normally we should write like: math.ceil(2.3)
# print(floor(2.3))


# THIRD WAY - IMPORT ONLY WHAT WE NEED

from math import ceil, floor

print(ceil(3.7))
print(floor(3.7))

#for example we can't user factorial function because we did not import it.