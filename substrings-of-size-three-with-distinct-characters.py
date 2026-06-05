def countGoodSubstrings(s: str) -> int:
    # Initialize count of good substrings
    count = 0
    
    # Iterate over the string with a sliding window of size 3
    for i in range(len(s) - 2):
        # Get the current substring
        substring = s[i:i+3]
        
        # Check if all characters in the substring are distinct
        if len(set(substring)) == 3:
            # If distinct, increment the count
            count += 1
    
    # Return the count of good substrings
    return count