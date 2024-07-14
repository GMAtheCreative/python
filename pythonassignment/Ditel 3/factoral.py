
number = int(input('your number to get the factorial: '))
factoral = 1

for counter in range(1, number+1):
	factoral *= counter

print(factoral)