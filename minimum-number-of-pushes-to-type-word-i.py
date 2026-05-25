def minPushes(word1, word2):
    # Initialize a 2D array to store the minimum number of pushes
    dp = [[0] * (len(word2) + 1) for _ in range(len(word1) + 1)]

    # Fill the first row and column with the index value
    for i in range(len(word1) + 1):
        dp[i][0] = i
    for j in range(len(word2) + 1):
        dp[0][j] = j

    # Fill the rest of the 2D array
    for i in range(1, len(word1) + 1):
        for j in range(1, len(word2) + 1):
            # If the current characters match, no push is needed
            if word1[i - 1] == word2[j - 1]:
                dp[i][j] = dp[i - 1][j - 1]
            # If the current characters do not match, consider all possibilities
            else:
                # Push the current character in word1
                push_word1 = dp[i - 1][j] + 1
                # Push the current character in word2
                push_word2 = dp[i][j - 1] + 1
                # Do not push any character
                no_push = dp[i - 1][j - 1] + 1
                # Choose the minimum number of pushes
                dp[i][j] = min(push_word1, push_word2, no_push)

    # The minimum number of pushes is stored in the last cell of the 2D array
    return dp[-1][-1]