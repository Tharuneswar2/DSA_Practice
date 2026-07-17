# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def smallest_missing_integer(nums):
    # Create a set from the input list for efficient lookups
    num_set = set(nums)
    
    # Initialize the smallest missing integer to 1
    smallest_missing = 1
    
    # Initialize the prefix sum to 0
    prefix_sum = 0
    
    # Iterate over the input list
    for num in nums:
        # Add the current number to the prefix sum
        prefix_sum += num
        
        # While the prefix sum is greater than or equal to the smallest missing integer
        # and the smallest missing integer is in the set, increment the smallest missing integer
        while prefix_sum >= smallest_missing and smallest_missing in num_set:
            smallest_missing += 1
    
    # Return the smallest missing integer
    return smallest_missing