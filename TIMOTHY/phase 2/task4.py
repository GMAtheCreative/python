#prompt for an input
#check if number inputed is even number by using % 2
#print result of odd and even number 


number = int(input('Enter number: '))

if number % 2 == 0:
	print (f'{number} is even number')
else:
	print(f'{number} is an odd number')