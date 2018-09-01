# the Multiplication Table

key = 11

for numbers in range(1, key):
    for numbersX2 in range(1, key):
        print("{} x {} = {}".format(numbers, numbersX2 , numbers * numbersX2))