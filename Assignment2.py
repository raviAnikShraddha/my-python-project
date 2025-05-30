'''# Assignment2
# taking the userinput number and checking the even or odd
userInput=int(input('Enter the number: '))
if userInput%2==0:
    print('Entered number is even: ', userInput)
else:
    print('Entered number is odd: ', userInput)
'''
# Sum of 1 to 50 number using for loop

sum=0
for i in range(1, 50):
    sum += i
print('The sum of numbers from  1 to 50 is: ', sum)
