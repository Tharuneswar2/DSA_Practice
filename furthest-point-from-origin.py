import math

def furthest_point(points):
    # Initialize the maximum distance and the furthest point
    max_distance = 0
    furthest_point = None

    # Iterate over each point in the list of points
    for point in points:
        # Calculate the Euclidean distance of the current point from the origin
        distance = math.sqrt(point[0]**2 + point[1]**2)

        # If the current distance is greater than the maximum distance found so far
        if distance > max_distance:
            # Update the maximum distance and the furthest point
            max_distance = distance
            furthest_point = point

    # Return the furthest point
    return furthest_point

# Example usage:
points = [(1, 2), (3, 4), (5, 6), (7, 8)]
print(furthest_point(points))