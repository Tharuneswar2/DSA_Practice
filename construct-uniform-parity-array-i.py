# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def constructArray(n, k):
    # Initialize an empty list to store the result
    result = []
    
    # Start with the first number and the last number
    left, right = 1, n
    
    # Fill the result list with numbers from both ends
    while left <= right:
        # If k is odd, append the number from the left
        if k % 2 == 1:
            result.append(left)
            left += 1
        # If k is even, append the number from the right
        else:
            result.append(right)
            right -= 1
        # Decrement k by 1
        k -= 1
    
    # Fill the remaining numbers in the result list
    if left <= right:
        result.extend(range(left, right + 1))
    
    # Return the result
    return result