number = int(input('Enter a 5 digit number: '))

originalNumber = number
reverse = 0

while number != 0:
	newNumber = number % 10
	reverse = reverse * 10 + newNumber
	number /= 10

	if originalNumber == reverse:
		print('is palindrome')
	