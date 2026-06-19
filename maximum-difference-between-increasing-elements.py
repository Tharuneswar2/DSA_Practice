def maximumDifference(nums):
    # Initialize minimum value and maximum difference
    min_val = nums[0]
    max_diff = 0
    
    # Iterate through the list of numbers
    for num in nums:
        # If current number is smaller than min_val, update min_val
        if num < min_val:
            min_val = num
        # If difference between current number and min_val is greater than max_diff, update max_diff
        elif num - min_val > max_diff:
            max_diff = num - min_val
    
    # Return the maximum difference
    return max_diff

# Test the function
print(maximumDifference([7,1,5,4]))  # Output: 4
print(maximumDifference([9,4,3,2]))  # Output: 0