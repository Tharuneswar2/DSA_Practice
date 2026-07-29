# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def ant_on_boundary(n, m, x, y):
    # Initialize the directions in which the ant can move (up, down, left, right)
    directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
    
    # Initialize the current position of the ant
    current_position = (x, y)
    
    # Initialize the number of steps the ant has taken
    steps = 0
    
    # Continue moving the ant until it reaches the boundary
    while 0 < current_position[0] < n and 0 < current_position[1] < m:
        # For each possible direction
        for direction in directions:
            # Calculate the new position of the ant
            new_position = (current_position[0] + direction[0], current_position[1] + direction[1])
            
            # If the new position is within the grid and is closer to the boundary than the current position
            if (0 < new_position[0] < n and 0 < new_position[1] < m) and (min(new_position[0], n - new_position[0], new_position[1], m - new_position[1]) < min(current_position[0], n - current_position[0], current_position[1], m - current_position[1])):
                # Update the current position of the ant
                current_position = new_position
                
                # Increment the number of steps the ant has taken
                steps += 1
                
                # Break out of the loop as we have found a better direction
                break
    
    # Return the number of steps the ant took to reach the boundary
    return steps