def sort_even_odd_indices_independently(arr):
    # Separate even and odd indexed elements into two lists
    even_indexed = [arr[i] for i in range(0, len(arr), 2)]
    odd_indexed = [arr[i] for i in range(1, len(arr), 2)]

    # Sort the even and odd indexed elements independently
    even_indexed.sort()
    odd_indexed.sort()

    # Merge the sorted even and odd indexed elements back into the original array
    result = []
    for i in range(max(len(even_indexed), len(odd_indexed))):
        if i < len(even_indexed):
            result.append(even_indexed[i])
        if i < len(odd_indexed):
            result.append(odd_indexed[i])

    return result

# Test the function
arr = [1, 3, 5, 7, 9, 11, 13, 15]
print(sort_even_odd_indices_independently(arr))