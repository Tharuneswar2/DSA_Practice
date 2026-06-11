def max_adjacent_difference(nums):
    # Calculate the maximum difference between adjacent elements in a circular array
    # First, find the maximum difference between adjacent elements in a linear array
    max_diff_linear = max(abs(nums[i] - nums[i-1]) for i in range(1, len(nums)))
    
    # Then, find the maximum difference between the first and last elements in the array
    # considering the array as a circular array
    max_diff_circular = max(abs(nums[0] - nums[-1]), abs(nums[-1] - nums[0]))
    
    # The maximum difference between adjacent elements in a circular array is the maximum
    # of the maximum differences in the linear and circular arrays
    return max(max_diff_linear, max_diff_circular)

def max_adjacent_difference_optimized(nums):
    # Calculate the maximum difference between adjacent elements in a circular array
    # Find the minimum and maximum elements in the array
    min_val = min(nums)
    max_val = max(nums)
    
    # If the array contains only one element, return 0
    if min_val == max_val:
        return 0
    
    # Initialize the maximum difference between adjacent elements
    max_diff = 0
    
    # Iterate over the array to find the maximum difference between adjacent elements
    for i in range(len(nums)):
        # Calculate the difference between the current element and the next element
        diff = abs(nums[i] - nums[(i+1) % len(nums)])
        
        # Update the maximum difference if the current difference is larger
        max_diff = max(max_diff, diff)
    
    # Return the maximum difference between adjacent elements in the circular array
    return max_diff