# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def largestLocal(self, grid):
    # Get the size of the grid
    n = len(grid)
    
    # Initialize an empty result matrix with the same size as the grid
    res = [[0]* (n - 2) for _ in range(n - 2)]
    
    # Iterate over each cell in the grid, excluding the last two rows and columns
    for i in range(n - 2):
        for j in range(n - 2):
            # Initialize the maximum value to negative infinity
            max_val = float('-inf')
            
            # Check all 3x3 sub-matrices centered at the current cell
            for x in range(i, i + 3):
                for y in range(j, j + 3):
                    # Update the maximum value if the current cell has a larger value
                    max_val = max(max_val, grid[x][y])
            
            # Store the maximum value in the result matrix
            res[i][j] = max_val
    
    # Return the result matrix
    return res