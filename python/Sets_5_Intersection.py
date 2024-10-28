
# Example 5: Set Intersection
# The intersection() method returns a new set containing common elements from both sets.
# You can also use the & operator to perform the intersection operation.

# Example sets
country_set1 = {'Finland', 'Sweden', 'Denmark', 'Norway', 'Czech Republic', 'Austria'}
country_set2 = {'Switzerland','Czech Republic','Portugal', 'Luxemburg','Norway', 'France','Austria', 'Italy'}

# Performing intersection
intersection_set = country_set1.intersection(country_set2)

# Printing the intersection set
print('Intersection of country Sets are :', intersection_set)
