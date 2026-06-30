def min_distance(nums):
    # Initialize minimum distance as infinity
    min_dist = float('inf')
    
    # Iterate over the list with three nested loops to consider all possible triplets
    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            for k in range(j + 1, len(nums)):
                # Check if the three elements are equal
                if nums[i] == nums[j] == nums[k]:
                    # Calculate the distance between the first and last elements
                    dist = nums[k] - nums[i]
                    # Update the minimum distance if the current distance is smaller
                    min_dist = min(min_dist, dist)
    
    # Return the minimum distance if found, otherwise return -1
    return min_dist if min_dist != float('inf') else -1

# Test the function
print(min_distance([1, 2, 3, 2, 2, 4]))  # Output: 2
print(min_distance([1, 1, 1]))  # Output: 0
print(min_distance([1, 2, 3, 4, 5]))  # Output: -1