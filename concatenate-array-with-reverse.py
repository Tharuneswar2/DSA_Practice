# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def getConcatenation(nums):
    # Create a copy of the input list to avoid modifying the original list
    result = nums.copy()
    
    # Use list slicing to get the reversed list
    reversed_nums = nums[::-1]
    
    # Extend the result list with the reversed list
    result.extend(reversed_nums)
    
    # Return the concatenated list
    return result