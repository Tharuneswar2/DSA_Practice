# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def maxDepth(s):
    # Initialize a stack to keep track of opening parentheses
    stack = []
    
    # Initialize the maximum depth and current depth
    max_depth = 0
    curr_depth = 0
    
    # Iterate over each character in the string
    for char in s:
        # If the character is an opening parenthesis, push it to the stack and increment the current depth
        if char == '(':
            stack.append(char)
            curr_depth += 1
            # Update the maximum depth if the current depth is greater
            max_depth = max(max_depth, curr_depth)
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack and decrement the current depth
        elif char == ')':
            stack.pop()
            curr_depth -= 1
    
    # Return the maximum depth
    return max_depth