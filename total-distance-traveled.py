# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def total_distance_traveled(speeds, hours):
    # Initialize total distance to 0
    total_distance = 0
    
    # Iterate over each speed and corresponding hour
    for speed, hour in zip(speeds, hours):
        # Calculate the distance traveled in the current hour
        distance = speed * hour
        
        # Add the distance to the total distance
        total_distance += distance
    
    # Return the total distance traveled
    return total_distance