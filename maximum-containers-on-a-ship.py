# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def maxContainersOnShip(height, width, max_size, containers):
    # Sort the containers based on their heights in descending order
    containers.sort(key=lambda x: x[0], reverse=True)
    
    # Initialize the count of containers that can be placed on the ship
    count = 0
    
    # Initialize the current width of the ship
    curr_width = 0
    
    # Iterate over the sorted containers
    for h, w in containers:
        # If the current container can fit in the remaining width of the ship
        if curr_width + w <= width:
            # Add the container to the ship
            count += 1
            # Update the current width of the ship
            curr_width += w
        # If the current container cannot fit in the remaining width of the ship
        else:
            # If the current container can fit in the ship if placed at the start
            if w <= width:
                # Update the current width of the ship
                curr_width = w
                # Add the container to the ship
                count += 1
            # If the current container cannot fit in the ship at all
            else:
                # Break the loop as no more containers can be placed on the ship
                break
    
    # Return the maximum number of containers that can be placed on the ship
    return count