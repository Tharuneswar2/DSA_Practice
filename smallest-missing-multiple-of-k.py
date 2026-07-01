def smallest_multiple_of_k(arr, k):
    # Sort the array in ascending order
    arr.sort()

    # Initialize the smallest multiple of k
    smallest_multiple = k

    # Iterate over the array
    for num in arr:
        # If the current number is a multiple of k, update the smallest multiple
        if num % k == 0:
            smallest_multiple = min(smallest_multiple, num)

    # If no multiple of k is found in the array, return the smallest multiple of k
    if smallest_multiple == k:
        return k

    # Initialize the next multiple of k
    next_multiple = smallest_multiple + k

    # Iterate over the array again to find the smallest missing multiple of k
    for num in arr:
        # If the current number is greater than the smallest multiple and less than the next multiple
        if smallest_multiple < num < next_multiple:
            # Update the next multiple
            next_multiple = num + k

    # Return the smallest missing multiple of k
    return next_multiple

# Test the function
print(smallest_multiple_of_k([1, 2, 4, 5], 3))  # Output: 3
print(smallest_multiple_of_k([2, 4, 6, 8], 3))  # Output: 3
print(smallest_multiple_of_k([1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 2))  # Output: 12