# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def removeDigit(number: str, digit: str) -> str:
    # Initialize an empty string to store the result
    result = ""
    
    # Initialize a flag to track if the digit is found and removed
    found = False
    
    # Iterate over each character in the number string
    for char in number:
        # If the character is the digit we want to remove and we haven't removed it yet
        if char == digit and not found:
            # Set the found flag to True
            found = True
        else:
            # If the character is not the digit or we've already removed it, add it to the result
            result += char
    
    # If we didn't find the digit in the number, remove the first occurrence of the digit
    if not found:
        result = number.replace(digit, "", 1)
    
    # Return the result
    return result

def maximumNumber(num: str, k: int) -> str:
    # Initialize an empty stack to store the digits
    stack = []
    
    # Iterate over each character in the num string
    for char in num:
        # While the stack is not empty, the top of the stack is less than the current character, and we can still remove digits
        while stack and stack[-1] < char and k:
            # Remove the top of the stack
            stack.pop()
            # Decrement the count of digits to remove
            k -= 1
        # Add the current character to the stack
        stack.append(char)
    
    # If we still have digits to remove, remove them from the end of the stack
    if k:
        stack = stack[:-k]
    
    # Join the stack into a string and remove leading zeros
    return ''.join(stack).lstrip('0') or '0'