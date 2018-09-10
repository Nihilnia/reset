# number Reader!

def NumberReader(number):
    
    OneDigits = {0: "zero", 1: "one", 2: "two", 3: "three", 4: "four",
    5: "five", 6: "six", 7: "seven", 8: "eight", 9: "nine"}

    TwoDigits = {10: "ten", 11: "eleven", 12: "twelve", 13: "thirteen",
    14: "fourteen", 15: "fiveteen", 16: "sixteen", 17: "seventeen",
    18: "eighteen", 19: "nineteen", 20: "twelwe",
    30: "thirty", 40: "fourty", 50: "fifty", 60: "sixty",
    70: "seventy", 80: "eighty", 90: "ninety"}

    if len(number) == 1:
        print(OneDigits[int(number)])
    else:
        if "0" in number:
            print(TwoDigits[int(number)])
        else:
            if int(number) < 21:
                print(TwoDigits[int(number)])
            else:
                firstFloor = int((number[0]) + "0")
                secondFloor = int(number[1])
                print(TwoDigits[firstFloor], OneDigits[secondFloor])


while True:
    userInput = input("Give me a number or 'Q' For quit!: ")
    if userInput.lower() == "q":
        break
    else:
        NumberReader(userInput)