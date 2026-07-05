def count_days_together(arriveAlice, leaveAlice, arriveBob, leaveBob):
    # Calculate the total days Alice and Bob are together
    total_days = 0
    
    # Iterate over each day
    for i in range(len(arriveAlice)):
        # Calculate the maximum arrival day and the minimum leave day
        max_arrive = max(arriveAlice[i], arriveBob[i])
        min_leave = min(leaveAlice[i], leaveBob[i])
        
        # If the maximum arrival day is less than or equal to the minimum leave day, 
        # it means they are together on that day
        if max_arrive <= min_leave:
            # Add the days they are together to the total days
            total_days += min_leave - max_arrive + 1
    
    # Return the total days Alice and Bob are together
    return total_days

# Test the function
arriveAlice = [1, 2, 3]
leaveAlice = [3, 4, 5]
arriveBob = [2, 3, 4]
leaveBob = [4, 5, 6]
print(count_days_together(arriveAlice, leaveAlice, arriveBob, leaveBob))