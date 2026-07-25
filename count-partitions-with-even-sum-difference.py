# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def countPartitions(nums, k):
    # Calculate the total sum of the array
    total_sum = sum(nums)
    
    # If the total sum is odd or k is greater than the total sum, no partition is possible
    if total_sum % 2 != 0 or k > total_sum:
        return 0
    
    # Calculate the target sum for each partition
    target_sum = total_sum // 2
    
    # Initialize a 2D array to store the dynamic programming state
    dp = [[0] * (target_sum + 1) for _ in range(len(nums) + 1)]
    
    # Base case: one way to get a sum of 0 (by not taking any elements)
    for i in range(len(nums) + 1):
        dp[i][0] = 1
    
    # Fill up the dp array in a bottom-up manner
    for i in range(1, len(nums) + 1):
        for j in range(1, target_sum + 1):
            # If the current element is greater than the current sum, skip it
            if nums[i - 1] > j:
                dp[i][j] = dp[i - 1][j]
            else:
                # Two choices: include the current element or skip it
                dp[i][j] = dp[i - 1][j] + dp[i - 1][j - nums[i - 1]]
    
    # The answer is the number of ways to get a sum of target_sum
    return dp[-1][-1]