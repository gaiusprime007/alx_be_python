num1 = float(input('Enter the first number'))
num2 = float(input('Enter the second number'))

operation = input('Choose the operation (+, -, *, /): ')

match operation:
    case '+':
        result = num1 + num2
        print ('The result is '+ result)
    case '-':
        result = num1 - num2
        print ('The result is '+ result)

    case '*':
        result = num1 * num2
        print ('The result is '+ result)

    case '+':
        result = num1 / num2
        if num1 !=0 :   
            print ('The result is '+ result)
        else:
            print('Cannot divide by zero')
    case _:
        print('Invalid operation selected. Please choose from +, -, *, / ')
