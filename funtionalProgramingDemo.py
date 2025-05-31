def add(i,j):
    print(f"function add is called with value of i is: {i} and value of j is: {j}")
    return i+j

# we can assign the function into the variable

a = add
print(a(2,3))

def call(i,j):
    print(f"function call is called with value of i is: {i} and value of j is: {j}")
    return add(i,j)

print("Calling function call and the output is: ",call(2,3))

