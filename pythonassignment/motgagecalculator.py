amounttoborrow = int(input('Enter the amount you want to borrow: '))
annualinterestrate = int(input('What is the Annual interest rate: '))
yearsofmotgage = int(input('How many years do you want to motgage for: '))

monthlyinterestrate = annualinterestrate / 1200

monthlyduration = yearsofmotgage * 12

monthlypayment = amounttoborrow * ( monthlyinterestrate * (1 + monthlyinterestrate) ** monthlyduration) / ((1 + monthlyinterestrate)** monthlyinterestrate - 1)

print(f'Your monthly payment is ${monthlypayment:.2f}')