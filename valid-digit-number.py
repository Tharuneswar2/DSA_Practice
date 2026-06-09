def isNumber(s: str) -> bool:
    # Initialize flags for seen e, seen digit, and seen dot
    seen_e = seen_digit = seen_dot = False

    # Iterate over the string
    for i, c in enumerate(s):
        # If the character is a digit, set seen_digit to True
        if c.isdigit():
            seen_digit = True
        # If the character is a dot, check if we've seen a dot or an e before
        elif c == '.':
            if seen_dot or seen_e:
                return False
            seen_dot = True
        # If the character is an e, check if we've seen an e or a digit before
        elif c.lower() == 'e':
            if seen_e or not seen_digit:
                return False
            seen_e = True
            seen_digit = False  # Reset seen_digit after seeing an e
        # If the character is a sign, check if it's at the start or after an e
        elif c in ['+', '-']:
            if i > 0 and s[i-1].lower() != 'e':
                return False
        # If the character is none of the above, return False
        else:
            return False

    # Return True if we've seen a digit, False otherwise
    return seen_digit