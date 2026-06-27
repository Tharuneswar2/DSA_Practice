def buildArray(nums):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for i in range(len(nums)):
        # For each index, append the value at the index specified by the current element
        result.append(nums[nums[i]])
    
    # Return the resulting list
    return result

# Example usage:
print(buildArray([0,2,1,5,3,4]))  # Output: [0,1,2,4,5,3]