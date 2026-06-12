def slowestKey(releaseTimes, keysPressed):
    # Initialize variables to store the slowest key and its duration
    slowest_key = keysPressed[0]
    max_duration = releaseTimes[0]

    # Iterate over the release times and keys pressed
    for i in range(1, len(releaseTimes)):
        # Calculate the duration of the current key press
        duration = releaseTimes[i] - releaseTimes[i - 1]
        
        # If the current key press duration is greater than the max duration, update the slowest key and max duration
        if duration > max_duration or (duration == max_duration and keysPressed[i] > slowest_key):
            slowest_key = keysPressed[i]
            max_duration = duration

    # Return the slowest key
    return slowest_key