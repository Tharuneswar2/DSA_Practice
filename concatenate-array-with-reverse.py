def getConcatenation(nums):
    # Create a copy of the input array
    reversed_nums = nums[:]
    
    # Reverse the copied array
    reversed_nums.reverse()
    
    # Concatenate the original array with the reversed array
    concatenated_nums = nums + reversed_nums
    
    # Return the concatenated array
    return concatenated_nums

# Alternatively, using list slicing
def getConcatenationAlternative(nums):
    # Concatenate the original array with the reversed array using list slicing
    return nums + nums[::-1]