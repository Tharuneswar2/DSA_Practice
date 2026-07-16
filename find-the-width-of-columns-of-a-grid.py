# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def findColumnWidths(grid):
    # Initialize an empty list to store the maximum width of each column
    col_widths = []
    
    # Iterate over each column index
    for col in range(len(grid[0])):
        # Initialize the maximum width of the current column to 0
        max_width = 0
        
        # Iterate over each row in the grid
        for row in grid:
            # Convert the current cell to a string and find its length
            cell_len = len(str(row[col]))
            
            # Update the maximum width of the current column if the length of the current cell is greater
            max_width = max(max_width, cell_len)
        
        # Append the maximum width of the current column to the list
        col_widths.append(max_width)
    
    # Return the list of maximum widths of all columns
    return col_widths