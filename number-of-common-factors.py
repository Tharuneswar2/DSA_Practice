def common_factors(a, b):
    # Initialize count of common factors
    count = 0
    
    # Find the smaller number to optimize the loop
    smaller = min(a, b)
    
    # Iterate from 1 to the smaller number
    for i in range(1, smaller + 1):
        # Check if the current number is a factor of both a and b
        if a % i == 0 and b % i == 0:
            # If it is, increment the count
            count += 1
    
    # Return the count of common factors
    return count

# Test the function
print(common_factors(12, 18))  # Output: 6