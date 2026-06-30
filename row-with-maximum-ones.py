def rowWithMax1s(arr, n, m):
    max_row = -1
    max_count = 0

    # Traverse each row of the matrix
    for i in range(n):
        # Initialize count of 1s in the current row
        count = 0
        # Traverse each element in the row from left to right
        for j in range(m):
            # If the element is 1, increment the count
            if arr[i][j] == 1:
                count += 1
        # If the count of 1s in the current row is more than the max_count
        if count > max_count:
            # Update max_count and max_row
            max_count = count
            max_row = i

    # If no row contains 1, return -1
    if max_count == 0:
        return -1
    else:
        return max_row

# Test the function
arr = [[0, 1, 1, 1],
       [0, 0, 1, 0],
       [0, 0, 1, 1],
       [0, 0, 0, 1]]

n = len(arr)
m = len(arr[0])

print("Index of row with maximum 1s is", rowWithMax1s(arr, n, m))