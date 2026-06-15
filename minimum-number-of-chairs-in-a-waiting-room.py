def min_chairs(arrivals, departures):
    # Combine arrivals and departures into a single list of events
    events = [(time, 1) for time in arrivals] + [(time, -1) for time in departures]
    
    # Sort the events by time
    events.sort()
    
    # Initialize the current number of people and the maximum number of chairs needed
    current_people = 0
    max_chairs = 0
    
    # Iterate over the events
    for time, delta in events:
        # Update the current number of people
        current_people += delta
        
        # Update the maximum number of chairs needed
        max_chairs = max(max_chairs, current_people)
    
    return max_chairs

# Example usage:
arrivals = [1, 2, 6, 5, 3]
departures = [5, 4, 7, 6, 8]
print(min_chairs(arrivals, departures))  # Output: 3