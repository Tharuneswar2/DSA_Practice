def finalValueAfterOperations(operations):
    # Initialize the variable 'x' to 0
    x = 0
    
    # Iterate over each operation in the list of operations
    for operation in operations:
        # Check if the operation is an increment operation
        if operation == "X++" or operation == "++X":
            # If it's an increment operation, increment 'x' by 1
            x += 1
        # Check if the operation is a decrement operation
        elif operation == "X--" or operation == "--X":
            # If it's a decrement operation, decrement 'x' by 1
            x -= 1
    
    # Return the final value of 'x'
    return x