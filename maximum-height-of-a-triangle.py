# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maximumHeight(a, b, c):
    # Sort the sides of the triangle in ascending order
    a, b, c = sorted([a, b, c])
    
    # Check if the sides can form a valid triangle
    if a + b <= c:
        return -1
    
    # Calculate the semi-perimeter of the triangle
    s = (a + b + c) / 2
    
    # Calculate the area of the triangle using Heron's formula
    area = (s*(s-a)*(s-b)*(s-c)) ** 0.5
    
    # Calculate the maximum height of the triangle
    # The height is calculated as 2 * area / base, where the base is the longest side
    max_height = 2 * area / c
    
    return max_height