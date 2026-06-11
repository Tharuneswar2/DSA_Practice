def lexicographically_smallest_string_after_swap(s):
    # Convert the string to a list of characters for easier manipulation
    s = list(s)
    
    # Initialize variables to store the indices of the characters to be swapped
    first = -1
    second = -1
    
    # Iterate over the string from left to right
    for i in range(len(s)):
        # For each character, check if there's a smaller character to its right
        for j in range(i + 1, len(s)):
            # If a smaller character is found, update the indices
            if s[j] < s[i]:
                # If this is the first pair of characters to be swapped, update 'first' and 'second'
                if first == -1:
                    first = i
                    second = j
                # If this pair of characters is closer to the start of the string than the previous pair, update 'first' and 'second'
                elif j - i < second - first:
                    first = i
                    second = j
    
    # If a pair of characters to be swapped was found, swap them
    if first != -1:
        s[first], s[second] = s[second], s[first]
    
    # Convert the list of characters back to a string and return it
    return ''.join(s)