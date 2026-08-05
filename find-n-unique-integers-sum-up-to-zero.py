# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sumZero(n):
    # Initialize an empty list to store the result
    result = []
    
    # If n is odd, we can always include 0 in the result
    if n % 2 != 0:
        # Add 0 to the result
        result.append(0)
        # Decrement n by 1 since we've already included one number
        n -= 1
    
    # Now n is even, we can pair numbers with their negations
    # We start from 1 and go up to n//2 (integer division)
    for i in range(1, n//2 + 1):
        # Add the current number to the result
        result.append(i)
        # Add the negation of the current number to the result
        result.append(-i)
    
    # Return the result
    return result