# range Function

# # BASIC LOTTERY NUMBER GENERATOR

# import random

# a = 0

# while a < 15: 
#     sayilar = []
#     for f in range(7):
#         rastgeleSayi = random.randint(1, 50)
#         if rastgeleSayi not in sayilar:
#             sayilar.append(rastgeleSayi)

#     sayilar.sort()
#     print(a + 1, sayilar)
#     a += 1

# range(baslama, bitis, atlama)

# a = 0
# while a <= 100:
#     print(a)
#     a += 2

# for f in range(0, 101, 2):
#     print(f)


tekSayilar = []
ciftSayilar = []

for f in range(101):
    if f % 2 != 0:
        tekSayilar.append(f)
    else:
        ciftSayilar.append(f)

print("Tek sayilar:")
print(*tekSayilar,  sep = "\n")
print(" # " * 20)
print("Çift sayilar:")
print(*ciftSayilar, sep = "\n")