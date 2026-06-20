def total_distance_traveled(speeds, hours):
    # Initialize total distance to 0
    total_distance = 0
    
    # Iterate over the speeds and hours
    for speed, hour in zip(speeds, hours):
        # Calculate the distance traveled in the current hour
        distance = speed * hour
        
        # Add the distance to the total distance
        total_distance += distance
    
    # Return the total distance
    return total_distance

# Example usage:
speeds = [60, 70, 80]
hours = [1, 2, 3]
print(total_distance_traveled(speeds, hours))