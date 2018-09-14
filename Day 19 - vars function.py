class planets():

    def __init__(self, name = "unknown", diameter = 0, day = 0):
        self.name = name
        self.diameter = diameter
        self.day = day

mercury = planets(name = "Mercury", diameter = 3.31, day = 58.6)
venus = planets(name = "Venus", diameter = 7.521, day = 241)
jupiter = planets(name = "Jupiter", diameter = 86.881, day = 9.8)

print("Mercury", vars(mercury))
print("Venus", vars(venus))
print("Mercury", vars(jupiter))