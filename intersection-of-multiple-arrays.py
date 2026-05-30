def intersection(nums):
    # Initialize the intersection set with the first array
    intersection_set = set(nums[0])
    
    # Iterate over the rest of the arrays
    for num in nums[1:]:
        # Update the intersection set to include only elements common to the current array and the intersection set
        intersection_set &= set(num)
    
    # Convert the intersection set back to a list and return it
    return list(intersection_set)

# Example usage:
nums = [[1, 2, 3], [2, 3, 4], [2, 4, 5]]
print(intersection(nums))  # Output: [2]