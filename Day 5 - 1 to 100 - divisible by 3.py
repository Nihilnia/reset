# list of numbers which ones divisible with three

# for number in range(1, 101):
#     if number % 3 == 0:
#         print(number)

# or 

for number in range(1, 101):
    if number % 3 != 0:
        continue
    print(number)