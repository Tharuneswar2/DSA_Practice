def minCost(nums, k):
    n = len(nums)
    dp = [float('inf')] * (n + 1)
    dp[0] = 0

    for i in range(1, n + 1):
        # Initialize the frequency map
        freq_map = {}
        max_freq = 0
        # Initialize the cost
        cost = 0

        # Iterate backwards to find the optimal subarray
        for j in range(i, 0, -1):
            # Update the frequency map
            freq_map[nums[j - 1]] = freq_map.get(nums[j - 1], 0) + 1
            max_freq = max(max_freq, freq_map[nums[j - 1]])

            # Calculate the cost
            cost = max_freq * 2 + (i - j)

            # Update the dp array
            dp[i] = min(dp[i], dp[j - 1] + cost)

    return dp[n]