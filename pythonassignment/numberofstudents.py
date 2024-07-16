passes = 0
fail = 0

for counter in range (1,11):
	scores = int(input(f'Enter student{counter} score: '))

	if scores <= 45:
		fail += 1

	else:
		passes += 1

print(f'The number of student that passed is {passes}, The number of students that failed is {fail}')
