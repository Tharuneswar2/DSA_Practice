# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def longestSubsequence(arr):
    # Initialize variables to store the length of the longest subsequence and the previous element in the subsequence
    n = len(arr)
    dp = [1] * n  # dp[i] stores the length of the longest subsequence ending at index i
    
    # Initialize the maximum length of the subsequence
    max_length = 1
    
    # Iterate over the array to fill the dp table
    for i in range(1, n):
        # For each element, compare it with all previous elements
        for j in range(i):
            # If the current element is not equal to the previous element, update the dp table
            if arr[i] != arr[j]:
                # Update the length of the subsequence ending at index i
                dp[i] = max(dp[i], dp[j] + 1)
        
        # Update the maximum length of the subsequence
        max_length = max(max_length, dp[i])
    
    # Return the maximum length of the subsequence
    return max_length