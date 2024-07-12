totalbalance = 0

actions = 'Deposit, withdraw or check your account balance "Exit to stop"'

print('Hello \nWelcome to Ace Bank')

prompt = input('What will you love to do today: ' + actions)


while prompt != 'exit':

	match (prompt):
	
		case 'deposit':
			deposit = int(input('How much do you want to deposit:\n '))
			totalbalance += deposit
			print('keep it up :)')

		case 'withdraw':
			withdraw = int(input('How much do you want to withdraw:\n '))
			totalbalance -= withdraw
			if withdraw > totalbalance:
				print('Insufficient fund :( \nplease make some deposit')

		case 'account balance':
			print('your acount balance is ', totalbalance)

	prompt = input('will you love to continue transaction: ' + actions)
