def findColumnWidths(grid):
    # Get the number of columns in the grid
    num_cols = len(grid[0])
    
    # Initialize a list to store the maximum width of each column
    col_widths = [0] * num_cols
    
    # Iterate over each row in the grid
    for row in grid:
        # Iterate over each element in the row
        for i, elem in enumerate(row):
            # Update the maximum width of the current column if necessary
            col_widths[i] = max(col_widths[i], len(str(elem)))
    
    # Return the list of column widths
    return col_widths