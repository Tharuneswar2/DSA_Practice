# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def max_difference(nums):
    # Initialize variables to store the maximum and minimum frequency of even and odd numbers
    max_even = float('-inf')  # Initialize max_even as negative infinity
    min_odd = float('inf')  # Initialize min_odd as positive infinity

    # Initialize variables to store the frequency of even and odd numbers
    even_freq = 0
    odd_freq = 0

    # Iterate through the list of numbers
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # Increment the frequency of even numbers
            even_freq += 1
            # Update max_even if the current frequency is higher
            max_even = max(max_even, even_freq)
        else:
            # Increment the frequency of odd numbers
            odd_freq += 1
            # Update min_odd if the current frequency is lower
            min_odd = min(min_odd, odd_freq)

    # Return the maximum difference between the frequency of even and odd numbers
    return max_even - min_odd