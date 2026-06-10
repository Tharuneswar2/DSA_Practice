def checkIfPangram(sentence: str) -> bool:
    # Convert the sentence to lowercase to handle case insensitivity
    sentence = sentence.lower()
    
    # Create a set of all lowercase English letters
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    # Iterate over each character in the sentence
    for char in sentence:
        # If the character is an alphabet letter, remove it from the set
        if char in alphabet:
            alphabet.discard(char)
    
    # If the set is empty, the sentence is a pangram
    return len(alphabet) == 0

# Alternative solution using Python's built-in set operations
def checkIfPangramAlternative(sentence: str) -> bool:
    # Convert the sentence to lowercase to handle case insensitivity
    sentence = sentence.lower()
    
    # Create a set of all lowercase English letters
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    # Create a set of unique letters in the sentence
    sentence_letters = set(sentence)
    
    # If the set of sentence letters is a superset of the alphabet, the sentence is a pangram
    return alphabet.issubset(sentence_letters)