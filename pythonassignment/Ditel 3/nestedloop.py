#this will print box/squre


for rows in range(10):
	for column in range (10):
		print('*', end =' ')
	print()


for rows in range(10):
	for column in range (rows + 1):
		print('*', end =' ')
	print()


for rows in range(10):
	for column in range (rows, 10):
		print('*', end =' ')
	print()


for rows in range(10):
	for column in range (rows + 1):
		print(' ', end =' ')
	for asterics in range(rows, 10):
		print('*', end = ' ')
	print()

for rows in range(10):
	for column in range (rows, 10):
		print(' ', end =' ')
	for asterics in range(rows + 1):
		print('*', end = ' ')
	print()