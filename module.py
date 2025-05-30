import math
from math import *
num = int(input("Enter a number: "))

def square(num):
    return math.pow(num,2)
print("Square of the num is : ", square(num))

def naturalLogarithm(num):
    return math.log(num, 2)
print("Natural Logarithm of num is : ", naturalLogarithm(num))

def sineOfNum(num):
    return math.sin(num)
print("Sine of Num is : ", sineOfNum(num))