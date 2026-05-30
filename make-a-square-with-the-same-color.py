def make_square_same_color(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Iterate over each cell in the matrix
    for i in range(rows - 1):
        for j in range(cols - 1):
            # Check if the current cell and the cell to its right and below have the same color
            if matrix[i][j] == matrix[i][j + 1] == matrix[i + 1][j] == matrix[i + 1][j + 1]:
                # If they do, return True
                return True

    # If no 2x2 square with the same color is found, return False
    return False


def make_square_same_color_optimized(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Iterate over each cell in the matrix
    for i in range(rows - 1):
        for j in range(cols - 1):
            # Check if the current cell and the cell to its right have the same color
            if matrix[i][j] == matrix[i][j + 1]:
                # Check if the current cell and the cell below have the same color
                if matrix[i][j] == matrix[i + 1][j]:
                    # Check if the cell to the right and below has the same color
                    if matrix[i][j] == matrix[i + 1][j + 1]:
                        # If they do, return True
                        return True

    # If no 2x2 square with the same color is found, return False
    return False