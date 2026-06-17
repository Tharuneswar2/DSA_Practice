def getMinDistance(nums, target, start):
    # Initialize minimum distance to infinity
    min_distance = float('inf')
    
    # Iterate through the list of numbers
    for i in range(len(nums)):
        # Check if the current number is the target
        if nums[i] == target:
            # Calculate the absolute difference between the current index and the start index
            distance = abs(i - start)
            # Update the minimum distance if the current distance is smaller
            min_distance = min(min_distance, distance)
    
    # Return the minimum distance
    return min_distance

# Test the function
nums = [1, 2, 3, 4, 5]
target = 5
start = 0
print(getMinDistance(nums, target, start))  # Output: 4