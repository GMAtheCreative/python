#create a function name it sum_of_string
#in the functioncollect the parameters/arguments as a string
#cast the collected input to an int
#add it together
#return the sum as a string



def sum_of_string (number1, number2):
	new_number1 = int(number1)
	new_number2 = int(number2)

	result = new_number1 + new_number2
	string_result = str(result)
	return string_result



number1 = input("Number 1: ")
number2 = input("Number 2: ")

result = sum_of_string(number1, number2)

print(result)