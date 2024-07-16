from random import randint
random_number = randint(1,1000)
prompt = input('lets play a game "yes or no" :)')

too_low = 0
too_high = 0

while prompt != "no":

	lets_ask_the_user = int(input('Guess my number between "1 and 1000" with the fewest guesses: '))

	while lets_ask_the_user != random_number:
	
	

		if lets_ask_the_user <  random_number:
		
			too_low += 1
			print('Too low')

		elif lets_ask_the_user > random_number:

			too_high +=1
			print('Too high')

		else:
			print('Congratulations. you guessed the number!!')
	
		lets_ask_the_user = int(input('Guess my number between "1 and 1000" with the fewest guesses: '))


	if too_low > 10:
		print(f'The number of your lower guesses is {too_low}\nThe number of your lower guesses is {too_high}\nYour performance is too low\nTRY AGAIN!! :(')

	elif too_high > 10:
		print(f'The number of your lower guesses is {too_low}\nThe number of your higher guesses is {too_high}\nYour performance is too low\nTRY AGAIN!! :(')

	else:
		print(f'The number of your lower guesses is {too_low}\nThe number of your higher guesses is {too_high}\nGOOD JOB!! :)')


	prompt = input('Will you love to continue "yes or no" :)')

print('Good bye, hope to see you soon')
