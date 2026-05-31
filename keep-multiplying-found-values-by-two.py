def keep_multiplying_found_values_by_two(nums):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over each number in the input list
    for num in nums:
        # If the number is even, multiply it by 2 and add it to the result list
        if num % 2 == 0:
            result.append(num * 2)
        # If the number is odd, just add it to the result list
        else:
            result.append(num)
    
    # Return the result list
    return result

# Test the function
print(keep_multiplying_found_values_by_two([1, 2, 3, 4, 5, 6]))