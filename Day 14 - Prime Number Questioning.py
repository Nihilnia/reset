# Prime Number Questioning!

while True:
    userInput = int(input("Give me a number bitch: "))
    key = 0
    for summs in range(2, userInput):
        if userInput % summs == 0:
            key += 1
    if key != 0:
        print("It's not a Prime Number!")
    else:
        print("It's a prime Number babe!")


####################################################
# WITH DEFINE A FUNCTION

def PrimeNumber():
    userInput = int(input("Give me a number: "))
    key = 0
    for summs in range(2, userInput):
        if userInput % summs == 0:
            key += 1
    if key != 0:
        print("It's not a Prime Number!")
    else:
        print("It's a Prime number Babe!")

while True:
    PrimeNumber()