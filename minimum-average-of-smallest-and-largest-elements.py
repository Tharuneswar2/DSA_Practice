def minAverage(nums):
    # Sort the list in ascending order
    nums.sort()
    
    # Initialize minimum average difference
    min_diff = float('inf')
    
    # Iterate over the list to find the minimum average difference
    for i in range(len(nums) - 1):
        # Calculate the average of the smallest and largest elements
        avg = (nums[i] + nums[-(i+1)]) / 2
        
        # Update the minimum average difference
        min_diff = min(min_diff, avg)
    
    # Return the minimum average difference
    return min_diff

# Test the function
print(minAverage([3, 1, 5, 2, 4]))