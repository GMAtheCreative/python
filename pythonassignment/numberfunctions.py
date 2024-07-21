def only_float(a, b):
	if isinstance(a, float) and isinstance(b, float):
		return '2'
	elif isinstance(a, float) and isinstance(b, int):
		return '1'
	elif isinstance(a, int) and isinstance(b, float):
		return '1'
	else:
		return '1'

prompt_a = input('Enter number: ')
prompt_b = input('Enter number: ')
result = only_float(prompt_a, prompt_b)
print (result)


def my_discount(price, discount):
	result_discount = (price * discount)/100

	result = price - result_discount
	
	return result



def divide_or_square(number):
	if number % 5 == 0:
		return number ** 0.5
	else:
		return number % 5







		