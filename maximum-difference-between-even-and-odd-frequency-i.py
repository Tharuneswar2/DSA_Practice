# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def max_difference(nums):
    # Initialize variables to store the maximum and minimum frequencies of even and odd numbers
    max_even_freq = float('-inf')  
    min_odd_freq = float('inf')
    
    # Initialize variables to store the frequency of even and odd numbers
    even_freq = 0  
    odd_freq = 0
    
    # Iterate over the list of numbers
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # Increment the frequency of even numbers
            even_freq += 1
            # Update the maximum frequency of even numbers
            max_even_freq = max(max_even_freq, even_freq)
        else:
            # Increment the frequency of odd numbers
            odd_freq += 1
            # Update the minimum frequency of odd numbers
            min_odd_freq = min(min_odd_freq, odd_freq)
    
    # Return the maximum difference between the maximum frequency of even numbers and the minimum frequency of odd numbers
    return max_even_freq - min_odd_freq