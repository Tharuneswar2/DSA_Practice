# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def max_difference(nums):
    # Initialize variables to store the maximum frequency of even and odd numbers
    max_even_freq = 0
    max_odd_freq = 0
    
    # Initialize variables to store the current frequency of even and odd numbers
    curr_even_freq = 0
    curr_odd_freq = 0
    
    # Initialize variables to store the previous even and odd numbers
    prev_even = None
    prev_odd = None
    
    # Iterate over the list of numbers
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # If the number is even, increment the current even frequency
            curr_even_freq += 1
            
            # If the previous number was odd, update the maximum odd frequency
            if prev_odd is not None:
                max_odd_freq = max(max_odd_freq, curr_odd_freq)
                curr_odd_freq = 0
            
            # Update the previous even number
            prev_even = num
        else:
            # If the number is odd, increment the current odd frequency
            curr_odd_freq += 1
            
            # If the previous number was even, update the maximum even frequency
            if prev_even is not None:
                max_even_freq = max(max_even_freq, curr_even_freq)
                curr_even_freq = 0
            
            # Update the previous odd number
            prev_odd = num
    
    # Update the maximum even and odd frequencies one last time
    max_even_freq = max(max_even_freq, curr_even_freq)
    max_odd_freq = max(max_odd_freq, curr_odd_freq)
    
    # Return the maximum difference between the maximum even and odd frequencies
    return max_even_freq - max_odd_freq