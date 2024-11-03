
# Example 2: Tuple Unpacking
# Unpacking a tuple with multiple values into variables, including using the * operator for remaining values.

# Example tuple
person_info = ('Ruben', 18, 'Job - Analyst', 'Berliner street 15, Berlin')

# Unpacking tuple into variables
name, age, *other_details = person_info

print('Name:', name)
print('Age:', age)
print('Other Details:', other_details)