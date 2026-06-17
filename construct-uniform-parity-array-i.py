def constructArray(n, k):
    # Initialize the result array with the first n - k - 1 elements
    result = list(range(1, n - k))
    
    # Initialize the two pointers for the remaining elements
    left, right = n - k, n
    
    # Fill the remaining elements in the result array
    for i in range(n - k, n):
        # If k is even, append the left element, otherwise append the right element
        if k % 2 == 0:
            result.append(left)
            left += 1
        else:
            result.append(right)
            right -= 1
        # Decrement k by 1
        k -= 1
    
    return result