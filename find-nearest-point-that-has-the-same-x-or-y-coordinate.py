def nearestValidPoint(x, y, points):
    min_distance = float('inf')
    nearest_point = None

    # Iterate over each point in the list of points
    for point in points:
        # Check if the point has the same x or y coordinate as the target point
        if point[0] == x or point[1] == y:
            # Calculate the Manhattan distance between the target point and the current point
            distance = abs(point[0] - x) + abs(point[1] - y)
            # If the distance is less than the current minimum distance, update the minimum distance and the nearest point
            if distance < min_distance:
                min_distance = distance
                nearest_point = point

    # Return the nearest point, or -1 if no point has the same x or y coordinate
    return nearest_point if nearest_point else -1