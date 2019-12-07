def balance(string: str) -> str:
    """

    @rtype: bool
    """
    num_x = 0
    num_y = 0

    for char in string:
        if char == 'x':
            num_x += 1
        elif char == 'y':
            num_y += 1
    print("number of x's: " + str(num_x))
    print("number of y's: " + str(num_y))

    if num_x == num_y:
        print("String is balanced, number of x's and y's are equal!")
        return True
    else:
        print("String is NOT balanced, number of x's and y's are NOT equal!")
        return False


balance("xxxyyyy")
