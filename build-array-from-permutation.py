# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def buildArray(nums):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for i in range(len(nums)):
        # For each index, append the value at the index specified by the current element
        # This is because the problem states that the value at index i in the result is the value at index nums[i] in the input list
        result.append(nums[nums[i]])
    
    # Return the resulting list
    return result