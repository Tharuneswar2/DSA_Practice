def maximumUniqueSubarray(nums):
    # Initialize variables to store the maximum sum and the current sum
    max_sum = 0
    curr_sum = 0
    
    # Initialize a set to store unique elements in the current window
    unique_nums = set()
    
    # Initialize two pointers for the sliding window
    left = 0
    
    # Iterate over the array
    for right in range(len(nums)):
        # While the current number is in the set, remove the leftmost number from the set and subtract it from the current sum
        while nums[right] in unique_nums:
            unique_nums.remove(nums[left])
            curr_sum -= nums[left]
            left += 1
        
        # Add the current number to the set and add it to the current sum
        unique_nums.add(nums[right])
        curr_sum += nums[right]
        
        # Update the maximum sum
        max_sum = max(max_sum, curr_sum)
    
    return max_sum