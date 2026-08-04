# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sum_of_indices_with_k_set_bits(nums, k):
    # Initialize the sum of values at indices with k set bits to 0
    total_sum = 0
    
    # Iterate over the list of numbers with their indices
    for i, num in enumerate(nums):
        # Convert the number to binary and count the number of set bits
        set_bits = bin(num).count('1')
        
        # Check if the number of set bits is equal to k
        if set_bits == k:
            # If true, add the value at the current index to the total sum
            total_sum += num
    
    # Return the total sum of values at indices with k set bits
    return total_sum