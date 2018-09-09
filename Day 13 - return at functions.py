# return At functions

# If you wanna get value from a function, you should use return
#So, with return you can use that value everywhere. An example:

def addition(x, y, z):
    result = x + y + z
    print("X = {}, Y = {}, Z = {}, result = {}".format(x, y, z, result))
    return result

def multiplication(x, y):
    result = x * y
    print("X = {}, Y = {}, result = {}".format(x, y, result))
    return result

multiplication(addition(2, 3, 4), 2)



# another examples:


def theoryX1(a = int(input("a: "))):
    print("theoryX1 Worked!")
    result = a * 3
    print("a = {0} so, {0} x 3 = {1}".format(a, result))
    return result

def theoryX2(a):
    print("theoryX2 Worked!")
    result = a + 2
    print("a = {0} so, {0} + 2 = {1}".format(a, result))
    return result

def theoryX3(b, c):
    print("theoryX3 Worked!")
    result = b / c
    print("b = {0} and c = {2} so, {0} / 4 = {1}".format(b, result, c))
    return result

theoryX3(theoryX2(theoryX1()), 4)