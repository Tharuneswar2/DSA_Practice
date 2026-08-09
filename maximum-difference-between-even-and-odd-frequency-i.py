# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxEvenOdd(nums):
    # Initialize variables to store the maximum difference and the current difference
    max_diff = 0
    curr_diff = 0
    
    # Initialize variables to store the count of even and odd numbers
    even_count = 0
    odd_count = 0
    
    # Iterate over the array
    for num in nums:
        # Check if the number is even
        if num % 2 == 0:
            # If the number is even, increment the even count
            even_count += 1
        else:
            # If the number is odd, increment the odd count
            odd_count += 1
        
        # Update the current difference
        curr_diff = even_count - odd_count
        
        # Update the maximum difference if the current difference is greater
        max_diff = max(max_diff, curr_diff)
    
    # Return the maximum difference
    return max_diff