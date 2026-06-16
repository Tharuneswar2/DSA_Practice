def minOperations(logs):
    # Initialize a stack to keep track of the directories
    stack = []
    
    # Iterate over each log in the list of logs
    for log in logs:
        # If the log is '../', it means we need to go back to the parent directory
        if log == '../':
            # If the stack is not empty, pop the last directory from the stack
            if stack:
                stack.pop()
        # If the log is './', it means we are already in the current directory, so do nothing
        elif log == './':
            continue
        # If the log is not '../' or './', it means we need to go into a new directory
        else:
            # Add the new directory to the stack
            stack.append(log)
    
    # The minimum number of operations is the number of directories in the stack
    return len(stack)