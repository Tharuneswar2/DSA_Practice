def minimumLength(s: str) -> int:
    stack = []
    
    # Iterate over the string
    for char in s:
        # If the stack is not empty and the top of the stack is equal to the current character
        if stack and stack[-1] == char:
            # Remove the top of the stack
            stack.pop()
        else:
            # Add the current character to the stack
            stack.append(char)
    
    # Return the length of the stack
    return len(stack)