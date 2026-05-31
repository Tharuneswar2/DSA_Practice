def count_indices_with_opposite_parity(arr):
    # Initialize variables to store the count of even and odd indices
    even_count = 0
    odd_count = 0
    
    # Iterate over the array
    for i in range(len(arr)):
        # Check if the index is even
        if i % 2 == 0:
            # If the index is even, increment the even count
            even_count += 1
        else:
            # If the index is odd, increment the odd count
            odd_count += 1
    
    # The count of indices with opposite parity is the minimum of even and odd counts
    return min(even_count, odd_count)

# Test the function
arr = [1, 2, 3, 4, 5]
print(count_indices_with_opposite_parity(arr))