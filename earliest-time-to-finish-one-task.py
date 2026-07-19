# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def earliestTimeToFinish(tasks, finishTime):
    # Sort the tasks based on their finish times
    tasks.sort(key=lambda x: x[1])  # x[1] represents the finish time of each task
    
    # Initialize the current time and the number of tasks completed
    currentTime = 0
    tasksCompleted = 0
    
    # Iterate over the sorted tasks
    for task in tasks:
        # If the current time is less than the start time of the task, update the current time
        if currentTime < task[0]:  # task[0] represents the start time of each task
            currentTime = task[0]
        
        # Increment the current time by 1 (assuming each task takes 1 unit of time)
        currentTime += 1
        
        # Increment the number of tasks completed
        tasksCompleted += 1
        
        # If the current time is greater than or equal to the finish time, return the number of tasks completed
        if currentTime >= finishTime:
            return tasksCompleted
    
    # If no tasks can be finished by the given finish time, return 0
    return 0