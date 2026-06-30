def largestAltitude(gain):
    # Initialize the maximum altitude and the current altitude to 0
    max_altitude = 0
    current_altitude = 0
    
    # Iterate over each gain in the gain array
    for g in gain:
        # Update the current altitude by adding the gain
        current_altitude += g
        
        # Update the maximum altitude if the current altitude is greater
        max_altitude = max(max_altitude, current_altitude)
    
    # Return the maximum altitude
    return max_altitude