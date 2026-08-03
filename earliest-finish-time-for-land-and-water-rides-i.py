# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def earliestFinishTime(rides):
    # Sort the rides based on their finish times
    rides.sort(key=lambda x: x[1])  # x[1] represents the finish time of each ride
    
    # Initialize the earliest finish time and the number of rides taken
    earliest_finish_time = 0
    num_rides_taken = 0
    
    # Iterate over each ride
    for start, finish in rides:
        # If the current ride starts after the earliest finish time, update the earliest finish time
        if start >= earliest_finish_time:
            earliest_finish_time = finish  # Update the earliest finish time
            num_rides_taken += 1  # Increment the number of rides taken
    
    # Return the number of rides taken
    return num_rides_taken