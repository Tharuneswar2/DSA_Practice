def makeGood(s: str) -> str:
    stack = []
    
    # Iterate over each character in the string
    for char in s:
        # If the stack is not empty and the last character in the stack is the same as the current character but with different case
        if stack and stack[-1].lower() == char.lower() and stack[-1] != char:
            # Remove the last character from the stack
            stack.pop()
        else:
            # Add the current character to the stack
            stack.append(char)
    
    # Join all characters in the stack into a string and return it
    return ''.join(stack)