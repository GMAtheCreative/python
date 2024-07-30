#prompt user for the grvity rate and gravity rate
#calculate the amount of gravity by: subtotal/gravityrate/10
#calculate the total by: gravity + subtotal
#print the result of the amou nt of gravity and the total 
#>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>


subtotal = int(input('Enter the subtotal of gravity: '))
gravity_rate = int(input('Enter the gravity rate: '))
actual_gravity = gravity_rate / 10
total = subtotal + actual_gravity

print (f'the gravity is {actual_gravity}, the total is {total}')