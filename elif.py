operator=input('Enter the operator (+, -, *, /)')
operand_1=int(input('Enter the first number: '))
operand_2=int(input('Enter the second number: '))

if operator == '+':
    print(operand_1 + operand_2)
elif operator == '-':
    print(operand_1 - operand_2)
elif operator == '*':
    print(operand_1 * operand_2)
elif operator == '/':
    print(operand_1 / operand_2)
else:
    print('None')
