def makeFancyString(s: str) -> str:
    # Initialize an empty stack to store characters
    stack = []
    
    # Iterate over each character in the string
    for char in s:
        # If the stack has less than 2 elements or the top two elements are not the same as the current character
        if len(stack) < 2 or stack[-1] != char or stack[-2] != char:
            # Push the character onto the stack
            stack.append(char)
    
    # Join the characters in the stack into a string and return
    return ''.join(stack)