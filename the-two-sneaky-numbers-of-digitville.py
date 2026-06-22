def sneaky_numbers(arr):
    # Sort the array in ascending order
    arr.sort()

    # Initialize variables to store the result
    first = 0
    second = 0

    # Iterate over the array to find the first and second smallest numbers
    for i in range(len(arr)):
        if arr[i] > 0:
            if first == 0:
                first = arr[i]
            elif second == 0:
                second = arr[i]
                break

    # Return the result
    return first, second

# Test the function
arr = [4, 2, -8, 5, 1, 6, 3, -1, 7, -2]
print(sneaky_numbers(arr))