# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minimumMountainRemovals(nums):
    # Initialize variables to store the length of the longest increasing subsequence (LIS) and the longest decreasing subsequence (LDS)
    n = len(nums)
    lis = [1] * n
    lds = [1] * n
    
    # Compute the LIS for each element in the array
    for i in range(1, n):
        for j in range(i):
            # If the current element is greater than the previous element, update the LIS
            if nums[i] > nums[j]:
                lis[i] = max(lis[i], lis[j] + 1)
    
    # Compute the LDS for each element in the array
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            # If the current element is greater than the next element, update the LDS
            if nums[i] > nums[j]:
                lds[i] = max(lds[i], lds[j] + 1)
    
    # Initialize a variable to store the maximum length of the mountain subsequence
    max_len = 0
    
    # Compute the maximum length of the mountain subsequence
    for i in range(n):
        # The mountain subsequence must have at least 3 elements
        if lis[i] > 1 and lds[i] > 1:
            # Update the maximum length
            max_len = max(max_len, lis[i] + lds[i] - 1)
    
    # Return the minimum number of elements to remove to make the array a mountain subsequence
    return n - max_len