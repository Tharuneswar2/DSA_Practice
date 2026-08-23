# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def max_difference(nums):
    # Initialize variables to store the maximum and minimum frequency differences
    max_diff = 0
    min_diff = 0
    
    # Initialize variables to store the frequency of even and odd numbers
    even_freq = 0
    odd_freq = 0
    
    # Iterate through the list of numbers
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # If the number is even, increment the even frequency
            even_freq += 1
        else:
            # If the number is odd, increment the odd frequency
            odd_freq += 1
        
        # Calculate the current difference between even and odd frequencies
        curr_diff = abs(even_freq - odd_freq)
        
        # Update the maximum difference if the current difference is greater
        if curr_diff > max_diff:
            max_diff = curr_diff
        
        # Update the minimum difference if the current difference is smaller
        if curr_diff < min_diff or min_diff == 0:
            min_diff = curr_diff
    
    # Return the maximum difference
    return max_diff