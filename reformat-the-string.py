# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def reformat(s):
    # Separate digits and letters into two lists
    digits = [c for c in s if c.isdigit()]
    letters = [c for c in s if c.isalpha()]
    
    # If the difference in lengths of the two lists is more than 1, 
    # it's impossible to reformat the string
    if abs(len(digits) - len(letters)) > 1:
        return ""
    
    # Initialize the result string
    res = []
    
    # If the number of digits is more than or equal to the number of letters, 
    # put a digit first in each pair
    if len(digits) >= len(letters):
        for i in range(len(letters)):
            res.append(digits[i])
            res.append(letters[i])
        # If there's one more digit, append it at the end
        if len(digits) > len(letters):
            res.append(digits[-1])
    # If the number of letters is more than the number of digits, 
    # put a letter first in each pair
    else:
        for i in range(len(digits)):
            res.append(letters[i])
            res.append(digits[i])
        # If there's one more letter, append it at the end
        if len(letters) > len(digits):
            res.append(letters[-1])
    
    # Join the characters in the result list into a string
    return "".join(res)