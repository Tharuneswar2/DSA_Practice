def minHoursToTrain(n, k, hours, training):
    # Sort the hours array in ascending order
    hours.sort()
    
    # Initialize the minimum hours required
    min_hours = 0
    
    # Iterate over the hours array
    for i in range(n):
        # If the current hour is less than the kth hour, update the minimum hours
        if hours[i] < training[k-1]:
            # Calculate the difference between the kth hour and the current hour
            diff = training[k-1] - hours[i]
            # Update the minimum hours
            min_hours += diff
    
    # Return the minimum hours required
    return min_hours

# Example usage:
n = 5
k = 3
hours = [1, 2, 3, 4, 5]
training = [2, 4, 6, 8, 10]
print(minHoursToTrain(n, k, hours, training))