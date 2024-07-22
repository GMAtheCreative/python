def tax_calculator_single(earning):

	tax = 0
	tax_1 = 0
	tax_2 = 0
	first_cut = 0

	if earning <= 8_350:
		tax += earning * 0.1
		

	elif earning > 8_350:

		first_cut += earning - 8_350
		tax_1 += 8_350 * 0.1
		
		if first_cut <= 8_350:
			tax_2 += first_cut * 0.1

		elif first_cut > 8_350 and first_cut < 33_951:
			tax_2 += first_cut * 0.15

		elif first_cut > 33_950 and first_cut < 82_251:
			tax_2 += first_cut * 0.25
		
		elif first_cut > 82_250 and first_cut < 171_551:
			tax_2 += first_cut * 0.28

		
		elif first_cut > 171_550 and first_cut < 372_951:
			tax_2 += first_cut * 0.33
		
		elif first_cut > 372_950:
			tax_2 += first_cut * 0.35

		tax += tax_1 + tax_2

	return tax



def tax_calculator_married_jointly(earning):

	tax = 0
	tax_1 = 0
	tax_2 = 0
	first_cut = 0

	if earning <= 16_700:
		tax += earning * 0.1
		

	elif earning > 16_700:

		first_cut += earning - 16_700
		tax_1 += 16_700 * 0.1
		
		if first_cut <= 16_700:
			tax_2 += first_cut * 0.1

		elif first_cut > 16_700 and first_cut < 67_901:
			tax_2 += first_cut * 0.15

		elif first_cut > 67-900 and first_cut < 137_051:
			tax_2 += first_cut * 0.25
		
		elif first_cut > 137_050 and first_cut < 208_851:
			tax_2 += first_cut * 0.28

		
		elif first_cut > 208_850 and first_cut < 372_951:
			tax_2 += first_cut * 0.33
		
		elif first_cut > 372_950:
			tax_2 += first_cut * 0.35

		tax += tax_1 + tax_2

	return tax



def tax_calculator_married_separately(earning):
	tax = 0
	tax_1 = 0
	tax_2 = 0
	first_cut = 0

	if earning <= 8_350:
		tax += earning * 0.1
		

	elif earning > 8_350:

		first_cut += earning - 8_350
		tax_1 += 8_350 * 0.1
		
		if first_cut <= 8_350:
			tax_2 += first_cut * 0.1

		elif first_cut > 8_350 and first_cut < 33_951:
			tax_2 += first_cut * 0.15

		elif first_cut > 33_950 and first_cut < 68_526:
			tax_2 += first_cut * 0.25
		
		elif first_cut > 68_526 and first_cut < 104_426:
			tax_2 += first_cut * 0.28

		
		elif first_cut > 104_425 and first_cut < 186_476:
			tax_2 += first_cut * 0.33
		
		elif first_cut > 186_475:
			tax_2 += first_cut * 0.35

		tax += tax_1 + tax_2

	return tax




def tax_calculator_head_of_household(earning):
	tax = 0
	tax_1 = 0
	tax_2 = 0
	first_cut = 0

	if earning <= 11_950:
		tax += earning * 0.1
		

	elif earning > 11_950:

		first_cut += earning - 11_950
		tax_1 += 11_950 * 0.1
		
		if first_cut <= 11_950:
			tax_2 += first_cut * 0.1

		elif first_cut > 11_950 and first_cut < 45_501:
			tax_2 += first_cut * 0.15

		elif first_cut > 45_500 and first_cut < 117_451:
			tax_2 += first_cut * 0.25
		
		elif first_cut > 117_450 and first_cut < 190_201:
			tax_2 += first_cut * 0.28

		
		elif first_cut > 190_200 and first_cut < 372_951:
			tax_2 += first_cut * 0.33
		
		elif first_cut > 372_950:
			tax_2 += first_cut * 0.35

		tax += tax_1 + tax_2

	return tax
