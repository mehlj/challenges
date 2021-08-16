#!/usr/bin/env python3

def mini_max_sum(integers):
    """
    Accepts a list[] of five positive integers and returns the min and max values via summing four values
    Ex: mini_max_sum([1,3,5,7,9]) --> 16 24
    @param integers: A list of positive integers
    @return: min_sum, 
    """    
    integers.sort()

    min_sum = integers[0] + integers[1] + integers[2] + integers[3]
    max_sum = integers[4] + integers[3] + integers[2] + integers[1]

    print(min_sum, max_sum)


if __name__ == '__main__':
  mini_max_sum([1,3,5,7,9])
