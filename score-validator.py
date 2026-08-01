# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def score_validator(score):
    # Check if the input score is an integer
    if not isinstance(score, int):
        return "Invalid input. Score must be an integer."
    
    # Check if the score is within the valid range (0-1000)
    if score < 0 or score > 1000:
        return "Invalid score. Score must be between 0 and 1000."
    
    # If the score is valid, return a success message
    return "Valid score."