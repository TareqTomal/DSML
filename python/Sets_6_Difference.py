
# Example 6: Set Difference
# The difference() method returns a new set containing elements present in one set but not in the other.
# You can also use the - operator to perform the difference operation.

# Example sets
country_set1 = {'Finland', 'Sweden', 'Denmark', 'Norway', 'Czech Republic', 'Austria'}
country_set2 = {'Switzerland','Czech Republic','Portugal', 'Luxemburg','Norway', 'France','Austria', 'Italy'}

# Performing difference (elements in set1 but not in set2)
difference_set = country_set1.difference(country_set2)

# Printing the difference set
print('Difference countries of Sets:', difference_set)
