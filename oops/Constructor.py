class car:
    def __init__(self,make,year,color,type):
        self.make = make
        self.year = year
        self.color = color
        self.type = type
        print("Constructed...")

    def __del__(self):
        print("Destructed...")

c = car("Billy Harley and Davidson Brothers",1999,"blue","Sedan")
print(f"Made by {c.make} in year of {c.year} which color is {c.color} and model is {c.type}")