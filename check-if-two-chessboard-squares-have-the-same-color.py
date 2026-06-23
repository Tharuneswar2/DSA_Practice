def squareIsWhite(coordinates):
    # Convert the coordinates to a standard algebraic notation
    # where 'a' is 1, 'b' is 2, ..., 'h' is 8
    x = ord(coordinates[0]) - ord('a') + 1
    y = int(coordinates[1])

    # In a chessboard, the color of a square is determined by the sum of its coordinates
    # If the sum is even, the square is white; otherwise, it's black
    return (x + y) % 2 == 1

def sameColor(coordinates1, coordinates2):
    # Check if the two squares have the same color
    return squareIsWhite(coordinates1) == squareIsWhite(coordinates2)

# Test the function
print(sameColor("a1", "c3"))  # False
print(sameColor("a1", "h8"))  # True