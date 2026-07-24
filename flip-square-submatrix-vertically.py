# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def flip_square_submatrix_vertically(matrix, submatrix_size):
    # Check if the submatrix size is valid
    if submatrix_size <= 0 or submatrix_size > len(matrix):
        return matrix
    
    # Iterate over each row in the matrix
    for i in range(len(matrix)):
        # Iterate over each column in the matrix
        for j in range(len(matrix[0])):
            # Check if the current position can form a submatrix of the given size
            if i + submatrix_size <= len(matrix) and j + submatrix_size <= len(matrix[0]):
                # Flip the submatrix vertically
                for k in range(submatrix_size):
                    # Swap the top and bottom elements of the submatrix
                    matrix[i + k][j], matrix[i + submatrix_size - k - 1][j] = matrix[i + submatrix_size - k - 1][j], matrix[i + k][j]
    
    # Return the modified matrix
    return matrix