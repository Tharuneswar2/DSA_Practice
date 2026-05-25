def countPartitions(n, nums, difference):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # If the difference is greater than the total sum, no partition is possible
    if difference > total_sum:
        return 0
    
    # If the total sum minus the difference is odd, no partition is possible
    if (total_sum - difference) % 2 != 0:
        return 0
    
    # Calculate the target sum for the subset
    target_sum = (total_sum - difference) // 2
    
    # Initialize a 2D array to store the dynamic programming state
    dp = [[0] * (target_sum + 1) for _ in range(n + 1)]
    
    # Base case: one way to get a sum of 0 (by not choosing any elements)
    for i in range(n + 1):
        dp[i][0] = 1
    
    # Fill up the dynamic programming table
    for i in range(1, n + 1):
        for j in range(1, target_sum + 1):
            # If the current element is greater than the target sum, skip it
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Choose the current element or skip it
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
    
    # The answer is the number of ways to get the target sum
    return dp[n][target_sum]

# Test the function
n = 4
nums = [5, 2, 6, 3]
difference = 3
print(countPartitions(n, nums, difference))