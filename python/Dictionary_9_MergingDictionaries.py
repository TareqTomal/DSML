
# Example 9: Merging Dictionaries
# You can merge dictionaries using the update() method or the ** operator in Python 3.9+.

gio_info1 = {'place': 'Dhaka', 'postal_code': 1219}       # Example dictionary
gio_info2 = {'country': 'BD', 'population': 70000000}    


gio_info1.update(gio_info2)                               # Merging using update()

print('Merged gio information:', gio_info1)                        # Printing the merged dictionary
