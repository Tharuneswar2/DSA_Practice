def triangle_type(a, b, c):
    # Check if the sides can form a triangle
    if a + b <= c or a + c <= b or b + c <= a:
        return "Not a triangle"

    # Check if all sides are equal
    if a == b == c:
        return "Equilateral"

    # Check if two sides are equal
    if a == b or a == c or b == c:
        return "Isosceles"

    # If none of the above conditions are met, it's a scalene triangle
    return "Scalene"

# Test the function
print(triangle_type(3, 4, 5))  # Scalene
print(triangle_type(5, 5, 5))  # Equilateral
print(triangle_type(7, 7, 2))  # Isosceles
print(triangle_type(1, 2, 5))  # Not a triangle