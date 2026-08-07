# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def scoreOfParentheses(s: str) -> int:
    # Initialize the score and depth variables
    score = 0
    depth = 0
    
    # Iterate over each character in the string
    for i in range(len(s)):
        # If the character is an opening parenthesis, increment the depth
        if s[i] == '(':
            depth += 1
        # If the character is a closing parenthesis
        elif s[i] == ')':
            # If the previous character is an opening parenthesis, it means we have a valid pair, so add 1 to the score
            if s[i-1] == '(':
                score += 2 ** (depth - 1)
            # Decrement the depth
            depth -= 1
    
    # Return the final score
    return score