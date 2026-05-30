def transformed_array(nums, left, right):
    # Create a copy of the input array to avoid modifying the original array
    transformed = nums[:]
    
    # Iterate over the range of indices from left to right (inclusive)
    for i in range(left, right + 1):
        # If the current element is even, divide it by 2
        if transformed[i] % 2 == 0:
            transformed[i] //= 2
        # If the current element is odd, multiply it by 2 and add 1
        else:
            transformed[i] = transformed[i] * 2 + 1
    
    # Return the transformed array
    return transformed

# Example usage:
nums = [1, 2, 3, 4, 5]
left = 1
right = 3
print(transformed_array(nums, left, right))