def numEmployees(satisfaction, target):
    # Sort the satisfaction array in descending order
    satisfaction.sort(reverse=True)
    
    # Initialize the total satisfaction and the count of employees
    total_satisfaction = 0
    count = 0
    
    # Iterate over the sorted satisfaction array
    for sat in satisfaction:
        # Add the current satisfaction to the total satisfaction
        total_satisfaction += sat
        
        # If the total satisfaction is greater than or equal to the target, increment the count
        if total_satisfaction >= target:
            count += 1
    
    # Return the count of employees who met the target
    return count

# Example usage:
satisfaction = [1, 2, 3, 4, 5]
target = 10
print(numEmployees(satisfaction, target))