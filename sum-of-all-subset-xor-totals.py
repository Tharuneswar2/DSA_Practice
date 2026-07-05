def subsetXORSum(nums):
    # Initialize result variable to store the sum of all subset XOR totals
    result = 0
    
    # Calculate the total number of subsets (2^n, where n is the number of elements)
    total_subsets = 1 << len(nums)
    
    # Iterate over all possible subsets
    for i in range(total_subsets):
        # Initialize XOR total for the current subset
        xor_total = 0
        
        # Iterate over the elements in the current subset
        for j in range(len(nums)):
            # Check if the jth bit is set in the binary representation of i
            if (i & (1 << j)):
                # If the bit is set, include the jth element in the XOR total
                xor_total ^= nums[j]
        
        # Add the XOR total of the current subset to the result
        result += xor_total
    
    # Return the sum of all subset XOR totals
    return result