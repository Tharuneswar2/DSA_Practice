# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def diagonalSum(mat):
    # Get the size of the matrix
    n = len(mat)
    
    # Initialize variables to store the sum of primary and secondary diagonals
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    # Iterate over the matrix
    for i in range(n):
        # For the primary diagonal, the row index is equal to the column index
        primary_diagonal_sum += mat[i][i]
        
        # For the secondary diagonal, the row index is equal to the difference between the size of the matrix and the column index minus one
        secondary_diagonal_sum += mat[i][n - i - 1]
    
    # If the size of the matrix is odd, the middle element is counted twice, so we subtract it once
    if n % 2 == 1:
        return primary_diagonal_sum + secondary_diagonal_sum - mat[n // 2][n // 2]
    else:
        return primary_diagonal_sum + secondary_diagonal_sum