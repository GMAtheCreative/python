largest = 0
secondlargest = 0

for count in range(10):


	number = int (input("enter number: "))

	if number > largest:
		largest = number
		
	elif number < largest and number > secondlargest:
		secondlargest = number


print(f'largest number is {largest}, second largest number is {secondlargest}')
 		