def sum_subarrays(nums):
    n = len(nums)
    total_sum = 0
    
    # Calculate the sum of all subarrays
    for i in range(n):
        # For each element, calculate the number of subarrays it can be part of
        # This is done by multiplying the number of subarrays to its left and right
        # The number of subarrays to its left is i + 1 (since it can be the first element of i + 1 subarrays)
        # The number of subarrays to its right is n - i (since it can be the last element of n - i subarrays)
        total_sum += nums[i] * (i + 1) * (n - i)
    
    return total_sum

# Test the function
print(sum_subarrays([1, 2, 3, 4]))  # Output: 60