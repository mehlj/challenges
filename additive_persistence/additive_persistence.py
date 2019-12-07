def split(num):
	digits = []

	while (num > 0):
		digit = num % 10
		digits.append(digit)
		num //=10

	return digits

def calc_ap(digits):
	sum = 0
	ap = 0

	for digit in digits:
		sum += digit

	ap += 1
	newsum = 0

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