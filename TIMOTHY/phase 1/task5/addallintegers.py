#prompt for numbers from the user
#declare a loop (while loop): control the loop by dividing the entered digits by 10
#declare new variables: new_number 
#separate the number into different single digits by: new number Equals number mod 10 will give the last digit, plus new number... (this separates and add the numbers together)
#print new number


number = int(input('Enter number: '))

reverse = 0
new_number = 0


while number != 0:
	new_number = number % 10 + new_number
	
	number //= 10

	
print(new_number)