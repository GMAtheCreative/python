milesdriven = int(input('Enter miles driven : '))
gallons = int(input('Enter gallons useds (-1 to end): '))

milespergallon = 0
totalmilespergallon = 1

while gallons != -1:
	
	milespergallon = milesdriven / gallons
	
	print(f'The amount of miles per gallon is {milespergallon}')
	
	milesdriven = int(input('Enter miles driven : '))
	gallons = int(input('Enter miles driven (-1 to end): '))

totalmilespergallon *= milespergallon

print(f' The overall average mile/gallon was {totalmilespergallon}')