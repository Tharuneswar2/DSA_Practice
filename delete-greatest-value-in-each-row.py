def deleteGreatestValue(grid):
    # Transpose the grid to easily access columns
    transposed_grid = list(map(list, zip(*grid)))
    
    # Sort each column in descending order
    for col in transposed_grid:
        col.sort(reverse=True)
    
    # Initialize result variable to store the sum of the greatest values
    result = 0
    
    # Iterate over each row in the transposed grid
    for col in transposed_grid:
        # Add the first element (greatest value) of each column to the result
        result += col[0]
    
    return result