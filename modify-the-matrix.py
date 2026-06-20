def modify_matrix(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create a copy of the matrix to store the modified values
    modified_matrix = [[0 for _ in range(cols)] for _ in range(rows)]

    # Iterate over each element in the matrix
    for i in range(rows):
        for j in range(cols):
            # If the current element is 0, set all elements in the same row and column to 0
            if matrix[i][j] == 0:
                # Set all elements in the same row to 0
                for k in range(cols):
                    modified_matrix[i][k] = 0
                # Set all elements in the same column to 0
                for k in range(rows):
                    modified_matrix[k][j] = 0

    # Iterate over each element in the matrix again
    for i in range(rows):
        for j in range(cols):
            # If the current element is not 0, set the corresponding element in the modified matrix to the original value
            if matrix[i][j] != 0:
                modified_matrix[i][j] = matrix[i][j]

    return modified_matrix

def modify_matrix_efficient(matrix):
    # Get the number of rows and columns in the matrix
    rows = len(matrix)
    cols = len(matrix[0])

    # Create two lists to store the rows and columns that need to be set to 0
    rows_to_zero = set()
    cols_to_zero = set()

    # Iterate over each element in the matrix
    for i in range(rows):
        for j in range(cols):
            # If the current element is 0, add the row and column to the sets
            if matrix[i][j] == 0:
                rows_to_zero.add(i)
                cols_to_zero.add(j)

    # Iterate over each element in the matrix again
    for i in range(rows):
        for j in range(cols):
            # If the current row or column is in the sets, set the corresponding element to 0
            if i in rows_to_zero or j in cols_to_zero:
                matrix[i][j] = 0

    return matrix