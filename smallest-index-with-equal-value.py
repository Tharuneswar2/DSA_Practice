def smallestEqual(nums):
    # Iterate over the list with enumerate to get both index and value
    for i, num in enumerate(nums):
        # Check if the index is equal to the value
        if i == num:
            # If it is, return the index
            return i
    # If no such index is found, return -1
    return -1

# Test the function
print(smallestEqual([0,1,2]))  # Output: 0
print(smallestEqual([4,3,2]))  # Output: -1
print(smallestEqual([1,2,3,4,5,6]))  # Output: -1