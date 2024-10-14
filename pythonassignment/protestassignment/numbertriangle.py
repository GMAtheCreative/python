prompt = int(input('Enter the number lines from 1-13: '))
number = 1

for rows in range(prompt):
	for column in range (rows, prompt):
		print(' ', end =' ')
	for column in range (rows + 1):
		print(number, end =' ')
		number = prompt - 1
	for column in range (rows + 1-1):
		print(rows, end =' ')
	print()