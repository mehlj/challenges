## Implementation
This program's purpose is to determine the amount of `n / 2` and `n - 1` operations are needed to bring `n` to zero.

For example:
```
16 -> 5
16 is even; divide by 2 and obtain 8.
8 is even; divide by 2 and obtain 4.
4 is even; divide by 2 and obtain 2.
2 is even; divide by 2 and obtain 1.
1 is odd; subtract 1 and obtain 0.
```

This Python program:
* Accepts user input in the form of a non-negative integer
* Loops until `num = 0`
* Divides `num / 2` if `num` is even
* Subtracts `num - 1` if `num` is odd
* Increments a counter
* Returns the counter once `num = 0`