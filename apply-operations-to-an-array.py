def apply_operations(nums):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for i in range(len(nums) - 1):
        # If the current element is equal to the next element, 
        # append the current element to the result list
        if nums[i] == nums[i + 1]:
            result.append(nums[i])
        # If the current element is not equal to the next element, 
        # append the current element to the result list
        else:
            result.append(nums[i])
    
    # Append the last element of the input list to the result list
    result.append(nums[-1])
    
    return result

def apply_operations_optimized(nums):
    # Initialize an empty list to store the result
    result = []
    
    # Iterate over the input list
    for num in nums:
        # If the result list is empty or the current number is not equal to the last number in the result list, 
        # append the current number to the result list
        if not result or num != result[-1]:
            result.append(num)
    
    return result