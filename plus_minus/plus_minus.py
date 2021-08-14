#!/usr/bin/env python3

import decimal

def plus_minus(integers):
    """
    Accepts a list[] of integers and returns ratio of elements that are positive, negative and zero
    Ex: plus_minus([1,1,0,-1,-1]) --> 0.400000,0.400000,0.200000
    @param integers: A list of integers, zero, positive, or negative
    @return: N/A
    """    
    positives = []
    negatives = []
    zeroes    = []

    for i in integers:
      if i > 0:
        positives.append(i)
      elif i < 0:
        negatives.append(i)
      else:
        zeroes.append(i)

    print(round(decimal.Decimal(len(positives) / len(integers)),6))
    print(round(decimal.Decimal(len(negatives) / len(integers)),6))
    print(round(decimal.Decimal(len(zeroes) / len(integers)),6))


if __name__ == '__main__':
  plus_minus([1,1,-1,-1,0])
