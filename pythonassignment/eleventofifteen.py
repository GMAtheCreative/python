#11

num = int(input("Enter a five-digit integer: "))

digit1 = num // 10000
digit2 = (num // 1000) % 10
digit3 = (num // 100) % 10
digit4 = (num // 10) % 10
digit5 = num % 10

print(digit1, digit2, digit3, digit4, digit5)

#12

p = int(input("Enter amount invested: "))

r = 7

n1= 10
n2 = 20
n3 = 30

a = p * 1+r ** n1
b = p * 1+r ** n2
c = p * 1+r ** n3
print(a)
print(b)
print(c)