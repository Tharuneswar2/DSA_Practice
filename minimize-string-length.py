# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def minimize_string_length(s):
    # Initialize an empty stack to store characters
    stack = []
    
    # Iterate over each character in the string
    for char in s:
        # If the stack is not empty and the current character is smaller than the top of the stack
        if stack and char < stack[-1]:
            # Pop the top of the stack (remove the larger character)
            stack.pop()
        else:
            # Otherwise, push the current character into the stack
            stack.append(char)
    
    # Join all characters in the stack into a string and return the result
    return ''.join(stack)