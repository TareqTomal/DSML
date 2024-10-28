To remove elements from a list we have used the remove() and pop() methods.

1. Creating a List

ice_cream_flavors = ['vanilla', 'chocolet', 'mango', 'lemon', 'cherry']
--> A list called ice_cream_flavors is created with initial flavors: 'vanilla', 'chocolet', 'mango', 'lemon', and 'cherry'.

2. Removing an Element with remove()

ice_cream_flavors.remove('mango')

--> Function: remove(element) removes the first occurrence of the specified element from the list.
--> Operation: Removes 'mango' from ice_cream_flavors.
--> Result: The list becomes ['vanilla', 'chocolet', 'lemon', 'cherry'].

3. Removing an Element with pop()

popped_item = ice_cream_flavors.pop(3)

--> Function: pop(index) removes and returns the element at the specified index. If no index is specified, it removes the last item.
--> Operation: Removes the element at index 3, which is 'cherry'.
--> Result: The list becomes ['vanilla', 'chocolet', 'lemon'], and 'cherry' is stored in the variable popped_item.

4. Printing the Updated List and Popped Item

print('The ice cream flavors list after removal:', ice_cream_flavors)
print('Popped ice cream flavor:', popped_item)
--> Output: Displays the updated ice_cream_flavors list and the flavor that was removed using pop()


Example Output
The ice cream flavors list after removal: ['vanilla', 'chocolet', 'lemon']
Popped ice cream flavor: cherry

--> remove(element): Removes the specified element from the list.
--> pop(index): Removes and returns the element at the specified index.
--> Usage: This code demonstrates how to modify a list by removing specific elements using remove() and pop().


