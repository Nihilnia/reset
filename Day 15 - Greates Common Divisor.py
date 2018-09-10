# greates Common Divisor!

def greatesCD(numberOne, numberTwo):
    numberOne, numberTwo = int(numberOne), int(numberTwo)
    biggerNumber = 0
    if numberOne > numberTwo:
        biggerNumber += numberOne
    else:
        biggerNumber += numberTwo
    
    greatestCommonDivisor = 0
    for divisors in range(1, biggerNumber + 1):
        if numberOne % divisors == 0:
            if numberTwo % divisors == 0:
                if divisors > greatestCommonDivisor:
                    greatestCommonDivisor = divisors

    return greatestCommonDivisor

while True:
    userChoice = input("Give me first number or For quit 'Q': ")
    if userChoice.lower() != "q":
        userNumber2 = input("Second number: ")
        print(greatesCD(userChoice, userNumber2))
    else:
        break