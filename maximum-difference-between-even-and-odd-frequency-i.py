# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maxEvenOdd(arr):
    # Initialize variables to store the maximum difference and the current difference
    max_diff = 0
    curr_diff = 0
    
    # Initialize variables to store the count of even and odd numbers
    even_count = 0
    odd_count = 0
    
    # Iterate over the array to count the even and odd numbers
    for num in arr:
        # Check if the number is even
        if num % 2 == 0:
            # Increment the even count
            even_count += 1
        else:
            # Increment the odd count
            odd_count += 1
        
        # Update the current difference
        curr_diff = even_count - odd_count
        
        # Update the maximum difference if the current difference is greater
        max_diff = max(max_diff, curr_diff)
    
    # Return the maximum difference
    return max_diff