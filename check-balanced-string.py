def is_balanced(s):
    # Initialize a stack to store opening brackets
    stack = []
    
    # Iterate over each character in the string
    for char in s:
        # If the character is an opening bracket, push it onto the stack
        if char == '(' or char == '[' or char == '{':
            stack.append(char)
        # If the character is a closing bracket
        elif char == ')' or char == ']' or char == '}':
            # If the stack is empty, there's no matching opening bracket, so return False
            if not stack:
                return False
            # Get the last opening bracket from the stack
            last_opening_bracket = stack.pop()
            # Check if the opening and closing brackets match
            if (char == ')' and last_opening_bracket != '(') or \
               (char == ']' and last_opening_bracket != '[') or \
               (char == '}' and last_opening_bracket != '{'):
                return False
    
    # If the stack is empty after iterating over the entire string, the string is balanced
    return not stack

# Test the function
print(is_balanced("({[]})"))  # True
print(is_balanced("({[})"))   # False