# Armstrong Number Calculator

import math

userInput = input("Give me a number: ")
digit = len(userInput)
total = 0

for numbers in userInput:
    total += pow(int(numbers), int(digit))

if int(userInput) == total:
    print("Yes, {} is an Armstrong number!".format(userInput))
else:
    print("No, {} is not an Armstrong number!".format(userInput))