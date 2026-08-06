# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def numberOfSteps(num: int) -> int:
    # Initialize a variable to store the number of steps
    steps = 0
    
    # Continue the process until the number becomes zero
    while num != 0:
        # If the number is even, we can divide it by 2 in one step
        if num % 2 == 0:
            # Divide the number by 2
            num = num // 2
        # If the number is odd, we need to subtract 1 from it in one step
        else:
            # Subtract 1 from the number
            num = num - 1
        
        # Increment the steps counter
        steps += 1
    
    # Return the total number of steps
    return steps