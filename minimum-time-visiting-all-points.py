# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def minTimeToVisitAllPoints(points):
    # Initialize the total time to 0
    total_time = 0
    
    # Iterate over each pair of consecutive points
    for i in range(len(points) - 1):
        # Calculate the absolute difference in x and y coordinates
        dx = abs(points[i][0] - points[i + 1][0])
        dy = abs(points[i][1] - points[i + 1][1])
        
        # The time to travel between two points is the maximum of the differences in x and y coordinates
        # This is because we can move horizontally and vertically at the same time
        total_time += max(dx, dy)
    
    # Return the total time
    return total_time