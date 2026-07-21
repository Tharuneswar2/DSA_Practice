# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minOperations(logs):
    # Initialize a counter to track the number of operations needed to reach the root folder
    count = 0
    
    # Iterate over each log in the list of logs
    for log in logs:
        # If the log is '../', it means we need to move up one level, so decrement the count if it's not already 0
        if log == '../':
            count = max(0, count - 1)
        # If the log is './', it means we're staying in the same folder, so do nothing
        elif log == './':
            continue
        # If the log is a folder name, it means we're moving down one level, so increment the count
        else:
            count += 1
    
    # Return the total number of operations needed to reach the root folder
    return count