def snake_in_matrix(matrix):
    # Get the number of rows and columns in the matrix
    rows, cols = len(matrix), len(matrix[0])
    
    # Initialize the result list
    result = []
    
    # Initialize the row and column indices
    row, col = 0, 0
    
    # Initialize the direction (0: right, 1: down, 2: left, 3: up)
    direction = 0
    
    # Initialize the number of visited cells
    visited = 0
    
    # Continue until all cells are visited
    while visited < rows * cols:
        # Append the current cell to the result list
        result.append(matrix[row][col])
        
        # Mark the current cell as visited
        matrix[row][col] = None
        
        # Increment the number of visited cells
        visited += 1
        
        # Determine the next cell based on the current direction
        if direction == 0:  # right
            if col + 1 < cols and matrix[row][col + 1] is not None:
                col += 1
            else:
                direction = 1
                row += 1
        elif direction == 1:  # down
            if row + 1 < rows and matrix[row + 1][col] is not None:
                row += 1
            else:
                direction = 2
                col -= 1
        elif direction == 2:  # left
            if col - 1 >= 0 and matrix[row][col - 1] is not None:
                col -= 1
            else:
                direction = 3
                row -= 1
        elif direction == 3:  # up
            if row - 1 >= 0 and matrix[row - 1][col] is not None:
                row -= 1
            else:
                direction = 0
                col += 1
    
    return result

# Example usage:
matrix = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
print(snake_in_matrix(matrix))  # Output: [1, 2, 3, 6, 9, 8, 7, 4, 5]