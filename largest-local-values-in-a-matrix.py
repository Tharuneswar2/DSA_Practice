def largestLocal(mat):
    n = len(mat)
    res = [[0] * (n - 2) for _ in range(n - 2)]

    # Iterate over each 3x3 submatrix
    for i in range(n - 2):
        for j in range(n - 2):
            # Initialize max_val to negative infinity
            max_val = float('-inf')
            
            # Check each cell in the 3x3 submatrix
            for x in range(3):
                for y in range(3):
                    # Update max_val if current cell is larger
                    max_val = max(max_val, mat[i + x][j + y])
            
            # Store the max_val in the result matrix
            res[i][j] = max_val

    return res