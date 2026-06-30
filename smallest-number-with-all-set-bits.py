def smallest_number_with_all_set_bits(n):
    # Initialize the result with 1 (which has the least significant bit set)
    result = 1
    
    # Loop until we have set all the bits
    while bin(result).count('1') < n:
        # Left shift the result by 1 (to make space for the new bit)
        # and add 1 (to set the least significant bit)
        result = (result << 1) + 1
    
    return result

# Test the function
print(smallest_number_with_all_set_bits(3))  # Output: 7