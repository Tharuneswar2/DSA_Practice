# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minOperations(grid):
    # Get the number of rows and columns in the grid
    m, n = len(grid), len(grid[0])
    
    # Initialize the minimum operations count
    min_ops = 0
    
    # Iterate over each column in the grid
    for col in range(n):
        # Initialize the previous element in the column
        prev = grid[0][col]
        
        # Initialize the increment for the current column
        inc = 0
        
        # Iterate over each row in the column (starting from the second row)
        for row in range(1, m):
            # If the current element is not greater than the previous element plus the increment
            if grid[row][col] <= prev + inc:
                # Update the increment to make the current element greater than the previous element
                inc += prev + inc - grid[row][col] + 1
                # Update the minimum operations count
                min_ops += prev + inc - grid[row][col]
            # Update the previous element
            prev = grid[row][col]
    
    # Return the minimum operations count
    return min_ops