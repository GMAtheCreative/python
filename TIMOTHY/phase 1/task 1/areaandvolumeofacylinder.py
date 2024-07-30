#prompt user to enter the radius of the cylinder
#prompt user to enter the length of the cylinder
#given that pi is 3.142
#calculate the area of the cylinder using the formular: area = 3.142 * radius inputed by the user ** 2
#calculate the volume of the cylinder using the formular: volume = area * lenght
#print the answer (the area of the cylinder)
#print the answer (the volume of the cylinder)
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>



radius = float(input('Enter the value of the radius of a cylinder: '))
length = int(input('Enter the value of the length of a cylinder: '))
pi = 3.142

area = pi * radius ** 2
volume =  area * length

print(f'The area of the cylinder is {area}\nThe volume of the cylinder is {volume}')