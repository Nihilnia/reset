import time

def FindDivisors(number):
    userInput = number
    exactDivisors = list()
    for divisors in range(1, userInput + 1):
        if userInput % divisors == 0:
            exactDivisors.append(divisors)
    print("Exact divisors of {} = {}".format(userInput, exactDivisors))

while True:
    userChoice = input("Give me a number or For quit : 'Q'")
    if userChoice.lower() == "q":
        break
    else:
        FindDivisors(int(userChoice))

#or

def TamBolenleriBulma(sayi):
    tamBolenler = list()
    for sayilar in range(1, sayi):
        if sayi % sayilar == 0:
            tamBolenler.append(sayilar)
    return tamBolenler

while True:
    kullaniciSecimi = input("Çıkmak için Q: ")
    if kullaniciSecimi.lower == "q":
        break
    else:
        print(kullaniciSecimi, "sayisinin tam bolenleri", TamBolenleriBulma(int(kullaniciSecimi)))