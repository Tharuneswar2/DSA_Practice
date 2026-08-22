# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxEvenOdd(nums):
    # Initialize variables to store the maximum even and odd frequencies
    max_even = 0
    max_odd = 0
    
    # Initialize variables to store the current even and odd frequencies
    curr_even = 0
    curr_odd = 0
    
    # Iterate over the input array
    for num in nums:
        # Check if the current number is even
        if num % 2 == 0:
            # If the current number is even, increment the current even frequency
            curr_even += 1
            # Update the maximum even frequency if the current even frequency is greater
            max_even = max(max_even, curr_even)
            # Reset the current odd frequency
            curr_odd = 0
        else:
            # If the current number is odd, increment the current odd frequency
            curr_odd += 1
            # Update the maximum odd frequency if the current odd frequency is greater
            max_odd = max(max_odd, curr_odd)
            # Reset the current even frequency
            curr_even = 0
    
    # Return the maximum difference between the maximum even and odd frequencies
    return max(max_even, max_odd)