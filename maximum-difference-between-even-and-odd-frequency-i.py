# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def max_difference(nums):
    # Initialize variables to store the maximum frequency of even and odd numbers
    max_even_freq = 0
    max_odd_freq = 0
    
    # Initialize variables to store the current frequency of even and odd numbers
    curr_even_freq = 0
    curr_odd_freq = 0
    
    # Initialize variables to store the previous number and its parity
    prev_num = None
    prev_is_even = None
    
    # Iterate over the list of numbers
    for num in nums:
        # Check if the current number is even or odd
        is_even = num % 2 == 0
        
        # If the current number has the same parity as the previous number, increment its frequency
        if prev_num is not None and is_even == prev_is_even:
            if is_even:
                curr_even_freq += 1
            else:
                curr_odd_freq += 1
        # If the current number has a different parity than the previous number, update the maximum frequency and reset the current frequency
        else:
            if prev_num is not None:
                if prev_is_even:
                    max_even_freq = max(max_even_freq, curr_even_freq)
                else:
                    max_odd_freq = max(max_odd_freq, curr_odd_freq)
            # Reset the current frequency
            if is_even:
                curr_even_freq = 1
            else:
                curr_odd_freq = 1
        
        # Update the previous number and its parity
        prev_num = num
        prev_is_even = is_even
    
    # Update the maximum frequency one last time
    if prev_is_even:
        max_even_freq = max(max_even_freq, curr_even_freq)
    else:
        max_odd_freq = max(max_odd_freq, curr_odd_freq)
    
    # Return the maximum difference between the maximum even and odd frequencies
    return max_even_freq - max_odd_freq