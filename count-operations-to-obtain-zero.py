def count_operations(num1, num2):
    # Initialize the count of operations
    count = 0
    
    # Continue the process until num1 becomes 0
    while num1 != 0:
        # If num1 is greater than num2, subtract num2 from num1
        if num1 > num2:
            # Calculate the number of subtractions required
            subtractions = num1 // num2
            # Update the count of operations
            count += subtractions
            # Update num1
            num1 -= subtractions * num2
        # If num1 is less than num2, divide num1 by 2
        else:
            # Update the count of operations
            count += 1
            # Update num1
            num1 //= 2
    
    # Return the total count of operations
    return count