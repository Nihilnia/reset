# Simple Game - Number Guessing

from time import sleep
from random import randint

rights = 5
number = randint(1, 20)
hintForUser = list()
userChoices = list()

for f in range(number - 3, number + 3):
    hintForUser.append(f) 

print("Welcome to BASIC Number Guessing Game!")

while rights != 0:
    print("You have {} rights for find the number!".format(rights))
    userChoice = int(input("What's your choice?\n"))

    if userChoice in range(1, 21):
        if rights == 1:
            if userChoice != number:
                print("Let me check..")
                sleep(2)
                rights -= 1
                userChoices.append(userChoice)
                print("Game is Over baby. Number was", number)
                print("And your choices was:", userChoices)
            else:
                print("Let me check..")
                userChoices.append(userChoice)
                sleep(2)
                print("Well done! Number was", number)
                print("Your choices was:", userChoices)
                break
        elif userChoice == number:
            print("Let me check..")
            userChoices.append(userChoice)
            sleep(2)
            print("Well done! Number was", number)
            break
        elif userChoice in hintForUser:
            print("Let me check..")
            userChoices.append(userChoice)
            sleep(2)
            print("\nClose! Try again!\n")
            rights -= 1
        else:
            print("Let me check..")
            userChoices.append(userChoice)
            sleep(2)
            print("\nNot even close!.. Try again!\n")
            rights -= 1      
    else:
        print("Mate.. You should give me a number between 1 - 20!")