# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maximumDifference(nums):
    # Initialize minimum value and maximum difference
    min_val = nums[0]  # assume the first element as the minimum value
    max_diff = 0  # initialize maximum difference as 0
    
    # Iterate through the list of numbers
    for num in nums:
        # If current number is smaller than the minimum value, update the minimum value
        if num < min_val:
            min_val = num  # update the minimum value
        # If the difference between the current number and the minimum value is greater than the maximum difference, update the maximum difference
        elif num - min_val > max_diff:
            max_diff = num - min_val  # update the maximum difference
    
    # Return the maximum difference
    return max_diff