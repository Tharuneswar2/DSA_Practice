# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def construct2DArray(original, m, n):
    # Check if the total number of elements in the 2D array matches the length of the original array
    if m * n != len(original):
        return []

    # Initialize an empty 2D array with m rows and n columns
    result = [[0] * n for _ in range(m)]

    # Initialize an index to track the current position in the original array
    index = 0

    # Iterate over each row in the 2D array
    for i in range(m):
        # Iterate over each column in the 2D array
        for j in range(n):
            # Assign the current element from the original array to the corresponding position in the 2D array
            result[i][j] = original[index]
            # Move to the next element in the original array
            index += 1

    # Return the constructed 2D array
    return result