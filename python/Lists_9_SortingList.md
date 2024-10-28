This code shows how to use the sort() method in Python to arrange the elements of a list in ascending and descending order.

01. Creating a List

list1 = ['Ruben', 'Matthias', 'Lina', 'Daniel', 'Timo', 'Benedikt']

--> A list called list1 is created with names as elements.

02. Sorting in Ascending Order

list1.sort()

--> Function: sort() arranges the elements of list1 in ascending (alphabetical) order.
--> Operation: Modifies list1 so that the names are ordered from A to Z.
--> Result: After sorting, the list becomes ['Benedikt', 'Daniel', 'Lina', 'Matthias', 'Ruben', 'Timo'].

03. Printing the Ascending Order List
print('Sorted List (Ascending):', list1)

--> Output: Displays the sorted list in ascending order.

04. Sorting in Descending Order
list1.sort(reverse=True)

--> Function: sort(reverse=True) arranges the elements of list1 in descending (reverse alphabetical) order.
--> Operation: Re-sorts list1 in reverse, ordering names from Z to A.
--> Result: The list becomes ['Timo', 'Ruben', 'Matthias', 'Lina', 'Daniel', 'Benedikt'].

05. Printing the Descending Order List
print('Sorted List (Descending):', list1)
--> Output: Displays the sorted list in descending order.

Example Output
Sorted List (Ascending): ['Benedikt', 'Daniel', 'Lina', 'Matthias', 'Ruben', 'Timo']
Sorted List (Descending): ['Timo', 'Ruben', 'Matthias', 'Lina', 'Daniel', 'Benedikt']

--> sort(): Sorts the list in ascending order by default.
--> sort(reverse=True): Sorts the list in descending order.
--> Usage: This code demonstrates how to sort a list alphabetically in both ascending and descending order using the sort() method.










