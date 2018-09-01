# Perfect Number Calculator

userInput = int(input("Give me a number: "))
sumOfDivisors= 0

for f in range(1, userInput):
    if userInput % f == 0:
        sumOfDivisors += f

if sumOfDivisors == userInput:
    print("Your number {} a Perfect Number!".format(userInput))
else:
    print("Your number {} not a Perfect Number!".format(userInput))