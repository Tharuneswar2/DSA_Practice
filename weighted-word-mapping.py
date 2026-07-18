# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def weighted_word_mapping(words, weights):
    # Create a dictionary to store the weighted word mapping
    weighted_mapping = {}
    
    # Iterate over each word and its corresponding weight
    for word, weight in zip(words, weights):
        # If the word is already in the dictionary, update its weight
        if word in weighted_mapping:
            # Update the weight by adding the new weight to the existing weight
            weighted_mapping[word] += weight
        else:
            # If the word is not in the dictionary, add it with its weight
            weighted_mapping[word] = weight
    
    # Return the weighted word mapping
    return weighted_mapping

def main():
    # Example usage
    words = ["apple", "banana", "apple", "orange", "banana", "banana"]
    weights = [2, 3, 1, 4, 2, 1]
    
    # Create the weighted word mapping
    weighted_mapping = weighted_word_mapping(words, weights)
    
    # Print the weighted word mapping
    print(weighted_mapping)

if __name__ == "__main__":
    main()