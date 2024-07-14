amounttoinvest = int(input('Enter the Amount you want to invest: '))

investmentaftertenyears = 0
investmentaftertwentyyears = 0
investmentafterthirtyyears = 0

for counter in range(1,31):

	if counter == 10:
		investmentaftertenyears = amounttoinvest * (1 + 0.07) ** counter

	if counter == 20:
		investmentaftertwentyyears = amounttoinvest * (1 + 0.07) ** counter

	if counter == 30: 
		investmentafterthirtyyears = amounttoinvest * (1 + 0.07) ** counter 

print(f'Your investment in 10yrs is {investmentaftertenyears:.2f}\nYour investment in 20yrs is {investmentaftertwentyyears:.2f}\nYour investment in 30yrs is {investmentafterthirtyyears:.2f}')
