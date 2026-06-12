def zigzag_traversal(grid, skip):
    if not grid or not grid[0]:
        return []

    rows, cols = len(grid), len(grid[0])
    result = []
    direction = 1  # 1 for right, -1 for left

    for i in range(rows):
        if i % 2 == 0:
            for j in range(cols):
                if (i, j) not in skip:
                    result.append(grid[i][j])
        else:
            for j in range(cols - 1, -1, -1):
                if (i, j) not in skip:
                    result.append(grid[i][j])

    return result

# Example usage:
grid = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]
skip = {(1, 1)}
print(zigzag_traversal(grid, skip))