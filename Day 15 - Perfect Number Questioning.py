# perfect Number Questioning!

def perfectNumber(number):
    exactDivisors = 0
    listOfDivisors = list()
    for divisors in range(1, number):
        if number % divisors == 0:
            exactDivisors += divisors
            listOfDivisors.append(divisors)
    
    if exactDivisors == number:
        print("""{} is a Perfect Number. 
Because divisors of {} is {} and their sum {}""".format(number, number, listOfDivisors, exactDivisors))
    else:
        print("""{} is Not a Perfect Number. 
Because divisors of {} is {} and their sum {}""".format(number, number, listOfDivisors, exactDivisors))


while True:
    userChoice = input("Give me a Number or For quit: Q ")
    if userChoice.lower() == "q":
        break
    else:
        perfectNumber(int(userChoice))


#extra: All Perfect numbers between 1 - 1000:

listOfPerfectNumbers = []
for numbers in range(1, 1001):
    perfectNumber(numbers)