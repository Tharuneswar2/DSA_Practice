# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxScore(s):
    # Initialize the maximum score and the count of 1's in the string
    max_score = 0
    ones = s.count('1')
    
    # Initialize the count of zeros to the left of the split
    zeros = 0
    
    # Iterate over the string from the first character to the second last character
    for i in range(len(s) - 1):
        # If the current character is '0', increment the count of zeros
        if s[i] == '0':
            zeros += 1
        # If the current character is '1', decrement the count of ones
        else:
            ones -= 1
        # Update the maximum score
        max_score = max(max_score, zeros + ones)
    
    # Return the maximum score
    return max_score