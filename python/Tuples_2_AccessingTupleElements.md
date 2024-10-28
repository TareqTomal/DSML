This code example demonstrates how to access elements in a tuple using indices. 

01. Creating a Tuple

flowers = ('Rose', 'Marrygold', 'Sunflower', 'daizy', 'Lili', 'orchid')
--> A tuple called flowers is created, containing different flower names as elements.

02. Accessing Elements Using Indices

first_flower = flowers[0]
third_flower = flowers[2]
last_flower = flowers[-1]

--> Access by Positive Index: flowers[0] retrieves the first element, 'Rose'.
--> Access by Positive Index: flowers[2] retrieves the third element, 'Sunflower'.
--> Access by Negative Index: flowers[-1] retrieves the last element, 'orchid'.

03. Printing Accessed Elements

print('The first flower is :', first_flower)
print('The third flower is :', third_flower)
print('The Last flower is:', last_flower)

--> Output: Displays the specific elements accessed from the tuple using both positive and negative indexing.

Example Output

The first flower is : Rose
The third flower is : Sunflower
The Last flower is : orchid


--> Tuple Indexing: Allows access to elements by their position within the tuple.
--> Positive Indexing: Starts from 0 for the first element.
--> Negative Indexing: Starts from -1 for the last element.
--> Usage: This code demonstrates accessing tuple elements by index and printing them.





