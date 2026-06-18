def minimumMountainRemovals(nums):
    n = len(nums)
    # Initialize arrays to store the length of the longest increasing subsequence ending at each position
    # and the length of the longest decreasing subsequence starting at each position
    inc, dec = [1] * n, [1] * n
    
    # Calculate the length of the longest increasing subsequence ending at each position
    for i in range(1, n):
        for j in range(i):
            if nums[i] > nums[j]:
                inc[i] = max(inc[i], inc[j] + 1)
    
    # Calculate the length of the longest decreasing subsequence starting at each position
    for i in range(n - 2, -1, -1):
        for j in range(n - 1, i, -1):
            if nums[i] > nums[j]:
                dec[i] = max(dec[i], dec[j] + 1)
    
    # Initialize the minimum sum of mountain triplets
    min_sum = float('inf')
    
    # Calculate the minimum sum of mountain triplets
    for i in range(1, n - 1):
        if inc[i] > 1 and dec[i] > 1:
            min_sum = min(min_sum, nums[i] + nums[i - inc[i] + 1] + nums[i + dec[i] - 1])
    
    return min_sum if min_sum != float('inf') else -1