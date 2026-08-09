# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxEvenOdd(arr):
    # Initialize variables to store the maximum difference and the frequency of even and odd numbers
    max_diff = 0
    even_freq = 0
    odd_freq = 0
    
    # Iterate over the array to count the frequency of even and odd numbers
    for num in arr:
        # Check if the number is even
        if num % 2 == 0:
            # Increment the even frequency
            even_freq += 1
        else:
            # Increment the odd frequency
            odd_freq += 1
    
    # Calculate the maximum difference between even and odd frequencies
    max_diff = abs(even_freq - odd_freq)
    
    # Return the maximum difference
    return max_diff