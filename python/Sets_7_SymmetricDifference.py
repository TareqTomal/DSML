
# Example 7: Set Symmetric Difference
# The symmetric_difference() method returns a new set containing elements present in either set but not in both.
# You can also use the ^ operator to perform the symmetric difference operation.

# Example sets
country_set1 = {'Finland', 'Sweden', 'Denmark', 'Norway', 'Czech Republic', 'Austria'}
country_set2 = {'Switzerland','Czech Republic','Portugal', 'Luxemburg','Norway', 'France','Austria', 'Italy'}


# Performing symmetric difference
symmetric_difference_set = country_set1.symmetric_difference(country_set2)

# Printing the symmetric difference set
print('Symmetric Difference of the country Sets is :', symmetric_difference_set)
