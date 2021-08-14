## Implementation
This program's purpose is to accept a list/array of integers and calculate the ratio of its elements that are positive, negative and zero.

For example:
```
[1,1,-1,-1,0] -> 0.400000,0.400000,0.200000
```

This Python program:
* Accepts user input in the form of a standard list or array of integers
* Parses through the list and creates new lists positives[], negatives[] and zeroes[]
* Divides the len() of the original list and each new list to determine the ratio
* Uses the Decimal library to obtain the full decimal amounts and round them to 6 places
