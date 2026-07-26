# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def squareIsWhite(coordinates):
    # Convert the chessboard coordinates to a standard 0-based index
    # where 'a' is 0, 'b' is 1, ..., 'h' is 7
    x = ord(coordinates[0]) - ord('a')
    # Convert the row to a 0-based index
    # where '1' is 0, '2' is 1, ..., '8' is 7
    y = int(coordinates[1]) - 1
    
    # The color of a square is determined by the sum of its coordinates
    # If the sum is even, the square is white; otherwise, it's black
    # So, we can simply return whether the sum of the coordinates is even
    return (x + y) % 2 == 0