def ant_on_boundary(n, m, x, y, d):
    # Define the directions
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # right, down, left, up
    
    # Initialize the current direction
    current_direction = directions[d % 4]
    
    # Initialize the current position
    current_position = (x, y)
    
    # Simulate the ant's movement
    for _ in range(m):
        # Calculate the new position
        new_position = (current_position[0] + current_direction[0], current_position[1] + current_direction[1])
        
        # Check if the new position is within the grid
        if 0 <= new_position[0] < n and 0 <= new_position[1] < n:
            # Update the current position
            current_position = new_position
        else:
            # If the new position is not within the grid, change the direction
            current_direction_index = directions.index(current_direction)
            current_direction = directions[(current_direction_index + 1) % 4]
    
    # Return the final position
    return current_position

# Example usage
n = 5
m = 10
x = 0
y = 0
d = 0
print(ant_on_boundary(n, m, x, y, d))