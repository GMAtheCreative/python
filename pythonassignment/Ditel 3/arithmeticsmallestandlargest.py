sum = 0
average = 0
product = 1
smallest = 0
largest = 0

for counter in range(4):
	number = int(input('Enter number: '))
	
	product *= number

	sum += number

	if smallest == 0 or number < smallest:
	
		 smallest = number

	if largest == 0 or number > largest:
		largest = number


average = sum / 2
print(f'The sum is {sum}\nThe average is, {average}\nThe product of all the numbers is {product}\nThe smallest is, {smallest}\nThe largest is, {largest}')

	