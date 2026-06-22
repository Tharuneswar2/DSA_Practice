def smallestNumber(nums1, nums2):
    # Combine the two lists into one
    combined = nums1 + nums2
    
    # Sort the combined list in ascending order
    combined.sort()
    
    # Initialize an empty string to store the result
    result = ''
    
    # Iterate over the sorted list
    for num in combined:
        # Convert the number to a string and add it to the result
        result += str(num)
    
    # Return the smallest possible number as an integer
    return int(result)

# Test the function
print(smallestNumber([3, 5], [1, 2]))  # Output: 11235