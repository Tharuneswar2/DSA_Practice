# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def hardestWorker(n, logs):
    # Initialize the maximum time and the id of the employee who worked the longest
    max_time = 0
    max_id = -1
    
    # Initialize the previous timestamp
    prev_time = 0
    
    # Iterate over each log
    for log in logs:
        # Extract the id and timestamp from the log
        id, timestamp = log
        
        # Calculate the time spent on the task
        time_spent = timestamp - prev_time
        
        # Update the previous timestamp
        prev_time = timestamp
        
        # If the time spent is greater than the max time, update the max time and id
        if time_spent > max_time:
            max_time = time_spent
            max_id = id
            
        # If the time spent is equal to the max time, update the id if it's smaller
        elif time_spent == max_time:
            max_id = min(max_id, id)
    
    # Return the id of the employee who worked the longest
    return max_id