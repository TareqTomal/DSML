"""
# Dictionary Filtering Based on Conditions Example

This script demonstrates filtering a dictionary to retain only key-value pairs that meet a specific condition.

## Structure
- `scores`: A dictionary containing names as keys and corresponding scores as values.

## Operations

1. **Filtering Dictionary by Condition**
   - Uses dictionary comprehension to create a new dictionary with entries where the score is 30 or higher.
   - `filtered_scores = {name: score for name, score in scores.items() if score >= 30}`:
     - Iterates over each key-value pair in `scores`.
     - Retains pairs where `score >= 30`.

## Output
- Prints the filtered dictionary containing only names with scores 30 or above.

"""
