def minTimeToVisitAllPoints(points):
    # Initialize total time to 0
    total_time = 0
    
    # Iterate over each pair of consecutive points
    for i in range(1, len(points)):
        # Calculate the absolute difference in x and y coordinates
        dx = abs(points[i][0] - points[i-1][0])
        dy = abs(points[i][1] - points[i-1][1])
        
        # The time taken to move from one point to another is the maximum of dx and dy
        # This is because we can move diagonally, so we only need to consider the maximum difference
        total_time += max(dx, dy)
    
    # Return the total time
    return total_time