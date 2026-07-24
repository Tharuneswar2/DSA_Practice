# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def oddCells(n, m, indices):
    # Initialize a matrix with all zeros, representing the initial state of the matrix
    matrix = [[0]*m for _ in range(n)]
    
    # Iterate over each operation in the indices list
    for row, col in indices:
        # For each operation, increment the corresponding row in the matrix
        for j in range(m):
            matrix[row][j] += 1
        # For each operation, increment the corresponding column in the matrix
        for i in range(n):
            matrix[i][col] += 1
    
    # Initialize a counter to store the number of cells with odd values
    odd_count = 0
    
    # Iterate over each cell in the matrix
    for row in matrix:
        # For each cell, check if the value is odd
        for val in row:
            # If the value is odd, increment the counter
            if val % 2 != 0:
                odd_count += 1
    
    # Return the total count of cells with odd values
    return odd_count