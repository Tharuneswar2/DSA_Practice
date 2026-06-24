def diagonalSum(mat):
    # Get the size of the matrix
    n = len(mat)
    
    # Initialize variables to store the sums of the diagonals
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    # Iterate over the matrix
    for i in range(n):
        # Add the current element to the primary diagonal sum
        primary_diagonal_sum += mat[i][i]
        
        # Add the current element to the secondary diagonal sum
        secondary_diagonal_sum += mat[i][n - i - 1]
    
    # If the matrix is a square matrix with an odd size, 
    # subtract the middle element because it's counted twice
    if n % 2 == 1:
        return primary_diagonal_sum + secondary_diagonal_sum - mat[n // 2][n // 2]
    else:
        return primary_diagonal_sum + secondary_diagonal_sum