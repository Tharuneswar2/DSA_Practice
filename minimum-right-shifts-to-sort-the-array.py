def min_right_shifts_to_sort(arr):
    n = len(arr)
    shifts = 0
    sorted_arr = sorted(arr)

    # Find the first element in the sorted array that is not equal to the first element in the original array
    for i in range(n):
        if arr[i] != sorted_arr[i]:
            # Count the number of shifts required to move the first element to its correct position
            for j in range(i, n):
                if arr[j] == sorted_arr[i]:
                    shifts += j - i
                    # Shift the elements to the right
                    arr = arr[:j] + arr[j+1:] + [arr[j]]
                    break
            # Repeat the process for the remaining elements
            return shifts + min_right_shifts_to_sort(arr[:-1])

    # If the array is already sorted, return 0
    return shifts

# Test the function
print(min_right_shifts_to_sort([3, 1, 4, 1, 5, 9, 2, 6]))