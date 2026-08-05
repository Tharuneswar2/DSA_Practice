# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def checkStraightLine(coordinates):
    # Calculate the slope of the line formed by the first two points
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    # If the x-coordinates of the two points are the same, the slope is infinity
    if x1 - x0 == 0:
        slope = float('inf')
    else:
        # Calculate the slope using the formula (y1 - y0) / (x1 - x0)
        slope = (y1 - y0) / (x1 - x0)

    # Iterate over the rest of the points
    for x, y in coordinates[2:]:
        # If the x-coordinates of the current point and the first point are the same, 
        # the slope should be infinity
        if x - x0 == 0:
            if slope != float('inf'):
                return False
        else:
            # Calculate the slope of the line formed by the current point and the first point
            new_slope = (y - y0) / (x - x0)
            # If the slopes are different, the points do not form a straight line
            if new_slope != slope:
                return False

    # If we have checked all points and the slopes are the same, the points form a straight line
    return True