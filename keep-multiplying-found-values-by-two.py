# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def keep_multiplying_found_values_by_two(nums):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each number in the input list
    for num in nums:
        # If the number is already in the result list, multiply it by 2
        if num in result:
            # Find the index of the number in the result list
            index = result.index(num)
            # Multiply the number by 2
            result[index] *= 2
        else:
            # If the number is not in the result list, append it
            result.append(num)
    
    # Return the result list
    return result