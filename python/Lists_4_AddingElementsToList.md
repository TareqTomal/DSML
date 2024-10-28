To demonstrate the code, we have used append() and insert() methods to add elements in a list.

creating list:
product_name = ['Book', 'Pencil', 'Marker', 'Box', 'Eraser']

Adding an Element with append()
product_name.append('Sharpner')

Function: append() adds an element to the end of the list.
Operation: Adds 'Sharpner' to the end of the product_name list.
Result: The list becomes ['Book', 'Pencil', 'Marker', 'Box', 'Eraser', 'Sharpner']

Inserting an Element with insert()
product_name.insert(1, 'Inserted')
Function: insert(index, element) adds an element at the specified index.
Operation: Inserts the element 'Inserted' at index 1.
Result: The list becomes ['Book', 'Inserted', 'Pencil', 'Marker', 'Box', 'Eraser', 'Sharpner']

Printing the Updated List
print('Updated product list :', product_name)
Output: Displays the updated product_name list with all modifications applied.

Example Output
Updated product list : ['Book', 'Inserted', 'Pencil', 'Marker', 'Box', 'Eraser', 'Sharpner']

append(): Adds an element to the end of the list.
insert(index, element): Adds an element at the specified index, shifting the other elements to the right.
Usage: This code demonstrates how to expand a list dynamically by appending and inserting elements.

