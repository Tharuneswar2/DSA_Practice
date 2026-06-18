def maximum_number(num, k):
    # Convert the number to a list of characters for easier manipulation
    num = list(str(num))
    
    # Initialize a stack to store the digits
    stack = []
    
    # Iterate over each digit in the number
    for digit in num:
        # While the stack is not empty, the top of the stack is less than the current digit, and we have swaps left
        while stack and stack[-1] < digit and k:
            # Remove the top of the stack (swap it out)
            stack.pop()
            # Decrement the number of swaps left
            k -= 1
        # Add the current digit to the stack
        stack.append(digit)
    
    # If we still have swaps left, remove the last k digits from the stack
    if k:
        stack = stack[:-k]
    
    # Join the stack into a string and convert it back to an integer
    return int(''.join(stack))

# Test the function
print(maximum_number(2736, 1))  # Output: 7236
print(maximum_number(9973, 2))  # Output: 9973