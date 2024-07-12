#6

number = int(input('Enter a number: '))

if number % 2 == 0:
	print('Even number')

else:
	print('Odd number')


#7

if 1024%4 == 0:
	print('its a multiple')

else:
	print('its not a multiple')

if 10%2 == 0:
	print('its a multiple')


#8

print('number\t Square\t Cube')

zero = 0

one = 1

two = 2
twosquare = 2**2
twocube = two*two

three = 3
threesquare = 3**3
threecube = three * three

four = 4
foursquare = 4**4
fourcube = four*four

five = 5
fivesquare = 5**5
fivecube = five*five

print(f'{zero}\t {zero}\t {zero} \n{one}\t {one}\t {one} \n{two}\t {twosquare}\t {twocube} \n{three}\t {threesquare}\t {threecube} \n{four}\t {foursquare}\t {fourcube} \n{five}\t {fivesquare}\t {fivecube}')

#9

1 = ord('B')
2 = ord('C')
3 = ord('D')
4 = ord('b')
5 = ord('c')
6 = ord('d')
7 = ord('0')
8 = ord('1')
9 = ord('2')
10 = ord('$')
11 = ord('*')
12 = ord('+')
13 = ord(' ')

print(1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13)


#10

num1 = int(input("Enter first number: "))
num2 = int(input("Enter second number: "))
num3 = int(input("Enter third number: "))


sum = num1 + num2 + num3
average = sum / 3
product = num1 * num2 * num3
smallest = min(num1, num2, num3)
largest = max(num1, num2, num3)


print("Sum:", sum)
print("Average:", average)
print("Product:", product)
print("Smallest:", smallest)
print("Largest:", largest)


