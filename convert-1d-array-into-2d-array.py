def construct2DArray(original, m, n):
    # Check if the original array can be reshaped into an m x n array
    if len(original) != m * n:
        return []

    # Initialize an empty 2D array with m rows and n columns
    result = [[0 for _ in range(n)] for _ in range(m)]

    # Fill the 2D array with elements from the original array
    index = 0
    for i in range(m):
        for j in range(n):
            # Place the next element from the original array at the current position in the 2D array
            result[i][j] = original[index]
            index += 1

    return result

def construct2DArray_pythonic(original, m, n):
    # Check if the original array can be reshaped into an m x n array
    if len(original) != m * n:
        return []

    # Use list comprehension to create the 2D array
    return [original[i * n:(i + 1) * n] for i in range(m)]

# Test the functions
original = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12]
m = 3
n = 4
print(construct2DArray(original, m, n))
print(construct2DArray_pythonic(original, m, n))