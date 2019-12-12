def split(num):
	"""
    	Accepts an int and returns a list[] of its digits
    	Ex: split(199) --> [1,9,9]
    	@param num: An integer
    	@return: The digits of the provided int, in the
	form of a list[]
    	"""
	digits = []

	while (num > 0):
		digit = num % 10
		digits.append(digit)
		num //=10

	return digits


def calc_ap(digits):
	"""
    	Accepts a list[] of digits and returns the Additive Persistence
	of the number. 
    	Ex: calc_ap(199) --> 3
    	@param digits: An integer in the form of a list of digits
    	@return: The additive persistence of the number provided (int)
    	"""

	sum = 0
	ap = 0

	for digit in digits:
		sum += digit

	ap += 1
	newsum = 0

	# Loop through sum of digits until amount of digits is 1
	while (len(split(sum)) > 1):
		for digit in split(sum):
			newsum += digit
		ap += 1
		sum = newsum
		if len(split(newsum)) == 1:
			break
		newsum = 0

	return ap


print(str(calc_ap(split(199))))
