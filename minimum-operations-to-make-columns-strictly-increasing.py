def minOperations(grid):
    # Get the number of rows and columns in the grid
    rows, cols = len(grid), len(grid[0])
    
    # Initialize the minimum operations count
    min_ops = float('inf')
    
    # Iterate over each column in the grid
    for col in range(cols):
        # Initialize the previous element and operations count for the current column
        prev, ops = grid[0][col], 0
        
        # Iterate over each row in the current column
        for row in range(1, rows):
            # If the current element is not greater than the previous element, increment the operations count
            if grid[row][col] <= prev:
                ops += prev - grid[row][col] + 1
            # Update the previous element
            prev = grid[row][col]
        
        # Update the minimum operations count
        min_ops = min(min_ops, ops)
    
    # Return the minimum operations count
    return min_ops