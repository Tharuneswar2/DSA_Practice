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
    
    # Iterate over the list of numbers
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # Increment the current frequency of even numbers
            curr_even_freq += 1
            # Update the maximum frequency of even numbers if necessary
            max_even_freq = max(max_even_freq, curr_even_freq)
        else:
            # Increment the current frequency of odd numbers
            curr_odd_freq += 1
            # Update the maximum frequency of odd numbers if necessary
            max_odd_freq = max(max_odd_freq, curr_odd_freq)
        
        # Update the maximum difference between even and odd frequencies if necessary
        max_diff = max(max_diff, abs(max_even_freq - max_odd_freq))
    
    # Return the maximum difference between even and odd frequencies
    return max_diff