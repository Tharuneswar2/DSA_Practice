# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def count_indices_with_opposite_parity(arr):
    # Initialize variables to store the count of even and odd indices
    even_count = 0
    odd_count = 0
    
    # Iterate over the array with enumerate to get both index and value
    for i, val in enumerate(arr):
        # Check if the index is even
        if i % 2 == 0:
            # If the index is even, increment the even count if the value is odd
            if val % 2 != 0:
                even_count += 1
        else:
            # If the index is odd, increment the odd count if the value is even
            if val % 2 == 0:
                odd_count += 1
                
    # Return the sum of even and odd counts
    return even_count + odd_count