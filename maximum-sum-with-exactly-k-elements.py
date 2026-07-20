# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxSumWithKElements(arr, n, k):
    # Initialize a table to store the maximum sum with i elements
    dp = [[0 for _ in range(k + 1)] for _ in range(n + 1)]

    # Fill the table in a bottom-up manner
    for i in range(1, n + 1):
        for j in range(1, min(i, k) + 1):
            # For each element, consider two possibilities: include the current element or not
            # If the current element is included, add its value to the maximum sum with j - 1 elements
            # If the current element is not included, the maximum sum remains the same as the previous row
            dp[i][j] = max(dp[i - 1][j], dp[i - 1][j - 1] + arr[i - 1])

    # The maximum sum with exactly k elements is stored in the last cell of the table
    return dp[n][k]

# Test the function
arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 3
print(maxSumWithKElements(arr, n, k))