Python List Sorting Techniques
This guide details five key methods for sorting numerical lists in Python, ideal for different requirements and levels of efficiency.

1. sorted() Function
Description: Generates a new sorted list without modifying the original.
Example: sorted(list).
Use Case: Suitable for when you need both sorted and unsorted versions.

3. sort() Method
Description: Sorts the list in place, directly changing the original.
Example: list.sort().
Use Case: Efficient when you don’t need to retain the original order.

5. Reverse Sorting with Slicing ([::-1])
Description: Reverses list order, useful for descending order post-sort.
Example: list[::-1].
Use Case: Quickly reverses sorted or unsorted lists.

7. Custom Sorting Using Lambda with sorted()
Description: Allows defining custom sort criteria, useful for sorting based on specific values or patterns.
Example: sorted(list, key=lambda x: condition).
Use Case: Advanced sorting based on specific attributes or conditions.

9. heapq Module
Description: Provides heap-based sorting, offering memory efficiency for large lists.
Example: heapq.nsmallest(n, list).
Use Case: Ideal for large datasets where memory usage is critical.
