def maxSumWithKElements(arr, n, k):
    # Initialize a 2D array to store the maximum sum for each subproblem
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Fill the dp array in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            # For each element, consider two options: include the current element or not
            # If we include the current element, add its value to the maximum sum of the previous subproblem
            # If we don't include the current element, the maximum sum remains the same as the previous subproblem
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + arr[i - 1])

    # The maximum sum with exactly k elements is stored in the last cell of the dp array
    return dp[n][k]

# Example usage:
arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 3
print(maxSumWithKElements(arr, n, k))  # Output: 12