def roman_arbic_digits_parser(roman_string):

	roman_string = list(roman_string.replace(' ',''))
	roman_digits ={
		'I': 1,
		'V': 5,
		'X': 10,
		'L': 50,
		'C': 100,
		'D': 500,
		'M': 1000
	}
	current_rank_digit = 0
	result = 0
	for digit in roman_string[::-1]:

		if roman_digits[digit]>=current_rank_digit: 
			current_rank_digit = roman_digits[digit]
			result += roman_digits[roman_string.pop()]
		else:
			result -= roman_digits[roman_string.pop()]

	return result
print(roman_arbic_digits_parser('XIV'))

