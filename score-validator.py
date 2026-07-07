def score_validator(score):
    # Check if the score is within the valid range (0-1000)
    if score < 0 or score > 1000:
        return False
    
    # Check if the score is a multiple of 10
    if score % 10 != 0:
        return False
    
    # If the score passes both checks, it's valid
    return True

# Test the function
print(score_validator(990))  # Expected output: True
print(score_validator(1001))  # Expected output: False
print(score_validator(901))  # Expected output: False