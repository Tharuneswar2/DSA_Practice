def checkStraightLine(coordinates):
    # Calculate the slope of the line formed by the first two points
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    slope = float('inf') if x1 - x0 == 0 else (y1 - y0) / (x1 - x0)

    # Iterate over the rest of the points
    for x, y in coordinates[2:]:
        # If the line is vertical, check if the x-coordinate is the same
        if slope == float('inf'):
            if x != x0:
                return False
        # If the line is not vertical, calculate the slope and check if it's the same
        else:
            new_slope = float('inf') if x - x0 == 0 else (y - y0) / (x - x0)
            if new_slope != slope:
                return False

    # If we've checked all points and haven't returned False, the points are collinear
    return True