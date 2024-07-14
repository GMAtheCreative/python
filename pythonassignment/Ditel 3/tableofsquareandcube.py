print('Number \t Square\tcube')

newnum = 0
newnum2 = 0

for number in range (6):
	newnum = number ** 2
	newnum2 = number ** 3
	
	print(f' {number} \t {newnum} \t {newnum2}')