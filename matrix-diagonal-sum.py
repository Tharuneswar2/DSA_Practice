# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def diagonalSum(mat):
    # Get the size of the matrix (assuming it's a square matrix)
    n = len(mat)
    
    # Initialize variables to store the sums of the diagonals
    primary_diagonal_sum = 0
    secondary_diagonal_sum = 0
    
    # Iterate over the matrix
    for i in range(n):
        # For each row, add the element at the current row and column to the primary diagonal sum
        primary_diagonal_sum += mat[i][i]
        
        # For each row, add the element at the current row and the column mirrored across the center to the secondary diagonal sum
        secondary_diagonal_sum += mat[i][n - i - 1]
    
    # If the matrix has an odd size, the middle element is counted twice, so subtract it once
    if n % 2 == 1:
        middle_element = mat[n // 2][n // 2]
        return primary_diagonal_sum + secondary_diagonal_sum - middle_element
    else:
        # If the matrix has an even size, return the sum of the diagonals
        return primary_diagonal_sum + secondary_diagonal_sum