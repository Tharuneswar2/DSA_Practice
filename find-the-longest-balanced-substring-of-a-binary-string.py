# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def findLongestBalancedSubstring(s):
    # Initialize variables to keep track of the longest balanced substring and the current balance
    max_len = 0
    curr_balance = 0
    
    # Initialize variables to keep track of the start of the current substring
    start = 0
    
    # Iterate over the string
    for end, char in enumerate(s):
        # If the character is '1', increment the current balance
        if char == '1':
            curr_balance += 1
        # If the character is '0', decrement the current balance
        else:
            curr_balance -= 1
        
        # If the current balance is negative, reset the start of the substring and the current balance
        if curr_balance < 0:
            start = end + 1
            curr_balance = 0
        
        # If the current balance is zero, update the maximum length of the balanced substring
        if curr_balance == 0:
            max_len = max(max_len, end - start + 1)
    
    # Return the maximum length of the balanced substring
    return max_len