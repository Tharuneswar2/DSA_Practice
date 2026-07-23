# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countOperationsToObtainZero(num1, num2):
    # Initialize a variable to store the count of operations
    operations = 0
    
    # Continue the process until both numbers become zero
    while num1 != 0 and num2 != 0:
        # If num1 is greater than num2, subtract num2 from num1
        if num1 > num2:
            # Calculate the number of times num2 can be subtracted from num1
            operations += num1 // num2
            # Update num1 by subtracting num2 the calculated number of times
            num1 %= num2
        # If num2 is greater than num1, subtract num1 from num2
        else:
            # Calculate the number of times num1 can be subtracted from num2
            operations += num2 // num1
            # Update num2 by subtracting num1 the calculated number of times
            num2 %= num1
    
    # Add the remaining non-zero number to the operations count
    operations += num1 + num2
    
    # Return the total count of operations
    return operations