def findKthCharacter(s, k):
    # Initialize an empty string to store the result
    res = s
    
    # Continue the process until the length of the result string is less than or equal to k
    while len(res) < k:
        # Initialize an empty string to store the next string
        next_s = ''
        
        # Initialize counters for the current character and its count
        curr_char = res[0]
        curr_count = 0
        
        # Iterate over the current string
        for char in res:
            # If the current character is the same as the previous one, increment the count
            if char == curr_char:
                curr_count += 1
            # If the current character is different from the previous one, append the previous character and its count to the next string, and reset the count
            else:
                next_s += curr_char + str(curr_count)
                curr_char = char
                curr_count = 1
        
        # Append the last character and its count to the next string
        next_s += curr_char + str(curr_count)
        
        # Update the result string
        res = next_s
    
    # Return the k-th character of the result string
    return res[k-1]