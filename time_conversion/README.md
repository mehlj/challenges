## Implementation
This program's purpose is to accept a 12-hour time (string) and return the 24-hour equivalent (string)

For example:
```
"06:40:03PM" -> "18:40:03"
```

This Python program:
* Accepts user input in the form of a string
* Splits the string by the delimiter `":"`
* Determines AM/PM nature using find()
* Converts the hour portion of the string to 24-hour, using a simple logic flow
* Builds the return string using the new hour format, the original minutes/seconds portions
* Strips the AM/PM from the return string
