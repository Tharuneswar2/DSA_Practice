# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def count_common_words(sentence1, sentence2):
    # Convert both sentences to lower case to handle case insensitivity
    sentence1 = sentence1.lower()
    sentence2 = sentence2.lower()

    # Split the sentences into words
    words1 = sentence1.split()
    words2 = sentence2.split()

    # Create dictionaries to store word frequencies for both sentences
    freq1 = {}
    freq2 = {}

    # Populate the frequency dictionaries
    for word in words1:
        # If the word is already in the dictionary, increment its count
        if word in freq1:
            freq1[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            freq1[word] = 1

    for word in words2:
        # If the word is already in the dictionary, increment its count
        if word in freq2:
            freq2[word] += 1
        # If the word is not in the dictionary, add it with a count of 1
        else:
            freq2[word] = 1

    # Initialize a variable to store the count of common words with one occurrence
    common_count = 0

    # Iterate over the words in the first sentence
    for word in freq1:
        # Check if the word is in the second sentence and has a frequency of 1 in both sentences
        if word in freq2 and freq1[word] == 1 and freq2[word] == 1:
            # If the conditions are met, increment the common count
            common_count += 1

    # Return the count of common words with one occurrence
    return common_count