a = int(input())
b = int(input())
sign = input()
if sign == '+':
    print(a, '+', b, '=', a + b)
elif sign == '-':
    print(a, '-', b, '=', a - b)
elif sign == '*':
    print(a, '*', b, '=', a * b)
elif sign == '/':
    if b == 0:
        print('Division by zero!')
    else:
        print(a, '/', b, '=', a / b)
elif sign == '%':
    if b == 0:
        print('Division by zero!')
    else:
        print(a, '%', b, '=', a % b)
elif sign == '//':
    if b == 0:
        print('Division by zero!')
    else:
        print(a, '//', b, '=', a // b)
else:
    print('Error!')
