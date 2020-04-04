def numJewelsInStones(J, S):
    """
    Determines the amount of jewels (J) present in list of stones (S)
    Ex: numJewelsInStones("agAsd","aGA") --> 2
    @param J: Defined list of jewels
    @param S: Defined list of stones
    @return: Number of jewels present in stones
    """
    num = 0

    for jewel in J:
        for stone in S:
            if jewel == stone:
                num += 1
    return num


print(numJewelsInStones("agAsd","aGA"))