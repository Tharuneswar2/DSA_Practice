def shiftGrid(grid, k):
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
    
    # Calculate the total number of elements in the grid
    total_elements = rows * cols
    
    # Calculate the actual number of shifts required
    # This is done by taking the modulus of k with the total number of elements
    # This is because after total_elements shifts, the grid will be the same as the original grid
    k = k % total_elements
    
    # Initialize an empty list to store the result
    result = [[0] * cols for _ in range(rows)]
    
    # Iterate over each element in the grid
    for i in range(total_elements):
        # Calculate the new position of the element after shifting
        new_position = (i + k) % total_elements
        
        # Calculate the row and column of the new position
        new_row, new_col = divmod(new_position, cols)
        
        # Calculate the row and column of the current position
        row, col = divmod(i, cols)
        
        # Assign the value of the current position to the new position in the result grid
        result[new_row][new_col] = grid[row][col]
    
    # Return the result grid
    return result