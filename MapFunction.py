# using map
# map(function, iterable)
# map and filter they both have same expression but different functionality
'''
def square(x):
    return x*x
numbers = [1,2,3,4,5]

resultMap = list(map(square,numbers))
print("resultMap --> ", resultMap)
# this is output of map resultMap -->  [1, 4, 9, 16, 25]

resultFilter = list(filter(square,numbers))
print("resultFilter --> ", resultFilter)
# this is output of filter resultMap -->  [1, 4, 9, 16, 25]
'''
#---------------------------using lambda------------------------------

print("map using lambda --> ",list(map(lambda x: x*x,range(10))))

print("filter using lambda --> ",list(filter(lambda x: x*x,range(10))))

print("filter using lambda with even numbers --> ",list(filter(lambda x: x%2==0,range(10))))
