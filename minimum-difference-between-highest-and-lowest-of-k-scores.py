def minimumDifference(nums, k):
    # Sort the list in ascending order
    nums.sort()
    
    # Initialize the minimum difference as infinity
    min_diff = float('inf')
    
    # Iterate over the sorted list with a sliding window of size k
    for i in range(len(nums) - k + 1):
        # Calculate the difference between the highest and lowest scores in the current window
        diff = nums[i + k - 1] - nums[i]
        
        # Update the minimum difference if the current difference is smaller
        min_diff = min(min_diff, diff)
    
    # Return the minimum difference
    return min_diff

# Example usage:
nums = [9, 4, 5, 7, 6, 8, 2, 1, 3]
k = 4
print(minimumDifference(nums, k))