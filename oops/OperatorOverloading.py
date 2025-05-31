'''
class Vegetable:
    def __init__(self, carrot, beans):
        self.carrot = carrot
        self.beans = beans

v1 = Vegetable(7, 9)
v2 = Vegetable(8, 13)
v3 = v1 + v2
print(v3.carrot) #---> giving error
'''

class Vegetable:
    def __init__(self, carrot, beans):
        self.carrot = carrot
        self.beans = beans
    #for adding two object we need implement this below add function
    def __add__(self, other):
        carrot = self.carrot + other.carrot
        beans = self.beans + other.beans
        return Vegetable(carrot, beans)

v1 = Vegetable(7, 9)
v2 = Vegetable(8, 13)
v3 = v1 + v2
print(v3.carrot)
print(v3.beans)