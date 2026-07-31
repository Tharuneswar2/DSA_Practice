# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def generate_tags(video_caption):
    # Convert the caption to lowercase to handle case-insensitive comparison
    caption = video_caption.lower()
    
    # Split the caption into words
    words = caption.split()
    
    # Initialize an empty set to store unique tags
    tags = set()
    
    # Iterate over each word in the caption
    for word in words:
        # Remove punctuation from the word
        word = ''.join(e for e in word if e.isalnum())
        
        # Check if the word is not empty and not a common word (like 'the', 'and', etc.)
        if word and word not in ['the', 'and', 'a', 'an', 'is', 'in', 'it', 'of', 'to']:
            # Add the word to the set of tags
            tags.add(word)
    
    # Convert the set of tags to a list and sort it
    tags = sorted(list(tags))
    
    # Join the tags with commas and return the result
    return ', '.join(tags)

# Example usage:
video_caption = "This is a sample video caption for testing the generate tags function."
print(generate_tags(video_caption))