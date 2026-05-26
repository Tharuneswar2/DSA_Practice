def findExtra(nums1, nums2):
    # Calculate the sum of the first array
    sum1 = sum(nums1)
    
    # Calculate the sum of the second array
    sum2 = sum(nums2)
    
    # The extra integer is the difference between the two sums
    # Since the second array has one extra integer, we subtract the sum of the first array from the sum of the second array
    extra = sum2 - sum1
    
    # Return the extra integer
    return extra

# Alternatively, we can use XOR operation to find the extra integer
def findExtraXOR(nums1, nums2):
    # Initialize the result as 0
    result = 0
    
    # Iterate over the first array
    for num in nums1:
        # XOR the result with the current number
        result ^= num
    
    # Iterate over the second array
    for num in nums2:
        # XOR the result with the current number
        result ^= num
    
    # The result will be the extra integer
    return result