def count_pairs_with_diff_k(arr, n, k):
    # Create a hashmap to store frequency of each element
    freq_map = {}
    for num in arr:
        if num in freq_map:
            freq_map[num] += 1
        else:
            freq_map[num] = 1

    # Initialize count of pairs with absolute difference k
    count = 0

    # Iterate over the hashmap
    for num in freq_map:
        # Check if num + k exists in the hashmap
        if num + k in freq_map:
            # If num + k exists, add the product of their frequencies to the count
            count += freq_map[num] * freq_map[num + k]
        # Check if num - k exists in the hashmap and k is not zero
        if k != 0 and num - k in freq_map:
            # If num - k exists, add the product of their frequencies to the count
            count += freq_map[num] * freq_map[num - k]

    # If k is zero, we have counted each pair twice, so divide the count by 2
    if k == 0:
        count //= 2

    return count

# Example usage:
arr = [1, 2, 3, 4, 5]
n = len(arr)
k = 1
print(count_pairs_with_diff_k(arr, n, k))