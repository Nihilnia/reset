# Finding Factorial

userInput = input("Give me a number: ")

factorial = 1

for number in range(1, int(userInput) + 1):
    factorial *= number

print(factorial)