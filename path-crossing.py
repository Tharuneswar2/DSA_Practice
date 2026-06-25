def isPathCrossing(path):
    # Initialize a set to store the visited points
    visited = set([(0, 0)])
    # Initialize the current position
    x, y = 0, 0
    
    # Iterate over the path
    for direction in path:
        # Move in the specified direction
        if direction == 'N':
            y += 1
        elif direction == 'S':
            y -= 1
        elif direction == 'E':
            x += 1
        elif direction == 'W':
            x -= 1
        
        # If the new position has been visited before, return True
        if (x, y) in visited:
            return True
        # Otherwise, add the new position to the visited set
        visited.add((x, y))
    
    # If the function hasn't returned True by now, the path doesn't cross itself
    return False