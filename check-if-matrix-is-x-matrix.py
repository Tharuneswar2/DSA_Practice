# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def checkXMatrix(grid):
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
    
    # Iterate over each row in the grid
    for i in range(rows):
        # Iterate over each column in the grid
        for j in range(cols):
            # If the current element is on the main diagonal or the anti-diagonal
            if i == j or i + j == rows - 1:
                # If the current element is 0, return False
                if grid[i][j] == 0:
                    return False
            # If the current element is not on the main diagonal or the anti-diagonal
            else:
                # If the current element is not 0, return False
                if grid[i][j] != 0:
                    return False
    # If we have checked all elements and haven't returned False, return True
    return True