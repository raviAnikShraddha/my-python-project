# using Filter
# filter(function, iterable)
'''
def evenNumbers(a):
    return a%2==0

listOfNumbers = [1,2,3,4,5,6,7,8,9]

result = list(filter(evenNumbers,listOfNumbers))
print(result)
'''
# --------------- It can also used as lambda -----------------
# we can use return as list, tuple, set whatever as per the requirement
resultSet = set(filter(lambda a: a%2==0, range(11)))
resultList = list(filter(lambda a: a%2==0, range(11)))
resultTuple = tuple(filter(lambda a: a%2==0, range(11)))
print("Set --> ",resultSet)
print("List --> ",resultList)
print("Tuple --> ",resultTuple)


