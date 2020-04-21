def numberOfSteps(num):
    """
    Determines the amount of iterations needed to reach zero starting from num
    Ex: numberOfSteps(16) --> 5
    @param num: Integer that needs to reach zero
    @return: Number of iterations needed to reach zero
    """
    counter = 0

    while num != 0:
        if num % 2 == 0:
            print(str(num) + " is even; divide by 2 and obtain " + str((num // 2)) + ".")
            counter += 1
            num = num // 2
        else:
            print(str(num) + " is odd; subtract 1 and obtain " + str((num - 1)) + ".")
            counter += 1
            num = num - 1
    return counter


print(numberOfSteps(16))