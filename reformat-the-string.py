def reformat(s: str) -> str:
    # Separate digits and letters into two lists
    digits = [c for c in s if c.isdigit()]
    letters = [c for c in s if c.isalpha()]
    
    # If the difference in lengths of the two lists is more than 1, 
    # it's impossible to reformat the string
    if abs(len(digits) - len(letters)) > 1:
        return ""
    
    # Determine which list should be the first in the result
    first, second = (digits, letters) if len(digits) >= len(letters) else (letters, digits)
    
    # Initialize the result
    result = []
    
    # Merge the two lists into the result
    for i in range(len(second)):
        result.append(first.pop(0))
        result.append(second.pop(0))
    
    # If the first list is longer, append its remaining element
    if first:
        result.append(first.pop(0))
    
    # Join the characters in the result into a string
    return "".join(result)