# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def checkIfPangram(sentence: str) -> bool:
    # Convert the sentence to lowercase to handle case insensitivity
    sentence = sentence.lower()
    
    # Create a set of all lowercase English letters
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    
    # Use set intersection to find the letters in the sentence that are also in the alphabet
    # If the intersection is equal to the alphabet, then the sentence is a pangram
    return set(sentence) & alphabet == alphabet