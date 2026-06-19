def maxDepth(s: str) -> int:
    # Initialize a stack to keep track of opening parentheses
    stack = []
    
    # Initialize the maximum depth
    max_depth = 0
    
    # Iterate over each character in the string
    for char in s:
        # If the character is an opening parenthesis, push it to the stack
        if char == '(':
            stack.append(char)
            # Update the maximum depth if the current depth is greater
            max_depth = max(max_depth, len(stack))
        # If the character is a closing parenthesis, pop the corresponding opening parenthesis from the stack
        elif char == ')':
            stack.pop()
    
    # Return the maximum depth
    return max_depth