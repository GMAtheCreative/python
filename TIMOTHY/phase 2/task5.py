#create two variables …. new_number and reverse
#collect a number as in the parameter/argument
#using a loop
#get the last digit of the number using % 10
#add the retrieved number to reverse * 10
#keep doing 4 and 5 till we have finished with the digits in the number



def return_reversal_of_an_integer (number):
	new_number = 0
	reverse = 0

	while number != 0:
		new_number = number % 10
		reverse = reverse * 10 + new_number 
		number = number // 10
	return reverse



def is_palindrome(number):
	
	original_number = number
	reverse = return_reversal_of_an_integer (number)
	

	if reverse == original_number:
		return True
	
	else:
		return False





print(is_palindrome(121))
