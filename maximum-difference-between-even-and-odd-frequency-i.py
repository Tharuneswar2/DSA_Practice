# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maxEvenOddDiff(arr):
    # Initialize variables to store the maximum even and odd frequencies
    max_even = 0
    max_odd = 0
    
    # Initialize variables to store the current even and odd frequencies
    curr_even = 0
    curr_odd = 0
    
    # Initialize variable to store the maximum difference
    max_diff = 0
    
    # Iterate over the array
    for num in arr:
        # If the number is even, increment the current even frequency
        if num % 2 == 0:
            curr_even += 1
            # Update the maximum even frequency
            max_even = max(max_even, curr_even)
        # If the number is odd, increment the current odd frequency
        else:
            curr_odd += 1
            # Update the maximum odd frequency
            max_odd = max(max_odd, curr_odd)
        
        # Update the maximum difference
        max_diff = max(max_diff, abs(max_even - max_odd))
    
    # Return the maximum difference
    return max_diff