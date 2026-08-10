# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maxEvenOddDiff(arr):
    # Initialize variables to store the maximum even and odd frequency differences
    max_diff = 0
    
    # Initialize variables to store the current even and odd frequency counts
    even_count = 0
    odd_count = 0
    
    # Iterate over the array
    for num in arr:
        # Check if the number is even
        if num % 2 == 0:
            # If the number is even, increment the even count
            even_count += 1
        else:
            # If the number is odd, increment the odd count
            odd_count += 1
        
        # Calculate the absolute difference between the even and odd counts
        diff = abs(even_count - odd_count)
        
        # Update the maximum difference if the current difference is greater
        max_diff = max(max_diff, diff)
    
    # Return the maximum difference
    return max_diff