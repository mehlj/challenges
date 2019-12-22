def split(num):
    """
    Accepts an int and returns a list[] of its digits
    Ex: split(199) --> [1,9,9]
    @param num: An integer
    @return: The digits of the provided int, in the
    form of a list[]
    """
    digits = []

    while num > 0:
        digit = num % 10
        digits.append(digit)
        num //= 10

    return digits


def digit_add(digits):
    """
    Accepts a list[] of digits and returns all digits incremented by 1
    Ex: digit_add(150) --> 261
    @param digits: An integer in the form of a list of digits
    @return: int with each of the digits incremented by 1 (int)
    """

    digits_added = 0
    digits_added_list = []

    for digit in digits:
        digits_added_list.insert(0, digit + 1)

    for digit in digits_added_list:
        print(digit, end="")


digit_add(split(998))
