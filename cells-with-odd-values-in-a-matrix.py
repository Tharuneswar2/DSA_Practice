def oddCells(n, m, indices):
    # Initialize a matrix with all zeros
    matrix = [[0]*m for _ in range(n)]
    
    # Iterate over each operation in indices
    for i, j in indices:
        # For each operation, increment the corresponding row and column in the matrix
        for k in range(m):
            matrix[i][k] += 1
        for k in range(n):
            matrix[k][j] += 1
    
    # Count the number of cells with odd values
    count = sum(val % 2 for row in matrix for val in row)
    
    return count