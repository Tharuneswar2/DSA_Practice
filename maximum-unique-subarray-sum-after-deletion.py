# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maximumUniqueSubarray(nums):
    # Initialize variables to store the maximum sum, current sum, and the start of the window
    max_sum = 0
    curr_sum = 0
    window_start = 0
    
    # Create a set to store unique elements in the current window
    unique_nums = set()
    
    # Iterate over the array
    for window_end in range(len(nums)):
        # While the current number is in the set, shrink the window from the left
        while nums[window_end] in unique_nums:
            # Remove the leftmost number from the set and subtract it from the current sum
            unique_nums.remove(nums[window_start])
            curr_sum -= nums[window_start]
            # Move the window to the right
            window_start += 1
        
        # Add the current number to the set and add it to the current sum
        unique_nums.add(nums[window_end])
        curr_sum += nums[window_end]
        
        # Update the maximum sum
        max_sum = max(max_sum, curr_sum)
    
    return max_sum