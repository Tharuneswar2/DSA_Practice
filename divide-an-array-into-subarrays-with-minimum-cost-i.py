# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minCost(nums, k):
    n = len(nums)
    # Initialize a list to store the prefix sum of the array
    prefix_sum = [0] * (n + 1)
    for i in range(n):
        # Calculate the prefix sum
        prefix_sum[i + 1] = prefix_sum[i] + nums[i]
    
    # Initialize a list to store the minimum cost for each subarray
    dp = [float('inf')] * (n + 1)
    dp[0] = 0
    
    # Iterate over the array
    for i in range(1, n + 1):
        # For each subarray ending at index i
        for j in range(i):
            # Calculate the cost of the subarray
            cost = prefix_sum[i] - prefix_sum[j] + k
            # Update the minimum cost
            dp[i] = min(dp[i], dp[j] + cost)
    
    # Return the minimum cost for the entire array
    return dp[n]