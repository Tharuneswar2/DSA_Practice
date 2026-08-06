# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step
def countAsterisks(s):
    # Split the input string into a list of strings separated by '|'
    rows = s.split('|')
    
    # Initialize a counter for asterisks
    count = 0
    
    # Initialize a flag to track whether we are currently between two '|'
    between_bars = False
    
    # Iterate over each character in the input string
    for row in rows:
        # Iterate over each character in the current row
        for char in row:
            # If the character is '|', toggle the between_bars flag
            if char == '|':
                between_bars = not between_bars
            # If we are currently between two '|' and the character is '*', increment the count
            elif between_bars and char == '*':
                count += 1
                
    # Return the total count of asterisks
    return count