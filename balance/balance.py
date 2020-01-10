def balance(string: str) -> str:
    """
    Accepts a string and determines if the amount of "x" chars
    match the amount of "y" chars
    Ex: balance("xxxyyy") -> True
    Ex: balance("xxxxyyy") -> False

    @param str: String of various x and y chars
    @return: bool (if the string is balanced or not)
    """
    num_x = 0
    num_y = 0

    # determine amount of "x" and "y" chars for future comparison
    for char in string:
        if char == 'x':
            num_x += 1
        elif char == 'y':
            num_y += 1

    # String is balanced
    if num_x == num_y:
        return True
    # String is not balanced
    else:
        return False


balance("xxxyyyy")
