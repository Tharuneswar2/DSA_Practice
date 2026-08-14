# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def max_difference(nums):
    # Initialize variables to store the maximum frequency of even and odd numbers
    max_even_freq = 0
    max_odd_freq = 0
    
    # Initialize variables to store the current frequency of even and odd numbers
    curr_even_freq = 0
    curr_odd_freq = 0
    
    # Initialize variables to store the maximum difference between even and odd frequencies
    max_diff = 0
    
    # Iterate over the array
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # Increment the current even frequency
            curr_even_freq += 1
            # Update the maximum even frequency if necessary
            max_even_freq = max(max_even_freq, curr_even_freq)
        else:
            # Increment the current odd frequency
            curr_odd_freq += 1
            # Update the maximum odd frequency if necessary
            max_odd_freq = max(max_odd_freq, curr_odd_freq)
        
        # Update the maximum difference between even and odd frequencies
        max_diff = max(max_diff, abs(max_even_freq - curr_odd_freq), abs(max_odd_freq - curr_even_freq))
    
    # Return the maximum difference between even and odd frequencies
    return max_diff