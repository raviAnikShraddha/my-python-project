# printing factorial using recursion

def calculateFactorial(n):
    if n<2:
        return 1
    else:
        return n*calculateFactorial(n-1)

print("Using recursion -> Factorial of n is : ", calculateFactorial(4))


# printing factorial using loop
num = int(input('Enter the number : '))
def usingLoop(num):
    factorial = 1
    i = 1
    while i <= num:
        factorial = factorial * i
        i += 1
    return factorial

print("using loop -> Factorial of num is : ", usingLoop(num))