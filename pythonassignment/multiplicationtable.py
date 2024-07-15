number = int (input('Enter any Number to get the multiplication table: '))

for counter in range (1, 11):
	multiplication = number * counter
	
	print(f'{number} x {counter} = {multiplication}')