def sumZero(n):
    # Initialize an empty list to store the result
    result = []
    
    # If n is odd, we can start with 0 and then add pairs of numbers that sum to 0
    if n % 2 != 0:
        result.append(0)
        n -= 1
    
    # Calculate the pairs of numbers that sum to 0
    for i in range(1, n // 2 + 1):
        # Append the positive number
        result.append(i)
        # Append the negative number
        result.append(-i)
    
    return result

# Test the function
print(sumZero(5))  # Output: [0, 1, -1, 2, -2]