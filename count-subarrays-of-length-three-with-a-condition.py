def count_subarrays(arr):
    n = len(arr)
    count = 0
    
    # Iterate over all possible subarrays of length 3
    for i in range(n - 2):
        # Check if the middle element is greater than its neighbors
        if arr[i] < arr[i + 1] and arr[i + 1] > arr[i + 2]:
            count += 1
    
    return count

# Test the function
arr = [1, 2, 3, 2, 1]
print(count_subarrays(arr))