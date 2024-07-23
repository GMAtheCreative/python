def get_lenght(argument):
	length = 0
	for index in argument:
		length += 1
	return length

prompt = input('Enter anything: ')

lenght = get_lenght(prompt)
print(lenght)	