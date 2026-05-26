def is_trionic_array(arr):
    # Check if the array has at least 3 elements
    if len(arr) < 3:
        return False

    # Check if the array is sorted in ascending order
    if arr != sorted(arr):
        return False

    # Check if the difference between consecutive elements is the same
    diff = arr[1] - arr[0]
    for i in range(2, len(arr)):
        if arr[i] - arr[i-1] != diff:
            return False

    return True

# Test the function
print(is_trionic_array([1, 2, 3, 4, 5]))  # True
print(is_trionic_array([1, 3, 5, 7, 9]))  # True
print(is_trionic_array([1, 2, 4, 6, 8]))   # True
print(is_trionic_array([1, 2, 3, 5, 6]))   # False