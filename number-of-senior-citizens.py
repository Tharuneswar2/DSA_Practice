# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def count_seniors(citizens):
    # Initialize a counter variable to store the number of senior citizens
    senior_citizens = 0
    
    # Iterate over each citizen in the list of citizens
    for citizen in citizens:
        # Check if the citizen's age is greater than or equal to 60 (assuming 60 is the age for a senior citizen)
        if citizen['age'] >= 60:
            # If the citizen is a senior citizen, increment the counter
            senior_citizens += 1
    
    # Return the total number of senior citizens
    return senior_citizens