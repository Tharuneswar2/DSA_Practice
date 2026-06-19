def minCostToReachEveryPosition(grid):
    rows, cols = len(grid), len(grid[0])
    dp = [[float('inf')] * cols for _ in range(rows)]
    dp[0][0] = grid[0][0]

    # Initialize the first row
    for col in range(1, cols):
        dp[0][col] = dp[0][col-1] + grid[0][col]

    # Initialize the first column
    for row in range(1, rows):
        dp[row][0] = dp[row-1][0] + grid[row][0]

    # Fill up the dp table
    for row in range(1, rows):
        for col in range(1, cols):
            # For each cell, the minimum cost to reach it is the minimum cost to reach the cell above it or to its left, plus the cost of the current cell
            dp[row][col] = grid[row][col] + min(dp[row-1][col], dp[row][col-1])

    # The minimum cost to reach every position is the minimum cost to reach the bottom right cell
    return dp[-1][-1]

# Example usage:
grid = [[1, 3, 1], [1, 5, 1], [4, 2, 1]]
print(minCostToReachEveryPosition(grid))