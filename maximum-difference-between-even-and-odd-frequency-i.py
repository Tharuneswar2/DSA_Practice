# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxEvenOdd(arr):
    # Initialize variables to store the maximum difference, even frequency, and odd frequency
    max_diff = 0
    even_freq = 0
    odd_freq = 0
    
    # Iterate through the array
    for num in arr:
        # Check if the number is even
        if num % 2 == 0:
            # If the number is even, increment the even frequency
            even_freq += 1
        else:
            # If the number is odd, increment the odd frequency
            odd_freq += 1
        
        # Calculate the absolute difference between even and odd frequencies
        diff = abs(even_freq - odd_freq)
        
        # Update the maximum difference if the current difference is greater
        max_diff = max(max_diff, diff)
    
    # Return the maximum difference
    return max_diff