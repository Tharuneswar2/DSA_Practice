# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def nearestValidPoint(x, y, points):
    # Initialize the minimum distance and the index of the nearest point
    min_distance = float('inf')  # Initialize with positive infinity
    nearest_point_index = -1  # Initialize with -1, indicating no nearest point found yet

    # Iterate over each point in the list of points
    for i, point in enumerate(points):
        # Check if the x-coordinate or y-coordinate of the current point matches with the given point
        if point[0] == x or point[1] == y:
            # Calculate the Manhattan distance between the given point and the current point
            distance = abs(point[0] - x) + abs(point[1] - y)
            # Check if the calculated distance is less than the current minimum distance
            if distance < min_distance:
                # Update the minimum distance and the index of the nearest point
                min_distance = distance
                nearest_point_index = i

    # Return the index of the nearest point, or -1 if no nearest point is found
    return nearest_point_index