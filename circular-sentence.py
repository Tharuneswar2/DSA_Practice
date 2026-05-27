def isCircularSentence(sentence: str) -> bool:
    # Split the sentence into words
    words = sentence.split()
    
    # Check if the last character of the first word is the same as the first character of the last word
    if words[0][-1].lower() != words[-1][0].lower():
        return False
    
    # Iterate over the words in the sentence
    for i in range(len(words) - 1):
        # Check if the last character of the current word is the same as the first character of the next word
        if words[i][-1].lower() != words[i + 1][0].lower():
            return False
    
    # If all checks pass, the sentence is circular
    return True