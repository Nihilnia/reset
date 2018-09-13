# Object Oriented Programming

class human():
    weight = 80
    height = 1.80
    eyesColor = "red"
    hairsColor = "black"

# We create an object, and there is some properties.
#Now let's create another object with that class.

# There is TWO WAYS for create.

# 1 - All of Them #

human001 = human()
human002 = human()

print("Human001:")
print(human001.weight, human001.eyesColor) 
print("Human002:")
print(human002.weight, human002.hairsColor)

# 2 - Spesific #

human003 = human().hairsColor
human004 = human().eyesColor

print("Human003:")
print(human003) #while using we just call the object, because we insert just a spesific property
print("Human004:")
print(human004)



#as you can see we have two different variables but all properties are the same.

#Now what we need? Create a class with own properties and
# after that creating new objects by that class.

# __init__ (the first function which is running first!)


class programmingLanguages():

    def __init__(self, name, popularity):
        self.name = name
        self.popularity = popularity

#look now:

python = programmingLanguages("Python", "So popular")
jS = programmingLanguages("JavaScript", "Popular")

print(python.name, python.popularity)
print(jS.name, jS.popularity)


class exampleApp():

    def __init__(self, appName = "unknown", version = 0.00 , platform = "unkown"):
        self.appName = appName
        self.version = version
        self.platform = platform

appNumber001 = exampleApp(appName = "Gloria", version = 1.0, platform = "Windows OS")

print(appNumber001.appName)