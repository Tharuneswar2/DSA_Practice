# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def sortEvenOdd(arr):
    # Separate even and odd indexed elements into two lists
    even = sorted([arr[i] for i in range(0, len(arr), 2)])
    odd = sorted([arr[i] for i in range(1, len(arr), 2)], reverse=True)

    # Initialize result list
    res = []

    # Merge even and odd lists into result list
    for i in range(max(len(even), len(odd))):
        if i < len(even):
            res.append(even[i])
        if i < len(odd):
            res.append(odd[i])

    return res