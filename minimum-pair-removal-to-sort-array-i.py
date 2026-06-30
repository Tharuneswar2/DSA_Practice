def minPairRemovalToSort(arr):
    n = len(arr)
    # Initialize a list to store the longest increasing subsequence (LIS) ending at each position
    lis = [1] * n

    # Compute the LIS ending at each position
    for i in range(1, n):
        for j in range(i):
            if arr[i] > arr[j]:
                lis[i] = max(lis[i], lis[j] + 1)

    # The minimum number of pairs to remove is the difference between the length of the array and the maximum LIS
    return n - max(lis)

# Test the function
arr = [4, 2, 3, 1]
print(minPairRemovalToSort(arr))  # Output: 2