import math

def maximum_height(base, area):
    # Calculate the height using the formula for the area of a triangle
    # area = (base * height) / 2
    # height = (2 * area) / base
    height = (2 * area) / base
    
    # Return the maximum possible height as an integer
    return math.floor(height)

# Test the function
base = 10
area = 25
print(maximum_height(base, area))