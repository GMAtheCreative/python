def tax_calculator(earning):

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
