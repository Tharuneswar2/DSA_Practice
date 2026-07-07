def sort_string(s):
    # Create a frequency dictionary to store the frequency of each character
    freq = {}
    for char in s:
        if char in freq:
            freq[char] += 1
        else:
            freq[char] = 1

    # Initialize an empty result string
    result = ""

    # Loop until all characters have been used
    while len(result) < len(s):
        # First, add all characters in increasing order
        for char in sorted(freq.keys()):
            if freq[char] > 0:
                result += char
                freq[char] -= 1

        # Then, add all characters in decreasing order
        for char in sorted(freq.keys(), reverse=True):
            if freq[char] > 0:
                result += char
                freq[char] -= 1

    return result