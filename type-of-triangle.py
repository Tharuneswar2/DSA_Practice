# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def triangle_type(a, b, c):
    # First, we sort the sides of the triangle in ascending order
    a, b, c = sorted([a, b, c])
    
    # Check if the given sides can form a valid triangle
    # The sum of the lengths of any two sides of a triangle must be greater than the length of the third side
    if a + b <= c:
        return "Not a triangle"
    
    # Check if the triangle is equilateral (all sides are equal)
    if a == b == c:
        return "Equilateral"
    
    # Check if the triangle is isosceles (two sides are equal)
    if a == b or b == c:
        return "Isosceles"
    
    # If none of the above conditions are met, the triangle is scalene (all sides are unequal)
    return "Scalene"