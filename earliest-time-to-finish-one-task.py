def earliest_time_to_finish(tasks, workers):
    # Sort tasks by their deadlines
    tasks.sort(key=lambda x: x[1])
    
    # Initialize the current time and the number of tasks completed
    current_time = 0
    tasks_completed = 0
    
    # Iterate over the sorted tasks
    for task in tasks:
        # If the current time is less than the deadline of the task, update the current time
        if current_time < task[1]:
            current_time = task[1]
        
        # Decrement the deadline of the task by 1 (since a worker is working on it)
        task[1] -= 1
        
        # Increment the number of tasks completed
        tasks_completed += 1
        
        # If the number of tasks completed is equal to the number of workers, break the loop
        if tasks_completed == workers:
            break
    
    # Return the current time
    return current_time

# Example usage:
tasks = [[1, 3], [2, 4], [3, 5]]  # Each task is represented as [duration, deadline]
workers = 2
print(earliest_time_to_finish(tasks, workers))