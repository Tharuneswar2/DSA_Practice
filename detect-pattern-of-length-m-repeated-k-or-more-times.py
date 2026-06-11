def hasAllCodes(s: str, length: int) -> bool:
    # Calculate the total number of possible binary strings of length 'length'
    total = 2 ** length
    
    # Initialize a set to store unique substrings of length 'length'
    substrings = set()
    
    # Iterate over the string 's' with a sliding window of size 'length'
    for i in range(len(s) - length + 1):
        # Extract the substring of length 'length'
        substring = s[i:i + length]
        
        # Add the substring to the set
        substrings.add(substring)
        
        # If the number of unique substrings is equal to the total number of possible binary strings
        if len(substrings) == total:
            # Return True
            return True
    
    # If the loop completes without finding all possible substrings, return False
    return False