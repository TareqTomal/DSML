Tuple Immutability

This code example demonstrates the immutability of tuples, a fundamental characteristic that prevents elements from being modified once the tuple is created. Attempting to alter a tuple element raises a TypeError.


01. Creating a Tuple

roll_number = (20, 52, 63, 77, 82, 95)

--> A tuple called roll_number is created with six integer elements representing roll numbers.


02. Attempting to Modify an Element

try:
    roll_number[0] = 17
except TypeError as e:
    print('Error:', e)

--> mmutability Check: Since tuples are immutable, the line roll_number[0] = 17 attempts to change the first element, but this is not allowed in tuples.

--> Error Handling: The try-except block is used to handle the resulting TypeError.
------> TypeError: Raised when attempting to assign a new value to a tuple element.

--> Output: The error message is captured and printed, demonstrating that tuples cannot be modified.


03. Printing the Error Message
--> If the modification attempt fails, the error message explains why the operation is not permitted.


Example Output
Error: 'tuple' object does not support item assignment

--> Tuple Immutability: Tuples in Python are immutable, meaning their contents cannot be altered after creation.

--> Error Handling: The code demonstrates how attempting to modify a tuple results in a TypeError, which can be caught and handled using a try-except block.

--> Usage: This code illustrates tuple immutability and how to handle errors that arise from attempted modifications.


