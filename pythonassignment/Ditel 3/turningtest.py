name = input('What is your name \n')
print(name, ' welcome to Sunday Night therapy')

problem = input('What is your problem?\n')

question1 = input('have you had '+ problem + ' before now s(yes or no)?\n')

if question1.casefold() == 'yes':
	print('well, you have it again deal with it')
else:
	print('Well, you have it now deal with it')
