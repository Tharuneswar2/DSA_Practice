# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def restoreString(s, indices):
    # Initialize an empty list to store the characters at their respective indices
    res = [''] * len(s)
    
    # Iterate over the string and the indices list simultaneously
    for i, (char, idx) in enumerate(zip(s, indices)):
        # Place each character at its corresponding index in the result list
        res[idx] = char
    
    # Join the characters in the result list to form the shuffled string
    return ''.join(res)