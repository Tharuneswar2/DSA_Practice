# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countHillsAndValleys(arr):
    # Initialize variables to store the count of hills and valleys
    hills = 0
    valleys = 0
    
    # Initialize a variable to store the previous slope
    prev_slope = 0
    
    # Iterate over the array from the second element to the second last element
    for i in range(1, len(arr) - 1):
        # Calculate the current slope
        curr_slope = arr[i] - arr[i - 1]
        
        # Check if the current slope is positive and the previous slope is negative
        if curr_slope > 0 and prev_slope < 0:
            # If true, increment the count of hills
            hills += 1
        
        # Check if the current slope is negative and the previous slope is positive
        elif curr_slope < 0 and prev_slope > 0:
            # If true, increment the count of valleys
            valleys += 1
        
        # Update the previous slope
        prev_slope = curr_slope
    
    # Return the count of hills and valleys
    return hills, valleys