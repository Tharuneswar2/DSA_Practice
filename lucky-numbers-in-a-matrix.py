def luckyNumbers(matrix):
    # Get the number of rows and columns in the matrix
    rows, cols = len(matrix), len(matrix[0])
    
    # Initialize two sets to store the minimum values in each row and the maximum values in each column
    row_mins = set(min(row) for row in matrix)
    col_maxs = set(max(col) for col in zip(*matrix))
    
    # Find the intersection of the two sets, which are the lucky numbers
    lucky_nums = row_mins & col_maxs
    
    # Return the lucky numbers as a list
    return list(lucky_nums)