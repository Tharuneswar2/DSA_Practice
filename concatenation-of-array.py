def getConcatenation(nums):
    # Create a new list that is a copy of the input list
    concatenated_list = nums[:]
    
    # Extend the new list with the input list to concatenate it
    concatenated_list.extend(nums)
    
    # Return the concatenated list
    return concatenated_list

# Alternatively, you can use list slicing to achieve the same result
def getConcatenationAlternative(nums):
    # Return a new list that is the concatenation of the input list with itself
    return nums + nums

# Alternatively, you can use the * operator to repeat the list
def getConcatenationAlternative2(nums):
    # Return a new list that is the concatenation of the input list with itself
    return [num for num in nums * 2]