def squareIsWhite(coordinates: str) -> bool:
    # Convert the coordinates to a numerical representation
    # 'a' corresponds to 1, 'b' to 2, ..., 'h' to 8
    x = ord(coordinates[0]) - ord('a') + 1
    y = int(coordinates[1])

    # A square is white if the sum of its coordinates is even
    # This is because the chessboard is an 8x8 grid with alternating colors
    # The top-left square is black, so we need to check if the sum is even
    return (x + y) % 2 == 0