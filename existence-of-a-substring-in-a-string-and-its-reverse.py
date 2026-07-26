# Solution approach 2 - provide an efficient python solution with detailed inline comments explaining each step

def is_substring(s, t):
    # Concatenate the string with its reverse to check for the substring in both directions
    temp = s + '#' + s[::-1]
    
    # Initialize the failure function (lps) array with zeros
    lps = [0] * len(temp)
    
    # Initialize the length of the longest proper prefix which is also a proper suffix
    length = 0
    
    # Compute the failure function (lps) array
    i = 1
    while i < len(temp):
        # If the current character matches the character at the length index, increment the length
        if temp[i] == temp[length]:
            length += 1
            lps[i] = length
            i += 1
        # If the length is not zero and the current character does not match, update the length
        elif length != 0:
            length = lps[length - 1]
        # If the length is zero and the current character does not match, move to the next character
        else:
            lps[i] = 0
            i += 1
    
    # Check if the substring t exists in the concatenated string
    i = 0
    j = 0
    while i < len(temp):
        # If the current characters in the concatenated string and the substring match, move to the next characters
        if temp[i] == t[j]:
            i += 1
            j += 1
        # If the entire substring has been found, return True
        if j == len(t):
            return True
        # If the current characters do not match and the length of the substring is not zero, update the length
        elif i < len(temp) and temp[i] != t[j]:
            if j != 0:
                j = lps[j - 1]
            # If the length of the substring is zero, move to the next character in the concatenated string
            else:
                i += 1
    
    # If the substring is not found, return False
    return False