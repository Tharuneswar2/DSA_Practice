def count_seniors(citizens):
    # Initialize a counter for senior citizens
    senior_count = 0
    
    # Iterate over each citizen in the list
    for citizen in citizens:
        # Check if the citizen's age is greater than or equal to 60
        if citizen['age'] >= 60:
            # If the citizen is a senior, increment the counter
            senior_count += 1
    
    # Return the total count of senior citizens
    return senior_count

# Example usage:
citizens = [
    {'name': 'John', 'age': 55},
    {'name': 'Alice', 'age': 65},
    {'name': 'Bob', 'age': 70},
    {'name': 'Charlie', 'age': 58},
    {'name': 'David', 'age': 62}
]

print(count_seniors(citizens))  # Output: 3