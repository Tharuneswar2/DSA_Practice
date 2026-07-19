# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def min_chairs(arrivals, departures):
    # Combine arrivals and departures into a single list of events
    events = [(time, 1) for time in arrivals] + [(time, -1) for time in departures]
    
    # Sort the events by time
    events.sort()
    
    # Initialize the minimum chairs and current chairs
    min_chairs = 0
    curr_chairs = 0
    
    # Iterate over the events
    for time, delta in events:
        # Update the current chairs
        curr_chairs += delta
        
        # Update the minimum chairs if necessary
        min_chairs = max(min_chairs, curr_chairs)
    
    # Return the minimum chairs
    return min_chairs