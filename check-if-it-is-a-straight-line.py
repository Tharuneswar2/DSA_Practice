# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def checkStraightLine(coordinates):
    # If there are less than 2 points, they are always on the same line
    if len(coordinates) < 2:
        return True
    
    # Calculate the slope of the line formed by the first two points
    x0, y0 = coordinates[0]
    x1, y1 = coordinates[1]
    # If the x-coordinates of the two points are the same, the line is vertical
    if x1 - x0 == 0:
        # Check if all other points have the same x-coordinate
        return all(x == x0 for x, y in coordinates)
    else:
        # Calculate the slope of the line
        slope = (y1 - y0) / (x1 - x0)
        
        # Check if all other points lie on the same line
        return all((y - y0) == slope * (x - x0) for x, y in coordinates[2:])