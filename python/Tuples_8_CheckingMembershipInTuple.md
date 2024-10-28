Checking Membership in a Tuple:

This code example demonstrates how to check if an element exists within a tuple using the in keyword in Python.

01. Creating a Tuple

fruits = ('avocado', 'kiwi', 'cherry', 'mango', 'orange', 'papaya')

--> A tuple called fruits is created, containing several fruit names.

02. Checking Membership with in

if 'banana' in fruits:
    print('Banana is in the tuple')
else:
    print('Banana is not in the tuple')


--> Membership Check: The in keyword checks if 'banana' exists in the fruits tuple.
--> Condition:
	If 'banana' is found in the tuple, it prints "Banana is in the tuple".
	If 'banana' is not in the tuple, it prints "Banana is not in the tuple".

--> Operation: In this case, since 'banana' is not an element in the fruits tuple, the output will confirm its absence.

03. Printing the Result
--> Based on the membership check, a message is printed indicating whether 'banana' is in the tuple.


Example Output

Banana is not in the tuple

--> in Keyword: Used to check if an element exists within a tuple, returning True if present and False if not.
--> Usage: This code demonstrates a simple way to verify the presence of an item in a tuple and conditionally print a message based on the result.
















