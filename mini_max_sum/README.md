## Implementation
This program's purpose is to accept a list/array of five positive integers and return the minimum and maximum values that can be made by summing exactly four of the five values in the array.

For example:
```
[1,3,5,7,9] -> 16 24
```

This Python program:
* Accepts user input in the form of a standard list or array of integers
* Sorts the array in the order of least -> greatest
* Determines the min sum by summing the values at array[0-3]
* Determines the max sum by summing the values at array[4-1]
