# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def min_operations(nums, k):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # If the total sum is already divisible by k, no operations are needed
    if total_sum % k == 0:
        return 0
    
    # Calculate the remainder when the total sum is divided by k
    remainder = total_sum % k
    
    # The minimum number of operations is the minimum of the remainder and k - remainder
    # This is because we can either add the remainder to the total sum or subtract k - remainder from the total sum
    # to make the total sum divisible by k
    return min(remainder, k - remainder)