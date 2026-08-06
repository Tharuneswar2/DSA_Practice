# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def subsetXORSum(nums):
    # Initialize the result variable to store the sum of all subset XOR totals
    result = 0
    
    # Calculate the total number of subsets (2^n, where n is the number of elements in the array)
    n = len(nums)
    total_subsets = 1 << n  # Using bitwise left shift to calculate 2^n
    
    # Iterate over all subsets
    for subset_mask in range(total_subsets):
        # Initialize the XOR total for the current subset
        xor_total = 0
        
        # Iterate over each element in the array
        for i in range(n):
            # Check if the current element is included in the subset (using bitwise AND operation)
            if (subset_mask & (1 << i)):  # If the ith bit is set in the subset mask
                # XOR the current element with the XOR total
                xor_total ^= nums[i]
        
        # Add the XOR total of the current subset to the result
        result += xor_total
    
    # Return the sum of all subset XOR totals
    return result