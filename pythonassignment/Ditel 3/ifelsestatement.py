print('Enter two numbers and i will tell you the the relationships they satisfy')
number1 = int(input('Enter first number: '))
number2 = int(input('Enter second number: '))

if number1 == number2:
	print(number1, ' is equals ', number2)
else:
	print(number1, ' is not equals ', number2)

if number1 < number2:
	print(number1, ' is less than ', number2)
else:
	print(number1, ' is greater than ', number2)

if number1 <= number2:
	print(number1, ' is less than or equals ', number2)
else:
	print(number1, ' is greater than or equals ', number2)



