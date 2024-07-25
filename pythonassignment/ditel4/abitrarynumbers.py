def product_calculator(*number):
	result = 0
	for counter in number:
		result += number

	return result


result = product_calculator(2, 5, 6, 1, 4,)
print(result)