# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def weighted_word_mapping(words, weights):
    # Create a dictionary to store the weighted words
    weighted_words = {}
    
    # Iterate over the words and their corresponding weights
    for word, weight in zip(words, weights):
        # If the word is already in the dictionary, add the weight to its current value
        if word in weighted_words:
            weighted_words[word] += weight
        # If the word is not in the dictionary, add it with its weight
        else:
            weighted_words[word] = weight
    
    # Return the dictionary of weighted words
    return weighted_words

def find_word_with_max_weight(weighted_words):
    # Initialize the maximum weight and the corresponding word
    max_weight = 0
    max_weight_word = ""
    
    # Iterate over the weighted words
    for word, weight in weighted_words.items():
        # If the weight of the current word is greater than the maximum weight, update the maximum weight and the corresponding word
        if weight > max_weight:
            max_weight = weight
            max_weight_word = word
    
    # Return the word with the maximum weight
    return max_weight_word

def main():
    # Example usage
    words = ["apple", "banana", "apple", "orange", "banana", "banana"]
    weights = [2, 3, 1, 4, 2, 1]
    
    # Create a weighted word mapping
    weighted_words = weighted_word_mapping(words, weights)
    
    # Find the word with the maximum weight
    max_weight_word = find_word_with_max_weight(weighted_words)
    
    # Print the result
    print("Word with maximum weight:", max_weight_word)

if __name__ == "__main__":
    main()