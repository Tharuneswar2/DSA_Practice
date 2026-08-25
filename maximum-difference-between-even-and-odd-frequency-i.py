# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def max_difference(nums):
    # Initialize variables to store the maximum and minimum frequency of even and odd numbers
    max_even_freq = 0
    min_odd_freq = float('inf')  # Initialize with positive infinity
    
    # Initialize variables to store the frequency of even and odd numbers
    even_freq = 0
    odd_freq = 0
    
    # Iterate over the list of numbers
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # If the number is even, increment the even frequency
            even_freq += 1
            # Update the maximum even frequency
            max_even_freq = max(max_even_freq, even_freq)
        else:
            # If the number is odd, increment the odd frequency
            odd_freq += 1
            # Update the minimum odd frequency
            min_odd_freq = min(min_odd_freq, odd_freq)
    
    # Return the maximum difference between the maximum even frequency and the minimum odd frequency
    return max_even_freq - min_odd_freq