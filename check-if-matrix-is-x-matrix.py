def checkXMatrix(grid):
    n = len(grid)
    
    # Check the main diagonal
    for i in range(n):
        if grid[i][i] == 0:
            return False
    
    # Check the anti-diagonal
    for i in range(n):
        if grid[i][n - i - 1] == 0:
            return False
    
    # Check the rest of the matrix
    for i in range(n):
        for j in range(n):
            if i != j and i + j != n - 1 and grid[i][j] != 0:
                return False
    
    return True