def min_bitwise_array(nums):
    # Initialize the result array with the first element of the input array
    res = [nums[0]]
    
    # Iterate over the input array starting from the second element
    for i in range(1, len(nums)):
        # Calculate the bitwise AND of the current element and the last element in the result array
        # This is because the bitwise AND operation has the property that a & (a & b) = a & b
        # So, we can keep track of the bitwise AND of all elements seen so far by maintaining the last element in the result array
        res.append(nums[i] & res[-1])
    
    return res

# Test the function
print(min_bitwise_array([1, 2, 3, 4, 5]))