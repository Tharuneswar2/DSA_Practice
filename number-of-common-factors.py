# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def common_factors(a, b):
    # Initialize count of common factors to 0
    count = 0
    
    # Find the smaller number to optimize the loop
    smaller = min(a, b)
    
    # Iterate from 1 to the smaller number (inclusive)
    for i in range(1, smaller + 1):
        # Check if 'i' is a factor of both 'a' and 'b'
        if a % i == 0 and b % i == 0:
            # If 'i' is a common factor, increment the count
            count += 1
    
    # Return the total count of common factors
    return count