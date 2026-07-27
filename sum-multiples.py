# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def sum_of_multiples(limit, multiples):
    # Initialize sum to 0
    total_sum = 0
    
    # Iterate over all numbers from 1 to limit (exclusive)
    for num in range(1, limit):
        # Check if the current number is a multiple of any of the given multiples
        if any(num % multiple == 0 for multiple in multiples):
            # If it is, add it to the total sum
            total_sum += num
    
    # Return the total sum
    return total_sum

# Alternatively, using set to store multiples and math library for sum calculation
import math

def sum_of_multiples(limit, multiples):
    # Initialize a set to store unique multiples
    unique_multiples = set()
    
    # Iterate over each multiple
    for multiple in multiples:
        # Calculate the sum of multiples of the current number up to the limit
        # using the formula for the sum of an arithmetic series
        sum_of_multiple = multiple * (math.floor((limit - 1) / multiple) * (math.floor((limit - 1) / multiple) + 1)) // 2
        
        # Add the sum of the current multiple to the set
        unique_multiples.add(sum_of_multiple)
    
    # Return the sum of the unique multiples
    return sum(unique_multiples)