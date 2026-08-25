# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxEvenOdd(arr):
    # Initialize variables to store the maximum difference and the frequency of even and odd numbers
    max_diff = 0
    even_freq = 0
    odd_freq = 0
    
    # Iterate over the array to calculate the frequency of even and odd numbers
    for num in arr:
        # Check if the number is even
        if num % 2 == 0:
            # Increment the frequency of even numbers
            even_freq += 1
        else:
            # Increment the frequency of odd numbers
            odd_freq += 1
        
        # Calculate the absolute difference between the frequency of even and odd numbers
        diff = abs(even_freq - odd_freq)
        
        # Update the maximum difference if the current difference is greater
        max_diff = max(max_diff, diff)
    
    # Return the maximum difference
    return max_diff