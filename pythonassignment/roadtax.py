amount_of_car = int (input('How much did you buy your car? : '))

if amountOfCar <= 1_000_000:
	rate1 = amountOfCar * 10 / 100
	print(f'your tax in dollars is ${rate1}')

elifamountOfCar > 1_000_000 && amountOfCar <= 3_000_000:
	int rate2 = amountOfCar * 15 / 100

	print(f'Your tax in Dollars is ${rate2}') 

elif amountOfCar > 3_000_000 && amountOfCar <= 5_000_000:
	int rate3 = amountOfCar * 20 / 100

	print(f'Your tax in Dollars is ${rate3}')

elif amountOfCar > 5_000_000:
	rate4 = amountOfCar * 25 / 100

	print(f'Your tax in Dollars is ${rate4}')