def generate_tags(caption):
    # Convert the caption to lowercase to make the function case-insensitive
    caption = caption.lower()
    
    # Remove punctuation from the caption
    caption = ''.join(e for e in caption if e.isalnum() or e.isspace())
    
    # Split the caption into words
    words = caption.split()
    
    # Initialize an empty set to store unique words
    unique_words = set()
    
    # Initialize an empty list to store the tags
    tags = []
    
    # Iterate over each word in the caption
    for word in words:
        # If the word is not already in the set of unique words
        if word not in unique_words:
            # Add the word to the set of unique words
            unique_words.add(word)
            # Add the word to the list of tags
            tags.append(word)
    
    # Return the list of tags
    return tags

# Example usage:
caption = "This is a video about machine learning and artificial intelligence."
print(generate_tags(caption))