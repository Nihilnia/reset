# break

a = 0
while True:
    print(a)
    a += 1
    if a == 10:
        break 

for f in range(11):
    if f == 3 or f == 7:
        break
        # after the break expression, codes won't work.
    print("F değeri:", f)



# continue


for f in range(1, 11):
    if f == 5 or f == 7:
        continue
    else:
        print(f)