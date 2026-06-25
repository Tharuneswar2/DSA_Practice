def hardestWorker(n, logs):
    # Initialize the maximum time and the id of the employee who worked the longest
    max_time = 0
    hardest_worker_id = -1
    
    # Initialize the previous time to 0
    prev_time = 0
    
    # Iterate over each log
    for log in logs:
        # Extract the id and time from the log
        id, time = log
        
        # Calculate the time spent on the task
        time_spent = time - prev_time
        
        # Update the previous time
        prev_time = time
        
        # If the time spent is greater than the max time, update the max time and the hardest worker id
        if time_spent > max_time:
            max_time = time_spent
            hardest_worker_id = id
            
        # If the time spent is equal to the max time, update the hardest worker id if the id is smaller
        elif time_spent == max_time:
            hardest_worker_id = min(hardest_worker_id, id)
    
    # Return the id of the hardest worker
    return hardest_worker_id