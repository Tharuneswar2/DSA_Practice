def minimize_string_length(s):
    # Initialize an empty stack
    stack = []

    # Iterate over each character in the string
    for char in s:
        # If the stack is not empty and the top of the stack is equal to the current character
        if stack and stack[-1] == char:
            # Pop the top of the stack (remove the duplicate character)
            stack.pop()
        else:
            # Otherwise, push the current character onto the stack
            stack.append(char)

    # Join the characters in the stack into a string and return it
    return ''.join(stack)


# Test the function
print(minimize_string_length("aabaa"))  # Output: "b"
print(minimize_string_length("abc"))  # Output: "abc"
print(minimize_string_length("aaa"))  # Output: ""