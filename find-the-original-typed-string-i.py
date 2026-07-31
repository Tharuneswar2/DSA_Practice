# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def originalTypedString(typed: str) -> str:
    # Initialize an empty stack to store characters
    stack = []
    
    # Iterate over each character in the typed string
    for char in typed:
        # If the stack is not empty and the current character is 'B' (backspace), pop the last character from the stack
        if stack and char == 'B':
            stack.pop()
        # If the current character is not 'B', push it onto the stack
        elif char != 'B':
            stack.append(char)
    
    # Join all characters in the stack into a string and return the result
    return ''.join(stack)