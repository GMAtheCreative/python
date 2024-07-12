grade = int(input('Enter your grade in numbers: '))

if grade >= 75 and grade < 100:
	print('A')
elif grade >= 65 and grade < 75:
	print('B')

elif grade >= 50 and grade  < 65:
	print('C')

elif grade >= 40 and grade < 50:
	print('D')

elif grade < 40:
	print('F')
else:
	print('Invalid input')


grade = int(input('Enter your grade in numbers or -9 to exit: '))
total = 0
score = 0
counter = 1
while grade != -9:
	total += grade
	counter += 1
	grade = int(input('Enter your grade in numbers or -9 to exit: '))
averagescore = total / 2

print(counter, averagescore)

	



	