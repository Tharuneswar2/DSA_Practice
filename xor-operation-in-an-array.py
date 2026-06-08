def xorOperation(n, start):
    # Initialize result with the first element of the array
    result = start
    
    # Iterate over the range from 1 to n (exclusive)
    for i in range(1, n):
        # Calculate the next element in the array using the formula start + 2 * i
        next_element = start + 2 * i
        # XOR the result with the next element
        result ^= next_element
    
    # Return the final result
    return result