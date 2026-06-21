def getMaximumGenerated(n):
    # If n is 0 or 1, return n because the generated array will be [0] or [0, 1]
    if n == 0 or n == 1:
        return n
    
    # Initialize the generated array with the first two elements
    generated = [0, 1]
    
    # Initialize the maximum value
    max_val = 1
    
    # Generate the array up to n elements
    for i in range(2, n + 1):
        # If the index is even, the value is the same as the index divided by 2
        if i % 2 == 0:
            generated.append(generated[i // 2])
        # If the index is odd, the value is the sum of the two elements at the previous even index and the index divided by 2 plus 1
        else:
            generated.append(generated[i // 2] + generated[i // 2 + 1])
        
        # Update the maximum value
        max_val = max(max_val, generated[i])
    
    # Return the maximum value
    return max_val