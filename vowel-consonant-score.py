# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def score(s):
    # Initialize the score as 0
    score = 0
    
    # Define the vowels
    vowels = 'aeiou'
    
    # Iterate over each character in the string
    for char in s:
        # Check if the character is a vowel
        if char.lower() in vowels:
            # If it's a vowel, increment the score by 1
            score += 1
        # Check if the character is an alphabet letter and not a vowel
        elif char.isalpha():
            # If it's a consonant, decrement the score by 1
            score -= 1
    
    # Return the final score
    return score