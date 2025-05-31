# Iteration

numbers = [1,2,3,4,5,6,7,8,9]
'''
# if we need to print this we can use for loop
for number in numbers:
    print(number)
'''
'''
iteration = iter(numbers)
# it prints object of iteration
print(iteration)
# it prints values of iteration at once
print(iteration.__next__())
# it prints object of iteration
print(next(iteration))
'''
# Generator is something that create iterators
'''
def fn():
    yield 1
    yield 2
    yield 3
values = fn()
print(values.__next__())
'''
# let's have example of squares of numbers using while loop
def squares():
    n = 1
    while n <= 5:
        square = n ** 2
        yield square
        n += 1
values = squares()
for square in values:
    print(square)