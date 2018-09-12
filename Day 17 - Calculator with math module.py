# Calculator With Using Math Module

# pow()
# sqrt()
# log()
# log10()
# degrees()
# radians()
# cos()
# sin()
# tan

from math import pow, sqrt, log, log10, degrees, radians, cos, sin, tan
from time import sleep

print("Welcome to My Calculator!")
while True:
    userChoice = input("""
Please select your choice:
1 - pow
2 - sqrt
3 - log
4 - log10
5 - degrees
6 - radians
7 - cos
8 - sin
9 - tan
""")

    if userChoice.lower() != "q":
        if int(userChoice) in range(1, 10):
            firstNumber = int(input("Number: "))
            # Let the calculator begin!
            if userChoice == "1":
                userPow = int(input("Pow: "))
                print("Result", pow(firstNumber, userPow))
            elif userChoice == "2":
                print("Result", sqrt(firstNumber))
            elif userChoice == "3":
                print("Result", log(firstNumber, 2))
            elif userChoice == "4":
                print("Result", log10(firstNumber, 10))
            elif userChoice == "5":
                print("Result", degrees(firstNumber))
            elif userChoice == "6":
                print("Result", radians(firstNumber))
            elif userChoice == "7":
                print("Result", cos(firstNumber))
            elif userChoice == "8":
                print("Result", sin(firstNumber))
            else:
                print("Result", tan(firstNumber))
        else:
            print("You should select between 1-9")
    else:
        print("Bye!")
        sleep(2)
        break



# ilkSayi = 1
# ikinciSayi = 1
# fibonacci = [ilkSayi, ikinciSayi]
# for f in range(1, 20):
#     ilkSayi, ikinciSayi = ikinciSayi, ilkSayi + ikinciSayi
#     fibonacci.append(ilkSayi)

# print(fibonacci)

# def exampleOne(*x):
#     result = 0
#     for f in x:
#         result += f
#     return x

# print(exampleOne(2, 3, 4, 5))


hayaller = True
while hayaller:
    print("Elbet bir gün olmak istediğim yerde, yapmak istediğim şeyleri yapıyor olacağım!")
    
    if hayaller == False:
        print("Böyle bir şey mümkün değil!")

    else:
        print("""Bir daha kimsenin sana bir şey yapamayacağını söylemesine izin verme.
Bir hayalin varsa onun peşini bırakmamalısın.
Birisi bir şeyi yapamıyorsa senin de yapamayacağını söylemek istiyordur.
Bir şeyi istiyorsan, peşini bırakma. O kadar.""")