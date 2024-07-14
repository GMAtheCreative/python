number = int (input('Enter number "1" for passes or "2" for fails or enter -1 to stop: '))

passcounter = 0
failcounter = 0
invalidcounter = 0

while number != -1:
	
	

	if number == 1:
		passcounter += 1
	elif number == 2:
		failcounter += 1
	else:
		invalidcounter += 1
	
	number = int (input('Keep Entering number "1" for passes or "2" for fails or enter -1 to stop: '))

print(f'the number of passes is {passcounter}, the number of fails is {failcounter}, the number of invalids is {invalidcounter}')

