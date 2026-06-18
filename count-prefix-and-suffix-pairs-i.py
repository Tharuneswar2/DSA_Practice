def count_pairs(words):
    # Create a hashmap to store the frequency of each word
    freq_map = {}
    for word in words:
        if word not in freq_map:
            freq_map[word] = 1
        else:
            freq_map[word] += 1

    # Initialize count of pairs
    count = 0

    # Iterate over each word in the list
    for word in words:
        # Generate all possible prefixes and suffixes
        for i in range(1, len(word)):
            prefix = word[:i]
            suffix = word[i:]

            # Check if the prefix and suffix are the same and not the same as the original word
            if prefix == suffix and prefix != word:
                # Increment the count by the frequency of the prefix/suffix
                count += freq_map.get(prefix, 0)

    return count