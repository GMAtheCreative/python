import taxcalculatorfunction

status_filling = '''How are you filling as ?
A. single
B. Married filling jointly
C. married filling separately
D. Head of Household\n '''

print('Welcome to US.F.P.I(THE UNITED STATE FEDERAL PERSONAL INCOME TAXATION)\n')

print('please complete regitration and to pay your tax\n')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

print('<<<<<<<<<<<<<< Personal information >>>>>>>>>>>>>>')

name = input('Full Name: ')
contact= input('Phone Number: ')
marital_status= input('Marital Status: ')

print('>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>\n')

print('\n <<<<<<<<<<<<<<<<<< Tax Info >>>>>>>>>>>>>>>>')

income = int(input('Income: '))
filling = input(status_filling)

match (filling):

	case 'a':
		result = taxcalculatorfunction.tax_calculator_single(income)

		print(f'{name} Your tax is ${result}')

	case 'b':
		result = taxcalculatorfunction.tax_calculator_married_jointly(income)

		print(f'{name} Your tax is ${result}')

	case 'c':
		result = taxcalculatorfunction.tax_calculator_married_separately(income)

		print(f'{name} Your tax is ${result}')

	case 'd':
		result = taxcalculatorfunction.tax_calculator_head_of_household(income)

		print(f'{name} Your tax is ${result}')