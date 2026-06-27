def check_grid(grid):
    rows, cols = len(grid), len(grid[0])
    
    # Check each cell in the grid
    for i in range(rows):
        for j in range(cols):
            # If the cell is 1, check its neighbors
            if grid[i][j] == 1:
                # Check top neighbor
                if i > 0 and grid[i-1][j] == 1:
                    return False
                # Check bottom neighbor
                if i < rows - 1 and grid[i+1][j] == 1:
                    return False
                # Check left neighbor
                if j > 0 and grid[i][j-1] == 1:
                    return False
                # Check right neighbor
                if j < cols - 1 and grid[i][j+1] == 1:
                    return False
                
    # If no adjacent 1s are found, return True
    return True

# Test the function
grid = [
    [0, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
print(check_grid(grid))  # Output: True

grid = [
    [1, 1, 0, 0],
    [0, 0, 1, 0],
    [0, 0, 0, 1],
    [1, 0, 0, 0]
]
print(check_grid(grid))  # Output: False