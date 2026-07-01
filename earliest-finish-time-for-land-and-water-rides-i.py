def earliestFinishTime(rides):
    # Sort the rides based on their finish times
    rides.sort(key=lambda x: x[1])

    # Initialize the earliest finish time and the current time
    earliest_finish_time = 0
    current_time = 0

    # Iterate over the sorted rides
    for start, finish in rides:
        # If the current time is less than the start time of the ride, update the current time
        if current_time < start:
            current_time = start
        # Update the earliest finish time
        earliest_finish_time = max(earliest_finish_time, current_time + finish - start)
        # Update the current time
        current_time += finish - start

    return earliest_finish_time

# Example usage:
rides = [[1, 3], [2, 4], [3, 5]]
print(earliestFinishTime(rides))