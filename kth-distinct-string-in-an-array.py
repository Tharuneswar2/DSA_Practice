def kthDistinct(arr, k):
    # Create a dictionary to store the frequency of each string
    freq = {}
    for string in arr:
        if string in freq:
            freq[string] += 1
        else:
            freq[string] = 1

    # Create a list of distinct strings
    distinct = [string for string, count in freq.items() if count == 1]

    # Check if k is within the bounds of the distinct list
    if k > len(distinct):
        return ""

    # Return the kth distinct string
    return distinct[k - 1]