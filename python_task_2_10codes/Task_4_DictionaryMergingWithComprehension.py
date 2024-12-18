
# Example 4: Dictionary Merging with Comprehension
# Merging two dictionaries and modifying values using dictionary comprehension.

# Example dictionaries
fruit_box1 = {'apple': 20, 'berries': 28, 'cherry': 30}
fruit_box2 = {'berries': 42, 'cherry': 50, 'dates': 60}

# Merging and modifying values
total_fruits = {key: fruit_box1.get(key, 0) + fruit_box2.get(key, 0) for key in set(fruit_box1) | set(fruit_box2)}

print('Merged and Modified number of fruits are:', total_fruits)
