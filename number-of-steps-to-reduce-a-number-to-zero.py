def numberOfSteps(num: int) -> int:
    # Initialize a variable to store the number of steps
    steps = 0
    
    # Continue the process until the number becomes 0
    while num != 0:
        # If the number is even, divide it by 2
        if num % 2 == 0:
            num = num // 2
        # If the number is odd, subtract 1 from it
        else:
            num = num - 1
        
        # Increment the steps after each operation
        steps += 1
    
    # Return the total number of steps
    return steps