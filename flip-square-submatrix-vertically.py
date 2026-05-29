def flip_square_submatrix_vertically(matrix, row, col, size):
    # Check if the submatrix is within the bounds of the matrix
    if row < 0 or col < 0 or row + size > len(matrix) or col + size > len(matrix[0]):
        return matrix
    
    # Flip the submatrix vertically
    for i in range(row, row + size):
        # Calculate the middle index
        mid = (col + col + size - 1) // 2
        
        # Swap elements from the top and bottom of the submatrix
        for j in range(col, mid + 1):
            # Calculate the corresponding index from the bottom
            bottom_idx = col + size - 1 - (j - col)
            
            # Swap the elements
            matrix[i][j], matrix[i][bottom_idx] = matrix[i][bottom_idx], matrix[i][j]
    
    return matrix

# Example usage:
matrix = [
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9, 10, 11, 12],
    [13, 14, 15, 16]
]

print("Original Matrix:")
for row in matrix:
    print(row)

flipped_matrix = flip_square_submatrix_vertically(matrix, 1, 1, 2)

print("\nFlipped Matrix:")
for row in flipped_matrix:
    print(row)