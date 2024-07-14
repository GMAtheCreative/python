count = 0
count1 = 0
count2 = 0
count3 = 0
count4 = 0
count5 = 0

for counter in range(5):
	num = int(input("Enter a five-digit integer: "))
	
	digit1 = num // 10000
	digit2 = (num // 1000) % 10
	digit3 = (num // 100) % 10
	digit4 = (num // 10) % 10
	digit5 = num % 10
	count+=1
	if count == 1:
		count1 = digit1
	elif count == 2:
		count2 = digit2
	elif count == 3:
		count3 = digit3
	elif count == 4:
		count4 = digit4
	elif count == 5:
		count5 = digit5

print(f'{count1} {count2} {count3} {count4} {count5}')
