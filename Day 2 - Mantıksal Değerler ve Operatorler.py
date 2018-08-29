# Mantıksal Değerler ve Operatorler

# Mantıksal Değerler (Bools)
# True, False

a = True #bool
b = False #bool
c = "" #str

print("a", type(a)) #True
print("b", type(b)) #False
print("c", type(c)) #False

if bool(c) == False:
    print("C bir değer taşımıyor.")

#Not:
# bir değer 2 durumda False olur:
# 1 - Sıfır vermek - > degisken = 0
# 2 - False vermek -> degisken = False

print(bool(False))


#Karşılaştırma Operatorleri

# >
# <
# >=
# <=
# ==
# !=


isim = "reco"

if isim != "nihil": #True ise if bloğu çalışacaktır.
    print("isim Nihil değildir.")
