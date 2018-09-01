# sum Up! (basic)

total = 0
while True:
    userInput = input("Give me a number: (Q For quit!) ")
    
    if userInput.lower() != "q":
        total += int(userInput)
        print("Total is", total)
    else:
        break