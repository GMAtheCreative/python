#0. create a container
#1. prompt user to enter an input
#2. iterate through the input
#3. while running through the the input check if each of the character is either letter  or number
#4. is 3 Is true store it in a container created in step 0


number_of_digit = 0
number_of_letters = 0

prompt = input('Enter your sentence: ')

for counter in prompt:
	if counter.isdigit():
		number_of_digit += 1

	elif counter.isalpha():
		number_of_letters += 1

print(f'LETTERS {number_of_letters}, DIGITS {number_of_digit}')