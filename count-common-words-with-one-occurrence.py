def count_common_words(sentence1, sentence2):
    # Convert sentences to lower case and split into words
    words1 = sentence1.lower().split()
    words2 = sentence2.lower().split()

    # Create dictionaries to store word counts
    count1 = {}
    count2 = {}

    # Count word occurrences in the first sentence
    for word in words1:
        # Remove punctuation
        word = ''.join(e for e in word if e.isalnum())
        if word in count1:
            count1[word] += 1
        else:
            count1[word] = 1

    # Count word occurrences in the second sentence
    for word in words2:
        # Remove punctuation
        word = ''.join(e for e in word if e.isalnum())
        if word in count2:
            count2[word] += 1
        else:
            count2[word] = 1

    # Initialize count of common words with one occurrence
    common_count = 0

    # Iterate over words in the first sentence
    for word in count1:
        # Check if the word appears in both sentences with a count of 1
        if word in count2 and count1[word] == 1 and count2[word] == 1:
            common_count += 1

    return common_count