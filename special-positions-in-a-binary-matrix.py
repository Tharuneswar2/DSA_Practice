def numSpecial(mat):
    # Get the number of rows and columns in the matrix
    rows, cols = len(mat), len(mat[0])
    
    # Initialize arrays to store the count of 1s in each row and column
    row_counts = [0] * rows
    col_counts = [0] * cols
    
    # Count the number of 1s in each row and column
    for i in range(rows):
        for j in range(cols):
            if mat[i][j] == 1:
                row_counts[i] += 1
                col_counts[j] += 1
    
    # Initialize the count of special positions
    special_positions = 0
    
    # Iterate over the matrix to find special positions
    for i in range(rows):
        for j in range(cols):
            # A position is special if it has a 1 and the row and column counts are both 1
            if mat[i][j] == 1 and row_counts[i] == 1 and col_counts[j] == 1:
                special_positions += 1
    
    return special_positions